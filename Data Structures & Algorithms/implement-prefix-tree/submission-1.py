class PrefixTree:

    def __init__(self):
        self.memory = {}

    def insert(self, word: str) -> None:
        temp = self.memory
        for char in word:
            if char not in temp:
                temp[char] = {}
            temp = temp[char]
        temp["_end"] = True

    def search(self, word: str) -> bool:
        temp = self.memory
        for char in word:
            if char not in temp:
                return False
            temp = temp[char]
        if "_end" in temp:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        temp = self.memory
        for char in prefix:
            if char in temp:
                temp = temp[char]
            else:
                return False
        return True
    # Time comeplxity - O(n)
    # Space complexity - O(t)