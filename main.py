'''
================方法1： sklearn.cluster==================
'''
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import datasets
# from sklearn.cluster import DBSCAN
#
# # matplotlib inline
# X1, y1 = datasets.make_circles(n_samples=5000, factor=.6, noise=.05)
# X2, y2 = datasets.make_blobs(n_samples=1000, n_features=2, centers=[[1.2,1.2]], cluster_std=[[.1]], random_state=9)
#
# X = np.concatenate((X1, X2))
#
# # 展示样本数据分布
# plt.scatter(X[:, 0], X[:, 1], marker='o')
# plt.show()
#
# # eps和min_samples 需要进行调参
# y_pred = DBSCAN(eps = 0.1, min_samples = 10).fit_predict(X)
#
# # 分类结果
# plt.scatter(X[:, 0], X[:, 1], c=y_pred)
# plt.show()


'''
====================方法2：self-defined function===================
'''
import numpy as np
import matplotlib.pyplot as plt
from dbscan import DBSCAN

def loadDataSet(filename):
    dataSet = []
    fr = open(filename)
    for line in fr.readlines():
        # line1 = line.strip('')
        curLine = line.strip().split(',')
        # print('\n curLine = ', curLine)
        fltLine = map(float, curLine)
        # print('\n fltLine = ', fltLine)
        # print('\n list(fltLine) = ', list(fltLine))
        #python2.x map函数返回list
        #dataSet.append(fltLine)
        #python3.x map函数返回迭代器
        dataSet.append(list(fltLine))
    return dataSet

def draw(C , dataSet):
    color = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
    marker = ['*', 'o', 'v', 'p', 'd', 'x', '+']
    for i in C.keys():
        X = []
        Y = []
        datas = C[i]
        for j in range(len(datas)):
            X.append(dataSet[datas[j]][0])
            Y.append(dataSet[datas[j]][1])
        plt.scatter(X, Y, marker=marker[i % len(marker)], color=color[i % len(color)], label=i)
    plt.xlabel("x /m")
    plt.ylabel("y /m")
    plt.legend(loc='upper right')
    plt.show()

def main():
    # for index in range(99):
    dataSet = loadDataSet("./data/ped_percep_35.txt")
    # print(dataSet)
    # print(np.shape(dataSet))
    C = DBSCAN(dataSet, 2.5, 4)
    draw(C, dataSet)

if __name__ == '__main__':
    main()

