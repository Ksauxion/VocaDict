import argparse
parser = argparse.ArgumentParser(
                    prog='VocaDictSortTool',
                    description='Sorting dictionary.')
parser.add_argument('dict',help="Dictionary path.")
args = parser.parse_args()
dict = args.dict
f = open(dict, encoding='utf-8')
v = f.readline()
v = v.rstrip()
v = v.split(',')
v.sort(key=len)
v=list(reversed(v))
v = ','.join(v)+'\n'
ln=[]
for i in f:
    ln.append(i)
ln.sort()
l = [v]
l.extend(ln)
f.close()
f = open(dict,'w+',encoding='utf-8')
for i in l:
    f.write(i)
f.close()
print('Done!')