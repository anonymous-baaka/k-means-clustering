import math
import random
import decimal
import matplotlib.pyplot as plt

class Point:
    cluster=None
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.distance=math.inf

def getdistance(p1,p2):
    return round(math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2),2)

def updateCluster(point,clusterlist):
    if point not in clusterlist:
        point.distance=math.inf
    for clusterpoint in clusterlist:
         if point.distance>getdistance(point,clusterpoint):
             point.distance=getdistance(point,clusterpoint)
             point.cluster=clusterpoint
    return

def displayClusters():
    global clusterlist
    print("diosplaying clusterpoints: ")
    for cpoint in clusterlist:
        print(cpoint.x,cpoint.y)

def displayPoints():
    global pointlist
    global clusterlist
    print("displaing points:")
    str="X   Y\t"
    for i in range(len(clusterlist)):
        str+="distance-from-{}".format(i+1)+"\t"
    print(str)
    for cpoint in pointlist:
        print(cpoint.x, cpoint.y,end="\t")
        for cluspoint in clusterlist:
            print(getdistance(cpoint,cluspoint),end="\t\t\t")
        print()

def getnewclusterlist(pointlist,clusterlist):
    newclusterlist=[]
    for cpoint in clusterlist:
        sumX=0
        sumY=0
        num=0
        for point in pointlist:
            if point.cluster==cpoint:
                sumX+=point.x
                sumY+=point.y
                num+=1
        if num!=0:
            newclusterlist.append(Point((sumX)/num,sumY/num))
    return newclusterlist

def check_if_equal(l1,l2):
    for p1 in l1:
        for p2 in l2:
            if p1.x==p2.x and p1.y==p2.y:
                if p1.cluster.x!=p2.cluster.x or p1.cluster.y!=p2.cluster.y:
                    return False
    return True

pointlist=[]
clusterlist=[]
def main():
    decimal.getcontext().prec = 2
    global pointlist,clusterlist

    '''n=int(input("Number of points: "))
    k=int(input("k: "))
    
    for i  in range(n):
        arr=[int(x) for x in input().split()]
        pointlist.append(Point(arr[0],arr[1]))'''
    x= [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72]
    y= [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
    for i in range(len(x)):
        pointlist.append(Point(x[i],y[i]))
    k=3
    #1st iteration
    clusterlist=random.sample(pointlist,k)

    for point in pointlist:
        updateCluster(point,clusterlist)

    #displayClusters()
    #displayPoints()

    flag=True
    while flag:
        newclusterlist=getnewclusterlist(pointlist,clusterlist)
        #else:
        clusterlist=newclusterlist

        old=pointlist.copy()
        for point in pointlist:
            updateCluster(point,clusterlist)


        #displayClusters()
        #displayPoints()
        if check_if_equal(old,pointlist):
            break

    displayPoints()

    #to array
    arrX=[]
    colorlist=["red","blue","brown","green","purple"]
    for point in pointlist:
        arrX.append(point.x)
    arrY = []
    for point in pointlist:
        arrY.append(point.y)
    index=0
    for i in range(len(pointlist)):
        for j in range(len(clusterlist)):
            if pointlist[i].cluster==clusterlist[j]:
                index=j
                break
        plt.scatter(arrX[i],arrY[i],c=colorlist[index])
    plt.show()

main()
