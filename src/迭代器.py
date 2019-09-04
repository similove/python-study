from collections.abc import Iterable
from collections.abc import Iterator


class ClassMate(object):
    def __init__(self, tags):
        self.tags = tags
        self.ptr = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.ptr == len(self.tags):
            raise StopIteration
        else:
            res = self.tags[self.ptr]
            self.ptr += 1
            return res


if __name__ == '__main__':
    tags = ['张三', '李四', '王五', '赵六', '田七']
    classmate = ClassMate(tags)
    print(isinstance(classmate, Iterable))
    print(isinstance(classmate, Iterator))
    for tag in classmate:
        print("--->%s" % tag)
