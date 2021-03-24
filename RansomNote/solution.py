

class RansomNote(object):

    @staticmethod
    def solution(ransom: str, magazine: str) -> bool:
        counter = {}
        for i in magazine:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
        for s in ransom:
            if s not in magazine or counter[s] == 0:
                return False
            else:
                counter[s] -= 1
        return True


print(RansomNote().solution("aab", "abc"))  # False
print(RansomNote().solution("ab", "aab"))  # True
print(RansomNote().solution("a", "b"))  # False


