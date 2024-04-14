import os
import shutil

from copystatic import recursive_copy_files
from generate_content import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("Limpando pasta pública...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
        
    print("Copiando arquivos estáticos para pasta pública...")
    recursive_copy_files(dir_path_static, dir_path_public)
    
    print("Gerando página HTML...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html")
    )
    
main()