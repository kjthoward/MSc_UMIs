#!/bin/sh
#Amount of RAM for Java programs (gatk, bwa etc...) to use
#Currently set as 24GB
export _JAVA_OPTIONS="-Xmx24g"
############################################
# ONLY FIRST TWO IF SEQUENCING DONE LOCALLY #
############################################
python ExtractIlluminaBarcodes.py
python IlluminaBasecallsToSam.py
##############################################
# REST ARE USED FOR ALL SEQUENCING LOCATIONS #
##############################################
#python clean_sam.py #OPTIONAL, had to run for OGT made unmapped bams, if alignment fails, try running this!
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
