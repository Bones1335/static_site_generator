import htmlnode


class ParentNode(htmlnode.HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        elif self.children is None or self.children == []:
            raise ValueError("Invalid HTML: no children present")
        else:
            child_string = ""
            for child in self.children:
                child_string += child.to_html()
            if self.props is None:
                return f'<{self.tag}>{child_string}</{self.tag}>'
            else:
                return f'<{self.tag}{self.props}>{child_string}</{self.tag}>'


    def __repr__(self):
        return f'ParentNode({self.tag}, {self.children}, {self.props})'
