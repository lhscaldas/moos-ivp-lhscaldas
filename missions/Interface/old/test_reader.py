params={}
with open("itaguai.info", 'r') as f:
    text = f.readlines()
    for line in text:
        p = line.split(' ')
        p[:] = [x for x in p if x]
        params[p[0]]=float(p[2])
print(params)