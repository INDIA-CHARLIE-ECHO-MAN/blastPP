source = "UP000008783_418459.fasta"

def convert():

    geneset = {}

    # make json file
    with open('genes.json', 'w') as jsonFile:

        with open(source) as fastaFile:
            for line in fastaFile:
                if (line[:4] == ">tr|"):
                    


    






def main():
    

if __name__ == "__main__":
    main()