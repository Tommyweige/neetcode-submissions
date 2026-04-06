class MyHashSet:

    def __init__(self):
        self.hs = []
        self.output = []

    def add(self, key: int) -> None:
        self.hs.append(key)


    def remove(self, key: int) -> None:
        self.hs[:] = [x for x in self.hs if key != x]
        

    def contains(self, key: int) -> bool:
        return True if key in self.hs else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)