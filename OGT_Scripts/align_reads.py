#!/usr/bin/env python
import os, subprocess, yaml

print(__file__)

config = yaml.safe_load(open("OGT_Config.yml"))
threads = config["threads"]
ref = config["reference"]

for file in sorted(os.listdir(os.getcwd())):
    if file.endswith("cleaned.bam") or file.endswith("unmapped.bam"):
        # checks if an unmapped and a cleaned file exists for this sample
        # if it does this statement will make it so that only cleaned BAM gets alligned, not both
        if file.endswith("unmapped.bam") and os.path.exists(
            file.replace("unmapped.bam", "cleaned.bam")
        ):
            continue
        var = file.split("_")
        outfile = var[0] + "_mapped.bam"
        if os.path.exists(outfile):
            print(f"Skipping: {file}")
            continue
        command = f"picard SamToFastq I={file} F=/dev/stdout INTERLEAVE=true"
        p = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        command2 = f"bwa mem -p -t {threads} {ref} /dev/stdin"
        p2 = subprocess.Popen(command2.split(), stdout=subprocess.PIPE, stdin=p.stdout)
        command3 = f"picard MergeBamAlignment UNMAPPED={file} ALIGNED=/dev/stdin O={outfile} R={ref} SO=coordinate ALIGNER_PROPER_PAIR_FLAGS=true MAX_GAPS=-1 ORIENTATIONS=FR VALIDATION_STRINGENCY=SILENT CREATE_INDEX=true"
        p3 = subprocess.Popen(command3.split(), stdin=p2.stdout)
        p3.wait()
