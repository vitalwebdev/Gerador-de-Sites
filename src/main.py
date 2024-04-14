import os
import shutil

from copystatic import recursive_copy_files
from generate_content import recursive_generate_pages

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
    recursive_generate_pages(dir_path_content, template_path, dir_path_public)
    
    
main()