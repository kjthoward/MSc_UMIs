#!/usr/bin/env python
import os, subprocess, yaml

print(__file__)

config = yaml.safe_load(open("OGT_Config.yml"))
ref = config["reference"]
threads = config["threads"]
bed = config["bed"]
VAF = config["VAF"]
alt_reads = config["alt_reads"]

for file in sorted(os.listdir(os.getcwd())):
    if file.endswith("_consensus.mapped.bam"):
        var = file.split(".")
        outfile = var[0] + "_vardict.vcf"
        if os.path.exists(outfile):
            print(f"Skipping: {file}")
            continue
        command = f"vardict-java -G {ref} -f {VAF} -r {alt_reads} -q 25 -N {var[0]} -b {file} -th 8 -w 200 --adaptor AGATCGGAAGAGCACACGTCTGAACTCCAGTCA,AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -UN -c 1 -S 2 -E 3 -g 5 -z 0 {bed}"
        p = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        command2 = f"teststrandbias.R"
        p2 = subprocess.Popen(command2.split(), stdout=subprocess.PIPE, stdin=p.stdout)
        command3 = f"var2vcf_valid.pl -N {var[0]} -f {VAF} -A"
        with open(outfile, "w") as f:
            p3 = subprocess.Popen(command3.split(), stdin=p2.stdout, stdout=f)
            p3.wait()
