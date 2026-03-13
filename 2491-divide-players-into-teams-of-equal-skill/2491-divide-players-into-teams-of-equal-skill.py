class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) -1
        sum1 = 0
        sum2 = skill[0] + skill[-1]
        while left < right:
            if sum2 == skill[left] + skill[right]:
                sum1 += (skill[left] * skill[right])
                left +=1
                right -=1
            else:
                return -1
        return sum1            