#!/usr/bin/env python
import os, subprocess, sys, yaml

print(__file__)
config = yaml.safe_load(open("OGT_Config.yml"))
intervals = config["intervals"]
ref = config["reference"]

with open("input.list", "wt") as input_list:
    for file in os.listdir(os.getcwd()):
        if file.endswith("_mapped.bam"):
            input_list.write(f"{file}\n")

command = f"gatk DepthOfCoverage -R {ref} -O Mapped.cov -I input.list -L {intervals}"

p = subprocess.Popen(command.split())
p.wait()
os.remove("input.list")
# replaces ending with .csv for easy openning
for file in os.listdir(os.getcwd()):
    if file.startswith("Mapped.cov"):
        os.rename(file, f"{file}.csv")
