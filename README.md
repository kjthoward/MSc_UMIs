# Kieran Howard MSc UMI Analysis Scripts

This repository contains several subfolders which are used to analyse UMI data from the respective companies. Before starting, first install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) (tested with conda v4.10.3 and python 3.8.8) and create an environment using the included UMI_env.yml file:
`conda env create --file UMI_env.yml`

Each folder also contains a yml configuration file with various parameters that can be altered to change the analyse parameters. Each script can be invoked individually (e.g. `python align_reads.py`) or the included shell script (`run_all.sh`) can be used to run all scripts, in order, to perform the full analysis. The run_all.sh script all has a parameter at the top to specify the amount of memory to allocate to the JVM for Java programs, such as BWA and Picard.  Each script will only perform its steps if the output files do not already exist (to save unnecessary re-processing of data), so if a step needs to be repeated with different parameters the original output files must first be remove/renamed to enable to reanalysis to take place.

## IDT_Scripts
Contains scripts used to analyse UMI data from Integrated DNA Technologies (IDT).
- create_ubams.py
  - Used to create unmapped BAMs from fastq.gz files
  - Takes no additional parameters from the IDT_Config.yml file
- combine_bams.py
  - NOTE: This script is only required if the data came from a NextSeq
  - Used to combine the four lanes of NextSeq data into one unmapped BAM
- extract_umis.py
  - Uses fgbio to extra the UMI sequences from the unmapped BAM and stores the UMI value in the RX tag of the BAM file 
  - Requires the "read-structure" parameter from IDT_Config.yml
- align_reads.py
  - A multi-step script that first converts the unmapped BAM back into FASTQ, as bwa requires a FASTQ file for alignment. This then gets piped into BWA to be aligned. The aligned output is then piped into picard MergeBamAlignment where the UMI data from the unmapped BAM is merged into the mapped BAM (as the conversion to FASTQ loses the data in the BAM tags)
  - Requires a reference genome from the "reference" parameter from IDT_Config.yml
  - Requires the number a threads for BWA to use from the "threads" parameter from IDT_Config.yml
- Mapped_reads.py
  - A QC step used to determine the on-target rate
  - First uses gatk CountReads to determine the number of reads that are touching a target, then uses picard CollectAlignmentSummaryMetrics to gather other alignment metrics. On-target reads can be calculated using the "PF_READS" value from CollectAlignmentSummaryMetrics and the number of reads touching a target
  - Requires a reference genome from the "reference" parameter from IDT_Config.yml
  - Requires a list of targets as a bed file from the "bed" parameter from IDT_Config.yml
- coverage_mapped.py
  - Another QC step, determines the coverage of the BAM files before any UMI processing
  - Uses gatk DepthOfCoverage
  - Requires a reference genome from the "reference" parameter from IDT_Config.yml
  - Requires a list of targets as an interval list file from the "intervals" parameter from IDT_Config.yml
- duplicates_mapped.py
  - Another QC step, determines the duplicate rates of the BAM files before any UMI processing
  - Takes no additional parameters from the IDT_Config.yml file
- group_reads.py
  - Uses fgbio to group reads into read families based on their 5' location and UMI sequences
  - Requires a grouping strategy from the "grouping" parameter from IDT_Config.yml
  - Requires a number of edits to be specified from the "edits" parameter from IDT_Config.yml
    - Edits is the number of bases that a UMI can differ from another UMI and still be counted the same. For example if two reads have the same 5' position but the UMI Sequences ATT and ATG, with an edits of 0 they will be two separate families but with an edits of 1 they will counted as the same family as their UMIs only differ by one base
- Graph_Families.py
  - Another QC step, uses the families.txt outputs of group_reads.py to create graphs to visualise the relative size of each family. Each sample gets two graphs made, one with a linear y scale and one with a logarithmic y scale
- combine_consensus.py
  - Uses fgbio to create a consensus sequence BAM, using the groups that were made in group_reads.py
  - Requires a minimum numbers of reads to call the consensus, from the "min_reads" parameter from IDT_Config.yml
- remap_consensus.py
  - The output of combine_consensus.py is unmapped, this remaps it using similar parameters as in align_reads.py
- duplicates_consensus.py
  - QC step, creates duplicate metrics for the consensus BAM, similar to duplicates_mapped.py
- coverage_consensus.py
  - QC step, calculates the coverage for the consensus BAMs, similar to coverage_mapped.py
- vardict.py
  - Performs variant calling the consensus BAMs using VarDict.
  - Requires a reference genome from the "reference" parameter from IDT_Config.yml
  - Uses the "threads" parameter from IDT_Config.yml to specify the number of threads for VarDict to use
  - Requires a list of targets as a bed file from the "bed" parameter from IDT_Config.yml
  - Requires a minimum VAF for VarDict to call a variant, from "VAF" parameter from IDT_Config.yml
  - Requires a minimum number of alternate reads to call a variant, from "alt_reads" parameter from IDT_Config.yml
- annovar_vardict.py
  - Uses ANNOVAR to annotated the VCF output from VarDict 
  - Requires reference files, from the "humandb" parameter from IDT_Config.yml
  - Requires the path to the table_annovar.pl script, from the "annovar" parameter from IDT_Config.yml
