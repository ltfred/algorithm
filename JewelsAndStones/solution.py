
class JewelsAndStones(object):

    @staticmethod
    def solution(jewels: str, stones: str) -> int:
        # 转为集合
        jewels = set(jewels)
        count = 0
        for s in stones:
            if s in jewels:
                count += 1
        return count


print(JewelsAndStones().solution("ab", "Aabcha"))  # 3
print(JewelsAndStones().solution("e", "Aabcha"))  # 0
