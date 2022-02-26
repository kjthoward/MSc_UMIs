#!/usr/bin/env python
import os, subprocess, sys, yaml

print(__file__)

config = yaml.safe_load(open("ROCHE_DCS_Config.yml"))
ref = config["reference"]
intervals = config["intervals"]

with open("input.list", "wt") as input_list:
    for file in os.listdir(os.getcwd()):
        if file.endswith("_consensus.mapped.bam"):
            input_list.write(f"{file}\n")

command = f"gatk DepthOfCoverage -R {ref} -O Consensus.cov -I input.list -L {intervals}"

p = subprocess.Popen(command.split())
p.wait()
os.remove("input.list")
# replaces ending with .csv for easy openning
for file in os.listdir(os.getcwd()):
    if file.startswith("Consensus.cov"):
        os.rename(file, f"{file}.csv")
