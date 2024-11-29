"""
- create adjacency list
- bfs until node found
- note ignore duplicates?
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def differ(s1, s2):
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    if diff:
                        return False
                    diff += 1
            if diff:
                return True
            return False
        
        wordList.append(beginWord)
        word_dict = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                word1 = wordList[i]
                word2 = wordList[j]
                if differ(word1, word2):
                    word_dict[word1].append(word2)
                    word_dict[word2].append(word1)

        if len(word_dict[beginWord]) == 0:
            return 0

        queue = deque([(beginWord, 1)])
        visited = set()

        while queue:
            node, level = queue.popleft()
            if node not in visited:
                if node == endWord:
                    return level
                visited.add(node)
                for word in word_dict[node]:
                    queue.append((word, level + 1))
        return 0