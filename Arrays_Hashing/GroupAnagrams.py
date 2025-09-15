# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
#  O(m * n) time 


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        GroupRequired = defaultdict(list)
        #We need default dict to eliminate edge case of zero or empty

        for string in strs:
            #for every string in the list given to us  
            AlphabetOccurenceKey = [0] * 26
            #There are 26 alphabets
            for character in string:
                AlphabetOccurenceKey[ord(character) - ord('a')] = AlphabetOccurenceKey[ord(character) - ord('a')] + 1
                #We find the position of the character wrt a and add 1 cuz we are counting
            GroupRequired[tuple(AlphabetOccurenceKey)].append(string)
            #list arent keyable so we tuple em and add the string for the matching AlphabetOccurenceKey
        return list(GroupRequired.values())
        #returning the list of values


        