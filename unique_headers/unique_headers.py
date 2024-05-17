import sys

def main(multif: str, outf: str) -> None:
    fn = open(multif, "r").read()
    g = fn.split(">")[1:]
    out = open(outf, "w")

    saved = ""
    for j, line in enumerate(g):
        t = line.split()
        k = "".join(line).split("\n")
        header = "".join(k[0]).rstrip().split(" ")[0].replace(".", "").replace(",", "").replace("(","").replace(")","").replace(";", "").replace(":", "").replace("|", "").replace("*", "").replace("%", "")
        seq = "".join(k[1:]).rstrip()
        saved = saved + ">" + header + "_id" + str(j) + "\n" + seq + "\n"
    out.write(saved)

# checks script is run directly - only runs if direct
if __name__ == "__main__":

    # if there is a missing arg or too many, prints out usage.
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
        sys.exit(1)

    multif = sys.argv[1]
    outf = sys.argv[2]

    main(multif, outf)

