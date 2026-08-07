class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # '''
        # establish ranking for order, iterate through and 
        # '''
        ranking = {}
        for a in range(len(order)):
            ranking[order[a]] = a


        # #need to compare letter by letter in neighboring words and see if they are in order lexicographically, if not then return False early
        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i + 1]

            for j in range(min(len(word_1), len(word_2))):
                if ranking[word_1[j]] != ranking[word_2[j]]:
                    if ranking[word_1[j]] > ranking[word_2[j]]:
                        return False
                    break
            else:
                if len(word_1) > len(word_2):
                    return False
        
        return True
