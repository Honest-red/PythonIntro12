from random import randint


def bubble(array):
    cnt = 0
    for i in range(len(array)-1):
        cnt += 1
        flag = 1
        for j in range(len(array) - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = 0

        if flag:            # flag == True  flag == 4.5
            break
    print(cnt)


lst = [randint(10, 50) for _ in range(20)]
# lst = [11, 15, 15, 20, 21, 22, 23, 26, 24, 28, 30, 34, 36, 36, 39, 42, 44, 45, 45, 48]
print(lst)
bubble(lst)
print(lst)

