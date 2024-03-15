class main():
    def IND(self, index):
        print("Indexing is not supported with this instruction")
        return (1)
    def EXEC(self, params):
        print("Execution is not supported with this instruction")
        return (1)
    def ATR(self, target):
        print("Getting an attribute is not supported with this instruction")
        return (1)
    def STAT(self, params):
        print("Statements are not supported with this instruction")
        return (1)
    def OP(self, arg1, arg2):
        if arg1.isnumeric() and arg2.isnumeric():
            return (0, int(arg1)*int(arg2))
        else:
            return (0, arg1*arg2)