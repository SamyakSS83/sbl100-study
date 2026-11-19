const fs = require("fs");
const path = require("path");

const dir = __dirname;
const notes = JSON.parse(fs.readFileSync(path.join(dir, "notes-001-050.json"), "utf8"));

const tap = (label) => ({ type: "tap", label });
const mcq = (q, options, answer, explanation) => ({
  type: "mcq", q, options, answer, explanation
});

const diagramGuide = {
  1: [], 2: [],
  3: [
    "The lower-left loop pairs photosynthetic autotrophs with heterotrophs: plants supply organic products and O₂; heterotrophs return CO₂.",
    "Read the numbered text as four outputs of metabolism: obtain energy, make precursors, polymerize macromolecules, and make or degrade specialized biomolecules."
  ],
  4: [
    "The nitrogen-cycle arrows connect atmospheric N₂, ammonia (NH₄⁺), nitrite (NO₂⁻), nitrate (NO₃⁻), and amino acids.",
    "Red arrows show microbial interconversion, including nitrogen fixation, nitrification, denitrification, and anammox; blue arrows connect inorganic nitrogen to plants, animals, and amino acids."
  ],
  5: [
    "The blue upward arrow is anabolism: precursor molecules plus chemical energy form cell macromolecules.",
    "The red downward arrow is catabolism: energy-containing nutrients become energy-depleted products while producing ATP and reduced electron carriers.",
    "The center links the two directions through ATP/ADP and NAD(P)H/FADH₂ carrier pairs."
  ],
  6: [
    "The left network funnels many carbohydrates and amino acids into acetyl-CoA: this is converging catabolism.",
    "The right network branches from acetyl-CoA and other precursors to many products: this is diverging anabolism.",
    "The circular route below is a cyclic pathway: intermediates regenerate while material enters or leaves."
  ],
  7: [],
  8: [
    "The x-axis is substrate concentration and the y-axis is reaction rate.",
    "The curve approaches Vmax asymptotically as enzyme becomes saturated.",
    "Projecting from ½Vmax to the curve and then down to the x-axis identifies KM."
  ],
  9: [
    "The small saturation curve reinforces that when substrate concentration is below KM, reaction rate is below half Vmax."
  ],
  10: [],
  11: [
    "In ΔG = ΔH − TΔS, increasing positive ΔS makes the subtracted TΔS term larger and therefore makes ΔG more negative.",
    "A negative ΔH also drives ΔG downward; either heat release or increased entropy can favor a reaction."
  ],
  12: [
    "In the equilibrium expression, product concentrations are in the numerator and reactant concentrations are in the denominator; stoichiometric coefficients become exponents.",
    "The double arrow means the reaction can proceed in either direction until equilibrium is reached."
  ],
  13: [
    "The energy profile rises to an activation barrier and ends with products below reactants.",
    "The vertical difference between reactant and product levels is negative ΔG; the downward final level represents net energy release."
  ],
  14: [
    "The profile ends with products above reactants, so ΔG is positive.",
    "An energy input is required to move from the lower reactant level to the higher product level."
  ],
  15: [
    "The table links K′eq > 1 with negative ΔG′° and forward direction, K′eq = 1 with ΔG′° = 0, and K′eq < 1 with positive ΔG′° and reverse direction."
  ],
  16: [
    "Moving K′eq by each tenfold step changes ΔG′° by about 5.7 kJ/mol at 25°C.",
    "Values above 1 give negative ΔG′°; reciprocal values below 1 give equal positive magnitudes."
  ],
  17: [
    "For A ⇌ B, K′eq is [B]/[A]. Substituting 12 into −RT ln K′eq gives approximately −6.16 kJ/mol."
  ],
  18: [
    "The reaction quotient shown is [C][D]/[A][B]: raising products raises ΔG, whereas raising reactants lowers ΔG.",
    "Actual ΔG equals the standard transformed value plus the concentration-dependent RT ln Q term."
  ],
  19: [
    "Follow glycolysis left-to-right across the upper row and then right-to-left across the lower row to pyruvate.",
    "ATP is consumed at hexokinase and phosphofructokinase; NADH is formed at glyceraldehyde-3-phosphate dehydrogenase; ATP is produced at phosphoglycerate kinase and pyruvate kinase."
  ],
  20: [
    "The two arrows A→B and B→C share intermediate B; cancellation of B gives the net reaction A→C.",
    "The net ΔG′° is the arithmetic sum ΔG′°₁ + ΔG′°₂."
  ],
  21: [
    "The unfavorable phosphorylation of glucose (+13.8 kJ/mol) is added to favorable ATP hydrolysis (−30.5 kJ/mol).",
    "Pi is the common intermediate and cancels, leaving ATP + glucose → ADP + glucose-6-phosphate with net −16.7 kJ/mol."
  ],
  22: [], 23: [],
  24: [],
  25: [],
  26: [
    "In the Nernst-style expression, the reducing-agent concentration is in the numerator and oxidizing-agent concentration in the denominator.",
    "The slide uses the NAD⁺/NADH + H⁺ pair as the biologically relevant redox ratio."
  ],
  27: [],
  28: [
    "Read each row as class → characteristic bond → examples: pyrophosphates, acyl phosphates, enol phosphates, thioesters, and guanidino phosphates."
  ],
  29: [
    "ATP consists of adenine attached to ribose at the ribose 1′ carbon, with three phosphates attached at the 5′ carbon.",
    "The diagram labels the nitrogenous base, ribose sugar, and triphosphate chain as separate structural regions."
  ],
  30: [
    "The table compares ATP, ADP, AMP, Pi, and phosphocreatine concentrations across cell types; these are millimolar values, not the 1 M standard state."
  ],
  31: [
    "Mg²⁺ is drawn chelating phosphate oxygens of ATP and ADP.",
    "The labeled complexes are MgATP²⁻ and MgADP⁻; for phosphoryl transfer, MgATP²⁻ is the true enzymatic substrate."
  ],
  32: [
    "The calculation inserts erythrocyte [ATP], [ADP], and [Pi] into ΔG = ΔG′° + RT ln([ADP][Pi]/[ATP]).",
    "The concentration term makes cellular ATP hydrolysis more favorable: the result is −51.8 kJ/mol rather than −30.5 kJ/mol."
  ],
  33: [
    "The glycolysis map highlights the two ATP-investment reactions, the NADH-producing oxidation, and the two ATP-producing substrate-level phosphorylation reactions."
  ],
  34: [
    "Each panel explains a favorable hydrolysis product: 1,3-bisphosphoglycerate gains resonance stabilization, PEP forms pyruvate by tautomerization, and phosphocreatine products gain resonance stabilization."
  ],
  35: [
    "Acetyl-CoA hydrolysis first forms acetic acid and CoA-SH; ionization then gives resonance-stabilized acetate.",
    "The table ranks PEP most negative, followed by 1,3-BPG, phosphocreatine, ADP→AMP+Pi, ATP→ADP+Pi, and lower-energy phosphate esters."
  ],
  36: [
    "The top drawing compresses glutamine synthesis into one arrow, but the lower drawing shows the actual two-step route.",
    "ATP first forms enzyme-bound glutamyl phosphate; NH₃ then displaces phosphate to form glutamine."
  ],
  37: [
    "The y-axis is ΔG′° of hydrolysis in kJ/mol; more negative values are higher phosphoryl-transfer potential.",
    "PEP, 1,3-BPG, and phosphocreatine lie above ATP; glucose-6-phosphate and glycerol phosphate lie below ATP.",
    "Arrows toward ATP indicate high-energy donors can phosphorylate ADP; arrows from ATP toward lower compounds indicate ATP can phosphorylate those acceptors."
  ],
  38: [
    "Attack at ATP's γ phosphate transfers phosphoryl and leaves ADP; attack at β transfers pyrophosphoryl and leaves AMP; attack at α transfers adenylyl and releases PPi.",
    "The three red attack arrows map directly to the three labeled products below."
  ],
  39: [],
  40: [
    "The cycle starts with luciferin activation by ATP to luciferyl adenylate, releasing PPi.",
    "Luciferase and O₂ convert the activated intermediate to oxyluciferin with light emission and release of CO₂ and AMP.",
    "Regenerating reactions return oxyluciferin to luciferin."
  ],
  41: [],
  42: [],
  43: [
    "The nesting sequence is cell → nucleus → chromosome → DNA; the bracket marks a gene as a segment of DNA."
  ],
  44: [
    "The central vertical arrows show DNA replication, DNA→RNA transcription, RNA→protein translation, and protein folding.",
    "Side arrows add recognized information transfers such as reverse transcription and RNA-dependent RNA replication.",
    "The diagram does not show information transfer from protein back to nucleic acid."
  ],
  45: [],
  46: [
    "The fork moves downward while helicase opens the parental duplex; topoisomerase acts ahead of helicase and SSB proteins coat separated strands.",
    "The leading strand is synthesized continuously toward the fork; the lagging strand is synthesized discontinuously as Okazaki fragments away from the fork.",
    "Every new DNA segment extends 5′→3′ from an RNA primer."
  ],
  47: [],
  48: [
    "The upper gene diagram places promoter upstream, structural gene in the middle, and terminator downstream; template and coding strands run antiparallel.",
    "In the transcription bubble, RNA polymerase moves along the template strand while the nascent RNA exits behind it.",
    "Read the stated sequence as initiation → promoter escape → elongation → termination."
  ],
  49: [
    "The three panels show initiation at the promoter with sigma factor, elongation by RNA polymerase, and termination near the terminator with rho factor.",
    "The RNA is complementary to the template/antisense strand and nearly matches the coding/sense strand except U replaces T."
  ],
  50: [
    "The top bar is pre-mRNA with cap, leader, alternating exons and introns, trailer, and poly(A) tail.",
    "The lower bar is mature mRNA after introns are removed and exons joined; the protein-coding sequence remains between untranslated end regions."
  ]
};

const I = {
  1: tap("Open the Bioenergetics lecture"),
  2: tap("Source slide acknowledged"),
  3: mcq("Which sequence correctly matches the four metabolic functions numbered on the slide?",
    ["Obtain energy → make cellular precursors → polymerize macromolecules → make/degrade specialized biomolecules",
     "Make cellular precursors → obtain energy → degrade all macromolecules → store pigments",
     "Polymerize macromolecules → obtain nitrogen → make ATP only → stop degradation",
     "Obtain energy → replicate DNA → translate proteins → excrete all lipids"], 0,
    "The slide numbers those four functions in that order."),
  4: mcq("Which conversion in the nitrogen-cycle diagram is labeled as nitrogen fixation?",
    ["Atmospheric N₂ → NH₄⁺/ammonia", "NH₄⁺/ammonia → NO₂⁻/nitrite",
     "NO₂⁻/nitrite → NO₃⁻/nitrate", "NO₃⁻/nitrate → atmospheric N₂"], 0,
    "Nitrogen-fixing bacteria and archaea convert atmospheric N₂ to ammonia/ammonium."),
  5: mcq("Which carrier set is shown linking catabolism to anabolism in the central part of the diagram?",
    ["ATP, NADH, NADPH, and FADH₂", "AMP, DNA, RNA, and CoA",
     "Glucose, glycogen, starch, and sucrose", "CO₂, H₂O, NH₃, and O₂"], 0,
    "The center lists ATP and reduced electron carriers NADH, NADPH, and FADH₂."),
  6: mcq("Which pathway pattern is paired correctly on the slide?",
    ["Converging catabolism; diverging anabolism", "Diverging catabolism; converging anabolism",
     "Cyclic catabolism only; linear anabolism only", "Branched catabolism only; cyclic anabolism only"], 0,
    "The figure explicitly labels catabolism as converging and anabolism as diverging."),
  7: mcq("Which paired pathways are given as the compartmentation example?",
    ["Fatty-acid synthesis in cytosol; fatty-acid degradation in mitochondria",
     "Fatty-acid synthesis in mitochondria; fatty-acid degradation in cytosol",
     "Glycolysis in nucleus; gluconeogenesis in lysosome",
     "Protein synthesis in mitochondria; protein degradation in Golgi"], 0,
    "The slide uses cytosolic fatty-acid synthesis and mitochondrial fatty-acid degradation."),
  8: mcq("On the Michaelis–Menten graph, the x-coordinate corresponding to ½Vmax is:",
    ["KM", "Vmax", "kcat", "ΔG"], 0,
    "KM is the substrate concentration at which v = ½Vmax."),
  9: mcq("Which mechanism changes enzyme abundance in response to an external signal such as a hormone or growth factor?",
    ["Hormonal regulation", "Substrate availability", "Competitive inhibition", "Product diffusion"], 0,
    "The slide says hormonal regulation alters the synthesis or degradation rate of an enzyme."),
  10: mcq("Which sign-description pairing is correct?",
    ["ΔH < 0: exothermic", "ΔH < 0: endothermic", "ΔS > 0: products less disordered",
     "ΔG < 0: endergonic"], 0,
    "Negative ΔH denotes heat release and therefore an exothermic reaction."),
  11: mcq("According to ΔG = ΔH − TΔS, which combination most strongly favors a negative ΔG?",
    ["ΔH negative and ΔS positive", "ΔH positive and ΔS negative",
     "ΔH positive and ΔS zero", "ΔH zero and ΔS negative"], 0,
    "Heat release and increased entropy both make ΔG more negative."),
  12: mcq("What distinguishes the biochemical standard transformed state used for ΔG′°?",
    ["pH 7 with [H₂O] treated as 55.5 M", "pH 0 with [H₂O] treated as 1 M",
     "pH 14 with [H₂O] omitted", "pH 7 with every solute fixed at 55.5 M"], 0,
    "The slide specifies [H⁺] = 10⁻⁷ M and water at 55.5 M."),
  13: mcq("In the exergonic energy profile, how are product and reactant free energies related?",
    ["Products are lower; ΔG < 0", "Products are higher; ΔG < 0",
     "Products are lower; ΔG > 0", "Products are equal; ΔG > 0"], 0,
    "The profile ends below the reactant level, giving negative ΔG."),
  14: mcq("Which statement identifies an endergonic reaction on the slide?",
    ["It is non-spontaneous and requires free-energy input", "It is spontaneous and releases free energy",
     "It has ΔG < 0 and lower-energy products", "It proceeds without coupling or energy input"], 0,
    "Endergonic reactions have positive ΔG and require energy input."),
  15: mcq("Starting with all components at 1 M, what is predicted when K′eq < 1?",
    ["ΔG′° is positive and the reaction proceeds in reverse", "ΔG′° is negative and the reaction proceeds forward",
     "ΔG′° is zero and the system is at equilibrium", "ΔG′° is negative and the reaction proceeds in reverse"], 0,
    "The table pairs K′eq below 1 with positive ΔG′° and reverse direction."),
  16: mcq("What ΔG′° value does the table associate with K′eq = 10³?",
    ["−17.1 kJ/mol", "−5.7 kJ/mol", "+17.1 kJ/mol", "+34.2 kJ/mol"], 0,
    "The 10³ row gives −17.1 kJ/mol (−4.1 kcal/mol)."),
  17: mcq("For A ⇌ B with K′eq = 12 at 298 K, the calculated ΔG′° is approximately:",
    ["−6.16 kJ/mol", "+6.16 kJ/mol", "−30.5 kJ/mol", "+12.0 kJ/mol"], 0,
    "Substitution into −RT ln K′eq gives about −6.16 kJ/mol."),
  18: mcq("For A + B ⇌ C + D, which expression is the reaction quotient used on the slide?",
    ["[C][D]/[A][B]", "[A][B]/[C][D]", "[A][C]/[B][D]", "[B][C]/[A][D]"], 0,
    "Products appear in the numerator and reactants in the denominator."),
  19: mcq("Which glycolytic enzyme is shown producing NADH?",
    ["Glyceraldehyde-3-phosphate dehydrogenase", "Hexokinase",
     "Phosphofructokinase", "Pyruvate kinase"], 0,
    "NAD⁺ + Pi is converted to NADH + H⁺ at the glyceraldehyde-3-phosphate dehydrogenase step."),
  20: mcq("For successive reactions A→B and B→C, the overall standard free-energy change is:",
    ["ΔG′°₁ + ΔG′°₂", "ΔG′°₁ − ΔG′°₂", "ΔG′°₁ × ΔG′°₂", "ΔG′°₁ / ΔG′°₂"], 0,
    "Free-energy changes are additive when the reactions are summed."),
  21: mcq("What is the net ΔG′° after coupling glucose phosphorylation to ATP hydrolysis?",
    ["−16.7 kJ/mol", "+16.7 kJ/mol", "−30.5 kJ/mol", "+13.8 kJ/mol"], 0,
    "+13.8 plus −30.5 equals −16.7 kJ/mol."),
  22: mcq("Which quantity is a reaction-specific physical constant calculable from K′eq?",
    ["ΔG′°", "ΔG", "Reactant concentration", "Product concentration"], 0,
    "The summary identifies standard transformed ΔG′° as the constant related to K′eq."),
  23: mcq("What condition corresponds to equilibrium?",
    ["ΔG = 0", "ΔG is large and negative", "ΔG is large and positive", "ΔG′° must equal −30.5 kJ/mol"], 0,
    "The slide states that the system is at equilibrium when ΔG equals zero."),
  24: mcq("What does the slide call the cellular ratio of ATP to ADP concentrations?",
    ["Energy charge", "Redox potential", "Equilibrium constant", "Phosphorylation index"], 0,
    "The ATP-to-ADP ratio is labeled the cell's energy charge."),
  25: mcq("Which pairing of cell type and free-energy source is correct?",
    ["Photosynthetic cells—absorbed solar radiation", "Photosynthetic cells—nutrient molecules only",
     "Heterotrophic cells—absorbed solar radiation", "Heterotrophic cells—atmospheric nitrogen"], 0,
    "Photosynthetic cells use solar radiation; heterotrophic cells use nutrient molecules."),
  26: mcq("Which redox pair is specifically used on the slide to describe bioenergetic redox status?",
    ["NAD⁺ / NADH + H⁺", "ATP / AMP + PPi", "FAD / ATP + Pi", "O₂ / CO₂ + H₂O"], 0,
    "The slide names the ratio of NAD⁺ to NADH + H⁺."),
  27: mcq("What threshold does the slide use for a high-energy compound at pH 7.0?",
    ["Hydrolysis liberates at least 7 Cal/mol", "Hydrolysis liberates less than 7 Cal/mol",
     "Synthesis absorbs exactly 7 J/mol", "Oxidation liberates at least 70 kJ/mol"], 0,
    "The slide defines high-energy compounds using at least 7 Cal/mol on hydrolysis."),
  28: mcq("Which class–example pairing is shown in the table?",
    ["Enol phosphate—phosphoenolpyruvate", "Acyl phosphate—phosphocreatine",
     "Thioester—1,3-bisphosphoglycerate", "Guanidino phosphate—acetyl-CoA"], 0,
    "Phosphoenolpyruvate is the listed enol phosphate."),
  29: mcq("At which ribose carbon are ATP's three phosphate groups attached?",
    ["5′ carbon", "1′ carbon", "2′ carbon", "3′ carbon"], 0,
    "The slide places adenine at 1′ and the triphosphate group at 5′."),
  30: mcq("What is ATP hydrolysis ΔG′° under standard conditions on the slide?",
    ["−30.5 kJ/mol", "−51.8 kJ/mol", "−16.7 kJ/mol", "+30.5 kJ/mol"], 0,
    "The standard transformed value shown is −30.5 kJ/mol."),
  31: mcq("For most ATP-dependent phosphoryl-transfer enzymes, what is the true substrate?",
    ["MgATP²⁻", "Free ATP⁴⁻", "MgADP⁻", "Free AMP²⁻"], 0,
    "The slide explicitly identifies MgATP²⁻ as the true substrate."),
  32: mcq("Using human erythrocyte concentrations, what actual ΔG of ATP hydrolysis is calculated?",
    ["−51.8 kJ/mol", "−30.5 kJ/mol", "−21.3 kJ/mol", "+51.8 kJ/mol"], 0,
    "The calculation ends at −51,820 J/mol, or −51.8 kJ/mol."),
  33: mcq("Which two glycolytic enzymes are shown consuming ATP?",
    ["Hexokinase and phosphofructokinase", "Phosphoglycerate kinase and pyruvate kinase",
     "Enolase and triose phosphate isomerase", "Aldolase and phosphoglucose isomerase"], 0,
    "ATP→ADP is marked at hexokinase and phosphofructokinase."),
  34: mcq("Which hydrolysis product relationship explains PEP's large negative ΔG′°?",
    ["Enol pyruvate tautomerizes to keto pyruvate", "Pyruvate polymerizes to glycogen",
     "PEP is reduced directly to lactate", "Phosphate converts pyruvate to oxaloacetate"], 0,
    "The diagram shows hydrolysis followed by enol-to-keto tautomerization."),
  35: mcq("Which compound has the most negative ΔG′° of hydrolysis in the displayed table?",
    ["Phosphoenolpyruvate", "1,3-bisphosphoglycerate", "Phosphocreatine", "ATP → ADP + Pi"], 0,
    "PEP is listed at −61.9 kJ/mol, the most negative value shown."),
  36: mcq("What activated intermediate is formed before NH₃ attacks in glutamine synthesis?",
    ["Enzyme-bound glutamyl phosphate", "Enzyme-bound glutamyl adenylate",
     "Free phosphocreatine", "Free carbamoyl phosphate"], 0,
    "ATP first phosphorylates glutamate to enzyme-bound glutamyl phosphate."),
  37: mcq("Which compound lies below ATP in phosphoryl-transfer potential on the graph?",
    ["Glucose 6-phosphate", "Phosphoenolpyruvate", "1,3-bisphosphoglycerate", "Phosphocreatine"], 0,
    "Glucose 6-phosphate has a less negative hydrolysis ΔG′° than ATP."),
  38: mcq("Nucleophilic attack at ATP's α phosphate produces which transfer?",
    ["Adenylyl transfer with PPi release", "Phosphoryl transfer with ADP release",
     "Pyrophosphoryl transfer with AMP release", "Phosphoryl transfer with AMP release"], 0,
    "The α position gives adenylyl transfer and PPi as the leaving group."),
  39: mcq("Which ATP cleavage activates luciferin to luciferyl adenylate?",
    ["ATP → AMP + PPi", "ATP → ADP + Pi", "ATP → adenosine + triphosphate", "ATP → ADP + PPi"], 0,
    "The slide states that pyrophosphate cleavage forms luciferyl adenylate."),
  40: mcq("Which products accompany light emission during luciferin oxidation in the cycle?",
    ["Oxyluciferin, CO₂, and AMP", "Luciferyl adenylate, PPi, and ATP",
     "Luciferin, O₂, and ADP", "Oxyluciferin, Pi, and NADH"], 0,
    "The figure shows formation of oxyluciferin with CO₂ and AMP release while light is emitted."),
  41: tap("Open the Gene Expression and Regulation lecture"),
  42: mcq("Which prokaryotic example is specifically listed under regulation of gene expression?",
    ["Lac operon", "TCA cycle", "Michaelis–Menten system", "Nitrogen cycle"], 0,
    "The contents list operons and specifically the lac operon."),
  43: mcq("In the diagram, which nesting order runs from largest structure to DNA segment?",
    ["Cell → nucleus → chromosome → DNA → gene", "Cell → chromosome → nucleus → gene → DNA",
     "Nucleus → cell → DNA → chromosome → gene", "Gene → DNA → chromosome → nucleus → cell"], 0,
    "The illustration nests the gene within DNA, DNA within a chromosome, chromosome in the nucleus, and nucleus in the cell."),
  44: mcq("Which information transfer is stated to be impossible?",
    ["Protein → nucleic acid", "DNA → RNA", "RNA → protein", "RNA → DNA"], 0,
    "The slide permits nucleic-acid transfers and nucleic acid to protein, but not protein back to nucleic acid."),
  45: mcq("Which description defines semiconservative DNA replication?",
    ["Each daughter duplex contains one old strand and one new strand",
     "One daughter duplex contains both old strands and the other both new strands",
     "Both daughter duplexes contain only newly synthesized strands",
     "Parental DNA remains intact while an unrelated duplex is synthesized"], 0,
    "Semiconservative replication preserves one parental strand in each daughter molecule."),
  46: mcq("Which replication-fork pairing is correct?",
    ["Leading strand—continuous; lagging strand—Okazaki fragments",
     "Leading strand—Okazaki fragments; lagging strand—continuous",
     "Leading strand—3′→5′ synthesis; lagging strand—5′→3′ synthesis",
     "Leading strand—requires no primer; lagging strand—requires no primer"], 0,
    "The diagram labels continuous leading synthesis and discontinuous lagging synthesis as Okazaki fragments."),
  47: tap("Video-reference slide acknowledged"),
  48: mcq("What is the sequence of transcription stages listed on the slide?",
    ["Initiation → promoter escape → elongation → termination",
     "Promoter escape → initiation → termination → elongation",
     "Elongation → initiation → promoter escape → termination",
     "Initiation → elongation → promoter escape → termination"], 0,
    "The slide numbers those four stages in that order."),
  49: mcq("How does mRNA sequence compare with the coding (sense) strand?",
    ["It is the same except U replaces T", "It is complementary and uses T instead of U",
     "It is identical including T", "It is unrelated because RNA polymerase reads the coding strand"], 0,
    "mRNA is complementary to the template strand and matches the coding strand except U replaces T."),
  50: mcq("Which sequences are removed when eukaryotic pre-mRNA becomes mature mRNA?",
    ["Introns", "Exons", "The 5′ cap", "The poly(A) tail"], 0,
    "RNA splicing removes non-coding introns and joins exons.")
};

const revised = notes.map((n) => ({
  page: n.page,
  title: n.title,
  explain: n.explain,
  mustKnow: n.mustKnow,
  terms: n.terms,
  diagramGuide: diagramGuide[n.page] || [],
  interaction: I[n.page]
}));

// Avoid a learnable answer-position pattern while preserving each option set.
for (const x of revised) {
  if (x.interaction.type !== "mcq") continue;
  const shift = x.page % 4;
  const old = x.interaction.options;
  const rotated = old.slice(shift).concat(old.slice(0, shift));
  x.interaction.options = rotated;
  x.interaction.answer = (x.interaction.answer - shift + 4) % 4;
}

if (revised.length !== 50 || revised.some((x, i) => x.page !== i + 1)) {
  throw new Error("Expected exactly 50 ordered slides");
}
for (const x of revised) {
  const keys = Object.keys(x).join(",");
  if (keys !== "page,title,explain,mustKnow,terms,diagramGuide,interaction") {
    throw new Error(`Bad schema on page ${x.page}: ${keys}`);
  }
  if (!Array.isArray(x.diagramGuide)) throw new Error(`diagramGuide missing on ${x.page}`);
  if (!x.interaction) throw new Error(`interaction missing on ${x.page}`);
  if (x.interaction.type === "mcq") {
    if (!Array.isArray(x.interaction.options) || x.interaction.options.length !== 4) {
      throw new Error(`MCQ options invalid on ${x.page}`);
    }
    if (!Number.isInteger(x.interaction.answer) || x.interaction.answer < 0 || x.interaction.answer > 3) {
      throw new Error(`MCQ answer invalid on ${x.page}`);
    }
  } else if (![1, 2, 41, 47].includes(x.page)) {
    throw new Error(`Tap used on content slide ${x.page}`);
  }
}

fs.writeFileSync(path.join(dir, "revised-001-050.json"), JSON.stringify(revised, null, 2) + "\n");
console.log("Wrote revised-001-050.json with", revised.length, "slides");
