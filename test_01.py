# a = input('请输入一个整数，程序会自动输出其因数：')

while True:
    a = None
    try: 
        a = int(input('请输入一个整数，程序会自动输出其因数：'))
    except :
        pass

    if type(a) == int:
        b = 1
        temp = []
    for num in range(b, a):
        if a % num == 0:
            c =  int(a / num)
            min = None
            max = None
            if c >= num:
                min = num
                max = c
            else:
                min = c
                max = num
            numTemp = [min, max]
            if not numTemp in temp: 
                temp.append(numTemp)

    if len(temp) > 0:
        print('整数 {num} 的因数是:{array}'.format(num = a, array = temp))