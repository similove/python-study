from collections.abc import Iterable, Iterator


class ClassMate(object):
    def __init__(self, tags):
        self.tags = tags
        self.ptr = 0

    def add(self, tag):
        self.tags.append(tag)

    def __iter__(self):
        return self

    def __next__(self):
        if self.ptr < len(self.tags):
            res = self.tags[self.ptr]
            self.ptr += 1
            return res
        else:
            raise StopIteration


if __name__ == '__main__':
    classmate = ClassMate(tags=[])
    classmate.add('有为青年')
    classmate.add('青春活力')
    classmate.add('年轻有为')
    print(isinstance(classmate, Iterator))
    print(isinstance(classmate, Iterable))
    for t in classmate:
        print(t)
