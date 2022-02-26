#!/bin/sh
#Amount of RAM for Java programs (gatk, bwa etc...) to use
#Currently set as 24GB
export _JAVA_OPTIONS="-Xmx24g"
python create_ubams.py
#COMBINE ONLY REQUIRED IF RUN ON NEXTSEQ
#It takes data from 4 lanes and combines it into 1, leaving just R1 and R2
#If not running combine_bams, then "if file.endswith" for future commands may need changing
python combine_bams.py
python extract_umis.py
python align_reads.py
python Mapped_reads.py
python coverage_mapped.py
python duplicates_mapped.py
python group_reads.py
python Graph_Families.py
python combine_consensus.py
python remap_consensus.py
python duplicates_consensus.py
python coverage_consensus.py
python vardict.py
python annovar_vardict.py
