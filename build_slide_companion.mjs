import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const dir=path.dirname(fileURLToPath(import.meta.url));
const source=JSON.parse(fs.readFileSync(path.join(dir,"slide-source.json"),"utf8"));
const names=[
  "revised-001-050.json","revised-051-120.json","revised-121-190.json",
  "revised-191-260.json","revised-261-330.json","revised-331-394.json"
];
const notes=names.flatMap(name=>JSON.parse(fs.readFileSync(path.join(dir,name),"utf8")));
const extraNames=[
  "extras-001-050.json","extras-051-120.json","extras-121-190.json",
  "extras-191-260.json","extras-261-330.json","extras-331-394.json"
];
const extraMap=new Map(extraNames.flatMap(name=>JSON.parse(fs.readFileSync(path.join(dir,name),"utf8"))).map(x=>[x.page,x.questions]));
if(notes.length!==394)throw new Error(`Expected 394 notes, found ${notes.length}`);
const slides=source.map((s,i)=>{
  const n=notes[i];
  if(n.page!==s.page)throw new Error(`Page mismatch at ${i+1}`);
  if(!Array.isArray(n.diagramGuide))throw new Error(`Missing diagram guide at ${i+1}`);
  if(!n.interaction||!["mcq","tap"].includes(n.interaction.type))throw new Error(`Bad interaction at ${i+1}`);
  if(n.interaction.type==="mcq"&&(n.interaction.options.length!==4||n.interaction.answer<0||n.interaction.answer>3))throw new Error(`Bad MCQ at ${i+1}`);
  const extras=extraMap.get(n.page)||[];
  const interaction=n.interaction.type==="mcq"?{type:"mcq-set",questions:[n.interaction,...extras]}:n.interaction;
  return {...s,...n,interaction,rawText:undefined};
});
const template=fs.readFileSync(path.join(dir,"slide-companion.template.html"),"utf8");
const json=JSON.stringify(slides).replaceAll("</script","<\\/script");
const built=template.replace("__SLIDE_DATA__",json);
fs.writeFileSync(path.join(dir,"slide-companion.html"),built);
fs.writeFileSync(path.join(dir,"index.html"),built);
console.log(`Built ${slides.length}-slide companion`);
