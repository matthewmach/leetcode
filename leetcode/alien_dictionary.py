"""
Sol:
- ideas:
    - each word gives you a relationship between letters
        - ex. t < f, e > w, r > e, t >
    - this works for a directed graph
    - extract all the relationships from each word
        - only information we can extract from each adjacent word is the first difference we see
    - put them on a directed graph
        - if graph is circular bad
        - if graph has arrows pointing to a node twice, bad
        - 
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        outgoing, incoming = {}, {}
        for word in words:
            for c in word:
                if not c in outgoing:
                    outgoing[c] = []
                    incoming[c] = 0

        for word_i in range(1, len(words)):
            char_i = 0
            while char_i < min(len(words[word_i-1]), len(words[word_i])) and words[word_i-1][char_i] == words[word_i][char_i]:
                char_i += 1
            if char_i < min(len(words[word_i-1]), len(words[word_i])):    
                outgoing[words[word_i-1][char_i]].append(words[word_i][char_i])
                incoming[words[word_i][char_i]] += 1
            elif len(words[word_i-1]) > len(words[word_i]):
                    return ""
            
        out = ""

        while incoming:
            to_delete = []
            for key in incoming:
                if incoming[key] == 0:
                    out = out + key
                    to_delete.append(key)

            if not to_delete:
                return ""

            for key in to_delete:               
                for node in outgoing[key]:
                    incoming[node] -= 1
                del incoming[key]
                del outgoing[key]

        return out
        