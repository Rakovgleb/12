def task1():
    # TODO: первое задание
    print(float(input())**2)
    
def task2():
    # TODO: второе задание
    a2 = input()
    b2 = 0
    for i in a2:
        if i in '0123456789':
            b2 += 1
    print(b2)
    
def task3():
    # TODO: третье задание
    a3 = input().split()
    b3 = 0
    for i in a3:
        if i[0] + i[1] == 'ab' and i[-2] + i[-1] =='ba':
            b3 += 1
    print(b3)
    
def task4(generator):
    # TODO: четвертое задание
    if generator % 2 == 1:
        print(generator)

def task5(list_of_smth):
    # TODO: пятое задание
    print(list_of_smth[5:-2:3])
    
def task6(list1, list2, list3, list4):
    # TODO: шестое задание
    a6 = []
    for i in list1:
        if i in list4:
            a6.append(i)
    b6 = []
    for i in list2:
        if i in list3:
            b6.append(i)
    c6 = a6 + b6
    d6 =[]
    for i in c6:
        if i not in d6:
            d6.append(i)
    print(d6)
def task7():
    # TODO: седьмое задание
    import numpy as np
    array = np.random.randint(50, size=49)
    matrix = array.reshape(7, 7)
    print(matrix)
    np.delete(matrix, 5, 0)
    np.delete(matrix, 5, 1)
    print(np.det(matrix))
    
def task8(f, min_x, max_x, N, min_y, max_y):
    # TODO: восьмое задание
    import matplotlib.pyplot as plt
    x = np.linspace(min_x, max_x, N)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()
    yy = np.cos(x)
    plt.plot(x, yy)
    plt.show()
def task9(data, x_array, y_array, threshold):
    # TODO: девятое задание

def task10(list_of_smth, n):
    # TODO: десятое задание
    a10 = len(list_of_smth)
    b10 = []
    for i in range(a10):
        b10.append(0)
        if a10 - i <= n:
            for j in range(i, i+n):
                b10[i] = b10[i] + list_of_smth[j]**2
            b10[i] = (b10[i] / n) ** 0.5
        else:
            for j in range(i, a10):
                b10[i] = b10[i] + list_of_smth[j]**2
            b10[i] = (b10[i] / (a10 - i)) ** 0.5
    print(b10)
def task11(filename="infile.csv"):
    # TODO: одиннадцатое задание

def task12(filename="video-games.csv"):
    # TODO: двенадцатое задание
    import pandas as pd
    f = pd.read_csv('video_games.csv')
    print('n_games', f.shape[0]-1)
    print('by_years')
    print(f.groupby(['year']).agg({'year': 'count'}))
    print('mean_price')
    print(f.groupby(['publisher']).agg({'price': 'mean'}))
    print('age_max_price')
    print(f.groupby(['age_raiting']).agg({'price': 'max'}))