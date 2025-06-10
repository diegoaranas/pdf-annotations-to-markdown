# PDF Annotations to Markdown

A Python tool that converts PDF annotations (highlights, comments, underlines, and strikeouts) into a well-formatted Markdown document.

## Features

- Extracts text from highlighted, underlined, and struck-out annotations
- Preserves comment content associated with annotations
- Organizes annotations by page number
- Formats output in clean, readable Markdown
- Supports multiple annotation types:
  - Highlights
  - Underlines
  - Strike-outs
  - Comments

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from pdf_annotations_to_markdown import extract_annotations_dict, format_annotations

# Extract annotations from a PDF file
annotations = extract_annotations_dict("path/to/your/file.pdf")

# Format annotations into markdown
markdown_output = format_annotations(annotations)

# Save to file
with open("output.md", "w", encoding="utf-8") as f:
    f.write(markdown_output)
```

## Requirements

- Python 3.6+
- PyMuPDF (fitz)
- See `requirements.txt` for full list of dependencies

## License

MIT License 