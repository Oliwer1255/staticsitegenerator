class HTMLNode:
    
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None:
            return ""

        attributes = []

        for attribute in self.props:
            attributes.append(f'{attribute}="{self.props[attribute]}"')

        return " " + " ".join(attributes)
    
    def __repr(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"



class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("No value in LeafNode")
        
        if self.tag == None:
            return self.value
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag in ParentNode")
        
        if self.children == None or len(self.children) == 0:
            raise ValueError("No children in ParentNode")
        
        children_text = ""

        for node in self.children:
            children_text += node.to_html()

        return f'<{self.tag}{self.props_to_html()}>{children_text}</{self.tag}>'