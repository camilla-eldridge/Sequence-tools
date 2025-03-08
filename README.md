# 🧬✨ **Sequence Tools**

Welcome to Sequence Tools – a repository of tools for wrangling sequence data in Python:

## Tools & Descriptions

### 🏷️ Header Management
- `replace_heads.py` – Swap out old headers in an MF file with new ones from a text file.
- `heditor.py` – Cleans up GenBank headers, leaving only the species name and accession number.
- `unique_headers.py` – Strips special characters from headers, truncates after the first space, and adds a unique ID.
- `unique_ids.py` – Replaces existing headers in a FASTA file with unique numeric IDs (`>1`, `>2`, etc.).

### 🔍 Sequence Search & Extraction
- `find_seq_overlap.py` – Identifies overlapping sequences in a target sequence.
- `get_seq_go.py` – Fetches sequences from a multi-FASTA file based on IDs.
- `splice.py` – Extracts sequence regions based on position input.
- `gbk_to_proteome.py` – Extracts all protein sequences from a GenBank file.
- `phd_to_fasta.py` – Converts PHD files to FASTA format.
- `nhmmer_or_hmmsearch_to_fasta.py` – Extracts FASTA sequences from HMMER search results.

### 🔢 ORF & Codon Analysis
-  `longest_orf.py` – Finds the longest ORF in all frames and detects in-frame stop codons.
-  `reverse_complement.py` – Generates the reverse complement of a sequence.

### 📊 File Splitting & Filtering
-  `mulif_to_singlef.py` – Converts a multi-FASTA file into individual FASTA files.
-  `get_by_size.py` – Extracts sequences from an MF file that meet a length threshold.
-  `split_fasta_ntimes.py` – Splits a multi-FASTA file into smaller multi-FASTA chunks of N sequences.
-  `remove_duplicate_fasta.py` – Removes duplicate sequences (including headers).

### 🤖 Exonerate Analysis
-  `extract_exonerate_output.py` – Extracts GFF, ORF, and CDS from Exonerate output.
-  `exonerate_highest_score.py` – Retrieves the highest-scoring alignment from Exonerate output (when you don't want to use `bestn`).

### 📜 Text & ID Comparisons
- `compare_txt.py` – Compares two text files (e.g., accession IDs) and reports differences.

## License
This work is licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You’re free to share and adapt the code, but credit the original author and indicate any modifications. 


