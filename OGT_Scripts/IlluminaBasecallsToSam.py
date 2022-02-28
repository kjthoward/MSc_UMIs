#!/usr/bin/env python
import os, subprocess, yaml

print(__file__)

config = yaml.safe_load(open("OGT_Config.yml"))
basecalls = config["basecalls"]
structure = config["read-structure"]
barcodesdir = config["barcodesdir"]
runname = config["runname"]
libparams["libparams"]
command = f"picard IlluminaBasecallsToSam BASECALLS_DIR={basecalls} BARCODES_DIR={barcodesdir} LANE=1 READ_STRUCTURE={structure} RUN_BARCODE={runname} LIBRARY_PARAMS={libparams} MOLECULAR_INDEX_TAG=RX SEQUENCING_CENTER=WIMM"
p = subprocess.Popen(command.split())
p.wait()
