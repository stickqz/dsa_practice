
'''
Given a text string and words (a list of strings), return all index pairs [i, j] so 
that the substring text[i]...text[j] is in the list of words.

Example 1:
Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
Output: [[3,7],[9,13],[10,17]]

Example 2:
Input: text = "ababa", words = ["aba","ab"]
Output: [[0,1],[0,2],[2,3],[2,4]]
Explanation: 
Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addword(self, word):
        root = self

        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()

            root = root.children[c]
        
        root.end = True

    

def indexPairs(text, words):
    n = len(text)
    ans = []

    root = TrieNode()
    for w in words:
        root.addword(w)

    for i in range(n):
        node = root
        j = i

        while j < n and text[j] in node.children:
            node = node.children[text[j]]
            if node.end:
                ans.append([i, j])
            j += 1
    
    return ans
