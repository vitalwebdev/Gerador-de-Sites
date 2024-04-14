import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link    
)

# Funçao que converte uma string pura (único TextNode) em uma lista de objetos TextNode
# Parâmetros: old_nodes - lista de objetos TextNodes tipo texto (texto puro
#             delimiter - delimitador (formatador markdown)
#             text_type - tipo de texto formatado pelo delimitador
def split_nodes_delimiter(old_nodes: list, delimiter:str, text_type:str):
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)
        else:
            split_nodes = []
            node_text_list = node.text.split(delimiter)
            if len(node_text_list) % 2 == 0:
                raise ValueError("ERRO! Markdown inválido, verificar marcadores não fechados.")
            for i in range(len(node_text_list)):
                if node_text_list[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(node_text_list[i], text_type_text))
                else:
                    split_nodes.append(TextNode(node_text_list[i], text_type))
            new_nodes.extend(split_nodes)
    return new_nodes

# Função para extrair urls de imagens contidas em sentenças markdown
def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

# Função para extrair urls de imagens contidas em sentenças markdown
def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes: list):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            images_list = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(images_list) != 2:
                raise ValueError("ERRO! Markdown inválido, verificar marcação.")
            if images_list[0] != "":
                new_nodes.append(TextNode(images_list[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1],))
            original_text = images_list[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes


def split_nodes_link(old_nodes: list):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            links_list = original_text.split(f"[{link[0]}]({link[1]})", 1)   
            if len(links_list) != 2:
                raise ValueError("ERRO! Markdown inválido, verificar marcação.")
            if links_list[0] != "":
                new_nodes.append(TextNode(links_list[0], text_type_text)) 
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = links_list[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

    