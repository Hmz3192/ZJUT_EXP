from django.shortcuts import render
from .exp.css import *
import json
from django.shortcuts import HttpResponse
from .exp.fuccy_wash import *
from .exp.test4 import *
from .exp.test5 import *
from .exp.ga_max import *
from .exp.test7 import *
from .exp.hopfield_tsp import *
from .exp.qpso import *
from .exp.qea_run import *
from .exp.ACO import *


def get_pso_tsp(request):
    data = pso_tsp()
    re_data = {"mes": "ok", "data": data}
    return HttpResponse(json.dumps(re_data))


def get_qea_run(request):
    data = qea_run()
    re_data = {"mes": "ok", "data": data}
    return HttpResponse(json.dumps(re_data))


def get_qpso_run(request):
    data = qpso()
    re_data = {"mes": "ok", "data": data}
    return HttpResponse(json.dumps(re_data))


def get_qpso(request):
    data = qpso()
    re_data = {"mes": "ok", "data": data}
    return HttpResponse(json.dumps(re_data))


def hop_tsp(request):
    data = hopfield_tsp()
    re_data = {"mes": "ok", "data": data}
    return HttpResponse(json.dumps(re_data))


def gp_tsp(request):
    data = find_tsp()
    re_data = {"mes": "ok", "data": data}
    return HttpResponse(json.dumps(re_data))


def gp_max(request):
    data = find_gp_max()
    re_data = {"mes": "ok", "data": data}
    return HttpResponse(json.dumps(re_data))


def migong(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    # map = eval(request.GET.get('map'))
    data = zhaomigong(start, end)
    re_data = {"mes": "ok", "data": data}
    return HttpResponse(json.dumps(re_data))


def bashuma(request):
    current = eval(request.GET.get('current'))
    target = eval(request.GET.get('target'))
    data = getbashuma(current, target)
    re_data = {"mes": "ok", "data": data}
    return HttpResponse(json.dumps(re_data))


def xiyiji(request):
    sg = request.GET.get('sg').split(',')
    gr = request.GET.get('gr').split(',')
    data = fuccy(sg, gr)
    re_data = {"mes": "ok", "data": data}
    return HttpResponse(json.dumps(re_data))


def chanshengshi(request):
    input = request.GET.get('data')
    list_real = input.split(',')
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
    # list_real = []
    # while (1):
    #     # 循环输入前提条件所对应的字典中的键
    #     num_real = input("请输入：")
    #     list_real.append(num_real)
    #     if (num_real == '0'):
    #         break
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
    re_data = {"mes": "ok", "data": data}
    return HttpResponse(json.dumps(re_data))
