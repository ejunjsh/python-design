class Operation(object):
    def GetResult(self):
        pass


class OperationAdd(Operation):
    def GetResult(self):
        return self.op1 + self.op2


class OperationSub(Operation):
    def GetResult(self):
        return self.op1 - self.op2


class OperationMul(Operation):
    def GetResult(self):
        return self.op1 * self.op2


class OperationDiv(Operation):
    def GetResult(self):
        try:
            result = self.op1 / self.op2
            return result
        except:
            print "error:divided by zero."
            return 0


class OperationUndef(Operation):
    def GetResult(self):
        print "Undefine operation."
        return 0


class OperationFactory:
    operation = {"+": OperationAdd(), "-": OperationSub(), "/": OperationDiv(), "*": OperationMul()}

    def createOperatioin(self, ch):
        if ch in self.operation:
            op = self.operation[ch]
        else:
            op = OperationUndef()
        return op


if __name__ == "__main__":
    op = raw_input("operator: ")
    opa = input("a: ")
    opb = input("b: ")
    factory = OperationFactory()
    cal = factory.createOperatioin(op)
    cal.op1 = opa
    cal.op2 = opb
    print cal.GetResult()
