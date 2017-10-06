class MathDojo(object):
    def __init__(self):
        self.total = 0

    def add(self, *num):
        for i in num:
            if type(i) == list:
                for j in i:
                    self.total += j
            if type(i) == int:
                self.total += i
            if type(i) == tuple:
                for k in i:
                    self.total += k

        return self

    def subtract(self, *num):
        for i in num:
            if type(i) == list:
                for j in i:
                    self.total -= j
            if type(i) == int:
                self.total -= i
            if type(i) == tuple:
                for k in i:
                    self.total -= k

        return self

    def result(self):
        print self.total

md = MathDojo()
md.add([1], 3, 4, (2, 23)).result()