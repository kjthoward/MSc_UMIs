#!/usr/bin/env python
import os, subprocess

for file in sorted(os.listdir(os.getcwd())):
    if file.endswith("unmapped.bam"):
        var=file.split(".")
        outsam=var[0]+"_cleaned.sam"
        outbam=var[0]+"_cleaned.bam"
        command=f"samtools view -h -o temp.sam {file}"
        p = subprocess.Popen(command.split())
        p.wait()
        with open(outsam,"wt") as out:
            with open("temp.sam","rt") as infile:
                for line in infile:
                    if line[:3]=="@M0":
                        out.write(line[1:])
                    else:
                        out.write(line)
        command2=f"samtools view -S -b {outsam}"
        outbam_file=open(outbam,"wb")
        p2 = subprocess.Popen(command2.split(), stdout=outbam_file)
        p2.wait()
        outbam_file.close()
        os.remove("temp.sam")
        
