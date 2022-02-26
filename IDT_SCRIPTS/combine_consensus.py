#!/usr/bin/env python
import os, subprocess, yaml

print(__file__)

config = yaml.safe_load(open("IDT_Config.yml"))
min_reads = config["min_reads"]

for file in sorted(os.listdir(os.getcwd())):
    if file.endswith("_grouped.bam"):
        var = file.split("_")
        outfile = var[0] + "_consensus.unmapped.bam"
        if os.path.exists(outfile):
            print(f"Skipping: {file}")
            continue
        command = f"fgbio CallDuplexConsensusReads --input={file} --output={outfile} --error-rate-pre-umi=45 --error-rate-post-umi=40 --min-input-base-quality=20 --min-reads {min_reads}"
        p = subprocess.Popen(command.split())
        p.wait()
