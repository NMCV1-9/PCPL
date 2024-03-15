class interpreter():
    def __init__(self, lexer):
        self.instructions = {}
        self.lexer = lexer
        self.vars = {}
        self.types = {"<": self.INDEXING, "{": self.EXECUTE, "[": self.ATTRIBUTING, "(": self.STATEMENT, ":": self.OPERATION}
        
    def addinstruction(self, name, instruction):
        self.instructions[name] = instruction
    
    def INDEXING(self, target):
        target = target[1:]
        target = target[:-1]
        target = target.split(",")
        for i in range(len(target)):
            target[i] = target[i].replace(".", ",")
        if target[0] in self.instructions:
            return self.instructions[target[0]].IND(target[1])
        else:
            return self.vars[target[0]].IND(target[1])
        
    def EXECUTE(self, target):
        target = target[1:]
        target = target[:-1]
        target = target.split(",")
        for i in range(len(target)):
            target[i] = target[i].replace(".", ",")
        if target[0] in self.instructions:
            return self.instructions[target[0]].EXEC(target[1:])
        else:
            return self.vars[target[0]].EXEC(target[1:])
        
    def ATTRIBUTING(self, target):
        target = target[1:]
        target = target[:-1]
        target = target.split(",")
        for i in range(len(target)):
            target[i] = target[i].replace(".", ",")
        if target[0] in self.instructions:
            return self.instructions[target[0]].ATR(target[1])
        else:
            return self.vars[target[0]].ATR(target[1])
        
    def STATEMENT(self, target):
        target = target[1:]
        target = target[:-1]
        target = target.split(",")
        for i in range(len(target)):
            target[i] = target[i].replace(".", ",")
        if target[0] in self.instructions:
            return self.instructions[target[0]].STAT(target[1:])
        else:
            return self.vars[target[0]].STAT(target[1:])
        
    def OPERATION(self, target):
        target = target[1:]
        target = target[:-1]
        target = target.split(",")
        for i in range(len(target)):
            target[i] = target[i].replace(".", ",")
        if target[0] in self.instructions:
            return self.instructions[target[0]].OP(target[1], target[2])
        else:
            return self.vars[target[0]].OP(target[1], target[2])
        
    def EXECINS(self, target):
        back = self.types[target[0]](target)
        if back[0] == 1:
            raise TypeError(f"Error in instruction, HALT! {target}")
        return back
    
    def PREPAST(self, target):
        # return codes 0: Normal 1: Error
        # print(f"Error in instruction, HALT! {target}")
        ACM = ""
        for i in range(len(target)):
            index = i
            i = target[i]
            if type(i) == list:
                i = self.PREPAST(i)
            #i = i.replace('"', "")
            if index != len(target)-1:
                if i[0] in self.types:
                    back = self.EXECINS(i)
                    ACM = ACM + "," + str(back[1])
                else:
                    ACM = ACM + i
            else:
                i = i[:-1]+ ACM + i[-1]
                return i

        


