from matplotlib import pyplot as plt
import copy
import numpy as np
import math

upper_bound = 600       # 变量上界
lower_bound = -600      # 变量下界
D = 4                   # 变量空间维度
m = 11 * D              # 量子染色体长度，每一维变量用11位二进制表示


T = 100     # 迭代次数
n = 50      # 种群规模
cr = 0.5    # 交叉概率·
mr = 0.05   # 变异概率


# 测试函数
def function(x):
    summary = 0
    multi = 1
    for i in range(D):
        summary += x[i] ** 2 / 4000
        multi *= np.cos(x[i] / math.sqrt(i+1))
    return summary - multi + 1


# 解码
def decoder(r):
    scale = (2 ** (m / D) - 1) / (upper_bound - lower_bound)
    x = [None] * D
    for i in range(D):
        # 染色体分割
        ri = r[i * m // D:i * m // D + m // D]
        # 二进制转十进制
        s = ''.join(str(j) for j in ri)
        # 映射到变量空间
        x[i] = int(s, 2) / scale + lower_bound
    return x


# 适应度
def getFitness(r):
    return function(decoder(r))

# 量子个体类
class QChromosome:
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta
        self.m = np.shape(self.alpha)[0]
        self.r = np.zeros(self.m, dtype=int)
        self.fit = np.inf

    # 初始化染色体
    def initChromosome(self):
        self.observe()
        self.fitness()

    # 量子观测
    def observe(self):
        rand = np.random.rand()
        for i in range(self.m):
            if rand > self.alpha[i] ** 2:
                self.r[i] = 1
            else:
                self.r[i] = 0

    # 进化-交叉
    def crossover(self, chromosome_):
        index = np.random.randint(self.m)
        # 交换量子位
        temp = self.r[index:]
        self.r[index:] = chromosome_.r[index:]
        chromosome_.r[index:] = temp

    # 进化-变异
    def mutate(self):
        index = np.random.randint(self.m)
        # 变异量子位
        self.r[index] = np.random.choice([0, 1])

    # 量子旋转门操作
    def gate(self, b):
        theta_min = 0.005 * np.pi
        theta_max = 0.01 * np.pi
        for i in range(self.m):
            # step 表示旋转步长，这里使用了根据适应度值自适应步长
            step = theta_min+(theta_max-theta_min)*(abs(self.fit-b.fit)/max(abs(b.fit), abs(self.fit)))
            # s 表示旋转方向
            if self.r[i] == 0:  # ri = 0
                if b.r[i] == 1 and self.fit < b.fit:
                    if self.alpha[i] * self.beta[i] > 0:
                        s = -1
                    elif self.alpha[i] * self.beta[i] < 0:
                        s = 1
                    elif self.alpha[i] == 0:
                        s = np.random.choice([1, -1])
                    else:
                        s = 0
                else:
                    s = 0
            else:               # ri = 1
                if b.r[i] == 0 and not self.fit < b.fit:
                    if self.alpha[i] * self.beta[i] > 0:
                        s = -1
                    elif self.alpha[i] * self.beta[i] < 0:
                        s = 1
                    elif self.alpha[i] == 0:
                        s = np.random.choice([1, -1])
                    else:
                        s = 0
                else:
                    if self.alpha[i] * self.beta[i] > 0:
                        s = 1
                    elif self.alpha[i] * self.beta[i] < 0:
                        s = -1
                    elif self.alpha[i] == 0:
                        s = 0
                    else:
                        s = np.random.choice([1, -1])
            theta = s * step
            a = np.cos(theta) * self.alpha[i] - np.sin(theta) * self.beta[i]
            b_ = np.sin(theta) * self.alpha[i] + np.cos(theta) * self.beta[i]
            self.alpha[i] = a
            self.beta[i] = b_

    # 适应度值
    def fitness(self):
        self.fit = function(decoder(self.r))


# 量子进化种群类
class QPop:
    def __init__(self, n, cr, mr):
        self.m = m
        self.n = n
        self.cr = cr
        self.mr = mr
        self.pop = [None] * n
        self.b = [None] * self.m

    # 初始化种群
    # 为了保证α²+β²=1，使用cos和sin
    def initPop(self):
        alpha = [None] * self.m
        beta = [None] * self.m
        for j in range(self.n):
            for i in range(self.m):
                temp_rand = np.random.rand()
                rand = 2 * np.pi * temp_rand
                alpha[i] = np.cos(rand)
                beta[i] = np.sin(rand)
            self.pop[j] = QChromosome(alpha, beta)
            self.pop[j].initChromosome()
        self.b = copy.deepcopy(self.pop[0])
        self.evaluationPop()

    # 种群量子观测
    def observePop(self):
        for i in range(self.n):
            self.pop[i].observe()

    # 种群进化
    def evolutionPop(self):
        for i in range(self.n):
            # 交叉
            if np.random.rand() < self.cr:
                rand1 = np.random.choice(self.pop)
                rand2 = np.random.choice(self.pop)
                if rand1.fit < rand2.fit:
                    choice1 = rand1
                else:
                    choice1 = rand2
                rand1 = np.random.choice(self.pop)
                rand2 = np.random.choice(self.pop)
                if rand1.fit < rand2.fit:
                    choice2 = rand1
                else:
                    choice2 = rand2
                choice1.crossover(choice2)
            # 变异
            if np.random.rand() < self.mr:
                self.pop[i].mutate()

    # 种群评价，保留最优个体
    def evaluationPop(self):
        for i in range(self.n):
            if self.pop[i].fit < self.b.fit:
                self.b = copy.deepcopy(self.pop[i])

    # 种群量子更新
    def updatePop(self):
        for i in range(self.n):
            self.pop[i].gate(self.b)

    # 计算种群适应度值
    def getPopFitness(self):
        for i in range(self.n):
            self.pop[i].fitness()

def qea_run():
    # 初始化种群
    qp = QPop(n, cr, mr)
    qp.initPop()
    best = copy.deepcopy(qp.b)
    # 记录种群最优适应度值
    all_fit = [best.fit]
    t = 0
    # 迭代，终止条件为达到一定代数T
    while t < T:
        qp.updatePop()
        qp.observePop()
        qp.evolutionPop()
        qp.getPopFitness()
        qp.evaluationPop()
        all_fit.append(qp.b.fit)
        t += 1

    # 画best迭代变化图
    plt.figure('Fitness')
    plt.plot(all_fit)
    plt.xlabel('Iteration')
    plt.ylabel('Fitness')
    # plt.show()
    return ""
# 主函数
if __name__ == '__main__':
    # 初始化种群
    qp = QPop(n, cr, mr)
    qp.initPop()
    best = copy.deepcopy(qp.b)
    # 记录种群最优适应度值
    all_fit = [best.fit]
    t = 0
    # 迭代，终止条件为达到一定代数T
    while t < T:
        qp.updatePop()
        qp.observePop()
        qp.evolutionPop()
        qp.getPopFitness()
        qp.evaluationPop()
        all_fit.append(qp.b.fit)
        t += 1

    # 画best迭代变化图
    plt.figure('Fitness')
    plt.plot(all_fit)
    plt.xlabel('Iteration')
    plt.ylabel('Fitness')
    plt.show()
