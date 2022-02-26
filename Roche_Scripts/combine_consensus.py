#!/usr/bin/env python
import os, subprocess, yaml

print(__file__)

config = yaml.safe_load(open("ROCHE_DCS_Config.yml"))
min_reads = config["min_reads"]

for file in sorted(os.listdir(os.getcwd())):
    if file.endswith("__grouped.bam"):
        var = file.split("_")
        outfile = var[0] + "_consensus.unmapped.bam"
        if os.path.exists(outfile):
            print(f"skipping {file}")
            continue
        command = f"fgbio CallDuplexConsensusReads --input={file} --output={outfile} --error-rate-pre-umi=45 --error-rate-post-umi=40 --min-input-base-quality=20 --read-name-prefix='consensus' --min-reads {min_reads}"
        p = subprocess.Popen(command.split())
        p.wait()
