class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxx=0
        for sentence in sentences:
            words=sentence.split()
            count=len(words)
            if count>maxx:
                maxx=count
        return maxx
