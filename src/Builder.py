from IconFamily import IconFamily
from JsonNodeFactory import JSONNodeFactory
from Factory import TreeStyledJSONNodeFactory, RectangleStyledJSONNodeFactory

class Builder:

    def __init__(self):
        self._icon_families = {
            '1': IconFamily(' ', ' '),
            '2': IconFamily('★', '☆'),
            '3': IconFamily('❀', '❁')
        }
        self._styles_factory = {
            'tree': TreeStyledJSONNodeFactory(),
            'rectangle': RectangleStyledJSONNodeFactory()
        }

    def create(self, filepath: str, icon_family: str, style: str):
        icon_family = self._icon_families[icon_family]
        style_factory = self._styles_factory[style]
        json_node = JSONNodeFactory(filepath).create()
        return style_factory.create(json_node, icon_family)