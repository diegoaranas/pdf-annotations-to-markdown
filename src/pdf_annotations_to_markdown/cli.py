import argparse
import sys

from .core import (
    extract_annotations_dict,
    format_annotations,
    format_annotations_by_author,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="extract-pdf-annotations",
        description="Extract annotations from a PDF file and render them as Markdown.",
    )
    parser.add_argument("input", help="Path to the input PDF file")
    parser.add_argument(
        "--out",
        help="Path to the output Markdown file (default: print to stdout)",
    )
    parser.add_argument(
        "--group-by",
        choices=["author", "page"],
        default="author",
        help="How to group the annotations (default: author)",
    )
    args = parser.parse_args()

    annotations = extract_annotations_dict(args.input)

    if not annotations:
        output = "No annotations found."
    elif args.group_by == "page":
        output = format_annotations(annotations)
    else:
        output = format_annotations_by_author(annotations)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(output)
    else:
        print(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
