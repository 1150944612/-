from abc import ABC, abstractmethod
from JsonNode import JsonNode
from IconFamily import IconFamily

class StyledJSONNode:

    def __init__(self, root: JsonNode, icon_family: IconFamily) -> None:
        self._root = root
        self._icon_family = icon_family

    @abstractmethod
    def render(self) -> None:
        pass

class StyledJSONNodeFactory(ABC):

    @abstractmethod
    def create(self, root: JsonNode, icon_family: IconFamily) -> StyledJSONNode:
        pass