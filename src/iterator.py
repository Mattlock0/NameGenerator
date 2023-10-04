class Iterator(object):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __str__(self):
        string = ""
        for index, element in enumerate(self.collection):
            if index == self.index:
                string += f"<{element}>"
            else:
                string += str(element)

        return string

    def __iter__(self):
        return self

    def prev(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.collection[self.index]

    def curr(self):
        return self.collection[self.index]

    def next(self):
        try:
            result = self.collection[self.index]
            self.index += 1
        except IndexError:
            raise StopIteration
        return result

    def has_prev(self):
        if self.index - 1 >= 0:
            return True
        return False

    def has_next(self):
        if self.index + 1 < len(self.collection):
            return True
        return False

    def get_next(self):
        if self.has_next():
            result = self.collection[self.index + 1]
        else:
            result = -1
        return result
