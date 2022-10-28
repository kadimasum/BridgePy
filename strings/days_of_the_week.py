


class Solution:
    days_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    number_of_days_in_week = 7

    @classmethod
    def solution(cls, S, k):
        position_of_S = cls.days_of_the_week.index(S)
        offset_days = (position_of_S + k) % cls.number_of_days_in_week
        return cls.days_of_the_week[offset_days]


result = Solution.solution("Tue", 28)
print(result)