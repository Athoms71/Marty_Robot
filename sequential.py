import file_management as fm
from Moves import Moves


class Sequence:
    def __init__(self, name: str, liste_instructions: list):
        self.name = name
        self.sequence = self.construction_queue(liste_instructions)

    def construction_queue(self, liste_instructions: list):

        for instr in liste_instructions:
            fm.write_file("sequence.txt", str(instr)+"\n")

    def play_dance(self, file_path):
        fichier = open(file_path, "r")
        lines = fichier.readlines()
        for line in lines[1:]:
            line = line.split("")
            for i in range(int(line[0])):
                if line[1] == "U":
