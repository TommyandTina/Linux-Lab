# "Correctly determine the fewest number of banknotes to be given to a customer such that the sum of the banknotes' value would equal the correct amount of change.
# Usinge raise statement to ""throw"" a ValueError when change cannot be made with the banknotes given
# Example 1:
# * We enter the denominations of the banknotes: [1, 5, 10, 25, 100]
# * The target value: 15
# * The result: [5, 10]
# Example 2:
# * We enter the denominations of the banknotes: [1, 4, 15, 20, 50]
# * The target value: 23
# * The result: [4, 4, 15]"

class money_denominations:
    def __init__(self, money_deno):
        self.money_deno = sorted(money_deno, reverse=True)
        self.money_return = []

    def __str__(self):
        return f"money_denominations = {self.money_deno}, money_return = {self.money_return}"
    
    def money_change(self, value):
        for money in self.money_deno:
            while value >= money:
                value -= money
                self.money_return.append(money)
        return self.money_return    

try:

    # Khởi tạo các mệnh giá để thối lại cho khác hàng
    p1 = money_denominations([1, 5, 10, 25, 100])
    value = input("Nhập số tiền cần thối: ")
    p1.money_change(int(value))
    print(p1)

except Exception as e:
    print(f"Có lỗi phát sinh: {e}")
