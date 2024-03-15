class main():
    def IND(self, index):
        print("Indexing is not supported with this instruction")
        return (1)
    def EXEC(self, params):
        text = ""
        if len(params) > 0:
            text = params[0]
        if len(params) > 1:
            return (1)
        return (0, input(text))
    def ATR(self, target):
        print("Getting an attribute is not supported with this instruction")
        return (1)
    def STAT(self, params):
        print("Statements are not supported with this instruction")
        return (1)
    def OP(self, arg1, arg2):
        print("Operations are not supported with this instruction")
        return (1)
