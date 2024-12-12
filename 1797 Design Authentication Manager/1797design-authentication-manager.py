class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl  = timeToLive
        self.expiry = {}


    def generate(self, tokenId: str, currentTime: int) -> None:
        self.expiry[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        
        if tokenId in self.expiry and self.expiry[tokenId] > currentTime:
            self.expiry[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token in self.expiry:
            if self.expiry[token] > currentTime:
                count += 1
        
        return count