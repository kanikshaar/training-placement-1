class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        wordMap = {}
        for word in words: # get counts of our word list into hashmap
            if word not in wordMap:
                wordMap[word] = 0
            wordMap[word] += 1

        ans = []
        wordLength = len(words[0]) # I didn't read at first but all words are same length which is key
        totalStringLength = wordLength * len(words)

        def checkSub(substring):
            """
            Creates counter of words for substring that is of length totalStringLength
            """
            counter = {}
            for i in range(0, len(substring), wordLength):
                subWord = substring[i : i + wordLength]
                if subWord in wordMap:
                    if subWord not in counter:
                        counter[subWord] = 0
                    counter[subWord] += 1
                    if counter[subWord] > wordMap[subWord]: #if the count of word is greater than our word list return false
                        return False
                else: #immediately return false if the word is not in word list
                    return False

            if counter == wordMap:
                return True

            return False
    
        for i in range(len(s)): #Checks substring of length totalStringLength at every index
            if i + totalStringLength <= len(s) and checkSub(s[i : i + totalStringLength]):
                ans.append(i)
        return ans
