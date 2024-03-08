import random as r
from matplotlib import pyplot as plt
import time as ti
import Heap2ary as h2
import Heap3ary as h3
import Heap4ary as h4


def TimeIt(heap, dataset):
    start = ti.time()
    heap.MaxHeap(dataset)
    return ti.time()-start


def GetData(k, max):
    temp = []
    for i in range(0, k):
        temp.append(r.randint(0, max))
    return temp


def Main():
    # platforma na testy
    # pokazać kopce
    n = []
    times2 = []
    times3 = []
    times4 = []
    for i in range(0, 100001, 10000):
        times2sum = 0
        times3sum = 0
        times4sum = 0
        for _ in range(1, 20):
            data_Set = GetData(i, 10000)
            times2sum += TimeIt(h2, data_Set)
            times3sum += TimeIt(h3, data_Set)
            times4sum += TimeIt(h4, data_Set)
        times2.append(times2sum/20)
        times3.append(times3sum/20)
        times4.append(times4sum/20)
        n.append(i)
    # pokaż pomiary

    plt.plot(n, times2, label="2-ary")
    plt.plot(n, times3, label="3-ary")
    plt.plot(n, times4, label="4-ary")
    plt.xlabel("n elements")
    plt.ylabel("time[s] in seconds")
    plt.legend()
    plt.savefig("combined.png")
    plt.clf()
    plt.plot(n, times2, label="2-ary")
    plt.xlabel("n elements")
    plt.ylabel("time[s] in seconds")
    plt.legend()
    plt.savefig("2ary.png")
    plt.clf()
    plt.plot(n, times2, label="3-ary")
    plt.xlabel("n elements")
    plt.ylabel("time[s] in seconds")
    plt.legend()
    plt.savefig("3ary.png")
    plt.clf()
    plt.plot(n, times2, label="4-ary")
    plt.xlabel("n elements")
    plt.ylabel("time[s] in seconds")
    plt.legend()
    plt.savefig("4ary.png")
    plt.clf()
    data_Set = GetData(27, 20)
    print(h2.MaxHeap(data_Set).DisplayHeap())
    print(h3.MaxHeap(data_Set).DisplayHeap())
    print(h4.MaxHeap(data_Set).DisplayHeap())


if __name__ == "__main__":
    Main()
