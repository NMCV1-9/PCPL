import importlib
import sys
version = 0.3
modules = ["interpreter", "ISL", "lexer", "compiler"]
initmodules = {}
def INITMODULES():
    global loader
    global lexer
    global interpreter
    global compiler
    print("Loading modules...")
    print("--------------------------------")
    for i in modules:
        print(i)
        try:
            initmodules[i] = importlib.import_module(i)
        except ModuleNotFoundError:
            print(f"Module '{i}' is missing! Exiting.", end="\r", flush=True)
            exit()
    print("--------------------------------")
    print("Modules loaded")
    print("Initialising ISL...")
    loader = initmodules["ISL"].loader()
    print("Initialising lexer...")
    lexer = initmodules["lexer"].lexer()
    print("Initialising interpreter...")
    interpreter = initmodules["interpreter"].interpreter(lexer)
    print("Initialising compiler...")
    compiler = initmodules["compiler"].compiler()
INITMODULES()
print("Types")
STRtypes = ['"', "<", "{", "[", "(", ":"]
ENDtypes = ['"', ">", "}", "]", ")", ";"]
print("Types initialised")
print(f"PCPL Command Line Version {version}, Made by ☐☐☐☐☐☐ ☐☐☐☐☐.")
print(f"Type 'help' to get a list of commands.")
commands = ["compile <path> <target>        compiles the file at the specified path and writes output to target", "load <path>         executes the file at the specified path", "Reload-M        Reloads core modules", "LIS <target instruction set name>        loads the specific instruction set under the file path", "exit           exits the PCPL Command Line", "help        Prints this message"]
while True:
    command = input(">")
    if command.startswith("compile"):
        if len(command.split(" ")) != 4:
            print("The compile command only accepts three parameters! <src> <dst> <onefile 1/0>")
        else:
            print(f"compiling {command.split(' ')[1]} as {command.split(' ')[3]} and saving at {command.split(' ')[2]}. y/n?")
            while True:
                temp = input("compile? >")
                if temp == "y":
                    targetfile = open(command.split(" ")[1], 'r')
                    code = targetfile.read()
                    targetfile.close()
                    code = compiler.compilecode(code, loader.loadedpaths, command.split(" ")[3])
                    targetfile = open(command.split(" ")[2], 'w')
                    targetfile.write(code)
                    targetfile.close()
                    break
                elif temp == "n":
                    break
    elif command.startswith("load"):
        if len(command.split(" ")) != 2:
            print("The load command only accepts one parameter!")
        else:
            targetfile = open(command.split(" ")[1], 'r')
            code = targetfile.read()
            targetfile.close()
            for i in code.split("\n"):
                #try:
                if True:
                    AST = lexer.tokenGEN(i, STRtypes, ENDtypes)
                    AST = interpreter.PREPAST(AST)
                    interpreter.EXECINS(AST)[1]
                #except Exception as e:
                    #print(f"Critical Error, HALT! {e}")
                    #break
    elif command.startswith("Reload-M"):
        INITMODULES()
    elif command.startswith("help"):
        for i in commands:
            print(i)
    elif command.startswith("LIS"):
        if len(command.split(" ")) != 2:
            print("The LIS command only accepts one parameter!")
        else:
            try:
                loader.RISloading(command.split(" ")[1], interpreter)
                for i in loader.instructions:
                    interpreter.addinstruction(i.split(".")[0], loader.instructions[i])
            except Exception as e:
                print(f"Critical Error, HALT! {e}")
    elif command.startswith("exit"):
        exit()
    else:
        try:
            AST = lexer.tokenGEN(command, STRtypes, ENDtypes)
            AST = interpreter.PREPAST(AST)
            print(interpreter.EXECINS(AST)[1])
        except Exception as e:
            print(f"Critical Error, HALT! {e}")

