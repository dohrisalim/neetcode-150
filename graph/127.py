class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def isNeighbour(word1, word2):
            count = 0
            for i, letter in enumerate(word1):
                if letter!=word2[i]:
                    count+=1
                if count>1:
                    return False
            return True

        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue1 = deque([beginWord])
        queue2 = deque([endWord])
        visited1 = set([beginWord])
        visited2 = set([endWord])
        level = 1
        while queue1 and queue2:
            if len(queue1) > len(queue2):
                queue1, queue2 = queue2, queue1
                visited1, visited2 = visited2, visited1
            
            n = len(queue1)
            for _ in range(n):
                node = queue1.popleft()
                if node in visited2:
                    return level
                for word in wordSet:
                    if word not in visited1 and isNeighbour(node,word):
                        queue1.append(word)
                        visited1.add(word)
            
            level += 1
        
        return 0