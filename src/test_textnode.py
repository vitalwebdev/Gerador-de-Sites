import unittest
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,    
)

# classe que concentra todos os métodos de teste
class TestTextNode(unittest.TestCase):
    
    # teste para verificar se dois objetos TextNode são iguais
    def test_equal(self):
        node = TextNode("Isto é um nó de texto", text_type_text)
        node2 = TextNode("Isto é um nó de texto", text_type_text)
        self.assertEqual(node, node2)
    
    # teste para verificar se dois objetos TextNode são diferentes  
    def test_not_equal_text(self):
        node = TextNode("Isto é um nó de texto", text_type_bold)
        node2 = TextNode("Isto é um nó de texto", text_type_italic)        
        self.assertNotEqual(node, node2)        
        
    def test_not_equal_text_type(self):
        node = TextNode("Isto é um nó de texto", text_type_link)
        node2 = TextNode("Isto é um nó de texto diferente", text_type_link)
        self.assertNotEqual(node, node2)
        
    def test_equal_url(self):
        node = TextNode("Isto é um nó de texto", text_type_link, "https://boot.dev")
        node2 = TextNode("Isto é um nó de texto", text_type_link, "https://boot.dev")
        self.assertEqual(node, node2)
        
    def test_not_equal_url(self):
        node = TextNode("Isto é um nó de texto", text_type_link, "https://boot.dev")
        node2 = TextNode("Isto é um nó de texto", text_type_link)
        self.assertNotEqual(node, node2)   


if __name__ == "__main__":
    unittest.main()
