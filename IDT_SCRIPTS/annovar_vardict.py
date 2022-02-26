#!/usr/bin/env python
import os, subprocess, yaml

print(__file__)

config = yaml.safe_load(open("IDT_Config.yml"))
humandb = config["humandb"]
annovar = config["annovar"]

for file in sorted(os.listdir(os.getcwd())):
    if file.endswith("_vardict.vcf"):
        var = file.split("_")
        outfile = var[0] + "_vardict_annovar.vcf"
        if os.path.exists(outfile):
            print(f"Skipping: {file}")
            continue
        command = f"{annovar} {file} {humandb} --buildver hg38 --remove --outfile {outfile} -protocol refGene,genomicSuperDups,gnomad_exome,esp6500siv2_all,1000g2015aug_all,cosmic88_coding,CHIP_variants_19102018,clinvar_20180603,nci60 -operation g,r,f,f,f,f,f,f,f -argument -hgvs,,,,,,,, -vcfinput"
        p = subprocess.Popen(command.split())
        p.wait()
