from abc import ABC, abstractmethod
from typing import List, Callable, Union
import json

id = 0

class JsonNode(ABC):
    def __init__(self, name: str, level: int):
        global id 
        self._name = name
        self._level = level
        self._id = id
        id += 1

    @abstractmethod
    def is_leaf(self) -> bool:
        pass

    @abstractmethod
    def get_childrens(self, function: Callable[['JsonNode'], None]):
        pass
    
class JSONComposite(JsonNode):
    def __init__(self, name: str, level: int):
        super().__init__(name, level)
        self._children: List[JsonNode] = []

    def is_leaf(self) -> bool:
        return False

    def get_childrens(self, function: Callable[['JsonNode'], None]):
        function(self)
        for child in self._children:
            child.get_childrens(function)

    def add_child(self, child: JsonNode):
        self._children.append(child)
    
    def get_children(self) -> List[JsonNode]:
        return self._children

    def __iter__(self):
        return iter(self._children)
    
class JSONLeaf(JsonNode):
    def __init__(self, name: str, level: int, value: Union[str, None]):
        super().__init__(name, level)
        self._value = value

    def is_leaf(self) -> bool:
        return True

    def get_childrens(self, function: Callable[['JsonNode'], None]):
        function(self)

    def get_value(self) -> Union[str, None]:
        return self._value