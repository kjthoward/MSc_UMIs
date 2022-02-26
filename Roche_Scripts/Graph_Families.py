#!/usr/bin/env python
import os, pdb
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import numpy as np

print(__file__)

folder = os.getcwd()
os.chdir(folder)
for file in os.listdir(folder):
    if file.endswith("_families.txt"):
        x = []
        y = []
        with open(file, "r") as f:
            f.readline()
            for line in f:
                values = line.split("\t")
                # values order:
                # family_size, count, fraction, fraction_gte_family_size
                x += [int(values[0])]
                y += [float(values[2]) * 100]
        plt.bar(x, y)
        plt.xticks(np.arange(0, max(x) + 1, 10))
        plt.title(f"Read Family Distribution of {file.split('_')[0]}, log scale")
        plt.xlabel("Family Size")
        plt.ylabel("Percentage of Families (log)")
        plt.yscale("log")
        plt.savefig(f"{file.strip('.txt')}_log_scale.pdf")
        plt.clf()
        plt.bar(x, y)
        plt.xticks(np.arange(0, max(x) + 1, 10))
        plt.title(f"Read Family Distribution of {file.split('_')[0]}")
        plt.xlabel("Family Size")
        plt.ylabel("Percentage of Families")
        plt.gca().yaxis.set_major_formatter(StrMethodFormatter("{x:,.2f}"))
        plt.savefig(f"{file.strip('.txt')}.pdf")
        plt.clf()
