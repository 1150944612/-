from JsonNode import *

class JSONNodeFactory:

    def __init__(self, filepath: str):
        with open(filepath, 'r', encoding='utf-8') as f:
            self.json_data = json.load(f)
    
    def create(self) -> JsonNode:
        return self._create('', 0, self.json_data)

    def _create(self, name: str, level: int, obj) -> JsonNode:
        if isinstance(obj, list):
            return self._create_composite_from_list(name, level, obj)
        elif isinstance(obj, dict):
            return self._create_composite_from_dict(name, level, obj)
        else:
            return self._create_leaf(name, level, obj)

    def _create_composite_from_list(self, name: str, level: int, obj) -> JSONComposite:
        composite = JSONComposite(name, level)
        for idx, item in enumerate(obj):
            child = self._create(f'Array[{idx}]', level + 1, item)
            composite.add_child(child)
        return composite

    def _create_composite_from_dict(self, name: str, level: int, obj) -> JSONComposite:
        composite = JSONComposite(name, level)
        for key, value in obj.items():
            child = self._create(key, level + 1, value)
            composite.add_child(child)
        return composite
    
    def _create_leaf(self, name: str, level: int, obj) -> JSONLeaf:
        if obj is None:
            return JSONLeaf(name, level, None)
        else:
            return JSONLeaf(name, level, str(obj))