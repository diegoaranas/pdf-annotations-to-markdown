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
pip install -e .
```

This installs the `pdf_annotations_to_markdown` package and the
`extract-pdf-annotations` command-line tool. You can also install via
`pip install -r requirements.txt`, which performs the same editable install.

## Command-line usage

```bash
extract-pdf-annotations <input.pdf> --out <output.md> [--group-by author|page]
```

- `--out` is optional; if omitted, the Markdown is printed to stdout.
- `--group-by` defaults to `author`, grouping annotations under a `## <author>`
  heading for each reader (annotations with no author are grouped under
  `Unattributed`). Pass `--group-by page` for the page-grouped layout.
- If the PDF has no extractable annotations, the tool prints
  `No annotations found.` and exits 0.

## Library usage

```python
from pdf_annotations_to_markdown import extract_annotations_dict, format_annotations_by_author

# Extract annotations from a PDF file
annotations = extract_annotations_dict("path/to/your/file.pdf")

# Format annotations into markdown, grouped by author
markdown_output = format_annotations_by_author(annotations)

# Save to file
with open("output.md", "w", encoding="utf-8") as f:
    f.write(markdown_output)
```

Use `format_annotations` instead of `format_annotations_by_author` for the
page-grouped layout. Each annotation dict includes an `author` key sourced from
the PDF annotation's title field (`None` when the annotation has no author).

## Requirements

- Python 3.8+
- PyMuPDF (fitz)
- See `pyproject.toml` for the full list of dependencies

## License

MIT License 