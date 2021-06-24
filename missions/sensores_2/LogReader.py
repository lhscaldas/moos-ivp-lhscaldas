#!/usr/bin/env python
def LogReader(log_file,var):
    t = []
    x = []
    with open(log_file, 'r') as f:
        text = f.readlines()
        for line in text[4:]:
            p = line.split(' ')
            p[:] = [x for x in p if x]
            if var in p:
              t.append(float(p[0]))
              x.append(float(p[-2]))
    return t, x