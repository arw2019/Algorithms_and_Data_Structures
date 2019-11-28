# top 4%
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(lambda x: int(x), version1.split('.')))
        while v1 and v1[-1] == 0: v1.pop()
        v2 = list(map(lambda x: int(x), version2.split('.')))
        while v2 and v2[-1] == 0: v2.pop()
        i = 0
        while i < min(len(v1),len(v2)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
            i+=1
        if len(v1) == len(v2): return 0
        return 1 if i == len(v2) else -1