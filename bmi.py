"""
class (成人の)BMI:
    関連しそうな属性:
        - 身長
        - 体重
        - BMIという値そのもの
    ルール:
        - BMIは10以上40以下 <- 常識的な範囲
        - 表示するときは小数点第2位まで
            - ex: 23.689 => 23.69
            - ex: 23.681 => 23.68
    できること:
        - BMIの計算
"""

class BMI:
    def __init__(self, height, weight):
        # self.height = height
        # self.weight = weight
        self.value = weight / (height ** 2)

    def __str__(self):
        return f"{self.value:.2f}"

    # def calculate_bmi(self):
    #     return self.weight / (self.height ** 2)

so_bmi = BMI(height=1.64, weight=61.0)

# print(so_bmi.height, so_bmi.weight)
# print(so_bmi.calculate_bmi())

print(so_bmi)
