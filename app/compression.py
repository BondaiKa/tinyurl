import string

class CompressionLink:
    """class that allow to convert long link to short"""
    CHARACTERS = string.printable[:62]
    LEN_CHAR = len(CHARACTERS)

    def __init__(self):
        self.INITIAL_ENCODE = 100_000_000

    def compress_url(self, counter):
        """get counter from redis and encode new short string"""
        self.INITIAL_ENCODE += counter
        shorten_url = self.encode(self.INITIAL_ENCODE)
        return shorten_url

    def encode(self, number):
        """generate new short link according to `id`"""
        ret = []
        while number > 0:
            val = number % self.LEN_CHAR
            ret.append(self.CHARACTERS[val])
            number = number // self.LEN_CHAR
        return "".join(ret[::-1])
