import os

from block_level_markdown import markdown_to_html_node
from extract_title import extract_title


def generate_pages(from_path, template_path, to_path):
    print(os.listdir(from_path))
    for content in os.listdir(from_path):
        content_path = os.path.join(from_path, content)

        if os.path.isfile(content_path):
            generate_page(content_path, template_path, os.path.join(to_path, content.replace(".md", ".html")))
        if os.path.isdir(content_path):
            if not os.path.exists(os.path.join(to_path, content)):
                os.makedirs(content, exist_ok=True)
            generate_pages(content_path, template_path, os.path.join(to_path, content))


def generate_page(from_path, template_path, to_path):
    print(f"Generating page from {from_path} to {to_path} using {template_path}")
    markdown = open(from_path, 'r')
    md_contents = markdown.read()
    markdown.close()

    template = open(template_path, 'r')
    template_file = template.read()
    template.close()

    title = extract_title(md_contents)

    html_nodes = markdown_to_html_node(md_contents)
    html_string = html_nodes.to_html()

    template_title = template_file.replace("{{ Title }}", title)
    template_content = template_title.replace("{{ Content }}", html_string)

    to_dir_path = os.path.dirname(to_path)
    if to_dir_path != "":
        os.makedirs(to_dir_path, exist_ok=True)
    to_file = open(to_path, "w")
    to_file.write(template_content)
