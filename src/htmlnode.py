# HTMLNode: classe que irá representar nós na árvore (DOM) HTML e renderizar
#           a si mesma como HTML
# Propriedades: tag - tipo da tag HTML (ex "p", "div", "a")
#               value - valor da tag HTML (ex texto dentro de uma tag p)
#               children - lista dos filhos (objetos HTMLNode) imediatos deste nó
#               props - dicionario contendo os atributos do nó, no formato {"atributo": "valor"}
class HTMLNode:
    def __init__(self, 
                 tag:str = None, 
                 value:str = None, 
                 children:list = None, 
                 props:dict = None
                 ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("função não implementada")
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        props_string = ""
        for prop in self.props:
            props_string += f' {prop}="{self.props[prop]}"'        
        return props_string
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
 
# LeafNode: classe para representar os nós folhas (pontas) da DOM
# Propriedades: herda da classe HTMLNode, não possui nós filhos  (children) 
class LeafNode(HTMLNode):
    def __init__(self, tag:str, value:str, props:dict = None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("ERRO!! Este nó requere um valor.")
        
        if self.tag is None:
            return self.value       
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


# ParentNode: classe que irá lidar com aninhamento de nós HTML
# Propriedades: herda da classe HTMLNode, não possue valor (value), lista de nós filhos (children) é obrigatório
class ParentNode(HTMLNode):
    def __init__(self, tag:str, children:list, props:dict = None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("ERRO! Tag HTML requerida.")        
        if self.children is None:
            raise ValueError("ERRO! LeafNode requere nós filhos.")
        
        children_str = ""
        for child in self.children:
            children_str += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{children_str}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
    

        
            
    