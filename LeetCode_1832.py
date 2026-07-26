class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphb="abcdefghijklmnopqrstuvwxyz"
        count=0
        for i in alphb:
            if i in sentence:
                count+=1
        if count==26:
            return True
        else:
            return False
