# https://leetcode.com/problems/design-hashset/description/


class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def _get_bucket(self, key: int) -> list:
        return self.buckets[hash(key) % self.size]

    def add(self, key: int) -> None:
        if key not in (bucket := self._get_bucket(key)):
            bucket.append(key)

    def remove(self, key: int) -> None:
        if key in (bucket := self._get_bucket(key)):
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        return key in self._get_bucket(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
