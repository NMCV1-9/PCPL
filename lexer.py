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
    
        
        