import sys
import deepdish as dd

filee = sys.argv[1]
print(filee)
data = dd.io.load(filee)

for k,v in data.items():
    v['borealis_git_hash'] = 'v0.6'

out_file = "edited." + filee
dd.io.save(out_file, data)
