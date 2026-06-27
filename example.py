from pdf_annotations_to_markdown import extract_annotations_dict, format_annotations

def main():
    # Replace with your PDF file path
    pdf_path = "example.pdf"
    
    # Extract annotations
    annotations = extract_annotations_dict(pdf_path)
    
    # Format annotations into markdown
    markdown_output = format_annotations(annotations)
    
    # Save to file
    output_path = "annotations.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_output)
    
    print(f"Annotations have been saved to {output_path}")

if __name__ == "__main__":
    main() 