


class Solution:
    days_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    number_of_days_in_week = 7

    @classmethod
    def solution(cls, day, k):
        position_of_day = cls.days_of_the_week.index(day)
        offset_days = (position_of_day + k) % cls.number_of_days_in_week
        return cls.days_of_the_week[offset_days]


result = Solution.solution("Tue", 28)
print(result)