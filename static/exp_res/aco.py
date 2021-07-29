import numpy as np
import random
import matplotlib.pyplot as plt

# city_location = np.loadtxt('test1.txt')  # 读取文件中城市的坐标数据，可根据需要修改，test1.txt包含14个城市坐标
city_location = np.array(
    [[106.54, 29.59], [91.11, 29.97], [87.68, 43.77], [106.27, 38.47], [111.65, 40.82], [108.33, 22.84],
     [126.63, 45.75], [125.35, 43.88], [123.38, 41.8], [114.48, 38.03], [112.53, 37.87], [101.74, 36.56],
     [117, 36.65], [113.6, 34.76]])
num_city = city_location.shape[0]  # 城市个数
num_ant = 5 * num_city  # 蚂蚁个数
alpha = 1  # 信息素启发式因子
beta = 5  # 期望影响因子
rho = 0.2  # 信息素的挥发率
Q = 1  # 信息素强度因子
cnt_iteration1 = 0  # 当前迭代次数
max_iteration = 200  # 最大迭代次数

'''该函数计算城市之间的欧式距离'''


def get_distance(city_location):
    num = city_location.shape[0]
    distmat = np.zeros((num, num))  # 初始化生成坐标信息的矩阵，所有元素的值都为0
    for i in range(num):
        for j in range(num):
            distmat[i][j] = np.linalg.norm(city_location[i] - city_location[j])  # 计算欧式距离
    return distmat


'''初始化参数'''

'''初始化各种矩阵'''


def pso_tsp():
    cnt_iteration = 0
    distmat = get_distance(city_location)  # 城市之间的距离矩阵
    pheromone_table = np.ones((num_city, num_city))  # 信息素浓度矩阵
    eta_table = 1.0 / (distmat + np.diag([10000] * num_city))  # 局部启发信息矩阵,为了使除数不为0，往矩阵对角线添加数值
    diag = np.diag([1.0 / 10000] * num_city)  # 创造和局部启发信息矩阵对角线元素相同的矩阵
    eta_table = eta_table - diag  # 把对角元素变回0

    route_best = np.zeros((max_iteration, num_city))  # 记录每一代的最佳路径
    length_best = np.zeros((max_iteration, 1))  # 记录每一代的最佳路径的长度
    length_average = np.zeros((max_iteration, 1))  # 记录每一代的路径平均长度
    path_mat = np.zeros((max_iteration, num_city)).astype(int)  # 初始化每只蚂蚁路径，初始所有元素都为0
    str = ''
    while cnt_iteration < max_iteration:
        '''产生一个随机数，用来决定每一只蚂蚁出生的城市'''
        for i in range(0, num_ant):
            rand_num = random.randint(0, num_city - 1)
            path_mat[i, 0] = rand_num

        length = np.zeros(num_ant)  # 初始化距离数组，用于存储每只蚂蚁走的路线长度

        '''计算出每只蚂蚁转移到下一个城市的概率'''
        for i in range(num_ant):
            visited = path_mat[i, 0]
            unvisited = list(range(num_city))
            unvisited.remove(visited)  # 删除已经访问过的城市

            '''j从1开始，循环num_city-1次，访问剩下的城市'''
            for j in range(1, num_city):
                trans_prob = np.zeros(len(unvisited))  # 初始化转移概率矩阵

                '''转移概率的计算'''
                for k in range(len(unvisited)):
                    trans_prob[k] = np.power(pheromone_table[visited][unvisited[k]], alpha) * np.power(
                        eta_table[visited][unvisited[k]], beta)

                '''找到要访问的下个城市'''
                cumsumtrans_prob = (trans_prob / sum(trans_prob)).cumsum()  # 求出每只蚂蚁转移到各个城市的概率斐波那契数列，方便后续赌轮盘选择
                cumsumtrans_prob -= np.random.rand()  # 减去一个随机数，然后找到转移概率矩阵里恰好大于0的城市

                index = 0
                cnt = 0
                for value in cumsumtrans_prob:
                    if value > 0:
                        index = unvisited[cnt]
                        break
                    else:
                        cnt += 1  # 记录下恰好大于0 处的第一个索引

                '''找到后，加入路径矩阵，并删除未访问列表中的该城市，并将这个城市加入到已访问的城市中'''
                path_mat[i, j] = index  # 将这个索引加入到路径的矩阵里
                unvisited.remove(index)  # 从未访问列表中删去这个索引
                length[i] += distmat[visited][index]  # 累加计算每个蚂蚁走过的总路程
                visited = index  # 将已访问的值设置为将要访问的城市

            length[i] += distmat[visited][path_mat[i, 0]]  # 添加上最后一个城市返回第一个城市的距离

        length_average[cnt_iteration] = length.mean()  # 计算出这一  代蚁群的路径的平均值
        '''求出最优路径'''
        if cnt_iteration == 0:
            length_best[cnt_iteration] = length.min()
            route_best[cnt_iteration] = path_mat[length.argmin()].copy()  # 第一轮选择本轮的最短路径，并返回索引下标
            str += ("The shortest distance in generation {} is {}. \n".format(cnt_iteration, length.min()))
        else:
            if length.min() > length_best[cnt_iteration - 1]:
                length_best[cnt_iteration] = length_best[cnt_iteration - 1]
                route_best[cnt_iteration] = route_best[cnt_iteration - 1].copy()
            else:
                length_best[cnt_iteration] = length.min()
                route_best[cnt_iteration] = path_mat[length.argmin()].copy()  # 如果不是第一轮，则选择本轮最短路径，并返回索引下标
            str += ("The shortest distance in generation {} is {}. \n".format(cnt_iteration, length.min()))

        '''更新信息素'''
        new_pheromone_table = np.zeros((num_city, num_city))
        for i in range(num_ant):
            for j in range(num_city - 1):
                new_pheromone_table[path_mat[i, j]][path_mat[i, j + 1]] += Q / distmat[path_mat[i, j]][
                    path_mat[i, j + 1]]  # 根据公式更新这只蚂蚁改变的城市间的信息素
            new_pheromone_table[path_mat[i, j + 1]][path_mat[i, 0]] += Q / distmat[path_mat[i, j + 1]][
                path_mat[i, 0]]  # 最后一个城市到第一个城市的信息素改变也计算进来

        pheromone_table = (1 - rho) * pheromone_table + new_pheromone_table

        cnt_iteration += 1  # 迭代次数+ 1

    '''打印出最优路径等信息'''
    str += ('The shortest distance is ：{}\n'.format(length_best.min()))
    str += ('The routine is as follows: {}\n').format(route_best[np.argmin(length_best)])

    '''画图验证最后的结果'''
    result = route_best[-1]  # 找到最后一个最优解
    # plt.plot(city_location[:,0].T,city_location[:,1].T,'*') #画出城市的点
    for i in range(num_city - 1):
        ax = plt.axes()
        ax.arrow(city_location[int(result[i]), 0], city_location[int(result[i]), 1],
                 (city_location[int(result[i + 1]), 0] - city_location[int(result[i]), 0]) \
                 , (city_location[int(result[i + 1]), 1] - city_location[int(result[i]), 1]), head_width=0,
                 head_length=0, fc='k', ec='k')  # 根据最后结果连接城市之间的线段
    ax.arrow(city_location[int(result[-1]), 0], city_location[int(result[-1]), 1],
             (city_location[int(result[0]), 0] - city_location[int(result[-1]), 0]), \
             (city_location[int(result[0]), 1] - city_location[int(result[-1]), 1]), head_width=0, head_length=0,
             fc='k', ec='k')  # 画出最后一个城市指向第一个城市的线段
    # plt.show() #展示出所画的图
    return str
