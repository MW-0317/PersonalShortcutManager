import os

class Inkscape:
    def __init__(self, file):
        if file.endswith(".svg"):
            file = file + ".svg"
        if file in os.listdir(os.curdir):
            self.open()
        else:
            self.create_file()
        

    def open(self):
        pass

    def is_file(self):
        pass

    def get_base():
        return """
            <svg></svg>

        """

    def create_file(self):
        with open(file, "w") as f:
            f.write(self.get_base())