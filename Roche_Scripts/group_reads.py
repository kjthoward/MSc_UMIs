#!/usr/bin/env python
import os, subprocess, yaml

print(__file__)

config = yaml.safe_load(open("ROCHE_DCS_Config.yml"))
grouping = config["grouping"]
edits = config["edits"]

for file in sorted(os.listdir(os.getcwd())):
    if file.endswith("_combined_mapped.corrected.bam"):
        var = file.split("_")
        outfile = var[0] + "_combined_grouped.bam"
        if os.path.exists(outfile):
            print(f"skipping {file}")
            continue
        hist_out = var[0] + "_families.txt"
        command = f"fgbio GroupReadsByUmi --input={file} --output={outfile} --family-size-histogram={hist_out} --strategy={grouping} --edits={edits} --min-map-q=20"
        p = subprocess.Popen(command.split())
        p.wait()
