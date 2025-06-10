import fitz
from collections import defaultdict
from .constants import PDF_ANNOT_HIGHLIGHT, PDF_ANNOT_UNDERLINE, PDF_ANNOT_STRIKE_OUT

def extract_marked_text(page: fitz.Page, annot: fitz.Annot) -> str:
    """
    Extract the text content that was marked up (highlighted, underlined, or struck out) in a PDF annotation.
    
    This function handles three types of marked annotations:
    - Highlights (PDF_ANNOT_HIGHLIGHT)
    - Underlines (PDF_ANNOT_UNDERLINE)
    - Strike-outs (PDF_ANNOT_STRIKE_OUT)
    
    Parameters:
        page (fitz.Page): The PDF page object containing the annotation
        annot (fitz.Annot): The annotation object containing the marked
        
    Returns:
        str: The extracted text content that was marked up, or None if no text could be extracted
    """
    text_parts = []
    quads = annot.vertices

    if quads is None:
        return text_parts

    for i in range(0, len(quads), 4):
        if i + 3 >= len(quads):
            break

        ul = quads[i]
        ur = quads[i+1]
        ll = quads[i+2]
        lr = quads[i+3]

        quad = fitz.Quad(ul, ur, ll, lr)
        text = page.get_text("text", clip=quad.rect)
        text_parts.append(text)

    return ''.join(text_parts).strip()

def extract_annotations_dict(file_path: str) -> list[dict]:
    """
    Extract annotations from a PDF file and return them as a list of dictionaries.
    
    Parameters:
        file_path (str): The path to the PDF file

    Returns:
        list[dict]: A list of dictionaries containing the annotations
    """
    doc = fitz.open(file_path)
    annotations = []

    for page_num, page in enumerate(doc):
        for annot in page.annots():
            content = annot.info.get("content", "").strip() or None
            marked = None

            if annot.type[0] in (PDF_ANNOT_HIGHLIGHT, PDF_ANNOT_UNDERLINE, PDF_ANNOT_STRIKE_OUT):
                marked = extract_marked_text(page, annot)

            annotations.append({
                "page": page_num + 1,
                "type": annot.type[1],
                "type_id": annot.type[0],
                "marked_text": marked,
                "comment": content})

    return [a for a in annotations if a["comment"] or a["marked_text"]]

def format_quote(quote: str) -> str:
    """
    Format a multi-line text to fit the 'quote' format in markdown.

    Parameters:
        quote (str): The multi-line text to format

    Returns:
        str: The formatted text
    """
    return "\n".join([f"> {line.strip()}" for line in quote.split("\n")]).strip()

def format_annotations(annotations: list[dict]) -> str:
    """
    Format annotations from a list of dictionaries into a formatted string.
    
    Parameters:
        annotations (list[dict]): A list of dictionaries containing annotation information

    Returns:
        str: A formatted string containing the annotations
    """
    lines = ["# Reviewer Comments and Annotations", "\n"]

    grouped = defaultdict(list)
    for ann in annotations:
        grouped[ann['page']].append(ann)

    comment_num = 1

    for page in sorted(grouped.keys()):
        lines.append(f"### Page # {page}\n")

        for i, ann in enumerate(grouped[page], start=1):
            lines.append(f"#### Comment {comment_num}\n")
            comment_num += 1

            if ann['marked_text'] is not None and ann['marked_text'] != "":
                lines.append(f"{format_quote(ann['marked_text'])}\n")

            comment = ann['comment'].strip() if ann['comment'] else "—"
            lines.append(f"{comment}\n")

    return "\n".join(lines) 