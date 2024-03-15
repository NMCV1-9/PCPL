import importlib.util
import sys
import os

class loader():
    def __init__(self):
        self.instructions = {}
        self.loadedpaths = []
    
    def RISloading(self, path, IR):
        for i in os.listdir(path):
            print(f"checking {i}")
            if os.path.isdir(path+"/"+i):
                print("Sub-instruction pack")
                for f in os.listdir(path+"/"+i):
                    if os.path.isfile(path+"/"+i+"/"+f):
                        print(f)
                        self.loadIS(path+"/"+i+"/"+f, IR)
                print("loaded Sub-instruction pack")
            else:
                print("Instruction")
                self.loadIS(path+"/"+i, IR)
                print("loaded")
        print("finished RIS instruction loading")
                    
    
    def loadIS(self, path, IR):
        print(f"loading instruction {os.path.basename(path)} at {path}")
        spec = importlib.util.spec_from_file_location(os.path.basename(path), path)
        print("loaded spec")
        module = importlib.util.module_from_spec(spec)
        print("module loaded")
        sys.modules[os.path.basename(path)] = module
        print("added to sys")
        spec.loader.exec_module(module)
        print("executed module")
        try:
            self.instructions[os.path.basename(path)] = module.main(IR)
        except:
            self.instructions[os.path.basename(path)] = module.main()
        print("added to instructions")
        self.loadedpaths.append(path)
        print("finished")
