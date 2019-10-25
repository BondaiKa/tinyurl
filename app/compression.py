class CompressionLink:
    id = 100000000

    def compress_url(self, counter):
        self.id += counter
        shorten_url = self.encode(self.id)
        return shorten_url

    def encode(self, id):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)
        ret = []
        while id > 0:
            val = id % base
            ret.append(characters[val])
            id = id // base
        return "".join(ret[::-1])
