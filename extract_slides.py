import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from pypdf import PdfReader

ROOT = Path("/Users/ambar/Downloads")
OUT = ROOT / "output" / "study-course"

SOURCES = [
    ("Bioenergetics", ROOT / "Bioenergetics.pptx", "pptx", 40),
    ("Gene Expression and Regulation", ROOT / "Gene Expression and Regulation ppt.pptx", "pptx", 35),
    ("Genetic Engineering Applications 1", ROOT / "genetic engg  applications 1.pptx", "pptx", 19),
    ("Genetic Engineering Applications 2", ROOT / "genetic engg and applicatins 2.pptx", "pptx", 7),
    ("Genetic Engineering Applications 3", ROOT / "genetic engg  applications 3.pptx", "pptx", 36),
    ("Biological Motors", ROOT / "sbl" / "Biological Motors.pdf", "pdf", 39),
    ("Cellular Signaling", ROOT / "sbl" / "Cellular Sigaling.pdf", "pdf", 22),
    ("Cell Death and Cell Division", ROOT / "sbl" / "cell death and cell division.pdf", "pdf", 30),
    ("Stem Cells and Differentiation", ROOT / "sbl" / "Stem cells and differentiation.pdf", "pdf", 30),
    ("Host Pathogen Interaction", ROOT / "sbl" / "Host pathogen interaction.pdf", "pdf", 59),
    ("Cell Death Pathways", ROOT / "sbl" / "Lecture 31 SMondal_16102026.pdf", "pdf", 13),
    ("Cancer Biology 1", ROOT / "sbl" / "Lecture 32 SMondal_21102026.pdf", "pdf", 11),
    ("Cancer Biology 2 and Drug Development", ROOT / "sbl" / "Lecture 33 SMondal_23102026.pdf", "pdf", 11),
    ("Drug Development 1", ROOT / "sbl" / "Lecture 34 SMondal_27102026.pdf", "pdf", 9),
    ("Drug Development 2", ROOT / "sbl" / "Lecture 35 SMondal_28102026.pdf", "pdf", 9),
    ("Drug Development and Techniques", ROOT / "sbl" / "Lecture 36 SMondal_30102026.pdf", "pdf", 12),
    ("Techniques in Biochemistry and Biophysics", ROOT / "sbl" / "Lecture 37 SMondal_03112026.pdf", "pdf", 12),
]


def natural_slide_key(name):
    match = re.search(r"slide(\d+)\.xml$", name)
    return int(match.group(1)) if match else 0


def pptx_text(path):
    ns = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}
    slides = []
    with zipfile.ZipFile(path) as archive:
        names = sorted(
            (name for name in archive.namelist() if re.search(r"ppt/slides/slide\d+\.xml$", name)),
            key=natural_slide_key,
        )
        for name in names:
            root = ET.fromstring(archive.read(name))
            pieces = [node.text.strip() for node in root.findall(".//a:t", ns) if node.text and node.text.strip()]
            slides.append("\n".join(pieces))
    return slides


def pdf_text(path):
    reader = PdfReader(path)
    return [(page.extract_text() or "").strip() for page in reader.pages]


result = []
global_page = 1
for lecture, path, kind, expected in SOURCES:
    texts = pptx_text(path) if kind == "pptx" else pdf_text(path)
    if len(texts) != expected:
        raise RuntimeError(f"{lecture}: expected {expected} slides, found {len(texts)}")
    for local_page, text in enumerate(texts, 1):
        result.append(
            {
                "page": global_page,
                "lecture": lecture,
                "slideInLecture": local_page,
                "rawText": text,
            }
        )
        global_page += 1

if len(result) != 394:
    raise RuntimeError(f"Expected 394 total slides, found {len(result)}")

(OUT / "slide-source.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
print(f"Wrote {len(result)} slides to {OUT / 'slide-source.json'}")
