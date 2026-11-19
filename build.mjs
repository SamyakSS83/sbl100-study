import fs from "node:fs";
import path from "node:path";

const dir = path.dirname(new URL(import.meta.url).pathname);
const parts = [
  "content-01-03.json",
  "content-04-06.json",
  "content-07-09.json",
  "content-10-12.json",
  "content-13-15.json",
];

const course = parts.flatMap((name) =>
  JSON.parse(fs.readFileSync(path.join(dir, name), "utf8")),
);

if (course.length !== 15) {
  throw new Error(`Expected 15 modules, found ${course.length}`);
}

for (const [index, module] of course.entries()) {
  for (const key of ["title", "sourcePages", "mission", "primer", "recall", "mcqs", "traps", "checkpoint"]) {
    if (!(key in module)) throw new Error(`Module ${index + 1} is missing ${key}`);
  }
  if (module.recall.length < 8 || module.mcqs.length < 8) {
    throw new Error(`Module ${index + 1} needs at least 8 recall prompts and 8 MCQs`);
  }
}

const template = fs.readFileSync(path.join(dir, "index.template.html"), "utf8");
const safeJson = JSON.stringify(course).replaceAll("</script", "<\\/script");
fs.writeFileSync(
  path.join(dir, "index.html"),
  template.replace("__COURSE_DATA__", safeJson),
);
console.log(`Built index.html with ${course.length} modules.`);
