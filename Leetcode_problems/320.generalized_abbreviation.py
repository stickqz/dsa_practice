'''
Write a function to generate the generalized abbreviations of a word. 

Note: The order of the output does not matter.

Example:

Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

'''

def generateAbbreviations(self, word: str):
    ans = []

    def bt(i, cur, count):
        if i == len(word):
            if count > 0:
                cur += str(count)
            ans.append(cur)
            return
        
        # Option 1: Abbreviate this character (increase count)
        bt(i+1, cur, count+1)

        # Option 2: Keep this character
        if count > 0:
            cur += str(count)
        bt(i+1, cur + word[i], 0)

    bt(0, "", 0)
    return ans