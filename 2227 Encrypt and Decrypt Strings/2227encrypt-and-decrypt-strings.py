class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):        
        self.decryptToEncrypt = {k: v for k, v in zip(keys, values)}
        self.dictToNumber = {}
        for dictItem in dictionary:
            encryptedDictItem = self.encrypt(dictItem)
            if encryptedDictItem != "":
                self.dictToNumber[encryptedDictItem] = self.dictToNumber.get(encryptedDictItem, 0) + 1

    def encrypt(self, word1: str) -> str:
        try:
            output_pieces = [self.decryptToEncrypt[c] for c in word1]
            return "".join(output_pieces)
        except KeyError as e:
            return ""    

    def decrypt(self, word2: str) -> int:
        return self.dictToNumber.get(word2, 0)