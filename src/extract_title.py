def extract_title(markdown):
    md_lines = markdown.split("\n")

    if md_lines[0].startswith("# "):
        return md_lines[0][2:]
