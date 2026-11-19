// Builds two separate pages from the existing data:
//   slides.html    – slides + explanations, grouped by topic (no questions)
//   questions.html – every question in one bank, filterable by topic
//   index.html     – small hub linking both
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const dir = path.dirname(fileURLToPath(import.meta.url));
const read = (n) => JSON.parse(fs.readFileSync(path.join(dir, n), "utf8"));
const ranges = ["001-050", "051-120", "121-190", "191-260", "261-330", "331-394"];

const source = read("slide-source.json");
const notes = ranges.flatMap((r) => read(`revised-${r}.json`));
const extras = new Map(ranges.flatMap((r) => read(`extras-${r}.json`)).map((x) => [x.page, x.questions]));
const modules = ["01-03", "04-06", "07-09", "10-12", "13-15"].flatMap((r) => read(`content-${r}.json`));
if (notes.length !== source.length) throw new Error("notes/source length mismatch");

// Topics = lectures, in slide order
const topics = [];
for (const s of source) if (!topics.includes(s.lecture)) topics.push(s.lecture);
const MIXED = "Mixed Review (all topics)";

// Which lecture topics each of the 15 summary modules covers
const moduleTopics = [
  ["Bioenergetics"],
  ["Gene Expression and Regulation"],
  ["Genetic Engineering Applications 1"],
  ["Genetic Engineering Applications 2", "Genetic Engineering Applications 3"],
  ["Biological Motors"],
  ["Cellular Signaling"],
  ["Cell Death and Cell Division"],
  ["Stem Cells and Differentiation"],
  ["Host Pathogen Interaction"],
  ["Host Pathogen Interaction"],
  ["Cell Death Pathways"],
  ["Cancer Biology 1", "Cancer Biology 2 and Drug Development"],
  ["Drug Development 1", "Drug Development 2"],
  ["Drug Development and Techniques", "Techniques in Biochemistry and Biophysics"],
  [MIXED],
];
for (const t of moduleTopics.flat()) if (t !== MIXED && !topics.includes(t)) throw new Error(`Unknown topic ${t}`);

// ---------- slides data ----------
const slides = source.map((s, i) => {
  const n = notes[i];
  if (n.page !== s.page) throw new Error(`Page mismatch at ${i + 1}`);
  return {
    page: s.page, topic: s.lecture, slideInLecture: s.slideInLecture,
    title: n.title, explain: n.explain, mustKnow: n.mustKnow || [],
    terms: n.terms || [], diagramGuide: n.diagramGuide || [],
  };
});
const overviews = modules.map((m, i) => ({
  title: m.title, source: m.sourcePages, mission: m.mission,
  primer: m.primer, traps: m.traps, checkpoint: m.checkpoint, topics: moduleTopics[i],
}));

// ---------- question bank ----------
const questions = [];
let id = 0;
for (const [i, n] of notes.entries()) {
  const qs = n.interaction.type === "mcq" ? [n.interaction, ...(extras.get(n.page) || [])] : (extras.get(n.page) || []);
  for (const q of qs) {
    if (q.options.length !== 4 || q.answer < 0 || q.answer > 3) throw new Error(`Bad MCQ on slide ${n.page}`);
    questions.push({ id: `s${id++}`, kind: "mcq", topics: [source[i].lecture], page: n.page,
      q: q.q, options: q.options, answer: q.answer, explanation: q.explanation });
  }
}
for (const [mi, m] of modules.entries()) {
  for (const q of m.mcqs) {
    if (q.options.length !== 4) throw new Error(`Bad module MCQ in ${m.title}`);
    questions.push({ id: `m${mi}-${questions.length}`, kind: "mcq", topics: moduleTopics[mi], module: m.title,
      q: q.q, options: q.options, answer: q.answer, explanation: q.explanation });
  }
  for (const r of m.recall) {
    questions.push({ id: `r${mi}-${questions.length}`, kind: "recall", topics: moduleTopics[mi], module: m.title, q: r.q, a: r.a });
  }
}
const allTopics = [...topics, MIXED];

const inject = (tpl, data) => {
  const t = fs.readFileSync(path.join(dir, tpl), "utf8");
  return t.replace("__DATA__", JSON.stringify(data).replaceAll("</script", "<\\/script"));
};
fs.writeFileSync(path.join(dir, "slides.html"), inject("slides.template.html", { topics, slides, overviews }));
fs.writeFileSync(path.join(dir, "questions.html"), inject("questions.template.html", { topics: allTopics, questions }));
// executive summaries (summary-*.json, one object per topic)
const summaries = fs.readdirSync(dir).filter((n) => /^summary-\d\d-\d\d\.json$/.test(n)).sort().flatMap(read);
for (const s of summaries) if (!topics.includes(s.topic)) throw new Error(`Summary has unknown topic: ${s.topic}`);
const missing = topics.filter((t) => !summaries.some((s) => s.topic === t));
if (missing.length) console.warn(`No summary yet for: ${missing.join(", ")}`);
summaries.sort((a, b) => topics.indexOf(a.topic) - topics.indexOf(b.topic));
fs.writeFileSync(path.join(dir, "summary.html"), inject("summary.template.html", summaries));
fs.writeFileSync(path.join(dir, "index.html"), fs.readFileSync(path.join(dir, "hub.template.html"), "utf8")
  .replace("__NSLIDES__", slides.length).replace("__NQ__", questions.length).replace("__NT__", topics.length));
const mcq = questions.filter((q) => q.kind === "mcq").length;
console.log(`slides.html: ${slides.length} slides in ${topics.length} topics`);
console.log(`questions.html: ${questions.length} questions (${mcq} MCQ, ${questions.length - mcq} recall)`);
