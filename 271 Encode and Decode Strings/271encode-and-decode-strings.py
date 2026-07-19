class Codec:
    def encode(self, strs):
        encoded_string = ''
        for s in strs:
            encoded_string += str(len(s))+'/:' + s
        return encoded_string

    
    def decode(self,s):
        decoded_string = []
        i = 0
        while i<len(s):
            delim = s.find('/:', i)
            length = int(s[i:delim])
            str_ = s[delim+2:delim+2+length]
            decoded_string.append(str_)
            i=delim+2+length
        return decoded_string