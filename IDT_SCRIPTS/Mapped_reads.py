#!/usr/bin/env python
import os, subprocess, yaml

print(__file__)

config = yaml.safe_load(open("IDT_Config.yml"))
ref = config["reference"]
bed = config["bed"]

alt_reads = config["alt_reads"]
for file in sorted(os.listdir(os.getcwd())):
    if file.endswith("_mapped.bam"):
        var = file.split("_")
        outfile = var[0] + "_target_reads.txt"
        if os.path.exists(outfile):
            print(f"Skipping: {file}")
            continue
        command = f"gatk CountReads -R {ref} -I {file} -L {bed} -LE true"
        with open(outfile, "wt") as f:
            f.write(subprocess.check_output(command.split()).decode("utf-8"))
        outfile2 = var[0] + "_Alignment_Metrics.txt"
        command2 = (
            f"picard CollectAlignmentSummaryMetrics R={ref} I={file} O={outfile2}"
        )
        p2 = subprocess.Popen(command2.split())
        p2.wait()
