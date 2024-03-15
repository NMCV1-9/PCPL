class main():
    def IND(self, index):
        print("Indexing is not supported with this instruction")
        return (1)
    def EXEC(self, params):
        end = "\n"
        flush = False
        text = ""
        if len(params) > 0:
            text = params[0]
        if len(params) > 1:
            end = params[1]
        if len(params) > 2:
            flush = bool(params[2])
        if len(params) > 3:
            return (1)
        print(text, end=end, flush=flush)
        return (0, None)
    def ATR(self, target):
        print("Getting an attribute is not supported with this instruction")
        return (1)
    def STAT(self, params):
        print("Statements are not supported with this instruction")
        return (1)
    def OP(self, arg1, arg2):
        print("Operations are not supported with this instruction")
        return (1)
