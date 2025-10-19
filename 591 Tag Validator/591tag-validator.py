class Solution:
    def isValid(self, code):
        if code == 't':
            return False
        code = re.sub(r'<!\[CDATA\[.*?\]\]>', 'c', code)
        prev = None
        while code != prev:
            prev = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
        return code == 't'