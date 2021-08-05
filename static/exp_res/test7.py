from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import time
import logging
import sys

logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.DEBUG)

def distance_matrix(coordinate_list, size):  # 生成距离矩阵，邻接矩阵
    d = np.zeros((size + 2, size + 2))
    for i in range(size + 1):
        x1 = coordinate_list[i][0]
        y1 = coordinate_list[i][1]
        for j in range(size + 1):
            if (i == j) or (d[i][j] != 0):
                continue
            x2 = coordinate_list[j][0]
            y2 = coordinate_list[j][1]
            distance = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            if (i == 0):  # 起点与终点是同一城市
                d[i][j] = d[j][i] = d[size + 1][j] = d[j][size + 1] = distance
            else:
                d[i][j] = d[j][i] = distance
    return d


def path_length(d_matrix, path_list, size):  # 计算路径长度
    length = 0
    for i in range(size + 1):
        length += d_matrix[path_list[i]][path_list[i + 1]]
    return length


def product_len_probability(my_list, d_matrix, size, p_num):
    len_list = []  # 种群中每个个体（路径）的路径长度
    pro_list = []
    path_len_pro = []
    for path in my_list:
        len_list.append(path_length(d_matrix, path, size))
    max_len = max(len_list) + 1e-10
    gen_best_length = min(len_list)  # 种群中最优路径的长度
    gen_best_length_index = len_list.index(gen_best_length)  # 最优个体在种群中的索引
    # 采用适应度比例的方法，计算最长路径与每个路径的长度的差值，该值越大说明路径越小
    mask_list = np.ones(p_num) * max_len - np.array(len_list)
    sum_len = np.sum(mask_list)  # mask_list列表元素的和
    for i in range(p_num):
        if (i == 0):
            pro_list.append(mask_list[i] / sum_len)
        elif (i == p_num - 1):
            pro_list.append(1)
        else:
            pro_list.append(pro_list[i - 1] + mask_list[i] / sum_len)
    for i in range(p_num):
        # 路径列表 路径长度 概率
        path_len_pro.append([my_list[i], len_list[i], pro_list[i]])
    # 返回 最短路径 最短路径的长度 种群（现在的population中每一元素有三项，第一项是路径，第二项是路径长度，第三项是使用时转盘的概率）
    return my_list[gen_best_length_index], gen_best_length, path_len_pro


def choose_cross(population, p_num):
    jump = np.random.random()  # 随机生成0-1之间的小数
    if jump < population[0][2]:
        return 0
    low = 1
    high = p_num
    mid = int((low + high) / 2)
    # 二分搜索
    # 如果jump在population[mid][2]和population[mid-1][2]之间，那么返回mid
    while (low < high):
        if jump > population[mid][2]:
            low = mid
            mid = (low + high) // 2
        elif jump < population[mid - 1][2]:  # 注意这里一定是mid-1
            high = mid
            mid = (low + high) // 2
        else:
            return mid


def veriation(my_list, size, pm):  # 随机变异
    ver_1 = np.random.randint(1, size + 1)
    ver_2 = np.random.randint(1, size + 1)
    while ver_2 == ver_1:  # 直到ver_2与ver_1不同
        ver_2 = np.random.randint(1, size + 1)
    my_list[ver_1], my_list[ver_2] = my_list[ver_2], my_list[ver_1]
    return my_list


def main(num, gen, pm):
    str = ""
    start = time.time()
    city_num = 10  # 城市数量
    # 随机生成各个城市点的坐标
    x = np.random.randint(0, 100, size=city_num)
    y = np.random.randint(0, 100, size=city_num)  # 生成一个数组1*city_num
    x = np.append(x, x[0])
    y = np.append(y, y[0])  # 把起始点作为终点
    coordinate_list = []  # 存放每个点的坐标
    for i in range(city_num + 1):
        coordinate_list.append([x[i], y[i]])
    size = city_num - 1  # 除去起点
    d = distance_matrix(coordinate_list, size)  # 各城市之间的距离矩阵

    # 初始化种群
    population = []
    path_list = list(range(size + 2))  # 生成从0到city_num+1的数字列表
    for i in range(num):  # 随机排序成为一个个体；种群有num个个体组成
        mid_list = path_list[1:-1]  # 取第二个到倒数第二个的序号
        np.random.shuffle(mid_list)  # 对中间点随机排序
        population.append(path_list[:1] + mid_list + path_list[-1:])

    # 计算最短路径，最短路径长度，以及种群中每个个体的适应值（路径长度）
    gen_best, gen_best_length, population = product_len_probability(population, d, size, num)
    son_list = [0] * num  # 子代
    # son_list = np.zeros(p_num,int)
    best_path = gen_best  # 最短路径
    best_path_length = gen_best_length  # 最短路径的长度
    every_gen_best = [gen_best_length]  # 每一代的最优值
    # 迭代
    for i in range(gen):  # 迭代
        son_num = 0
        # 循环产生子代
        while son_num < num:
            # 随机选择父代，这里采用轮盘赌的方法
            father_index = choose_cross(population, num)
            mother_index = choose_cross(population, num)
            father = population[father_index][0]
            mother = population[mother_index][0]
            son = father.copy()
            product_set = np.random.randint(1, size + 1)
            # 交叉序列集合
            parent_cross_set = set(mother[1:product_set])
            cross_complete = 1
            for j in range(1, size + 1):
                if son[j] in parent_cross_set:
                    son[j] = mother[cross_complete]
                    cross_complete += 1
                    if cross_complete > product_set:
                        break
            # 变异
            if np.random.random() < pm:
                son = veriation(son, size, pm)  # 随机变异
            son_list[son_num] = son
            son_num += 1
            if son_num == num:
                break
        #  计算子代中最短路径，最短路径长度，以及中每个个体的适应值（路径长度）
        gen_best, gen_best_length, population = product_len_probability(son_list, d, size, num)
        # 最短路径更新，如果迭代中的最短路径长度小于最短路径，则更新最短路径
        if (gen_best_length < best_path_length):
            best_path = gen_best
            best_path_length = gen_best_length
        every_gen_best.append(gen_best_length)
    end = time.time()
    str += "时间：{}".format((end - start))

    str += "\n最短路径：{}".format(best_path)  # 最短路径
    str += "\n最短路径长度：{}".format(best_path_length)  # 最短路径长度

    # 画图
    x = [coordinate_list[point][0] for point in best_path]
    y = [coordinate_list[point][1] for point in best_path]
    plt.figure(figsize=(8, 10))
    plt.subplot(211)
    plt.plot(every_gen_best)  # 画每一代中最优路径的路径长度
    plt.subplot(212)
    plt.scatter(x, y)  # 画点
    plt.plot(x, y)  # 画点之间的连线
    plt.grid()  # 给画布添加网格
    # plt.show()

    return str


def find_tsp():
    p_num = 200  # 种群个体数量
    gen = 1000  # 进化代数
    pm = 0.1  # 变异率
    return main(p_num, gen, pm)


if __name__ == "__main__":
    p_num = 200  # 种群个体数量
    gen = 1000  # 进化代数
    pm = 0.1  # 变异率
    main(p_num, gen, pm)
