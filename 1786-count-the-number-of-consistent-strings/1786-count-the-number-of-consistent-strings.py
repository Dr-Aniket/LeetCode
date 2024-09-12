class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        checked = {}
        def valid(word):
            word = ''.join(sorted(set(word)))
            if word in checked:
                return checked[word]
            a = False

            for i in word:
                if i not in allowed:
                    break
            else:
                a = True
            checked[word] = a
        
            return a

        return len([word for word in words if valid(word)])
            