# 动物识别系统
# 自定义函数，判断有无重复元素
def judge_repeat(value, list=[]):
    for i in range(0, len(list)):
        if (list[i] == value):
            return 1
        else:
            if (i != len(list) - 1):
                continue
            else:
                return 0


# 自定义函数，对已经整理好的综合数据库real_list进行最终的结果判断

def judge_last(list, data):
    for i in list:
        if i == '23':  # 食肉类
            for i in list:
                if i == '12':  # 黄褐色
                    for i in list:
                        if i == '21':  # 哺乳类
                            for i in list:
                                if i == '13':  # 有斑点
                                    data += "黄褐色，有斑点,哺乳类，食肉类->金钱豹\n"
                                    data += "所识别的动物为金钱豹\n"
                                    return data
                                elif i == '14':  # 有黑色条纹
                                    data += "黄褐色，有黑色条纹，哺乳类，食肉类->虎\n"
                                    data += "所识别的动物为虎\n"
                                    return data


        elif (i == '14'):  # 有黑色条纹
            for i in list:
                if i == '24':  # 蹄类
                    data += "有黑色条纹，蹄类->斑马\n"
                    data += "所识别的动物为斑马"
                    return data


        elif i == '24':  # 蹄类
            for i in list:
                if i == '13':  # 有斑点
                    for i in list:
                        if i == '15':  # 长脖
                            for i in list:
                                if i == '16':  # 长腿
                                    data += "有斑点，有黑色条纹，长脖，蹄类->长颈鹿\n"
                                    data += "所识别的动物为长颈鹿"
                                    return data
        elif i == '20':  # 善飞
            for i in list:
                if i == '22':  # 鸟类
                    data += "善飞，鸟类->信天翁\n"
                    data += "所识别的动物为信天翁"
                    return data

        elif i == '22':  # 鸟类
            for i in list:
                if i == '4':  # 不会飞
                    for i in list:
                        if i == '15':  # 长脖
                            for i in list:
                                if i == '16':  # 长腿
                                    data += "不会飞，长脖，长腿，鸟类->鸵鸟\n"
                                    data += "所识别的动物为鸵鸟"
                                    return data

        elif (i == '4'):  # 不会飞
            for i in list:
                if (i == '22'):  # 鸟类
                    for i in list:
                        if (i == '18'):  # 会游泳
                            for i in list:
                                if (i == '19'):  # 黑白二色
                                    data += "不会飞，会游泳，黑白二色，鸟类->企鹅\n"
                                    data += "所识别的动物企鹅"
                                    return data

        else:
            if (list.index(i) != len(list) - 1):
                continue
            else:
                data += "\n根据所给条件无法判断为何种动物"
            return data
