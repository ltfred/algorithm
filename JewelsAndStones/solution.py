
class JewelsAndStones(object):

    @staticmethod
    def solution(jewels, stones):
        # 转为集合
        jewels = set(jewels)
        count = 0
        for s in stones:
            if s in jewels:
                count += 1
        return count


print(JewelsAndStones().solution("ab", "Aabcha"))
