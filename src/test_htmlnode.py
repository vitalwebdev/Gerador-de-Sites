import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "link 1", [], {"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')
        
    def test_leaf_node(self):
        node = LeafNode("p", "Isto é um parágrafo")
        self.assertEqual(node.to_html(), '<p>Isto é um parágrafo</p>')
        
    def test_leaf_node2(self):
        node = LeafNode("a", "Clique aqui", {"href": "https://google.com"})
        self.assertEqual(node.to_html(), '<a href="https://google.com">Clique aqui</a>')
        
    def test_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Texto em negrito"),
                LeafNode(None, "Texto puro"),
                LeafNode("i", "Texto italico"),
                LeafNode(None, "Texto puro")
            ],
        )
        self.assertEqual(node.to_html(), '<p><b>Texto em negrito</b>Texto puro<i>Texto italico</i>Texto puro</p>')
        
    def test_parent_node2(self):
        node = ParentNode(
                "div",
                [
                    ParentNode("div", 
                               [
                                   LeafNode("h1", "Titulo 1", {"id": "titulo-principal"}),
                                   LeafNode("p", "Isto é um parágrafo.", {"class": "texto-principal"})
                                ],
                               ),
                    LeafNode("p", "Isto é um parágrafo.")
                ]
        )
        self.assertEqual(node.to_html(), '<div><div><h1 id="titulo-principal">Titulo 1</h1><p class="texto-principal">Isto é um parágrafo.</p></div><p>Isto é um parágrafo.</p></div>')

if __name__ == '__main__':
    unittest.main()
