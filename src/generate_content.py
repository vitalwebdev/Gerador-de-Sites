import os
from pathlib import Path
from block_markdown import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("ERRO! Título não encontrado.")

def generate_page(from_path, template_path, final_path):
    print(f" * {from_path} {template_path} -> {final_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()
    
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()
    
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()
    
    title = extract_title(markdown_content)
    template = template.replace("{{ Titulo }}", title)
    template = template.replace("{{ Conteudo }}", html)
    
    final_dir_path = os.path.dirname(final_path)
    if final_dir_path != "":
        os.makedirs(final_dir_path, exist_ok=True)
    to_file = open(final_path, "w")
    to_file.write(template)
    
def recursive_generate_pages(dir_path_content, template_path, final_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        final_path = os.path.join(final_dir_path, filename)
        if os.path.isfile(from_path):
            final_path = Path(final_path).with_suffix(".html")
            generate_page(from_path, template_path, final_path)
        else:
            recursive_generate_pages(from_path, template_path, final_path)