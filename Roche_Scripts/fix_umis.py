#!/usr/bin/env python
import os, subprocess

print(__file__)

for file in sorted(os.listdir(os.getcwd())):
    if file.endswith("_combined_mapped.bam"):
        var = file.split("_")
        outfile = var[0] + "_combined_mapped.corrected.bam"
        if os.path.exists(outfile):
            print(f"skipping {file}")
            continue
        metrics = var[0] + "_UMI_metrics.txt"
        command = f"fgbio CorrectUmis -i {file} -o {outfile} -M {metrics} -m 1 -d 1 -U UMIs.txt"
        p = subprocess.Popen(command.split())
        p.wait()
