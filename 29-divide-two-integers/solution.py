// 0 ms | 12.4 MB
class Solution(object):
    def divide(self, dividend, divisor):

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        count = 0

        while dividend >= divisor:

            temp = divisor
            multiple = 1

            # Keep doubling the divisor
            while dividend >= temp + temp:
                temp = temp + temp
                multiple = multiple + multiple

            dividend = dividend - temp
            count = count + multiple

        if negative:
            count = -count

        # 32-bit integer limits
        if count > 2147483647:
            return 2147483647

        if count < -2147483648:
            return -2147483648

        return count