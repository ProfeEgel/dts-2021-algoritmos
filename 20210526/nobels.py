import json
from search_algorithms import *

f = open('prize.json')
data = json.load(f)
f.close()

prizes = data["prizes"]
# print(len(prizes))

index_found = linear_search_conditional(prizes, lambda p: p["year"] == "1946")
for l in prizes[index_found]["laureates"]:
    print(l)

# prizes_found = linear_searchall_conditional(prizes, lambda p: p["year"] == "1942")
# for p in prizes_found:
#     print(p)
