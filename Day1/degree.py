# 将华氏度转换为摄氏度的方法
def degree():
    f = float(input('请输入华氏温度：'))
    c = (f - 32) / 1.8
    print('%.1f 华氏度 = %.1f 摄氏度' % (f, c))


if __name__ == '__main__':
    degree()
