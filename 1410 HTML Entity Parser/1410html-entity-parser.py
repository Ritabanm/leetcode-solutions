import re


class Solution:
    def __init__(self):
        self.parser = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
        }

    def entityParser(self, text: str) -> str:
        pattern = r"\&(\w*)\;"
        return re.sub(
            pattern,
            lambda m: self.parser.get(m.group(0)) or m.group(0),
            text,
        )