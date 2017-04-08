class SubSystemOne:
    def methodOne(self):
        print "SubSysOne"


class SubSystemTwo:
    def methodTwo(self):
        print "SubSysTwo"


class SubSystemThree:
    def methodThree(self):
        print "SubSysThree"


class SubSystemFour:
    def methodFour(self):
        print "SubSysFour"


class Facade:
    def __init__(self):
        self.one = SubSystemOne()
        self.two = SubSystemTwo()
        self.three = SubSystemThree()
        self.four = SubSystemFour()

    def methodA(self):
        print "method A"
        self.one.methodOne()
        self.two.methodTwo()
        self.four.methodFour()

    def methodB(self):
        print "method B"
        self.two.methodTwo()
        self.three.methodThree()


if __name__ == "__main__":
    facade = Facade()
    facade.methodA()
    facade.methodB()
