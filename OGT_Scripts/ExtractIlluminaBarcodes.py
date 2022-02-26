#!/usr/bin/env python
import os, subprocess, yaml

print(__file__)

config = yaml.safe_load(open("OGT_Config.yml"))
basecalls = config["basecalls"]
barcodes = config["barcodes"]
structure = config["read-structure"]
barcodesdir = config["barcodesdir"]

command = f"picard ExtractIlluminaBarcodes BASECALLS_DIR={basecalls} BARCODE_FILE={barcodes} READ_STRUCTURE={structure} LANE=1 OUTPUT_DIR={barcodesdir} METRICS_FILE=barcode_metrics.txt"
p = subprocess.Popen(command.split())
p.wait()
