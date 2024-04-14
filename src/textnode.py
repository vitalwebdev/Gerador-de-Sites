from htmlnode import LeafNode

# tipos de texto inline
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

# TextNode: classe para representar nós de texto inline (texto puro, negrito, italico, codigo, links, imagens)
# Propriedades: text - conteúdo textual do nó
#               text_type - tipo do texto do nó (ex "bold", "italic", "link")
#               url - url por tras do texto, caso seja um link
class TextNode:
    def __init__(self, text:str, text_type:str, url:str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, __value: object) -> bool:
        if (self.text == __value.text and
            self.text_type == __value.text_type and
            self.url == __value.url):
            return True
        
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
# ===============================================================================================================

# Função para converter instancias TextNode em LeafNode.
#       Parâmetros -> objeto TextNode
#       Retorno -> objeto LeafNode formatado  
def text_node_to_html_node(text_node:object):    
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception(f'ERRO! Tipo de dado "{text_node.text_type}" inválido.')

