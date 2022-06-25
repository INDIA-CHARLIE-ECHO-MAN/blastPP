import json
from Bio.Blast import NCBIWWW

source = "UP000008783_418459.fasta"
jsonFile = "genes.json"

def convert():
    geneset = []

    # produce list first
    with open(source, "r") as fastaFile:
        seq = ""

        for line in fastaFile:
            if (line[:4] == ">tr|"):
                seq = seq.strip()
                geneset.append(seq)
                seq = ""
            seq = seq + line
        geneset.append(seq)
        seq = seq.strip()

    geneset.remove("")

    with open(jsonFile, "w") as jFile:
        jFile.write(json.dumps(geneset))

def blaster():
    print("hi")


def main():
    convert()

if __name__ == "__main__":
    main()