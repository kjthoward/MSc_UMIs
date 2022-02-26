#!/usr/bin/env python
import os, subprocess, yaml

print(__file__)

config = yaml.safe_load(open("OGT_Config.yml"))
grouping = config["grouping"]
edits = config["edits"]

for file in sorted(os.listdir(os.getcwd())):
    if file.endswith("_mapped.bam"):
        var = file.split("_")
        outfile = var[0] + "_grouped.bam"
        hist_out = var[0] + "_families.txt"
        if os.path.exists(outfile):
            print(f"Skipping: {file}")
            continue
        command = f"fgbio GroupReadsByUmi --input={file} --output={outfile} --family-size-histogram={hist_out} --strategy={grouping} --edits={edits} --min-map-q=20"
        p = subprocess.Popen(command.split())
        p.wait()
