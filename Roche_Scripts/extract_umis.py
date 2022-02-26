#!/usr/bin/env python
import os, subprocess, yaml

print(__file__)

config = yaml.safe_load(open("ROCHE_DCS_Config.yml"))
read_structure = config["read-structure"]

for file in sorted(os.listdir(os.getcwd())):
    if file.endswith("_combined_unmapped.bam"):
        var = file.split("_")
        outfile = var[0] + "_combined_unmapped.withUMI.bam"
        if os.path.exists(outfile):
            print(f"skipping {file}")
            continue
        command = f"fgbio ExtractUmisFromBam --input={file} --output={outfile} --read-structure={read_structure} --molecular-index-tags=ZA ZB --single-tag=RX"
        p = subprocess.Popen(command.split())
        p.wait()
