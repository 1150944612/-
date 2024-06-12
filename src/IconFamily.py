class IconFamily:
    def __init__(self):
        self.composite_icon = ''
        self.leaf_icon = ''

    def __init__(self, composite_icon: str, leaf_icon: str):
        self.composite_icon = composite_icon
        self.leaf_icon = leaf_icon

    def load_icon_family(self, composite_icon: str, leaf_icon: str):
        self.composite_icon = composite_icon
        self.leaf_icon = leaf_icon