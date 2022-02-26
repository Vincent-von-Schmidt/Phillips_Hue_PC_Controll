
class TextString(str):
    def __init__(self, __text: str):
        super.__init__()
        self.__text = __text

    def replace(self, __old: str, __new: str, __count: int = ...) -> str:
        pass
