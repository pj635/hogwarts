#饿汉式
from threading import Lock


class SingleTon1:
    _instance = None
    _id = 0
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_id(self):
        self._id += 1
        return self._id

def test():
    s1 = SingleTon1()
    s2 = SingleTon1()
    print("\n")
    print(s1, s2)


#懒汉式
class SingleTon2:
    _instance = None
    _lock = Lock()
    _id = 0

    def __new__(cls):
        raise Exception("initialize the object failed")

    @classmethod
    def get_instace(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

    def get_id(self):
        self._id += 1
        return self._id

class Test:
    pass
def test2():
    s1 = SingleTon2.get_instace()
    s2 = SingleTon2.get_instace()
    print("\n")
    print(s1, s2)

    t1 = Test()
    t2 = Test()
    print(t1, t2)