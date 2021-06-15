class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.diction = {}

    def get(self, key: int) -> int:
        if key not in self.diction.keys():
            return -1
        else:
            rememval = self.diction.pop(key)
            self.diction[key] = rememval
            return self.diction[key]
        

    def put(self, key: int, value: int) -> None:
        if len(self.diction.items())>=self.capacity and key not in self.diction.keys():
            keys = self.diction.keys
            print(self.diction.pop(list(self.diction.keys())[0]))
        if key in self.diction.keys():
            rememval = self.diction.pop(key)
            self.diction[key] = value
        else:
            self.diction[key]=value
        return None



obj = LRUCache(2)
obj.put(2,1)
obj.put(1,1)
obj.put(2,3)
obj.put(4,1)
obj.get(1)
obj.get(2)

