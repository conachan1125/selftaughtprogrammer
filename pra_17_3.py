import re

line = "the ghost that says boo haunts the loo"

ma = re.findall(".oo", line)
print(ma)
