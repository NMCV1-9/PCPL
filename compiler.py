import os

class compiler():
    def compilecode(self, code, modules, onefile="1"):
        print("Initialising compiler...")
        out = ""
        print("Adding interpreter...")
        out = out + """
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
"""
        print("Adding lexer to output...")
        out = out + """
class lexer():
    def scantill(self, target, goin, ends, RS=False):
        temp = []
        tempt = target[0]
        breaki = None
        f = 1
        ignore = False
        while True:
            index = f
            i = target[f]
            if i == '"' and ignore == False:
                ignore = True
            elif i == '"' and ignore == True:
                ignore = False
            else:
                if ignore == False:
                    if i == ends[goin.index(target[0])]:
                        breaki = index
                        tempt = tempt + i
                        break
                    elif i in goin:
                        TI,tempo = self.scantill(target[index:], goin, ends, True)
                        f += TI
                        temp.append(tempo)
                    else:
                        tempt = tempt + i
                else:
                    tempt = tempt + i
            f += 1
        if breaki == None:
            breaki = len(target)-1
        temp.append(tempt)
        if RS == True:
            return breaki,temp
        else:
            return temp
        
    def tokenGEN(self, target, starts, ends):
        #AST = {}
        #types = {'"': 0, "<": 1, "{": 2, "[": 3, "(": 4, "-":5}
        temp = self.scantill(target, starts, ends)
        #for i in temp:
        #    if type(i) == str:
        #        if i[0] != "-":
        #            AST[i] = types[i[0]]
        #        else:
        #            AST[i] = types[i[0]] + i[1]
        #    else:
        
        return temp
        #return AST
"""
        print("Adding init to output...")
        out = out + """
lexerC = lexer()
interpreterC = interpreter(lexerC)
"""
        print("Reading modules...")
        if onefile == "1":
            instructions = []
            IDs = []
            for i in statusbar(len(modules)):
                file = open(modules[i], 'r')
                file = file.read()
                # os.path.basename(modules[i]).split(".")[0]
                file = file[:6]+os.path.basename(modules[i]).split(".")[0]+file[6:]
                out = out + file + "\n"
                instructions.append(os.path.basename(modules[i]).split(".")[0])
                IDs.append(os.path.basename(modules[i]).split(".")[0]+"main")
            print("Adding INS to output...")
            out = out + "INS = "+str(instructions)+"\n"
            out = out + "IDs = "+str(IDs).replace("'", "")
            print("Adding INS adder to output...")
            out = out + """
for i in range(len(INS)):
    try:
        interpreterC.addinstruction(INS[i], IDs[i](interpreterC))
    except:
        interpreterC.addinstruction(INS[i], IDs[i]())
"""
        else:
            os.mkdir("IS")
            for i in statusbar(len(modules)):
                file = open(modules[i], 'r')
                tcode = file.read()
                file.close()
                # os.path.basename(modules[i]).split(".")[0]
                file = open(f"IS/{os.path.basename(modules[i])}", 'w')
                file.write(tcode)
                file.close()
            print("Adding ISL because onefile is 0...")
            out = out + "RCHAR = " + repr("\r") + "\n"
            out = out + """
import importlib.util
import sys
import os

class statusbar:
    def __init__(self, repeat, length=30, step=1):
        self.length = length
        self.repeat = repeat
        self.steps = repeat/length
        self.step = step

    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        print("["+("#"*int(self.current/self.steps))+(" "*(self.length-int(self.current/self.steps)))+"]"+f"{self.current}/{self.repeat}", end=RCHAR, flush=True)
        if self.current >= self.repeat:
            print()
            raise StopIteration
        self.current += self.step
        return self.current-1

class loader():
    def __init__(self):
        self.instructions = {}
        self.loadedpaths = []
    
    def RISloading(self, path, IR):
        temp = os.listdir(path)
        for i in statusbar(len(temp)):
            i = temp[i]
            if os.path.isdir(path+"/"+i):
                for f in os.listdir(path+"/"+i):
                    if os.path.isfile(path+"/"+i+"/"+f):
                        self.loadIS(path+"/"+i+"/"+f, IR)
            else:
                self.loadIS(path+"/"+i, IR)
        print("finished RIS instruction loading")
                    
    
    def loadIS(self, path, IR):
        spec = importlib.util.spec_from_file_location(os.path.basename(path), path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[os.path.basename(path)] = module
        spec.loader.exec_module(module)
        try:
            self.instructions[os.path.basename(path)] = module.main(IR)
        except:
            self.instructions[os.path.basename(path)] = module.main()
        self.loadedpaths.append(path)
loaderC = loader()
"""
            print("Adding INS adder to output...")
            out = out + """
loaderC.RISloading("IS", interpreterC)
for i in loaderC.instructions:
    interpreterC.addinstruction(i.split(".")[0], loaderC.instructions[i])
"""
        print("Adding STR and END types to output...")
        out = out + """
STRtypes = ['"', "<", "{", "[", "(", ":"]
ENDtypes = ['"', ">", "}", "]", ")", ";"]
"""
        print("Adding target code...")
        code = code.replace("\n", "<PCPL-COM-NEWLINE>")
        out = out + 'code = '+ ('"'*3) + code + ('"'*3)
        print("Adding execution code...")
        out = out + """
for i in code.split("<PCPL-COM-NEWLINE>"):
    AST = lexerC.tokenGEN(i, STRtypes, ENDtypes)
    AST = interpreterC.PREPAST(AST)
    interpreterC.EXECINS(AST)
"""
        print("Done.")
        if onefile == "0":
            print("The folder 'IS' needs to always be in the same directory as the .py file or else the compiled program will crash.")
        return out

class statusbar:
    def __init__(self, repeat, length=30, step=1):
        self.length = length
        self.repeat = repeat
        self.steps = repeat/length
        self.step = step

    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        print("["+("#"*int(self.current/self.steps))+(" "*(self.length-int(self.current/self.steps)))+"]"+f"{self.current}/{self.repeat}", end="\r", flush=True)
        if self.current >= self.repeat:
            print()
            raise StopIteration
        self.current += self.step
        return self.current-1