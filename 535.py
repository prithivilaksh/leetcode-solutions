# class Codec:

#     def encode(self, longUrl: str) -> str:
#         """Encodes a URL to a shortened URL.
#         """
#         return longUrl
        

#     def decode(self, shortUrl: str) -> str:
#         """Decodes a shortened URL to its original URL.
#         """
#         return shortUrl
        

# # Your Codec object will be instantiated and called as such:
# # codec = Codec()
# # codec.decode(codec.encode(url))

# class Codec:

#     def __init__(self):
#         self.cnt=0
#         self.mp={}

#     def encode(self, longUrl: str) -> str:
#         """Encodes a URL to a shortened URL.
#         """
#         self.cnt+=1
#         shortUrl=str(self.cnt)
#         self.mp[shortUrl]=longUrl
#         return shortUrl
        

#     def decode(self, shortUrl: str) -> str:
#         """Decodes a shortened URL to its original URL.
#         """
#         return self.mp[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


import random
import string

class Codec:
    def __init__(self):
        self.chars = string.ascii_letters + string.digits
        self.code_to_url = {}
        self.url_to_code = {}
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]
        
        while True:
            code = "".join(random.choices(self.chars, k=6))
            if code not in self.code_to_url:
                self.code_to_url[code] = longUrl
                self.url_to_code[longUrl] = code
                return self.base_url + code

    def decode(self, shortUrl: str) -> str:
        code = shortUrl.replace(self.base_url, "")
        return self.code_to_url.get(code, "")