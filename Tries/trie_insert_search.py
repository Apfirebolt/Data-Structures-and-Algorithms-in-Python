"""
A Simple program to insert a word in trie and then search for it.
"""


class TrieNode:
  def __init__(self):
    self.children = [None] * 26
    self.word_end = False


class Trie:
  def __init__(self):
    self.root = self.getNode()

  def getNode(self):
    return TrieNode()

  def charToIndex(self, c):
    return ord(c) - ord('a')

  def insert(self, key):
    crawl_node = self.root
    l = len(key)

    for level in range(l):
      index = self.charToIndex(key[level])
      if not crawl_node.children[index]:
        crawl_node.children[index] = self.getNode()
      crawl_node = crawl_node.children[index]

    crawl_node.word_end = True

  def search(self, key):
    l = len(key)
    crawl_node = self.root

    for i in range(l):
      index = self.charToIndex(key[i])
      if not crawl_node.children[index]:
        return False
      crawl_node = crawl_node.children[index]

    return crawl_node and crawl_node.word_end

t1 = Trie()
keys = ["the","a","there","anaswe","any","by","their", "jade"]

for key in keys:
  t1.insert(key)

# Search operations on Trie
print(t1.search('there'))
print(t1.search('jade'))
print(t1.search('amit'))
print(t1.search('any'))
print(t1.search('anye'))

