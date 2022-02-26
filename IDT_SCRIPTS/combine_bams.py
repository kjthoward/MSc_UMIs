#!/usr/bin/env python
import os, subprocess

print(__file__)
for file in sorted(os.listdir(os.getcwd())):
    if file.endswith("_unmapped.bam"):
        if not "L001" in file:
            continue
        else:
            var = file.split("_")
            outfile = var[0] + "_combined_unmapped.bam"
            if os.path.exists(outfile):
                print(f"Skipping: {file}")
                continue
            command = f"picard MergeSamFiles I={file} I={file.replace('L001','L002')} I={file.replace('L001','L003')} I={file.replace('L001','L004')} O={outfile}"
            p = subprocess.Popen(command.split())
            p.wait()
