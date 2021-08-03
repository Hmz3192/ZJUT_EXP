import math

import numpy as np
from matplotlib import pyplot as plt
import copy
import random
import sys
sys.setrecursionlimit(1000000)

#D:变量维度
#n：种群规模
#T：迭代次数
#upper_bound:变量上界
#lower_bound:变量下界
D = 100
n = 300
T = 100
upper_bound = 600
lower_bound = -600
c1 = 2  # 学习因子，一般为2
c2 = 2
w = 0.4  # 自身权重因子


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
    def __init__(self, swarm_x=np.array([]),swarm_v=np.array([])):
        self.x = swarm_x
        self.v = swarm_v
        self.fit = None
        self.p_best = self
        self.ng_best = self

    # 随机初始化粒子位置
    def initSwarm(self):
        for i in range(D):
            xi = np.random.rand() * (upper_bound - lower_bound) + lower_bound
            self.x = np.append(self.x, xi)
            vi= random.uniform(0, 1)
            self.v=np.append(self.v, vi)
        self.getFitness()
        self.updateP_best(self)

    # 更新粒子位置
    def updateSwarm(self):
        self.v = w * self.v + c1 * random.uniform(0, 1) * (
                    self.p_best.x - self.x) + c2 * random.uniform(0, 1) * (self.ng_best.x - self.x)
        self.x=self.v+self.x
        self.checkSwarm()


    # 适应度
    def getFitness(self):
        self.fit = testFunction(self.x)

    # 比较两个粒子优劣
    def isBetter(self, another_swarm):
        flag = True
        if self.fit > another_swarm.fit:
            flag = False
        return flag

    # 检查粒子边界合法性
    def checkSwarm(self):
        for i in range(D):
            if upper_bound < self.x[i]:
                self.x[i] = upper_bound
            if lower_bound > self.x[i]:
                self.x[i] = lower_bound

    # 更新粒子历史最优
    def updateP_best(self, new_swarm):
        if new_swarm.isBetter(self.p_best):
            self.p_best = new_swarm


# 粒子种群类
class SwarmPop:
    def __init__(self, n):
        self.n = n
        self.pop = [None] * self.n
        self.g_best = Swarm(np.array([]))

    # 初始化种群
    def initPop(self):
        for i in range(self.n):
            self.pop[i] = Swarm()
            self.pop[i].initSwarm()

    #领域（环形）
    def circle(self,i,t,n):
        left = right = i
        for j in range(t):
            left=left-1
            right=right+1
            if left==-1:
                left=n-1
            if right==n:
                right=0
            if self.pop[left].fit < self.pop[i].ng_best.fit:
                self.pop[i].ng_best = copy.deepcopy(self.pop[left])
            if self.pop[right].fit < self.pop[i].ng_best.fit:
                self.pop[i].ng_best = copy.deepcopy(self.pop[right])

    # 更新种群
    def updatePopSwarm(self,t):
        for i in range(self.n):
            if t==0:
                self.pop[i].ng_best = copy.deepcopy(pso.pop[i])
            else:
                if t== math.floor(n/2): #已变成全局
                    self.pop[i].ng_best = copy.deepcopy(self.g_best)
                else:
                    self.circle(i,t,n)
            self.pop[i].updateSwarm()
            self.pop[i].getFitness()
            self.pop[i].updateP_best(self.pop[i])
            if self.pop[i].fit < self.g_best.fit:
                self.g_best = copy.deepcopy(self.pop[i])


if __name__ == "__main__":
    pso = SwarmPop(n)
    pso.initPop()
    pso.g_best = copy.deepcopy(pso.pop[0])
    for i in range(n):
        if pso.pop[i].fit < pso.g_best.fit:
            pso.g_best = copy.deepcopy(pso.pop[i])
    # 种群g_best记录
    G_BEST = []
    # 种群每代平均适应度值记录
    MEAN = []
    #迭代
    for t in range(T):
        pso.updatePopSwarm(t)
        G_BEST.append(pso.g_best.fit)
        mean = 0
        for i in range(n):
            mean += pso.pop[i].fit
        MEAN.append(mean / n)
    plt.figure()
    plt.plot(G_BEST,label="G_BEST")
    plt.plot(MEAN,label="MEAN")
    plt.legend()
    plt.show()
