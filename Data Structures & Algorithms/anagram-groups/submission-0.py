class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        dictionary = {}
        for word in strs:
            tmp = [0] * 26
            for w in word:
                tmp[ord(w)-ord('a')] += 1
            dictionary[tuple(tmp)] = []

        res = []
        print(dictionary)
        for word in strs:
            tmp = [0] * 26 
            for w in word:
                tmp[ord(w)-ord('a')] += 1
            print(tmp)
            dictionary[tuple(tmp)].append(word)
    
        for item,val in dictionary.items():
            res.append(val)

        return (res)

