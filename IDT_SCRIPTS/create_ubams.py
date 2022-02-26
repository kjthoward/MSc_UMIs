#!/usr/bin/env python
import os, subprocess

print(__file__)

for file in sorted(os.listdir(os.getcwd())):
    if file.endswith(".fastq.gz"):
        if "R2" in file:
            continue
        else:
            var = file.split("_")
            outfile = var[0] + "_" + var[2]
            if os.path.exists(outfile):
                print(f"Skipping: {file}")
                continue
            command = f"picard FastqToSam FASTQ={file} FASTQ2={file.replace('R1','R2')} O={outfile}_unmapped.bam SM={var[0]}"
            p = subprocess.Popen(command.split())
            p.wait()
