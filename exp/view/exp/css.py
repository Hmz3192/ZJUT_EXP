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

if __name__ == "__main__":
    dict_before = {'1': '有毛发', '2': '产奶', '3': '有羽毛', '4': '不会飞', '5': '会下蛋', '6': '吃肉', '7': '有犬齿',
                   '8': '有爪', '9': '眼盯前方', '10': '有蹄', '11': '反刍', '12': '黄褐色', '13': '有斑点', '14': '有黑色条纹',
                   '15': '长脖', '16': '长腿', '17': '不会飞', '18': '会游泳', '19': '黑白二色', '20': '善飞', '21': '哺乳类',
                   '22': '鸟类', '23': '食肉类', '24': '蹄类', '25': '金钱豹', '26': '虎', '27': '长颈鹿', '28': '斑马',
                   '29': '鸵鸟', '30': '企鹅', '31': '信天翁'}
    print("""输入对应条件前面的数字:
                                    *******************************************************
                                    *1:有毛发  2:产奶  3:有羽毛  4:不会飞  5:会下蛋          *
                                    *6:吃肉  7:有犬齿  8:有爪  9:眼盯前方  10:有蹄         *
                                    *11:反刍  12:黄褐色  13:有斑点  14:有黑色条纹  15:长脖 *
                                    *16:长腿  17:不会飞  18:会游泳  19:黑白二色  20:善飞   *
                                    *21：哺乳类  22:鸟类  23:食肉类  24：蹄类              *
                                    *******************************************************
                                    *******************当输入数字0时!程序结束***************
         """)
    # 综合数据库
    list_real = []
    while (1):
        # 循环输入前提条件所对应的字典中的键
        num_real = input("请输入：")
        list_real.append(num_real)
        if (num_real == '0'):
            break
    data = '前提条件为：\n'
    # 输出前提条件
    for i in range(0, len(list_real) - 1):
        data += dict_before[list_real[i]] + '  '
    data += '\n推理过程如下：\n'
    # 遍历综合数据库list_real中的前提条件
    for i in list_real:
        if i == '1':
            if judge_repeat('21', list_real) == 0:
                list_real.append('21')
                data += "有毛发->哺乳类\n"
        elif i == '2':
            if judge_repeat('21', list_real) == 0:
                list_real.append('21')
                data += "产奶->哺乳类\n"
        elif i == '3':
            if judge_repeat('22', list_real) == 0:
                list_real.append('22')
                data += "有羽毛->鸟类\n"
        else:
            if list_real.index(i) != len(list_real) - 1:
                continue
            else:
                break
    for i in list_real:
        if i == '4':
            for i in list_real:
                if i == '5':
                    if judge_repeat('22', list_real) == 0:
                        list_real.append('22')
                        data += "不会飞，会下蛋->鸟类\n"
        elif i == '6':
            for i in list_real:
                if i == '21':
                    if judge_repeat('21', list_real) == 0:
                        list_real.append('21')
                        data += "食肉->哺乳类\n"
        elif i == '7':
            for i in list_real:
                if i == '8':
                    for i in list_real:
                        if i == '9':
                            if judge_repeat('23', list_real) == 0:
                                list_real.append('23')
                                data += "有犬齿,有爪,眼盯前方->食肉类\n"
        elif i == '10':
            for i in list_real:
                if i == '21':
                    if judge_repeat('24', list_real) == 0:
                        list_real.append('24')
                        data += "有蹄，哺乳类->蹄类\n"

        elif i == '11':
            for i in list_real:
                if i == '21':
                    if judge_repeat('24', list_real) == 0:
                        list_real.append('24')
                        data += "反刍，哺乳类->哺乳类\n"

        else:
            if i != len(list_real) - 1:
                continue
            else:
                break
    data = judge_last(list_real, data)
    print(data)
