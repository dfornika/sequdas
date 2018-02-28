#!/usr/bin/env python

import sys
from sample_sheet import SampleSheet

sample_sheet_filename = sys.argv[1]

print(sample_sheet_filename)
sample_sheet = SampleSheet(sample_sheet_filename)
print(sample_sheet.Header.__dict__)
