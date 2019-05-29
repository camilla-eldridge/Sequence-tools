import sys

iD=sys.argv[1]
ffile=sys.argv[2]

with open(ffile, "r") as fasta:
    fasta=fasta.readlines()
    seq=fasta[1:]
    ali=">P1;" + str(iD) + "\n" + "sequence:" + str(iD) + ":::::::0.00: 0.00" + "\n" + "".join(seq) + "*"
    print ali


# usage cd63 file.fasta > cd63.ali

