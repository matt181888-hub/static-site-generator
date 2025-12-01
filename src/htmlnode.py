class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_description = ""
        for prop in self.props:
            sentence = f' {prop}="{self.props[prop]}"'
            props_description += sentence
        return props_description
        


    def __repr__(self):
        return f"tag = {self.tag}\nvalue = {self.value}\nchildren = {self.children}\nprops = {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):

        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"
        if not self.value:
            print("Bad LeafNode:", repr(self))
            raise ValueError       
        if not self.tag:
            return f"{self.value}"
        else:
            if not self.props:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            if self.props:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("missing tag")
        if not self.children:
            raise ValueError("missing children")
        else:
            final_string = f"<{self.tag}{self.props_to_html()}>"
            for child in self.children:
                final_string += child.to_html()
            return final_string+f"</{self.tag}>"



        
    

    