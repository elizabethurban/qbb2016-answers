#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = open(sys.argv[1])

for i, line in enumerate(df):
    if i == 0:
        print "FID\tIID" + line.rstrip()
    else:
        fields = line.rstrip("\n\r").split("\t")
        new_field = fields[0].split("_")
        new_row = new_field + fields[1:]
        print "\t".join(new_row)
