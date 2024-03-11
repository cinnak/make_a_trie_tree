import pygtrie
trie = pygtrie.CharTrie()
# add an element
trie["code"] = 7.3
trie["cobalt"] = 0.9
trie["coffee"] = 10

results = trie.keys(prefix="co")

results = sorted(results, key=lambda x: trie[x])
print(results)