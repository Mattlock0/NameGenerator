class Iterator(object):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def next(self):
        try:
            result = self.collection[self.index]
            self.index += 1
        except IndexError:
            raise StopIteration
        return result

    def copy_next(self):
        try:
            return self.collection[self.index+1]
        except IndexError:
            raise StopIteration

    def prev(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.collection[self.index]

    def has_next(self):
        if self.index + 1 <= len(self.collection):
            return True
        return False

    def __iter__(self):
        return self
