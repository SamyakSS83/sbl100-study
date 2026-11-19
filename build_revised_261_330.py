import json
from pathlib import Path

ROOT = Path("/Users/ambar/Downloads/output/study-course")

base = []
for name in ("notes-251-300.json", "notes-301-350.json"):
    base.extend(json.loads((ROOT / name).read_text()))
base = {x["page"]: x for x in base if 261 <= x["page"] <= 330}

guides = {
261:["Start at the multipotent hematopoietic stem cell, then follow the first split into common myeloid and common lymphoid progenitors.","Trace monocyte to macrophage; trace small lymphocyte to B cell/plasma cell, T cell, and NK cell.","Do not group NK cells with the myeloid phagocytes: the diagram places NK cells on the lymphoid branch."],
262:["Read the slide as a distributed system: barriers and secretions act at surfaces, WBCs circulate, bone marrow supplies cells, liver supplies complement, and lymphoid organs organize responses."],
263:["Red arrows show blood leaving the heart through arteries and returning through veins; green lymphatics collect tissue fluid and return lymph to the venous circulation.","At capillary beds, fluid leaves blood to become tissue fluid; lymphatic capillaries collect the excess."],
264:["The tree divides immunity into innate/nonspecific first-line defense and adaptive/specific second-line defense.","The bottom statement is important: the two arms interact rather than operating independently."],
265:["Compare each row horizontally: innate has no lag, no antigen specificity, and no memory; adaptive has a lag, specificity, and memory."],
266:["Follow invading microbes into external innate defenses first, then internal innate defenses; the adaptive branch splits into humoral antibodies and cell-mediated cytotoxic lymphocytes.","Complement is shown with internal innate defenses, not with antibody-producing humoral immunity."],
267:["The wall and fortress image represents intact external barriers preventing entry before immune cells need to attack."],
268:["Match each picture to its mechanical action: skin blocks entry, cilia move mucus upward, and saliva/tears/urine flush organisms away."],
269:["The three chemical mechanisms are antimicrobial peptides in sweat, very low gastric pH from HCl, and lysozyme in tears/saliva."],
270:["The body map marks colonized sites; the key relationship is competition by normal flora for nutrients and space, termed antagonism."],
271:["The enlarged response map adds internal innate defenses after the external barrier: phagocytes, antimicrobial proteins, inflammation, NK cells, and complement."],
272:["The breached-wall and army images signal the transition from barrier defenses to cellular and soluble internal defenses."],
273:["The centrifuged blood tube separates plasma from formed elements; complement, coagulation proteins, and cytokines are extracellular plasma components, whereas WBCs are cells."],
274:["Use morphology only as a cue, but learn the labels: monocyte has a kidney-shaped nucleus, neutrophil a multilobed nucleus, eosinophil a bilobed nucleus with granules, and basophil dense granules.","The arrows separately group B, T, and NK lymphocytes."],
275:["The neutrophil image has a multilobed nucleus. The bullets identify it as the most abundant WBC, an efficient phagocyte, and an early cell at infection sites."],
276:["Chemotaxis means directed movement along a chemical concentration gradient toward a microbial or inflammatory source."],
277:["The moving neutrophil changes shape and extends its leading edge toward the chemoattractant source; this is directional migration, not random motion."],
278:["The word roots explain the process: phago means eat and cyte means cell; the operational sequence is find, engulf, and digest."],
279:["The micrograph shows a neutrophil among red blood cells with bacteria being engulfed; recognition and enclosure precede intracellular digestion."],
280:["Read clockwise: attachment, pseudopod extension, phagosome formation, lysosome fusion, killing/digestion, and discharge of residual material.","Granules/lysosomes deliver antimicrobial molecules to the microbe-containing compartment."],
281:["The highlighted granules contain digestive enzymes and antimicrobial proteins; after fusion, these contents act inside the phagolysosome."],
282:["The red annotation adds a signaling role to killing: neutrophils release mediators that trigger inflammation and influence adaptive immunity."],
283:["Follow the numbered sequence: rolling, slow rolling, adhesion, transmigration, then effector actions including NET release and exocytosis/ROS.","The NET is a web-like extracellular scaffold that traps microbes."],
284:["The central monocyte leaves blood and differentiates into tissue macrophages; the organ icons show specialized macrophages in lung, liver, brain, intestine, and other tissues."],
285:["The slide assigns macrophages two linked jobs: tissue phagocytosis and antigen presentation to adaptive immune cells."],
286:["The cartoon separates NK cells from B and T lymphocytes and shows their targets as infected cells and cancer cells."],
287:["Compare the two target cells: normal cells display inhibitory self-surface signals, while infected/cancer cells may lose them; loss of inhibition permits NK killing."],
288:["The top panel shows inhibitory recognition sparing a healthy cell; the lower panel shows an abnormal target receiving released granules.","Perforin enables entry/pore formation and proteases such as granzymes activate target-cell death."],
289:["Treat the molecular image as the recognition/contact stage: a cytotoxic lymphocyte must first form a close interface with its target before polarized granule release."],
290:["The faint video frame belongs to the killing sequence: target recognition and synapse formation precede directed release of cytotoxic granules and target death."],
291:["The cytotoxic T-cell frame represents adaptive cell-mediated killing; unlike NK missing-self recognition, a cytotoxic T cell recognizes a specific peptide-MHC complex."],
292:["Read the flow left to right: portal of entry, penetration/evasion, damage, and portal of exit.","Adherence feeds into establishment of infection, while inoculum size and virulence factors influence whether disease occurs."],
293:["Follow the panels in order: exposure, adhesion, invasion, colonization/growth, toxicity, then tissue damage and disease.","The epithelial surface and mucus layer remain the spatial reference throughout."],
294:["The binding pair is asymmetric: the receptor is a host-cell component and the ligand/adhesin is microbial."],
295:["The diagram places GAS M protein on the bacterial surface, binding host proteins such as fibronectin; the resulting cloak changes antibody access and supports adherence/invasion."],
296:["The receptor-ligand cartoon explains host specificity: adherence succeeds only when a microbial adhesin matches a receptor on the host tissue."],
297:["The capsule is the outer polysaccharide layer beyond the cell wall; the slide links it to attachment and evasion of host defenses."],
298:["In the normal route, bacterial PAMP recognition by a TLR activates signaling and inflammatory cytokines; the capsule blocks access, so the crossed-out route produces little/no response."],
299:["Compare left and right: complement C3b opsonization promotes binding to the phagocyte; the capsule interferes with opsonization/binding and therefore uptake."],
300:["The bacterium is already inside a phagocyte, but its capsule resists lysosomal enzyme action; engulfment therefore does not guarantee killing."],
301:["Follow the biofilm stages left to right: attachment, initial adherence, microcolony/biofilm maturation, then dispersal.","Quorum sensing coordinates density-dependent gene expression during community development."],
302:["The diagram is layered: mucus is the first barrier, epithelial cells lie below it, and basement membrane is deeper. Pathogens must cross mucus to contact cell receptors."],
303:["The brick wall represents connective-tissue barriers; the listed enzymes are grouped by what they help bacteria overcome: clotting, matrix, or mucosal antibody."],
304:["Hyaluronidase digests hyaluronic-acid-rich ground substance; collagenase digests collagen. Both open paths through connective tissue.","The examples pair hyaluronidase with S. aureus/S. pyogenes and collagenase with C. perfringens."],
305:["The left-to-right clot sequence contrasts coagulase, which creates a protective clot, with kinase/streptokinase, which dissolves clots and permits spread.","The checks connect clot formation with reduced phagocyte, immune, and antibiotic access."],
306:["The envelope diagram places peptidoglycan outside the cytoplasmic membrane; surface proteins may project from or associate with the wall."],
307:["The phagocyte diagram shows mycobacteria surviving after uptake because the mycolic-acid-rich wall resists lysosomal digestion."],
308:["Follow the arrows: bacterial invasin signals to host actin, membrane ruffles rise around the bacterium, the bacterium is enclosed, and then enters the cell."],
309:["The lower cartoons contrast exotoxin secretion from a living bacterium with endotoxin as part of the outer envelope released especially when cells break down."],
310:["Follow the A-B toxin route: receptor binding and endocytosis, endosomal acidification, A-fragment translocation, then eEF-2 ADP-ribosylation and halted translation."],
311:["The AB5 diagram shows five B subunits binding GM1 and one enzymatic A subunit entering the cell.","The signaling chain is persistent Gs activation to adenylyl cyclase to high cAMP to ion/water secretion into the intestine."],
312:["The receptor crosses the membrane seven times; ligand binding changes the cytosolic face, where it activates a heterotrimeric G protein that regulates an effector such as adenylyl cyclase."],
313:["The left panels show signal amplification: one receptor activates multiple G proteins and effectors. The right panels show cessation/attenuation as GTP is hydrolyzed and components reset."],
314:["The envelope diagram locates LPS in the outer membrane of Gram-negative bacteria; lipid A is the membrane-anchored toxic portion."],
315:["The broken bacterium icon represents endotoxin release during bacterial lysis/digestion; listed causes include complement, phagocytes, and antibiotic treatment."],
316:["The central endotoxin node branches to cytokine secretion, inflammation, fever, and blood-brain-barrier effects; cytokines mediate several downstream effects."],
317:["Read the sequence left to right: macrophage uptake of endotoxin, cytokine release into blood, hypothalamic prostaglandin production, and increased temperature set point.","The red note separates bacterial killing from endotoxin removal because endotoxin is heat stable."],
318:["This is a section divider. The concentric-cell graphic introduces multiple regulated routes of cell death covered in the following slides."],
319:["The wheel groups physiological uses of programmed death: development/homeostasis, organ shaping, immune regulation, removal of infected or damaged cells, and stress responses."],
320:["Read the top sequence left to right: shrinkage, membrane blebbing, apoptotic-body formation, then phagocytosis.","The micrographs contrast an intact normal nucleus with condensed/fragmented apoptotic chromatin."],
321:["The diagram is a proteolytic cascade: apoptotic signals activate initiator caspases 8/9, which cleave executioner procaspases 3/6/7, and executioners cleave many cellular substrates."],
322:["The left tree groups caspase functions; the center gel illustrates CAD-mediated DNA laddering after ICAD cleavage; the lower membrane sketch shows phosphatidylserine exposure.","Caspase cleavage links molecular substrates to visible apoptotic features."],
323:["Follow the mitochondrial route: cellular stress activates BH3-only proteins, BAX/BAK permeabilize the outer mitochondrial membrane, cytochrome c is released, apoptosome forms, caspase-9 activates caspase-3/7."],
324:["Use the domain bars: effectors BAX/BAK and anti-apoptotic BCL-2-like proteins contain BH1-BH4; activators and sensitizers such as BID/BIM/PUMA or BAD/BIK/BMF are BH3-only.","The interaction grid shows anti-apoptotic proteins binding and restraining pro-apoptotic members."],
325:["Follow Fas ligand to Fas receptor clustering, FADD recruitment, DISC assembly, procaspase-8 activation, and executioner-caspase activation.","The alternative panel shows FLIP at the DISC blocking productive caspase activation and preventing apoptosis."],
326:["Compare micrographs feature by feature: necroptosis shows swelling, vacuolization, swollen mitochondria, and plasma-membrane rupture; apoptosis shows condensation/fragmentation and membrane blebbing while the membrane remains intact."],
327:["The top row shows extrinsic triggers at TNFR1/Fas/TRAIL receptors and TLR3/TLR4; downstream RIPK1/RIPK3 activate MLKL, which damages the membrane.","The intracellular branch shows ZBP1 sensing Z-nucleic acids and converging on RIPK3-MLKL."],
328:["The left cell releases intracellular DAMPs after lytic death; the right immune cell detects DAMPs through receptors such as TLRs/RAGE and activates inflammatory signaling including NF-kB/STAT pathways."],
329:["Follow autophagy left to right: initiation, phagophore expansion around cargo, closed autophagosome, lysosome fusion, autolysosome degradation, and recycling.","LC3 is shown on the autophagic membrane; acidic lysosomes contain cathepsins and other hydrolases."],
330:["The left branch builds PUFA-containing phospholipids through ACSL4/LPCAT3; iron and LOX promote lipid peroxidation and membrane damage.","Protective branches include GPX4/glutathione, FSP1/CoQ, and DHFR/BH4 systems that suppress phospholipid peroxide accumulation."]
}

Q = {
261:("A marrow precursor gives rise to neutrophils, monocytes, erythrocytes, and megakaryocytes but not T cells. Which labeled progenitor matches it?",["Common myeloid progenitor","Common lymphoid progenitor","Plasma cell","Natural killer cell"],0,"The lineage diagram places those four outputs under the common myeloid progenitor; T cells arise from the lymphoid branch."),
262:("Which source-product pairing is shown for a soluble innate immune component?",["Liver - complement proteins","Bone marrow - gastric HCl","Skin - immunoglobulin synthesis","Lymphatic vessel - lysozyme synthesis"],0,"The slide identifies the liver as a source of complement proteins."),
263:("After excess interstitial fluid enters the green vessels in the diagram, what is it called?",["Lymph","Plasma","Serum","Cytosol"],0,"Interstitial fluid becomes lymph after entering lymphatic capillaries."),
264:("Which classification correctly matches the two branches in the overview?",["Innate: nonspecific; adaptive: specific","Innate: specific; adaptive: nonspecific","Innate: memory-forming only; adaptive: no memory","Innate: second line only; adaptive: first line only"],0,"The overview labels innate immunity nonspecific and adaptive immunity specific."),
265:("A response begins slowly after first exposure but is faster on re-exposure to the same antigen. Which arm accounts for both properties?",["Adaptive immunity","Innate immunity","Mechanical barrier defense","Normal flora"],0,"A lag and immunological memory are paired features of adaptive immunity."),
266:("Which pair occupies the two adaptive branches at the right of the response map?",["Antibodies and cytotoxic lymphocytes","Complement and neutrophils","Skin and mucous membranes","Inflammation and natural killer cells"],0,"The adaptive arm divides into humoral antibody and cell-mediated cytotoxic-lymphocyte responses."),
267:("In the fortress analogy, what event must occur before internal innate defenses become relevant?",["Breach of an external barrier","Class switching by B cells","Formation of memory cells","Release of bacterial endotoxin"],0,"The wall represents external innate defenses that must be breached before internal defenses confront the invader."),
268:("Failure of ciliary beating would most directly impair which barrier mechanism?",["Mucociliary clearance","Gastric acidification","Complement activation","Normal-flora antagonism"],0,"Cilia propel mucus and trapped particles upward in the mucociliary escalator."),
269:("Which pairing is inconsistent with the chemical-barrier slide?",["Lysozyme - stomach acidification","HCl - low gastric pH","Antimicrobial peptides - sweat","Lysozyme - tears"],0,"HCl, not lysozyme, creates the low pH of the stomach."),
270:("Resident bacteria prevent a pathogen from establishing by consuming the same nutrient. Which labeled barrier principle is this?",["Antagonism by normal flora","Chemotaxis","Opsonization","Cytotoxicity"],0,"Competition for nutrients and space by normal flora is described as antagonism."),
271:("A pathogen has crossed mucus but adaptive immunity has not yet developed. Which listed defense can act immediately inside tissue?",["Phagocytic cells","Memory B cells","High-affinity antibodies from recall","Antigen-specific cytotoxic clones"],0,"Phagocytic cells are internal innate defenses and do not require clonal priming."),
272:("The breached-wall image marks the handoff from which defense category to which category?",["External innate to internal innate","Adaptive humoral to mechanical","Cell-mediated to normal flora","Memory to primary response"],0,"Once external barriers fail, internal innate defenses engage the invader."),
273:("Which component belongs in the extracellular plasma bracket rather than the WBC fraction?",["Complement protein","Neutrophil","Monocyte","Natural killer cell"],0,"Complement is soluble in plasma; the other options are leukocytes."),
274:("Which labeled leukocyte is identified by a multilobed nucleus and fine cytoplasmic granules?",["Neutrophil","Monocyte","Lymphocyte","Mast cell"],0,"The neutrophil drawing shows the characteristic multilobed nucleus."),
275:("A newly infected tissue recruits the most abundant circulating WBC as a primary responder. Which cell is expected?",["Neutrophil","Basophil","Monocyte","Natural killer cell"],0,"Neutrophils are shown as roughly 50-60% of WBCs and rapid primary-response phagocytes."),
276:("A neutrophil detects increasing chemoattractant concentrations toward a wound. Its net movement should be:",["Up the concentration gradient","Down the concentration gradient","Independent of the gradient","Restricted to the bloodstream"],0,"Positive chemotaxis directs movement toward higher chemoattractant concentration."),
277:("Which observation best distinguishes the filmed behavior as chemotaxis rather than random motility?",["Persistent movement toward a localized chemical source","Repeated engulfment without displacement","Symmetric membrane blebbing in all directions","Loss of all cell polarity"],0,"Chemotaxis is directional migration toward a chemical source."),
278:("Which sequence best operationalizes phagocytosis by a neutrophil?",["Recognition, engulfment, intracellular digestion","Secretion, diffusion, antibody synthesis","Adhesion, mitosis, memory formation","Lysis, antigen rearrangement, exocytosis"],0,"Phagocytes find/recognize, engulf, and digest microbes."),
279:("In the micrograph, bacterial enclosure by the neutrophil must occur before formation of which compartment?",["Phagosome","Nucleus","Golgi cisterna","Extracellular trap"],0,"Engulfment encloses the bacterium in a membrane-bound phagosome."),
280:("Which event immediately converts a microbe-containing phagosome into the main digestive compartment?",["Fusion with a lysosome","Binding to a B-cell receptor","Release through exocytosis","Division of the phagocyte"],0,"Phagosome-lysosome fusion creates the phagolysosomal digestive compartment."),
281:("A neutrophil forms phagosomes normally but cannot deliver granule contents. Which function is most directly lost?",["Intracellular microbial killing","Chemotactic gradient detection","Production of erythrocytes","Antigen-specific memory"],0,"Granules supply digestive enzymes and antimicrobial proteins to the microbe-containing compartment."),
282:("Which outcome shows that neutrophils do more than directly ingest bacteria?",["Recruitment/activation of other immune responses by inflammatory mediators","Differentiation into plasma cells","Production of gastric acid","Generation of antigen receptors by gene rearrangement"],0,"The slide emphasizes inflammatory signaling and links to adaptive immunity."),
283:("Which step occurs after firm adhesion but before neutrophil effector release in the vessel diagram?",["Transmigration across endothelium","Rolling on selectins","Initial tethering","Hematopoietic differentiation"],0,"The displayed recruitment order proceeds from rolling to adhesion to transmigration, then tissue effector actions."),
284:("Which tissue-cell relationship is supported by the differentiation arrows?",["Circulating monocyte becomes tissue macrophage","Neutrophil becomes natural killer cell","B cell becomes monocyte","Macrophage becomes erythrocyte"],0,"Monocytes migrate into tissues and differentiate into macrophages."),
285:("After ingesting a microbe, which macrophage activity most directly connects innate detection to an adaptive T-cell response?",["Presentation of microbial antigen","Synthesis of peptidoglycan","Release of gastric HCl","Formation of a bacterial capsule"],0,"Antigen presentation enables macrophages to communicate microbial information to T cells."),
286:("Which target profile is most consistent with the NK-cell panel?",["Virus-infected host cell","Extracellular collagen fiber","Free bacterial endotoxin molecule","Normal erythrocyte with intact self markers"],0,"NK cells kill infected and malignant host cells rather than free molecules or matrix."),
287:("An infected cell loses a surface protein that normally delivers an inhibitory signal to NK cells. What is the predicted result?",["NK-cell activation and target killing","Guaranteed protection from NK cells","Bacterial spore formation","Complement synthesis by the target"],0,"Loss of normal self-surface inhibition is the missing-self cue for NK killing."),
288:("Which molecule-function pairing fits granule-mediated NK killing?",["Perforin - enables pore/entry; granzyme - proteolytic death signal","Perforin - antibody; granzyme - complement receptor","Perforin - adhesin; granzyme - capsule enzyme","Perforin - cytokine receptor; granzyme - MHC molecule"],0,"Perforin facilitates access and granzyme proteases activate death pathways in the target."),
289:("Before polarized cytotoxic granule release, which event must occur at the target-cell interface?",["Stable recognition/contact synapse","Phagosome-lysosome fusion","Bacterial binary fission","Complement synthesis in the liver"],0,"Cytotoxic killing requires target recognition and close contact before directed granule release."),
290:("Which sequence best represents granule-mediated lymphocyte cytotoxicity?",["Target recognition, synapse formation, granule release, target-cell death","Granule release, target recognition, mitosis, phagocytosis","Chemotaxis, antibody secretion, capsule formation, lysis","Endotoxin release, receptor loss, DNA replication, memory"],0,"Recognition and synapse formation precede polarized cytotoxic granule release and death."),
291:("What gives a cytotoxic T cell greater antigen specificity than the missing-self mechanism of an NK cell?",["Recognition of a particular peptide-MHC complex","Recognition of any low-pH compartment","Binding directly to peptidoglycan","Sensing any extracellular ATP"],0,"Cytotoxic T cells use antigen receptors to recognize specific peptide-MHC complexes."),
292:("Which ordering follows the pathogenicity flowchart from entry to transmission?",["Portal of entry -> defense evasion -> host damage -> portal of exit","Host damage -> portal of exit -> adherence -> portal of entry","Portal of exit -> colonization -> entry -> inoculum","Adherence -> portal of exit -> entry -> no host damage"],0,"The chart runs from entry through penetration/evasion and damage to exit."),
293:("Which stage immediately precedes invasion in the illustrated pathogenesis sequence?",["Adhesion","Toxicity","Tissue damage","Portal of exit"],0,"The panel order is exposure, adhesion, invasion, colonization/growth, toxicity, and damage."),
294:("In a bacterial attachment pair, which component is expected on the microbe?",["Adhesin ligand","Host receptor","MHC class I","Complement C3 made by the bacterium"],0,"The microbial ligand/adhesin binds a receptor that is a host-cell component."),
295:("Which host-protein recruitment would most directly create the M-protein cloak shown for GAS?",["Fibronectin/fibrinogen coating the bacterial surface","Peptidoglycan coating the host nucleus","LPS coating a Gram-positive cell","Caspase coating an epithelial receptor"],0,"M protein recruits host proteins including fibronectin and fibrinogen, masking bacterial epitopes."),
296:("Why can the same bacterial adhesin colonize one tissue but not another?",["Its matching host receptor is tissue-restricted","All tissues have identical receptors","Adherence occurs without molecular binding","The capsule determines blood group"],0,"Tissue distribution of the matching host receptor helps determine tropism and host specificity."),
297:("Which structural description identifies a capsule?",["Polysaccharide layer external to the cell wall","Lipid bilayer inside the cytoplasm","Protein shell surrounding the nucleus","Peptidoglycan located inside ribosomes"],0,"The capsule is shown as an outer polysaccharide layer outside the bacterial cell wall."),
298:("If a capsule masks an LPS-containing surface from the pathway shown, which recognition event is reduced?",["TLR4 detection of a PAMP","T-cell receptor binding to peptide-MHC","Fas binding to Fas ligand","GPCR binding to epinephrine"],0,"The slide specifically identifies LPS as a PAMP recognized by TLR4."),
299:("In the opsonization diagram, loss of surface C3b deposition would first reduce:",["Binding of the bacterium to the phagocyte","Bacterial DNA replication","Host collagen synthesis","Lysosomal acidification"],0,"Opsonin deposition promotes phagocyte binding, so blocking it impairs attachment before engulfment."),
300:("A bacterium is visible inside a phagosome but remains viable. Which capsule-associated step has most likely failed?",["Effective lysosomal digestion","Initial exposure to a host receptor","Release through a portal of exit","Synthesis of cytokines by the liver"],0,"The diagram shows capsule-mediated resistance to lysosomal digestion after uptake."),
301:("Which biofilm stage supplies cells that can colonize a new site?",["Dispersal","Initial attachment","Irreversible attachment","Maturation only"],0,"The last panel shows cells leaving the mature community during dispersal."),
302:("After crossing the mucus layer, which structure does a pathogen encounter next in the displayed tissue arrangement?",["Epithelial cell surface","Bone marrow","Lymph-node germinal center","Mitochondrial matrix"],0,"The diagram places the epithelial surface directly beneath mucus."),
303:("Which enzyme is best matched to escape from a mucosal IgA defense rather than connective-tissue spread?",["IgA protease","Collagenase","Hyaluronidase","Coagulase"],0,"IgA protease targets mucosal antibody; collagenase and hyaluronidase target matrix."),
304:("A pathogen spreads through collagen-rich deep tissue. Which listed enzyme is the closest mechanistic match?",["Collagenase","Coagulase","IgA protease","Streptokinase"],0,"Collagenase digests collagen and is linked on the slide to tissue invasion."),
305:("Which contrast between the two enzyme types is correct?",["Coagulase forms a protective clot; streptokinase dissolves clots","Both enzymes exclusively form clots","Coagulase dissolves clots; streptokinase makes capsules","Both enzymes digest IgA"],0,"The figure contrasts coagulase-driven clot formation with kinase-mediated clot dissolution."),
306:("Which wall component is explicitly composed of sugars and amino acids?",["Peptidoglycan","Mycolic acid","Lipid A","Cholesterol"],0,"Peptidoglycan is identified as the sugar-and-amino-acid wall polymer."),
307:("Which organisms on the slide gain lysosomal resistance from a mycolic-acid-rich wall?",["Mycobacterium tuberculosis and M. leprae","Vibrio cholerae and E. coli","Streptococcus pyogenes and S. pneumoniae","Clostridium perfringens and Bacillus anthracis"],0,"The two listed examples are M. tuberculosis and M. leprae."),
308:("In the membrane-ruffling sequence, which host component is rearranged directly by invasin-triggered signaling?",["Actin cytoskeleton","Peptidoglycan wall","Nuclear DNA polymerase","Lysosomal cathepsin"],0,"Invasins alter host actin filaments, driving membrane ruffles around the microbe."),
309:("Which statement distinguishes exotoxin from endotoxin in the lower diagrams?",["Exotoxin is secreted protein; endotoxin is part of the bacterial outer envelope","Both are host antibodies","Endotoxin is secreted only by living Gram-positive cells","Exotoxin is the lipid A portion of LPS"],0,"The slide contrasts secreted exotoxin with envelope-associated endotoxin."),
310:("Diphtheria toxin fragment A reaches the cytosol. Which substrate modification causes translation arrest?",["ADP-ribosylation of eEF-2","Phosphorylation of actin","Cleavage of GM1 ganglioside","Acetylation of peptidoglycan"],0,"Fragment A ADP-ribosylates eEF-2, preventing protein synthesis."),
311:("Which molecular event lies directly between cholera-toxin entry and the cAMP surge?",["Persistent activation of Gs alpha","Inactivation of all adenylyl cyclase","Cleavage of eEF-2","Polymerization of peptidoglycan"],0,"A1 locks Gs alpha active, which persistently stimulates adenylyl cyclase."),
312:("A receptor has seven transmembrane helices and activates a trimeric G protein. Which effector shown may be activated next?",["Adenylyl cyclase","Peptidoglycan synthase","Caspase-9 apoptosome","Lysosomal collagenase"],0,"The GPCR diagram shows activated G protein regulating an effector such as adenylyl cyclase."),
313:("Which event terminates the active alpha-subunit state in the GPCR cycle?",["Hydrolysis of bound GTP to GDP","Exchange of GDP for GTP","Ligand binding to the receptor","Activation of adenylyl cyclase"],0,"GTP hydrolysis returns the alpha subunit to the inactive GDP-bound state and attenuates signaling."),
314:("Which nested identification is correct?",["Endotoxin = lipid A portion of LPS in Gram-negative outer membrane","Endotoxin = peptidoglycan of Gram-positive cytoplasm","Endotoxin = secreted A subunit of cholera toxin","Endotoxin = bacterial capsule polysaccharide"],0,"The slide identifies lipid A within LPS as Gram-negative endotoxin."),
315:("Why can antibiotic treatment transiently increase exposure to endotoxin?",["Bacterial damage/lysis releases LPS-associated lipid A","Antibiotics convert exotoxin into antibody","Antibiotics synthesize new capsules","Host cells begin producing LPS"],0,"Breakdown of Gram-negative bacteria can release envelope-associated endotoxin."),
316:("Which mediator most directly links endotoxin sensing to the multiple branches shown?",["Cytokine secretion","Bacterial collagen synthesis","Antibody gene rearrangement","Erythrocyte enucleation"],0,"The diagram places cytokine secretion downstream of endotoxin and upstream of systemic effects."),
317:("In the pyrogen pathway, cytokines raise temperature by acting through which intermediate site/process?",["Hypothalamic prostaglandin production","Bone-marrow peptidoglycan synthesis","Renal capsule formation","Mitochondrial cytochrome-c retention"],0,"The diagram routes cytokine signals to hypothalamic prostaglandins that alter the temperature set point."),
318:("Which topic begins with this divider and is developed in the following slides?",["Regulated cell-death pathways","Bacterial adherence","Blood-cell hematopoiesis","Mucociliary clearance"],0,"The divider explicitly introduces Lecture 31 on cell-death pathways."),
319:("Which scenario is a physiological use of programmed cell death rather than accidental injury?",["Removal of self-reactive lymphocytes","Immediate rupture after extreme trauma","Random protein denaturation by heat","Mechanical tearing of a membrane"],0,"Immune regulation, including deletion of inappropriate lymphocytes, is a normal role of programmed death."),
320:("Which sequence preserves the morphology shown for apoptosis?",["Cell shrinkage -> blebbing -> apoptotic bodies -> phagocytosis","Cell swelling -> rupture -> DAMP release -> inflammation","Ruffling -> invasion -> biofilm -> dispersal","Adhesion -> clotting -> collagen digestion -> exit"],0,"The top row shows shrinkage, blebbing, fragmentation into apoptotic bodies, then clearance."),
321:("Which pairing correctly assigns cascade level?",["Caspase-9 initiator; caspase-3 executioner","Caspase-3 initiator; caspase-9 executioner","Caspase-6 initiator; caspase-8 executioner","Caspase-7 initiator; caspase-9 executioner"],0,"Caspases 8/9 are initiators; caspases 3/6/7 are executioners."),
322:("ICAD cleavage releases CAD. Which experimental pattern in the slide is the expected consequence?",["Internucleosomal DNA laddering","Increased intact genomic DNA only","LPS band formation","Collagen cross-linking"],0,"Released CAD fragments DNA at regular intervals, producing the ladder pattern."),
323:("Which ordering correctly follows intrinsic apoptosis after cellular stress?",["BAX/BAK activation -> cytochrome c release -> apoptosome -> caspase-9","Fas ligation -> DISC -> caspase-8 -> BAX synthesis only","MLKL activation -> membrane rupture -> apoptosome","LPS release -> TLR4 -> caspase-9"],0,"The mitochondrial pathway proceeds through BAX/BAK permeabilization, cytochrome c, apoptosome, and caspase-9."),
324:("Which pair belongs to the multi-domain pro-apoptotic effector class rather than the BH3-only class?",["BAX and BAK","BID and BIM","BAD and BIK","BMF and NOXA"],0,"BAX and BAK contain BH1-BH4 and act as effectors; the other pairs are BH3-only."),
325:("Which complex forms at clustered Fas receptors before initiator-caspase activation?",["DISC containing FADD and procaspase-8","Apoptosome containing cytochrome c and caspase-9","Necrosome containing RIPK3 and MLKL","Autolysosome containing LC3 and cathepsin"],0,"Fas recruits FADD and procaspase-8 into the death-inducing signaling complex."),
326:("Electron microscopy shows swollen mitochondria, cytoplasmic vacuoles, and ruptured plasma membrane without condensed fragmented chromatin. Which death mode fits?",["Necroptosis","Apoptosis","Autophagic recycling alone","Adaptive immunity"],0,"The feature set matches the necroptotic micrograph rather than apoptotic condensation and intact blebbing membrane."),
327:("Which protein is the downstream membrane-disrupting effector of the RIPK1-RIPK3 necroptosis axis?",["MLKL","BCL-2","Caspase-9","LC3"],0,"Activated RIPK3 phosphorylates MLKL, which oligomerizes and damages the plasma membrane."),
328:("Why does the diagram predict stronger inflammation after necroptosis than after orderly apoptotic-body clearance?",["Lytic rupture releases DAMPs that activate immune receptors","Caspase-3 prevents all cytokine signaling","The nucleus produces bacterial LPS","Phosphatidylserine blocks phagocytosis"],0,"Necroptotic rupture releases intracellular DAMPs that stimulate immune cells and inflammatory mediators."),
329:("Which step converts a cargo-containing autophagosome into a degradative compartment?",["Fusion with a lysosome","Binding of Fas ligand","Activation of TLR4","Release of cytochrome c"],0,"Lysosome fusion creates an autolysosome where acidic hydrolases degrade cargo."),
330:("Loss of which defense would most directly permit phospholipid hydroperoxides to accumulate in the central ferroptosis pathway?",["GPX4-glutathione system","Fas-FADD complex","Caspase-8-FLIP complex","LC3-autophagosome system"],0,"GPX4 uses glutathione to reduce phospholipid hydroperoxides and suppress ferroptosis.")
}

assert set(base) == set(range(261, 331))
assert set(guides) == set(range(261, 331))
assert set(Q) == set(range(261, 331))

out = []
for page in range(261, 331):
    x = base[page]
    q, options, answer, explanation = Q[page]
    shift = page % len(options)
    options = options[shift:] + options[:shift]
    answer = (answer - shift) % len(options)
    x = {
        "page": page,
        "title": x["title"],
        "explain": x["explain"],
        "mustKnow": x["mustKnow"],
        "terms": x["terms"],
        "diagramGuide": guides[page],
        "interaction": {
            "type": "mcq",
            "q": q,
            "options": options,
            "answer": answer,
            "explanation": explanation,
        },
    }
    out.append(x)

target = ROOT / "revised-261-330.json"
target.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
print(target)
