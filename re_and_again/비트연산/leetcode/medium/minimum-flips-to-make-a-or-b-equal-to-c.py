'''
a, b의 bit를 최소한으로 뒤집어서 a || b == c를 만들어라.


a, b, c 를 >> 해가면서

c_bit == 0 일 때) a_bit + b_bit 만큼 filp해야함 (answer += (a_bit + b_bit_)
c_bit == 1 일 때) a_bit == 0 && b_bit == 0 이면 둘 중 하나 filp함 (answer += 1)

1 <= a, b, c < 10**9
이기 때문에, 최대 시간 복잡도 log(10**9)
'''

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        answer = 0

        while a > 0 or b > 0 or c > 0:
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1

            if c_bit == 0:
                answer += (a_bit + b_bit)
            else:
                if a_bit + b_bit == 0:
                    answer += 1
            
            a >>= 1
            b >>= 1
            c >>= 1
        
        return answer
                