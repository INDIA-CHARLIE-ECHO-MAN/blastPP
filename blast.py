from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML 
from Bio.Seq import Seq


seq = Seq("MPHSNSKNHQPGKSTSREAKCDDDRIRSSRRQSYNTSSEPKLIQKKWMENCYDVVTGDDSRFSAQKTVRANRVVERNEGSRRQSTSTVEPKAASNHTPVNRGPTTTGPTVNRFISDDERDFEMALFQLKQAKLVNDTVKDLVATFPLESILSANGRNFSQWANDLEKIGSGRFMRPNFFTTPCDNRTFEKMGKELILATIHSSHVPDLENIETSHEMFDLLKKKCTSISRAGQMKIWNQFVSFTINPNDSAESIATTLKDMYAEWEAMNVWMHSDVFLGFCFQSAVMKSSVPFKKEFELQVENLVQEHPRHPVPTFRSLTNIYESCKQQHKQAMAANTSSGQPSSSEGPTPLPAAEVDPDPPLYYACIPEPNQCLLEWQTYLKERYDERNRQ")
result_handle = NCBIWWW.qblast(program="blastp", database="nr", sequence=seq, format_type="Text", hitlist_size=10)

blast_result = open("blast_results2.txt", "w")
blast_result.write(result_handle.read())


# for record in NCBIXML.parse(open("blast_results.xml")):

#     if record.alignments : #skip queries with no matches
#         print("QUERY: %s" % record.query[:60])

#         for align in record.alignments:
#             for hsp in align.hsps:
#                 if hsp.expect < E_VALUE_THRESH:
#                     print("MATCH: %s " % align.title[:60])
#                     print(hsp.expect)