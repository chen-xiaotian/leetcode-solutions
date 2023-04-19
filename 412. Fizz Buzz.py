# https://leetcode.com/problems/fizz-buzz/
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        str_list = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 != 0:
                str_list.append("Fizz")
            elif i%5 == 0 and i%3 != 0:
                str_list.append("Buzz")
            elif i%5==0 and i%3 == 0:
                str_list.append("FizzBuzz")
            else:
                str_list.append(str(i))
        return str_list

# Cleaner solution
def fizzBuzz(self, n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]