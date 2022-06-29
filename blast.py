from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML 

my_query = SeqIO.read("testing.fasta", format="fasta")
result_handle = NCBIWWW.qblast("blastp", "nr", my_query)

blast_result = open("blast_results.xml", "w")
blast_result.write(result_handle.read())
blast_result.close()
result_handle.close()

for record in NCBIXML.parse(open("blast_results.xml")):
    if record.alignments : #skip queries with no matches
        print("QUERY: %s" % record.query[:60])
        
    for align in record.alignments:
        for hsp in align.hsps:
            print("MATCH: %s " % align.title[:60])
            print(hsp.expect)
