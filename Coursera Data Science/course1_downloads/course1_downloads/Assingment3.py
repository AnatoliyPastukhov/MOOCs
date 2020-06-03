import re

fhandle = open('university_towns.txt')
listo = list()
for line in fhandle:
    line = line.rstrip()
    if line.endswith('[edit]'):
        state = line
        estate = state.replace('[edit]', '')
    if '[edit]' not in line:
        regionname = re.sub('\s\(.+', '', line)
        if ':' not in regionname:
            listo.append((estate, regionname))

print(listo)
print(len(listo))

