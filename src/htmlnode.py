
class HTMLNode:
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props==None:
            return ""
        result = []
        for key, value in self.props.items():
            result.append(f" {key}=\"{value}\"")
        return ''.join(result)
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value== other.value and self.children==other.children and self.props==other.props

    def __repr__(self):
        return f"tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value:str, props:dict=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError('(leaf)Node has no value')
        elif not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag:str, children:list, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError('(parent)Node has no tag')
        elif not self.children:
            raise ValueError('(parent)Node has no children')
        def recurse_children(children):
            if not children:
                return ''
            return children[0].to_html() + recurse_children(children[1:])
        return f"<{self.tag}{self.props_to_html()}>{recurse_children(self.children)}</{self.tag}>"
            

        