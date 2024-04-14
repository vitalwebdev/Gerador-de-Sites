import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delimiter_bold(self):
        node = TextNode("Texto com palavra em **negrito**, massa.", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("Texto com palavra em ", text_type_text),
                TextNode("negrito", text_type_bold),
                TextNode(", massa.", text_type_text),
            ],
            new_nodes,
        )

    def test_delimiter_bold_2(self):
        node = TextNode("Texto com duas **palavras** em **negrito.**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("Texto com duas ", text_type_text),
                TextNode("palavras", text_type_bold),
                TextNode(" em ", text_type_text),
                TextNode("negrito.", text_type_bold),
            ],
            new_nodes,
        )

    def test_delimiter_bold_multi(self):
        node = TextNode(
            "Texto com um **trecho em negrito** e outra palavra **negrito.**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("Texto com um ", text_type_text),
                TextNode("trecho em negrito", text_type_bold),
                TextNode(" e outra palavra ", text_type_text),
                TextNode("negrito.", text_type_bold),
            ],
            new_nodes,
        )

    def test_delimiter_italic(self):
        node = TextNode("Texto com palavra em *itálico*, parça.", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("Texto com palavra em ", text_type_text),
                TextNode("itálico", text_type_italic),
                TextNode(", parça.", text_type_text),
            ],
            new_nodes,
        )

    def test_delimiter_code(self):
        node = TextNode("Texto com um `bloco de código` top.", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("Texto com um ", text_type_text),
                TextNode("bloco de código", text_type_code),
                TextNode(" top.", text_type_text),
            ],
            new_nodes,
        )

    def test_extract_images(self):
        text = "Este texto possui uma ![imagem](https://i.imgur.com/zjjcJKZ.png) e ![outra imagem](https://i.imgur.com/dfsdkjfd.png)"
        extraction = extract_markdown_images(text)
        self.assertListEqual(extraction, [("imagem", "https://i.imgur.com/zjjcJKZ.png"), ("outra imagem", "https://i.imgur.com/dfsdkjfd.png")])
        
    def test_extract_links(self):
        text = "Este texto possui um [link](https://www.example.com) e [outro link](https://www.example.com/another)"
        extraction = extract_markdown_links(text)
        self.assertListEqual(extraction, [("link", "https://www.example.com"), ("outro link", "https://www.example.com/another")])
        
    def test_split_image(self):
        node = TextNode(
            "Este texto possui uma ![imagem](https://i.imgur.com/zjjcJKZ.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Este texto possui uma ", text_type_text),
                TextNode("imagem", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![imagem](https://www.example.com/image.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("imagem", text_type_image, "https://www.example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "Este texto possui uma ![imagem](https://i.imgur.com/zjjcJKZ.png) e outra ![segunda imagem](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Este texto possui uma ", text_type_text),
                TextNode("imagem", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" e outra ", text_type_text),
                TextNode(
                    "segunda imagem", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "Este texto possui um [link](https://boot.dev) e [outro link](https://blog.boot.dev) com texto em seguida",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Este texto possui um ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" e ", text_type_text),
                TextNode("outro link", text_type_link, "https://blog.boot.dev"),
                TextNode(" com texto em seguida", text_type_text),
            ],
            new_nodes,
        )      

    
if __name__ == "__main__":
    unittest.main()