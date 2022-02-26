#!/usr/bin/env python
import os, subprocess

print(__file__)

for file in sorted(os.listdir(os.getcwd())):
    if file.endswith("_combined_mapped.bam"):
        var = file.split("_")
        outfile = var[0] + "mapped_marked.bam"
        metrics = var[0] + "_MarkDuplicate_Metrics.txt"
        if os.path.exists(outfile):
            print(f"skipping {file}")
            continue
        command = f"picard MarkDuplicates I={file} O={outfile} M={metrics} CREATE_INDEX=true TAGGING_POLICY=All REMOVE_DUPLICATES=true OPTICAL_DUPLICATE_PIXEL_DISTANCE=2500"
        p = subprocess.Popen(command.split())
        p.wait()
