"""
Print all words containing a given prefix using Trie data structure
"""


class TrieNode:
  def __init__(self):
    self.character = [None] * 26
    self.word_end = False


class Trie:
  def __init__(self):
    self.root = self.getNode()

  def getNode(self):
    return TrieNode()

  def convertCharacter(self, c):
    return ord(c) - ord('a')

  def printTrieData(self):
    pass

  def insertWord(self, key):
    crawl_node = self.root
    l = len(key)

    for i in range(l):
      current_index = self.convertCharacter(key[i])
      if crawl_node.character[current_index] is None:
        crawl_node.character[current_index] = self.getNode()
      crawl_node = crawl_node.character[current_index]
    crawl_node.word_end = True

  def searchWord(self, key):
    crawl_node = self.root
    l = len(key)

    for i in range(l):
      current_index = self.convertCharacter(key[i])
      if crawl_node.character[current_index] is None:
        return -1
      crawl_node = crawl_node.character[current_index]
    return crawl_node and crawl_node.word_end

  def prefixCount(self, search_keys, pre):
    word_len = len(search_keys)
    words_found = []
    res = {}

    for i in range(word_len):
      crawl_node = self.root
      key = search_keys[i]
      l = len(pre)
      found = True

      for j in range(l):
        current_index = self.convertCharacter(key[j])
        if crawl_node.character[current_index] is None:
          found = False
          break
        crawl_node = crawl_node.character[current_index]
      if found:
        words_found.append(key)
    res[len(words_found)] = words_found
    return res


t1 = Trie()
prefix = input()
search_keys = list(map(str, input().split(' ')))
t1.insertWord(prefix)

# Prefix count return function test
print(t1.prefixCount(search_keys, prefix))