import numpy as np
from matplotlib import pyplot as plt
import copy

"""
D:变量维度
n：种群规模
T：迭代次数
upper_bound:变量上界
lower_bound:变量下界
"""
D = 4
n = 30
T = 100
upper_bound = 600
lower_bound = -600


# 测试函数
def testFunction(x):
    summary = 0
    multi = 1
    for i in range(D):
        summary += x[i] ** 2 / 4000
        multi *= np.cos(x[i] / np.sqrt(i + 1))
    return summary - multi + 1


# 粒子类
class Swarm:
    def __init__(self, swarm_x=np.array([])):
        self.x = swarm_x
        self.fit = None
        self.p_best = self
        self.p_id = self.x

    # 随机初始化粒子位置
    def initSwarm(self):
        for i in range(D):
            xi = np.random.rand() * (upper_bound - lower_bound) + lower_bound
            self.x = np.append(self.x, xi)
        self.getFitness()
        self.updateP_best(self)

    # 更新粒子位置
    def updateSwarm(self, beta, m_best):
        u = np.random.rand()
        if u < 0.5:
            self.x = self.p_id + beta * abs(m_best - self.x) * np.math.log(1 / u, np.e)
        else:
            self.x = self.p_id - beta * abs(m_best - self.x) * np.math.log(1 / u, np.e)
        # 检查粒子边界合法性
        for i in range(D):
            if upper_bound < self.x[i]:
                self.x[i] = upper_bound
            if lower_bound > self.x[i]:
                self.x[i] = lower_bound

    # 获取粒子最优位置，由p_best和g_best获得
    def getPid(self, g_best):
        u = np.random.rand()
        self.p_id = u * self.p_best.x + (1 - u) * g_best.x

    # 适应度
    def getFitness(self):
        self.fit = testFunction(self.x)

    # 更新粒子历史最优
    def updateP_best(self, new_swarm):
        if self.fit > new_swarm.fit:
            self.p_best = new_swarm


# 粒子种群类
class SwarmPop:
    def __init__(self, n):
        self.n = n
        self.pop = [None] * self.n
        self.g_best = Swarm(np.array([]))
        self.m_best = np.array([])

    # 初始化种群
    def initPop(self):
        for i in range(self.n):
            self.pop[i] = Swarm()
            self.pop[i].initSwarm()

    # 计算种群的重心m_best
    def getM_best(self):
        m = np.array([0] * D)
        for i in range(self.n):
            m = m + self.pop[i].p_best.x
            m = m / self.n
        self.m_best = m

    # 更新种群
    def updatePopSwarm(self):
        for i in range(self.n):
            self.pop[i].getPid(self.g_best)
            self.pop[i].updateSwarm(beta, self.m_best)
            self.pop[i].getFitness()
            self.pop[i].updateP_best(self.pop[i])
            if self.pop[i].fit < self.g_best.fit:
                self.g_best = copy.deepcopy(self.pop[i])


def qpso():
    t = 0
    # 初始化beta、初始化种群
    # beta称为收缩-扩张因子，用来控制粒子的收敛速度，取值介于（0， 1）之间的随机分布数
    beta = ((1 - 0.5) * (T - t - 1)) / T + 0.5
    qpso = SwarmPop(n)
    qpso.initPop()

    # 获取初始种群g_best
    qpso.g_best = copy.deepcopy(qpso.pop[0])
    for i in range(n):
        if qpso.pop[i].fit < qpso.g_best.fit:
            qpso.g_best = copy.deepcopy(qpso.pop[i])
    qpso.getM_best()

    # 种群g_best记录
    G_BEST = [qpso.g_best.fit]

    # 迭代，终止条件未达到一定迭代次数T
    while t < T:
        qpso.updatePopSwarm()
        qpso.getM_best()
        G_BEST.append(qpso.g_best.fit)
        t += 1
        beta = ((1 - 0.5) * (T - t - 1)) / T + 0.5

    print(qpso.g_best.x)
    print(qpso.g_best.fit)
    # 画种群g_best迭代图
    plt.figure()
    plt.plot(G_BEST)
    plt.xlabel('Iteration')
    plt.ylabel('Best Fitness')
    # plt.show()
    str = "{}".format(qpso.g_best.x)
    return


if __name__ == '__main__':
    t = 0
    # 初始化beta、初始化种群
    # beta称为收缩-扩张因子，用来控制粒子的收敛速度，取值介于（0， 1）之间的随机分布数
    beta = ((1 - 0.5) * (T - t - 1)) / T + 0.5
    qpso = SwarmPop(n)
    qpso.initPop()

    # 获取初始种群g_best
    qpso.g_best = copy.deepcopy(qpso.pop[0])
    for i in range(n):
        if qpso.pop[i].fit < qpso.g_best.fit:
            qpso.g_best = copy.deepcopy(qpso.pop[i])
    qpso.getM_best()

    # 种群g_best记录
    G_BEST = [qpso.g_best.fit]

    # 迭代，终止条件未达到一定迭代次数T
    while t < T:
        qpso.updatePopSwarm()
        qpso.getM_best()
        G_BEST.append(qpso.g_best.fit)
        t += 1
        beta = ((1 - 0.5) * (T - t - 1)) / T + 0.5

    print(qpso.g_best.x)
    print(qpso.g_best.fit)
    # 画种群g_best迭代图
    plt.figure()
    plt.plot(G_BEST)
    plt.xlabel('Iteration')
    plt.ylabel('Best Fitness')
    plt.show()
