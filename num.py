import time

print("求和计算器——简易学习版")

time.sleep(1)
f1 = 0.0
f2 = 0.0


def mumm(num1, num2):
    return num1 + num2


while True:
    try:

        f1_input = (input("请输入第一个数字: "))
        f1_value = float(f1_input)

        f2_input = (input("请输入第二个数字: "))
        f2_value = float(f2_input)
        print(f"{f1_value}+{f2_value}求和结果为：{mumm(f1_value, f2_value)}")

        zifu = str(input("若想退出程序请输入tc："))
        if zifu == "tc":
            print("退出")
            time.sleep(1)
            break
        print("计算继续")
    except ValueError:
        print("输入错误，请重新输入有效的浮点数")
