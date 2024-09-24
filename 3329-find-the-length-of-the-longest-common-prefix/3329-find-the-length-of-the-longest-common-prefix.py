class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # def prefix_size(a,b):
        #     min_size = min(len(a),len(b))
        #     for size in range(min_size,0,-1):
        #         if a[:size] == b[:size]:
        #             return size
        #     return 0

        # arr1 = tuple(map(str,arr1))
        # arr2 = tuple(map(str,arr2))
        
        # max_size = 0        
        # for i in arr1:
        #     for j in arr2:
        #         x = prefix_size(i,j)
        #         if x > max_size:
        #             max_size = x
        
        # return max_size

        # if len(arr1) > len(arr2):
        #     arr1, arr2 = arr2, arr1
                        
        # arr1 = tuple(map(str,arr1))
        # arr2 = sorted(map(str,arr2),key=len,reverse = True)

        # def get_all_prefix(lst):
        #     prefixes = set()
        #     for ele in lst:
        #         size = len(ele)
        #         for i in range(size,0,-1):
        #             prefixes.add(ele[:i])
        #     return prefixes # sorted(prefixes,key=len,reverse = True)

        # prefixes1 = get_all_prefix(arr1)
        # print(arr2)

        # checked = []
        # for ele in arr2:
        #     size = len(ele)
        #     for i in range(size,0,-1):
        #         a = ele[:i]
        #         if a not in checked:
        #             checked.append(a)
        #             if a in prefixes1:
        #                 return i

        # return 0

        trie = Trie()

        # Step 1: Insert all numbers from arr1 into the trie
        for num in arr1:
            trie.insert(str(num))

        # Step 2: Find the longest common prefix between arr2 numbers and the trie
        max_length = 0
        for num in arr2:
            max_length = max(max_length, trie.find_longest_common_prefix(str(num)))

        return max_length
                


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a number string into the trie
    def insert(self, number_str):
        node = self.root
        for char in number_str:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    # Find the longest common prefix with a number in the trie
    def find_longest_common_prefix(self, number_str):
        node = self.root
        prefix_length = 0
        for char in number_str:
            if char in node.children:
                prefix_length += 1
                node = node.children[char]
            else:
                break
        return prefix_length
