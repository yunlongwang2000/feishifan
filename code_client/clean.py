from numpy import array
from matplotlib.pyplot import rcParams, subplots, plot, title, savefig
from pandas import DataFrame
from collections import Counter


def get_red_blue(data):
    global red, blue
    r = array(list(map(lambda x:x[2].split(), data)))
    red = list(map(lambda x: list(map(int, r[:, x])), range(6)))
    blue = list(map(lambda x: int(x[3]), data))


def draw_red_blue():
    rcParams['font.sans-serif'] = ['SimHei']
    des = []
    for x in (10, 30, 100, 300):
        for index, item in enumerate(red):
            y1 = item[:x]
            df = DataFrame(y1)
            des.append([Counter(y1).most_common(1)[0][0], df.describe()[0][2], df.describe()[0][4], df.describe()[0][5],df.describe()[0][6]])
            subplots(figsize=(6.5, 4.5))
            plot(range(1, x+1), list(reversed(item[:x])))
            title("红{}".format(index+1))
            savefig('./Resources/data/{}_{}.svg'.format(x, index+1))
        y2 = blue[:x]
        df = DataFrame(y2)
        des.append([Counter(y2).most_common(1)[0][0], df.describe()[0][2], df.describe()[0][4], df.describe()[0][5], df.describe()[0][6]])
        subplots(figsize=(6.5, 4.5))
        plot(range(1, x+1), list(reversed(y2)))
        title("蓝")
        savefig('./Resources/data/{}_7.svg'.format(x))
    d1, d2, d3, d4 = DataFrame(des[:7]), DataFrame(des[7:14]), DataFrame(des[14:21]), DataFrame(des[21:])
    return DataFrame(d1.values.T).values.tolist(), DataFrame(d2.values.T).values.tolist(), DataFrame(d3.values.T).values.tolist(), DataFrame(d4.values.T).values.tolist()


def vis(data):
    get_red_blue(data)
    sta = draw_red_blue()
    return sta
