from fileinput import filename


class Contextmanager:
    def __init__(self,filename):
        self.filename=filename
        self.file=None
    def __enter__(self):
        self.file=open(self.filename,"w")
        self.file.write("file is created\n")
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print("file closeed sucessfully")
        if exc_type:
            print("exception information ")
            print(exc_tb)
            print(exc_val)
        return True
with Contextmanager("d.txt") as f:
    print(f.write("code runned sucessfully"))
