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
        if str(params[1]) == "True":
            if params[0] in self.interpreter.instructions:
                self.interpreter.instructions[params[0]].EXEC([])
            elif params[0] in self.interpreter.vars:
                self.interpreter.vars[params[0]].EXEC([])
        return (0, None)
    def OP(self, arg1, arg2):
        print("Operations are not supported with this instruction")
        return (1)
