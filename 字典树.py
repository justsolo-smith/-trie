

class TrieNode():
    def __init__(self,value,count):
        self.value = value
        self.count = count
        self.children = {}

class Trie():

    def __init__(self):
        self.root = TrieNode(value = None,count = 0)
    
    def build(self,words):

        cur_node = self.root
        for item in words:
            if item not in cur_node.children:
                child = TrieNode(value=item,count=0)
                cur_node.children[item] = child
                cur_node = child
            else:
                cur_node = cur_node.children[item]
                cur_node.count +=1
    def search(self,test_word):
        cur_node = self.root
        mark = True
        for item in test_word:
            if item not in cur_node.children:
                mark = False
                break
            else:
                cur_node = cur_node.children[item]
        if cur_node.children:
            mark = False
        return mark
                


if __name__ == '__main__':
    trie = Trie()
    texts = ['what','rank','range','water','want','ranker','rant']
    for text in texts:
        trie.build(text)

    markx = trie.search('what')
    print(markx)