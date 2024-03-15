class main():
    def __init__(self, interpreter):
        self.interpreter = interpreter
        
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
        class temp():
            def __init__(self, interpreter):
                self.interpreter = interpreter
                self.CS = ""
                self.STRtypes = ['"', "<", "{", "[", "(", ":"]
                self.ENDtypes = ['"', ">", "}", "]", ")", ";"]
            def IND(self, index):
                return (0, self.CS[index])
            def EXEC(self, params):
                PREPEDAST = self.interpreter.lexer.tokenGEN(self.CS, self.STRtypes, self.ENDtypes)
                PREPEDAST = self.interpreter.PREPAST(PREPEDAST)
                PREPEDAST = self.interpreter.EXECINS(PREPEDAST)
                return (0, PREPEDAST)
            def ATR(self, target):
                return (0, self.CS)
            def STAT(self, params):
                self.CS = params[0]
                return (0, None)
            def OP(self, arg1, arg2):
                print("Operations are not supported with this CI")
                return (1)
        tempC = temp(self.interpreter)
        self.interpreter.vars[params[0]] = tempC
        return (0, None)
    def OP(self, arg1, arg2):
        print("Operations are not supported with this instruction")
        return (1)
