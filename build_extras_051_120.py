import json
from pathlib import Path


def q(prompt, options, answer, explanation):
    return {
        "q": prompt,
        "options": options,
        "answer": answer,
        "explanation": explanation,
    }


extras = {
    54: [q(
        "Which event belongs to protein maturation after translation rather than RNA processing?",
        ["Removal of introns", "Addition of a 5′ cap", "Chaperone-assisted folding", "Poly(A) tail addition"],
        2,
        "Chaperones assist the newly synthesized polypeptide in acquiring its three-dimensional structure.",
    )],
    56: [q(
        "Which regulatory level is specifically associated with movement of a eukaryotic transcript between compartments?",
        ["Transcription initiation", "RNA transport from nucleus to cytosol", "Ribosome assembly", "DNA replication"],
        1,
        "Eukaryotic gene expression can be regulated during transport of processed RNA from the nucleus to the cytosol.",
    )],
    58: [q(
        "Which feature allows several prokaryotic genes in one operon to be transcribed together?",
        ["Each gene has a separate enhancer", "The gene cluster is controlled by one promoter", "Each gene is on a different chromosome", "The genes use separate RNA polymerases"],
        1,
        "An operon is a cluster of functionally related genes controlled by a single promoter and transcribed as one unit.",
    )],
    60: [q(
        "Which lac-operon product directly transports lactose across the bacterial membrane?",
        ["β-galactosidase", "Lactose permease", "Transacetylase", "Lac repressor"],
        1,
        "LacY encodes lactose permease, the membrane protein that imports lactose.",
    )],
    61: [
        q(
            "Which molecule is the indirect signal through which the lac repressor detects lactose availability?",
            ["Glucose", "cAMP", "Allolactose", "ATP"],
            2,
            "Allolactose binds the lac repressor and signals that lactose is available.",
        ),
        q(
            "Which regulator–signal relationship is correct in the lac operon?",
            ["CAP–allolactose", "CAP–cAMP", "Repressor–cAMP", "RNA polymerase–allolactose"],
            1,
            "CAP senses low glucose indirectly through cAMP, whereas the repressor senses lactose through allolactose.",
        ),
    ],
    62: [q(
        "Which lac gene–product pairing is correct?",
        ["lacZ–lactose permease", "lacY–β-galactosidase", "lacA–transacetylase", "lacA–lac repressor"],
        2,
        "lacA encodes transacetylase; lacZ encodes β-galactosidase and lacY encodes lactose permease.",
    )],
    63: [q(
        "Binding of CAP to its regulatory DNA site primarily promotes transcription by:",
        ["Cleaving the operator", "Helping RNA polymerase bind the promoter", "Destroying the lac repressor", "Converting lactose to allolactose"],
        1,
        "DNA-bound CAP positively regulates the operon by improving RNA-polymerase recruitment to the promoter.",
    )],
    64: [q(
        "In the absence of lactose, which DNA element is occupied by the lac repressor?",
        ["CAP site", "Operator", "lacZ coding region", "Transcription terminator"],
        1,
        "Without allolactose, the repressor binds the operator and obstructs transcription.",
    )],
    66: [
        q(
            "The gene encoding CAP is best described as:",
            ["Part of the lac structural-gene cluster", "Constitutively expressed elsewhere on the chromosome", "Induced only by lactose", "Located within the lac operator"],
            1,
            "The CAP gene is separate from the lac operon and is constitutively expressed.",
        ),
        q(
            "Why does RNA polymerase produce only a few lac transcripts when CAP assistance is absent but repression has been removed?",
            ["The promoter binds RNA polymerase weakly", "The operator cleaves the mRNA", "lacZ inhibits transcription", "cAMP degrades RNA polymerase"],
            0,
            "RNA polymerase alone binds the lac promoter poorly, producing only basal or leaky transcription.",
        ),
    ],
    67: [q(
        "What molecular event converts CAP into its DNA-binding form?",
        ["Binding of lactose", "Binding of cAMP", "Phosphorylation by LacY", "Cleavage by β-galactosidase"],
        1,
        "When glucose is low, cAMP binds CAP and changes its conformation so that it can bind DNA.",
    )],
    68: [
        q(
            "Which condition supplies the positive-regulatory input required for strong lac-operon expression?",
            ["High glucose and low cAMP", "Low glucose and high cAMP", "High glucose and high allolactose only", "Low lactose and inactive CAP"],
            1,
            "Low glucose raises cAMP, activating CAP and allowing it to bind DNA.",
        ),
        q(
            "For strong lac transcription, allolactose and cAMP respectively cause:",
            ["CAP release and repressor binding", "Repressor release and CAP activation", "Repressor activation and CAP degradation", "RNA polymerase release and operator activation"],
            1,
            "Allolactose removes the repressor, while cAMP activates CAP; both conditions are required for strong transcription.",
        ),
    ],
    69: [q(
        "When both glucose and lactose are present, which regulator is inactive because cAMP is low?",
        ["Lac repressor", "CAP", "RNA polymerase", "β-galactosidase"],
        1,
        "Glucose keeps cAMP low, so CAP remains inactive even though lactose removes the repressor.",
    )],
    70: [q(
        "When neither glucose nor lactose is present, which pair is simultaneously DNA-bound?",
        ["Inactive CAP and free repressor", "Active CAP and lac repressor", "Allolactose and RNA polymerase", "LacY and β-galactosidase"],
        1,
        "Low glucose activates CAP, but absent lactose leaves the repressor bound to the operator.",
    )],
    71: [q(
        "Which condition gives low-level rather than strong lac-operon transcription?",
        ["Glucose present, lactose present", "Glucose absent, lactose present", "Glucose absent, lactose absent", "Glucose present, lactose absent"],
        0,
        "With both sugars present, the repressor is removed but CAP is inactive, so only basal transcription occurs.",
    )],
    72: [q(
        "The structural genes of the trp operon encode proteins primarily required for:",
        ["Lactose import", "Tryptophan biosynthesis", "Glucose phosphorylation", "DNA replication"],
        1,
        "The trp structural genes encode enzymes in the tryptophan-biosynthetic pathway.",
    )],
    73: [q(
        "In the presence of abundant tryptophan, the trp repressor becomes able to bind the operator because tryptophan acts as a:",
        ["Substrate", "Inducer", "Co-repressor", "Competitive inhibitor"],
        2,
        "Tryptophan binds the inactive repressor as a co-repressor, activating operator binding.",
    )],
    74: [
        q(
            "How do the newly synthesized repressors of the lac and trp operons differ?",
            ["Both are initially active", "Lac repressor is active; trp repressor is inactive", "Lac repressor is inactive; trp repressor is active", "Both are initially inactive"],
            1,
            "The lac repressor is made active, whereas the trp repressor requires its co-repressor to become active.",
        ),
        q(
            "Which example on the slide is classified as constitutively expressed rather than a regulated luxury gene?",
            ["lacZ", "trpE", "A glycolysis gene", "A lactose-permease gene"],
            2,
            "The slide cites glycolysis genes as housekeeping genes that are constitutively expressed.",
        ),
    ],
    79: [q(
        "After a gene of interest is introduced into a suitable host, which two outcomes may occur according to the definition of genetic engineering?",
        ["Replication and/or expression", "Splicing and/or mutation", "Translation and/or secretion only", "Deletion and/or chromosome loss"],
        0,
        "An introduced gene may be replicated, expressed, or both in the host.",
    )],
    80: [
        q(
            "Which step immediately precedes introduction of recombinant DNA into a host cell?",
            ["Isolation of genomic DNA", "Ligation of insert and vector", "Protein purification", "Screening of colonies"],
            1,
            "The insert is ligated into the vector before the recombinant vector is transferred into a host.",
        ),
        q(
            "What is the primary role of a selectable marker during the workflow?",
            ["Cut the insert DNA", "Identify cells that received the vector", "Induce protein folding", "Determine the insert sequence"],
            1,
            "A selectable marker allows vector-containing cells to survive or otherwise be selected.",
        ),
    ],
    81: [q(
        "Which term denotes DNA formed by joining sequences originating from different sources?",
        ["Vector", "Clone", "Recombinant DNA", "Competent cell"],
        2,
        "Recombinant DNA contains DNA sequences joined from different sources.",
    )],
    82: [
        q(
            "Restriction endonucleases occur naturally in bacteria mainly as protection against:",
            ["Foreign bacteriophage DNA", "Misfolded bacterial proteins", "Excess cellular RNA", "Damaged phospholipids"],
            0,
            "Bacterial restriction enzymes are part of a defense system against invading foreign DNA such as bacteriophage DNA.",
        ),
        q(
            "A typical restriction-enzyme recognition sequence is approximately:",
            ["1–2 base pairs", "4–8 base pairs", "20–30 base pairs", "Hundreds of base pairs"],
            1,
            "The slide states that restriction enzymes usually recognize short sequences 4–8 base pairs long.",
        ),
    ],
    83: [q(
        "Which enzyme shown produces blunt ends rather than staggered cohesive ends?",
        ["EcoRI", "HindIII", "SmaI", "BamHI"],
        2,
        "SmaI cuts straight across both DNA strands, producing blunt ends.",
    )],
    84: [
        q(
            "DNA ligase forms a covalent bond between which adjacent groups?",
            ["5′-OH and 3′-phosphate", "3′-OH and 5′-phosphate", "Two nitrogenous bases", "Two 3′-phosphate groups"],
            1,
            "Ligase seals the backbone by joining a 3′ hydroxyl to an adjacent 5′ phosphate.",
        ),
        q(
            "Compared with blunt-end ligation, sticky-end ligation is generally more efficient because:",
            ["Overhangs base-pair and align the fragments", "Sticky ends do not require ligase", "Blunt ends repel DNA polymerase", "Sticky ends contain ATP"],
            0,
            "Complementary overhangs transiently base-pair, holding the fragments in the correct alignment for ligase.",
        ),
    ],
    85: [q(
        "During T4 DNA-ligase catalysis, AMP is transferred directly to the:",
        ["3′-OH at the DNA end", "5′-phosphate at the DNA end", "Nitrogenous base at the nick", "2′-OH of deoxyribose"],
        1,
        "AMP activates the 5′ phosphate, forming a DNA–AMP intermediate before phosphodiester-bond formation.",
    )],
    86: [q(
        "Which energy source is specifically required by T4 DNA ligase?",
        ["GTP", "ATP", "CTP", "NADPH"],
        1,
        "T4 DNA ligase uses ATP to generate the ligase–AMP intermediate.",
    )],
    87: [q(
        "Which PCR component synthesizes new DNA while tolerating repeated heating?",
        ["RNA polymerase", "Thermostable DNA polymerase", "DNA ligase", "Reverse transcriptase"],
        1,
        "A heat-stable polymerase such as Taq synthesizes DNA through repeated thermal cycles.",
    )],
    88: [q(
        "Using PCR to detect a pathogen depends on amplification of:",
        ["A pathogen-specific nucleic-acid target", "All host genomic DNA equally", "Only bacterial proteins", "Only membrane lipids"],
        0,
        "Diagnostic PCR detects a pathogen by amplifying a nucleic-acid sequence specific to it.",
    )],
    89: [q(
        "Under ideal conditions, how many target copies are expected after 10 PCR cycles from one starting copy?",
        ["20", "100", "512", "1,024"],
        3,
        "Ideal PCR amplification follows 2^n; 2^10 equals 1,024.",
    )],
    90: [
        q(
            "Why does DNA migrate toward the anode during agarose-gel electrophoresis?",
            ["Its bases are positively charged", "Its phosphate backbone is negatively charged", "Agarose carries DNA by osmosis", "DNA binds positively charged SDS"],
            1,
            "The negatively charged phosphate backbone drives DNA toward the positive electrode.",
        ),
        q(
            "A DNA band remaining closest to the loading well most likely contains fragments that are:",
            ["Smaller than all other fragments", "Larger than bands that migrated farther", "More negatively charged per nucleotide", "Single-stranded rather than double-stranded"],
            1,
            "The agarose matrix slows large fragments more strongly, so they remain nearer the wells.",
        ),
    ],
    91: [q(
        "What is produced by occasional ddNTP incorporation during Sanger sequencing?",
        ["Fragments of identical length", "Fragments of different lengths ending at specific bases", "Only full-length double-stranded DNA", "RNA fragments lacking a 5′ cap"],
        1,
        "Random chain termination generates a nested set of DNA fragments ending at each possible nucleotide position.",
    )],
    92: [q(
        "CRISPR-Cas9 originated from a natural bacterial system that functions in defense against:",
        ["Fungi", "Viruses", "Protozoa", "Antibiotics"],
        1,
        "CRISPR-Cas systems evolved as bacterial adaptive defense mechanisms against invading viral genetic material.",
    )],
    93: [
        q(
            "Which repair pathway commonly creates small insertions or deletions after Cas9 cutting?",
            ["Homology-directed repair", "Non-homologous end joining", "Mismatch repair", "Base-excision repair"],
            1,
            "Error-prone non-homologous end joining frequently creates indels that can disrupt a gene.",
        ),
        q(
            "Precise insertion or correction at a Cas9 break requires which combination?",
            ["NHEJ without a template", "HDR with a donor DNA template", "Translation with a guide protein", "Ligase with no homologous sequence"],
            1,
            "Homology-directed repair can copy a designed change from a supplied donor template.",
        ),
    ],
    94: [
        q(
            "Which vector feature provides a defined region containing sites for insertion of foreign DNA?",
            ["Origin of replication", "Selectable marker", "Multiple cloning site", "Centromere"],
            2,
            "The MCS or cloning site contains restriction sites used to insert the gene of interest.",
        ),
        q(
            "Which factor most directly determines whether a plasmid, BAC, or YAC is suitable for a project?",
            ["Insert size and intended application", "Color of the host colony", "Number of introns in the host", "Charge of the encoded protein"],
            0,
            "Vector choice depends chiefly on the size of DNA to be carried and whether cloning or expression is required.",
        ),
    ],
    95: [
        q(
            "Which plasmid-vector feature primarily determines how many vector molecules accumulate per cell?",
            ["Selectable marker", "Origin of replication", "Reporter gene", "Transcription terminator"],
            1,
            "The origin of replication controls autonomous replication and influences plasmid copy number.",
        ),
        q(
            "Which feature is characteristic of the pUC vector series?",
            ["Low copy number and no reporter", "High copy number and lacZα", "A YAC centromere", "Only tetracycline resistance"],
            1,
            "pUC plasmids are high-copy vectors that use lacZα for blue–white screening.",
        ),
    ],
    96: [
        q(
            "In a bacterial expression vector, the ribosome-binding site is required primarily for:",
            ["Plasmid replication", "Translation initiation", "Antibiotic selection", "Transcription termination"],
            1,
            "The ribosome-binding site recruits the bacterial ribosome to initiate translation of the cloned gene.",
        ),
        q(
            "In the pET system, transcription of the cloned gene is driven by a:",
            ["T7 promoter", "lacZα reporter", "KanR promoter", "Eukaryotic enhancer"],
            0,
            "pET expression vectors place the insert downstream of a T7 promoter.",
        ),
    ],
    97: [q(
        "Which reporter–signal pairing is correct?",
        ["GFP–fluorescence", "lacZ–antibiotic resistance", "Luciferase–blue colonies only", "AmpR–luminescence"],
        0,
        "GFP produces fluorescence; lacZ gives a colorimetric signal and luciferase gives luminescence.",
    )],
    98: [
        q(
            "Which host is typically favored for rapid, inexpensive expression when complex post-translational processing is unnecessary?",
            ["E. coli", "Mammalian cells", "Plant cells", "Insect larvae only"],
            0,
            "E. coli grows quickly, is inexpensive, and can produce high protein yields, but lacks eukaryotic processing.",
        ),
        q(
            "Which host-system limitation is correctly matched?",
            ["Yeast–cannot perform any protein folding", "E. coli–no eukaryotic post-translational modifications", "Mammalian cells–cannot secrete proteins", "Plant cells–cannot express recombinant DNA"],
            1,
            "Bacteria generally cannot perform complex eukaryotic modifications such as authentic glycosylation.",
        ),
    ],
    99: [q(
        "In the displayed recombinant-DNA workflow, what follows confirmation of recombinant clones?",
        ["Restriction digestion of the original donor", "Gene-expression induction", "Initial isolation of the gene", "Transformation into competent cells"],
        1,
        "After clones are confirmed, expression is induced before protein production and purification.",
    )],
    100: [
        q(
            "Which starting material contains introns and native regulatory regions?",
            ["cDNA", "Genomic DNA", "Mature mRNA", "Purified recombinant protein"],
            1,
            "Genomic DNA contains introns and genomic regulatory sequences, unlike cDNA copied from mature mRNA.",
        ),
        q(
            "Which enzyme is used to convert mature mRNA into cDNA?",
            ["DNA ligase", "Reverse transcriptase", "Restriction endonuclease", "T7 RNA polymerase"],
            1,
            "Reverse transcriptase synthesizes complementary DNA using RNA as the template.",
        ),
    ],
    102: [
        q(
            "During chemical transformation, plasmid DNA is first mixed with competent bacterial cells under which condition?",
            ["On ice", "At 95°C", "In boiling SDS", "Under ultraviolet light"],
            0,
            "The plasmid and competent cells are incubated on ice before the brief heat shock.",
        ),
        q(
            "Which transformation method uses a short high-voltage pulse to create transient membrane pores?",
            ["Heat shock", "Electroporation", "Centrifugation", "Affinity chromatography"],
            1,
            "Electroporation transiently permeabilizes the membrane with an electric pulse and generally gives high efficiency.",
        ),
    ],
    103: [q(
        "After antibiotic selection, why is a separate screening step still required?",
        ["Selection cannot show whether surviving plasmids contain the insert", "Selection destroys all recombinant plasmids", "Screening makes cells competent", "Screening supplies antibiotic resistance"],
        0,
        "Antibiotic growth establishes vector uptake, but screening distinguishes empty vector from likely recombinant plasmids.",
    )],
    104: [q(
        "Which confirmation method is most directly used to check insert size by the pattern of DNA bands?",
        ["Restriction digestion", "Protein staining", "Affinity chromatography", "Flow cytometry"],
        0,
        "Diagnostic restriction digestion produces fragments whose gel-band sizes can reveal whether the expected insert is present.",
    )],
    105: [q(
        "Which vector element allows recombinant-gene expression to be switched on at a chosen time?",
        ["Inducible promoter", "Origin of replication", "Selectable marker", "Multiple cloning site"],
        0,
        "An inducible promoter permits controlled transcription after addition of an inducer.",
    )],
    106: [
        q(
            "A promoter directly determines which property of recombinant-gene expression?",
            ["When and how strongly transcription occurs", "The amino-acid sequence of the tag", "The plasmid's antibiotic target", "The pore size of the host membrane"],
            0,
            "Promoters regulate the timing, location, and level of transcription.",
        ),
        q(
            "Which expression system shown uses T7 RNA polymerase to transcribe the target gene?",
            ["pET/T7 system", "Ni-NTA system", "SDS-PAGE system", "Blue–white system"],
            0,
            "The pET system uses a T7 promoter recognized by T7 RNA polymerase.",
        ),
    ],
    107: [q(
        "Which operation releases an intracellular recombinant protein before purification?",
        ["Cell lysis", "Culture induction", "Transformation", "Antibiotic selection"],
        0,
        "Cells are lysed after harvesting so the intracellular recombinant protein enters the lysate.",
    )],
    108: [
        q(
            "What is the direct basis of His-tagged protein capture on Ni-NTA resin?",
            ["Histidines coordinate immobilized Ni²⁺", "The tag binds agarose by base pairing", "Imidazole covalently links the protein", "SDS binds the nickel ions"],
            0,
            "Histidine side chains in the tag coordinate Ni²⁺ immobilized on the NTA resin.",
        ),
        q(
            "Why is low imidazole used during the wash step?",
            ["To remove weak nonspecific binders while retaining the His-tagged protein", "To elute the His-tagged protein immediately", "To denature all proteins into peptides", "To polymerize the chromatography resin"],
            0,
            "Low imidazole competes weakly and removes nonspecific proteins; high imidazole is used for target elution.",
        ),
    ],
    109: [q(
        "What is the principal effect of SDS on proteins before PAGE?",
        ["It gives proteins a broadly uniform negative charge", "It gives larger proteins a positive charge", "It attaches a fluorescent antibody", "It preserves native quaternary structure"],
        0,
        "SDS denatures proteins and masks their native charge, making migration depend mainly on molecular size.",
    )],
    111: [
        q(
            "In the two-chain insulin strategy shown, which chains are produced separately in bacteria?",
            ["α and β globin chains", "A and B insulin chains", "Heavy and light antibody chains", "Factor VIII and IX chains"],
            1,
            "The insulin A and B chains are expressed and purified separately, then combined and folded.",
        ),
        q(
            "What stabilizes the final association of insulin's A and B chains?",
            ["Hydrogen bonds to DNA", "Disulfide bonds", "Phosphodiester bonds", "Peptide bonds formed by DNA ligase"],
            1,
            "Correct folding creates disulfide bonds between the insulin chains.",
        ),
    ],
    112: [
        q(
            "Which recombinant protein is used to stimulate red-blood-cell production in chronic kidney disease?",
            ["Human growth hormone", "Erythropoietin", "Interferon-α", "Factor IX"],
            1,
            "Recombinant EPO treats anemia by stimulating erythropoiesis.",
        ),
        q(
            "Hemophilia B is treated with recombinant:",
            ["Factor VIII", "Factor IX", "Erythropoietin", "Human growth hormone"],
            1,
            "Factor IX deficiency causes hemophilia B; factor VIII deficiency causes hemophilia A.",
        ),
    ],
    113: [
        q(
            "The antigen used in the recombinant hepatitis B vaccine is:",
            ["HBsAg", "HIV gp120", "Influenza hemagglutinin", "Tetanus toxin"],
            0,
            "The vaccine contains recombinant hepatitis B surface antigen, HBsAg.",
        ),
        q(
            "Which production host is used for the recombinant hepatitis B surface antigen shown?",
            ["E. coli", "Yeast", "Human erythrocytes", "Tobacco mosaic virus"],
            1,
            "HBsAg is expressed in yeast and purified to make a noninfectious vaccine.",
        ),
    ],
    114: [
        q(
            "A monoclonal antibody is defined by its ability to:",
            ["Bind specifically to one target antigen", "Replicate independently as a plasmid", "Cut DNA at a palindromic site", "Transport lactose into bacteria"],
            0,
            "Monoclonal antibodies are identical antibodies selected for specificity to one antigenic target.",
        ),
        q(
            "Which therapeutic-antibody application shown targets HER2-positive breast cancer?",
            ["Trastuzumab", "Palivizumab", "Erythropoietin", "Interferon-β"],
            0,
            "Trastuzumab binds HER2 and is used in HER2-positive breast cancer.",
        ),
    ],
    115: [
        q(
            "Which gene-therapy strategy aims to reduce expression of a harmful gene using siRNA or antisense molecules?",
            ["Gene addition", "Gene replacement", "Gene silencing", "Gene amplification"],
            2,
            "Gene silencing lowers or stops production from a harmful gene without necessarily changing its DNA sequence.",
        ),
        q(
            "Which strategy directly corrects a mutation at the DNA level?",
            ["Gene editing", "Gene addition", "Protein replacement", "RNA translation"],
            0,
            "Gene editing, for example with CRISPR, changes the genomic DNA sequence itself.",
        ),
    ],
    116: [
        q(
            "In the sickle-cell example, editing the BCL11A enhancer is intended to increase production of:",
            ["Adult hemoglobin A only", "Fetal hemoglobin", "Myoglobin", "Erythropoietin"],
            1,
            "Reducing BCL11A repression reactivates fetal hemoglobin, which helps prevent sickling.",
        ),
        q(
            "CAR-T therapy is best classified as:",
            ["In vivo replacement of a liver gene", "Ex vivo engineering of a patient's immune cells", "Direct injection of recombinant insulin", "Silencing of all T-cell genes"],
            1,
            "T cells are removed, genetically engineered to express a chimeric antigen receptor, and returned to the patient.",
        ),
    ],
    117: [
        q(
            "Which example is an abiotic rather than biotic stress target in crop engineering?",
            ["Insect infestation", "Fungal disease", "Drought", "Viral infection"],
            2,
            "Drought is a nonliving environmental stress; insects and pathogens are biotic stresses.",
        ),
        q(
            "Engineering higher vitamin or essential-amino-acid content primarily targets:",
            ["Nutritional quality", "Herbicide tolerance", "Pathogen resistance", "Delayed flowering only"],
            0,
            "Increasing vitamins, minerals, or essential amino acids is nutritional biofortification.",
        ),
    ],
    118: [
        q(
            "Bt Cry toxins are derived from which organism?",
            ["Bacillus thuringiensis", "Escherichia coli", "Agrobacterium tumefaciens", "Saccharomyces cerevisiae"],
            0,
            "Bt crops express Cry proteins originally produced by the bacterium Bacillus thuringiensis.",
        ),
        q(
            "Which practice is most directly needed to address a major long-term limitation of Bt crops?",
            ["Insect-resistance management", "Increasing chemical insecticide residues", "Removing the Cry gene from all seeds", "Preventing beta-carotene synthesis"],
            0,
            "Target insects can evolve resistance to Cry toxins, so resistance-management strategies are required.",
        ),
    ],
    119: [
        q(
            "In Golden Rice, beta-carotene accumulates specifically in the:",
            ["Root cortex", "Leaf cuticle", "Grain endosperm", "Pollen wall"],
            2,
            "The carotenoid pathway is engineered in the edible rice endosperm.",
        ),
        q(
            "Golden Rice is an example of which crop-improvement approach?",
            ["Nutritional biofortification", "Herbicide detoxification", "Insecticidal-protein production", "Delayed fruit softening"],
            0,
            "It increases provitamin A in a staple crop to improve micronutrient intake.",
        ),
    ],
    120: [
        q(
            "Which engineered trait most directly reduces post-harvest losses by keeping fruit firm longer?",
            ["Disease resistance", "Delayed ripening", "Herbicide tolerance", "Cold sensitivity"],
            1,
            "Delayed ripening extends shelf life and reduces spoilage after harvest.",
        ),
        q(
            "A transgenic crop that survives salinity has been engineered primarily for:",
            ["Biotic-stress resistance", "Abiotic-stress tolerance", "Nutritional biofortification", "Insecticidal activity"],
            1,
            "Salinity is a nonliving environmental condition and therefore an abiotic stress.",
        ),
    ],
}

# Distribute correct answers evenly across A-D without changing question content.
question_number = 0
for page in sorted(extras):
    for question in extras[page]:
        desired_position = question_number % 4
        current_position = question["answer"]
        question["options"][current_position], question["options"][desired_position] = (
            question["options"][desired_position],
            question["options"][current_position],
        )
        question["answer"] = desired_position
        question_number += 1

payload = [{"page": page, "questions": questions} for page, questions in sorted(extras.items())]
out = Path(__file__).with_name("extras-051-120.json")
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Wrote {out} with {len(payload)} dense slides and {sum(len(x['questions']) for x in payload)} questions")
