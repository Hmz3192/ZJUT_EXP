import numpy as np


def fuccy(sg, gr):
    ##################################第一条规则
    sludge = [1, 0.5, 0]  # x1 第一条规则
    grease = [1, 0.5, 0]  # y1 第一条规则
    time = [1, 0.8, 0.6, 0.4, 0.2]  # z1 第一条规则
    sludgeandgrease = np.zeros((len(sludge), len(grease)))  # 建立模糊关系 0矩阵
    for i in range(len(sludge)):  # 双for 形成污泥和油脂的模糊关系矩阵R
        for j in range(len(grease)):
            sludgeandgrease[i, j] = min(sludge[i], grease[j])
    sludgeandgrease = sludgeandgrease.reshape(9, 1)  # 拉直
    R1 = np.zeros((len(sludgeandgrease), len(time)))
    for i in range(len(sludgeandgrease)):  # 建立与输出的关系
        for j in range(len(time)):
            R1[i, j] = min(sludgeandgrease[i], time[j])  # R1规则

    ##################################第二条规则
    sludge = [1, 0.5, 0]  # x2 第二条规则
    grease = [0.5, 1, 0.5]  # y2 第二条规则
    time = [0.6, 0.8, 1, 0.8, 0.6]  # z2 第二条规则
    sludgeandgrease = np.zeros((len(sludge), len(grease)))  # 建立模糊关系 0矩阵
    for i in range(len(sludge)):  # 双for 形成污泥和油脂的模糊关系矩阵R
        for j in range(len(grease)):
            sludgeandgrease[i, j] = min(sludge[i], grease[j])
    sludgeandgrease = sludgeandgrease.reshape(9, 1)  # 拉直
    R2 = np.zeros((len(sludgeandgrease), len(time)))
    for i in range(len(sludgeandgrease)):  # 建立与输出的关系
        for j in range(len(time)):
            R2[i, j] = min(sludgeandgrease[i], time[j])  # R2规则

    ##################################第三条规则
    sludge = [1, 0.5, 0]  # x3 第三条规则
    grease = [0, 0.5, 1]  # y3 第三条规则
    time = [0.4, 0.6, 0.8, 1, 0.8]  # z3 第三条规则
    sludgeandgrease = np.zeros((len(sludge), len(grease)))  # 建立模糊关系 0矩阵
    for i in range(len(sludge)):  # 双for 形成污泥和油脂的模糊关系矩阵R
        for j in range(len(grease)):
            sludgeandgrease[i, j] = min(sludge[i], grease[j])
    sludgeandgrease = sludgeandgrease.reshape(9, 1)  # 拉直
    R3 = np.zeros((len(sludgeandgrease), len(time)))
    for i in range(len(sludgeandgrease)):  # 建立与输出的关系
        for j in range(len(time)):
            R3[i, j] = min(sludgeandgrease[i], time[j])  # R4规则

    ##################################第四条规则
    sludge = [0.5, 1, 0.5]  # x4 第四条规则
    grease = [1, 0.5, 0]  # y4 第四条规则
    time = [0.8, 1, 0.8, 0.6, 0.4]  # z4 第四条规则
    sludgeandgrease = np.zeros((len(sludge), len(grease)))  # 建立模糊关系 0矩阵
    for i in range(len(sludge)):  # 双for 形成污泥和油脂的模糊关系矩阵R
        for j in range(len(grease)):
            sludgeandgrease[i, j] = min(sludge[i], grease[j])
    sludgeandgrease = sludgeandgrease.reshape(9, 1)  # 拉直
    R4 = np.zeros((len(sludgeandgrease), len(time)))
    for i in range(len(sludgeandgrease)):  # 建立与输出的关系
        for j in range(len(time)):
            R4[i, j] = min(sludgeandgrease[i], time[j])  # R4规则

    ##################################第五条规则
    sludge = [0.5, 1, 0.5]  # x5 第五条规则
    grease = [0.5, 1, 0.5]  # y5 第五条规则
    time = [0.6, 0.8, 1, 0.8, 0.6]  # z5 第五条规则
    sludgeandgrease = np.zeros((len(sludge), len(grease)))  # 建立模糊关系 0矩阵
    for i in range(len(sludge)):  # 双for 形成污泥和油脂的模糊关系矩阵R
        for j in range(len(grease)):
            sludgeandgrease[i, j] = min(sludge[i], grease[j])
    sludgeandgrease = sludgeandgrease.reshape(9, 1)  # 拉直
    R5 = np.zeros((len(sludgeandgrease), len(time)))
    for i in range(len(sludgeandgrease)):  # 建立与输出的关系
        for j in range(len(time)):
            R5[i, j] = min(sludgeandgrease[i], time[j])  # R5规则

    ##################################第六条规则
    sludge = [0.5, 1, 0.5]  # x6 第六条规则
    grease = [0, 0.5, 1]  # y6 第六条规则
    time = [0.4, 0.6, 0.8, 1, 0.8]  # z6 第六条规则
    sludgeandgrease = np.zeros((len(sludge), len(grease)))  # 建立模糊关系 0矩阵
    for i in range(len(sludge)):  # 双for 形成污泥和油脂的模糊关系矩阵R
        for j in range(len(grease)):
            sludgeandgrease[i, j] = min(sludge[i], grease[j])
    sludgeandgrease = sludgeandgrease.reshape(9, 1)  # 拉直
    R6 = np.zeros((len(sludgeandgrease), len(time)))
    for i in range(len(sludgeandgrease)):  # 建立与输出的关系
        for j in range(len(time)):
            R6[i, j] = min(sludgeandgrease[i], time[j])  # R6规则

    ##################################第七条规则
    sludge = [0, 0.5, 1]  # x7 第七条规则
    grease = [1, 0.5, 0]  # y7 第七条规则
    time = [0.6, 0.8, 1, 0.8, 0.6]  # z7 第七条规则
    sludgeandgrease = np.zeros((len(sludge), len(grease)))  # 建立模糊关系 0矩阵
    for i in range(len(sludge)):  # 双for 形成污泥和油脂的模糊关系矩阵R
        for j in range(len(grease)):
            sludgeandgrease[i, j] = min(sludge[i], grease[j])
    sludgeandgrease = sludgeandgrease.reshape(9, 1)  # 拉直
    R7 = np.zeros((len(sludgeandgrease), len(time)))
    for i in range(len(sludgeandgrease)):  # 建立与输出的关系
        for j in range(len(time)):
            R7[i, j] = min(sludgeandgrease[i], time[j])  # R7规则

    ##################################第八条规则
    sludge = [0, 0.5, 1]  # x8 第八条规则
    grease = [0.5, 1, 0.5]  # y8 第八条规则
    time = [0.4, 0.6, 0.8, 1, 0.8]  # z8 第八条规则
    sludgeandgrease = np.zeros((len(sludge), len(grease)))  # 建立模糊关系 0矩阵
    for i in range(len(sludge)):  # 双for 形成污泥和油脂的模糊关系矩阵R
        for j in range(len(grease)):
            sludgeandgrease[i, j] = min(sludge[i], grease[j])
    sludgeandgrease = sludgeandgrease.reshape(9, 1)  # 拉直
    R8 = np.zeros((len(sludgeandgrease), len(time)))
    for i in range(len(sludgeandgrease)):  # 建立与输出的关系
        for j in range(len(time)):
            R8[i, j] = min(sludgeandgrease[i], time[j])  # R8规则

    ##################################第九条规则
    sludge = [0, 0.5, 1]  # x9 第九条规则
    grease = [0, 0.5, 1]  # y9 第九条规则
    time = [0.2, 0.4, 0.6, 0.8, 1]  # z9 第九条规则
    sludgeandgrease = np.zeros((len(sludge), len(grease)))  # 建立模糊关系 0矩阵
    for i in range(len(sludge)):  # 双for 形成污泥和油脂的模糊关系矩阵R
        for j in range(len(grease)):
            sludgeandgrease[i, j] = min(sludge[i], grease[j])
    sludgeandgrease = sludgeandgrease.reshape(9, 1)  # 拉直
    R9 = np.zeros((len(sludgeandgrease), len(time)))
    for i in range(len(sludgeandgrease)):  # 建立与输出的关系
        for j in range(len(time)):
            R9[i, j] = min(sludgeandgrease[i], time[j])  # R9规则

    R = np.zeros((len(sludgeandgrease), len(time)))
    for i in range(9):
        for j in range(3):
            R[i, j] = max(R1[i, j], R2[i, j], R3[i, j], R4[i, j], R5[i, j], R6[i, j], R7[i, j], R8[i, j],
                          R9[i, j])  # 总模糊关系

    # sludge = [0.5, 0.83, 0.6]  # 输入量的模糊集合
    # grease = [0.5, 0.71, 0.7]  # 输入量的模糊集合
    sludgeandgrease = np.zeros((len(sg), len(gr)))  # 建立模糊关系 0矩阵
    for i in range(len(sg)):  # 双for 形成污泥和油脂的模糊关系矩阵R
        for j in range(len(gr)):
            sludgeandgrease[i, j] = min(sg[i], gr[j])
    inputsludgeandgrease = sludgeandgrease.reshape(9, 1)  # 拉直
    C1 = np.zeros(9)
    C2 = np.zeros(9)
    C3 = np.zeros(9)
    C4 = np.zeros(9)
    C5 = np.zeros(9)
    for i in range(9):  # 计算模糊集合1
        C1[i] = min(inputsludgeandgrease[i], R[i][0])
    for i in range(9):  # 计算模糊集合2
        C2[i] = min(inputsludgeandgrease[i], R[i][1])
    for i in range(9):  # 计算模糊集合3
        C3[i] = min(inputsludgeandgrease[i], R[i][2])
    for i in range(9):  # 计算模糊集合3
        C4[i] = min(inputsludgeandgrease[i], R[i][3])
    for i in range(9):  # 计算模糊集合3
        C5[i] = min(inputsludgeandgrease[i], R[i][4])
    C = np.zeros(5)
    C = [max(C1), max(C2), max(C3), max(C4), max(C5)]  # 模糊集合
    print(C)  # 时间论域有五个，VS,S,M,L,VL.选取最大的作为输入结果。
    return C


if __name__ == "__main__":
    sg = [0.5, 0.83, 0.6]
    gr = [0.5, 0.71, 0.7]
    fuccy(sg, gr)
