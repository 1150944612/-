from AbstractFactory import StyledJSONNode, StyledJSONNodeFactory
from JsonNode import *
from JsonNodeFactory import *
from IconFamily import IconFamily

class TreeStyledJSONNode(StyledJSONNode):
    def __init__(self, root: JsonNode, icon_family: IconFamily):
        super().__init__(root, icon_family)

    def render(self) -> None:
        self._render_branch('', '', self._root)

    def _render(self, prefix_first: str, prefix_follow: str, node: JsonNode) -> None:
        if node.is_leaf():
            self._render_leaf(prefix_first, node)
        else:
            self._render_branch(prefix_first, prefix_follow, node)
    
    def _render_leaf(self, prefix: str, node: JSONLeaf) -> None:
        value = node.get_value()
        if value is None:
            print(f'{prefix}{self._icon_family.leaf_icon}{node._name}')
        else:
            print(f'{prefix}{self._icon_family.leaf_icon}{node._name}: {value}')

    def _render_branch(self, prefix_first: str, prefix_follow: str, node: JSONComposite) -> None:
        if not node._level == 0:
            print(f'{prefix_first}{self._icon_family.composite_icon}{node._name}')
        children = node.get_children()
        if len(children) == 0:
            return
        for child in children[:-1]:
            self._render(f'{prefix_follow}├─', f'{prefix_follow}│  ',child)
        self._render(f'{prefix_follow}└─', f'{prefix_follow}   ', children[-1])

class TreeStyledJSONNodeFactory(StyledJSONNodeFactory):

    def create(self, root: JsonNode, icon_family: IconFamily) -> StyledJSONNode:
        return TreeStyledJSONNode(root, icon_family)
    
class FirstLastDetector:
    def __init__(self, root: JsonNode):
        self.first_visited = False
        root.get_childrens(lambda node: self.function(node))

    def function(self, node: JsonNode):
        if node._level == 0:
            return
        if not self.first_visited:
            self.first_visited = True
            self.first_id = node._id
        else:
            self.last_id = node._id

    def is_first(self, node: JsonNode) -> bool:
        return node._id == self.first_id
    
    def is_last(self, node: JsonNode) -> bool:
        return node._id == self.last_id

class RectangleStyledJSONNode(StyledJSONNode):

    def __init__(self, root: JsonNode, icon_family: IconFamily):
        super().__init__(root, icon_family)
        self._grid_width = 16
        self._root.get_childrens(lambda node: self._update_grid_width(node))
        self.fl_detector = FirstLastDetector(root)
        
    def _update_grid_width(self, node: JsonNode) -> None:
        prefix_length = max((node._level - 1) * 3 + 2, 0)
        name_length = len(node._name) + 2
        if node.is_leaf() and node.get_value() is not None:
            name_length += len(node.get_value()) + 2
        self._grid_width = max(self._grid_width, prefix_length + name_length + 2)
    
    def render(self) -> None:
        self._root.get_childrens(lambda node: self._render(node))

    def _render(self, node: JsonNode) -> None:
        if node._level == 0:
            return
        result = ''

        if self.fl_detector.is_first(node):
            result += "┌─"
        elif self.fl_detector.is_last(node):
            result += "└─"
        elif node._level == 1:
            result += "├─"
        else:
            result += "│ "
            
        if node._level > 2:
            if self.fl_detector.is_last(node):
                result += '─┴─' * (node._level - 2)
            else:
                result += ' │ ' * (node._level - 2)
                
        if self.fl_detector.is_last(node):
            result += '─┴─'
        elif node._level > 1:
            result += ' ├─'
            
        if node.is_leaf():
            result += self._icon_family.leaf_icon
        else:
            result += self._icon_family.composite_icon
            
        result += node._name
        
        if node.is_leaf() and node.get_value() is not None:
            result += f': {node.get_value()}'
            
        result = f'{result} '.ljust(self._grid_width - 2, '─')
        
        if self.fl_detector.is_first(node):
            result += '─┐'
        elif self.fl_detector.is_last(node):
            result += '─┘'
        else:
            result += '─┤'
        print(result)

class RectangleStyledJSONNodeFactory(StyledJSONNodeFactory):

    def create(self, root: JsonNode, icon_family: IconFamily) -> StyledJSONNode:
        return RectangleStyledJSONNode(root, icon_family)
    
