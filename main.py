import time
from graphics import *
import copy
import sys

def load(filename1,filename2):
    print("loading nodes.....")
    nodes = {}
    with open(filename1,'r') as f:
        semua = f.read()
        for lines in semua.split('\n'):
            data = lines.split(' ')
            nodes[int(data[0])] = float(data[1]),float(data[2])
    
    print("loading edges.....")
    edges = {}
    with open(filename2,'r') as f:
        semua = f.read()
        for lines in semua.split('\n'):
            data = lines.split(' ')
            a = int(data[1])
            b = int(data[2])
            j = float(data[3])
            if a not in edges.keys():
                edges[a] = {}   
            edges[a][b] = j
            if b not in edges.keys():
                edges[b] = {}
            edges[b][a] = j
    return nodes,edges


def jaraklurus(a,b,nodes):
    # print(a,b)
    a = int(a)
    b = int(b)
    x = abs(nodes[a][0] - nodes[b][0])
    y = abs(nodes[a][1] - nodes[b][1])
    return x*x + y*y



def jarakjalanan(a,b,edges,nodes):  
    # print(a)
    # print(a,b)
    # print("here")
    if a == b:
        return -1,""
    frontier = []
    visited = set([])
    now = a
    route = str(now)
    cost = 0
    while now != b and cost != -1:
        visited.add(now)
        mini = -1
        for neighbours in edges[now].keys():
            lanjut = False
            if neighbours == b:
                # print(a,neighbours,mini)
                # print("done")
                cost += edges[now][neighbours]
                route += "," + str(neighbours) 
                return cost,route
            # print(now, neighbours)
            if neighbours not in visited:
                if mini == -1:
                    mini = neighbours
                if (jaraklurus(mini,b,nodes) > jaraklurus(neighbours,b,nodes)):
                    # print("new",mini)
                    mini = neighbours 
        if mini != -1:          
            cost += edges[now][mini]
        else:
            return -1, ""
            # for neighbours in edges[now].keys():
            #     if neighbours not in visited:
            #         if jarakjalanan(neighbours,b,edges,nodes)[0] != -1:
            #             mini = neighbours
        now = mini
        route += "," + str(now)

    return cost, route

#milestone1
def matriksjaraklurus(arrnode, nodes, edges):
    print(" ",end=" ")
    for node in arrnode:
        print(str(node),end=" "*(8-len(str(node))))
    print()
    for node in arrnode:
        print(node,end =" ")
        for node2 in arrnode:
            print(int(jaraklurus(node,node2,nodes)),end=(" "*(8-len(str(int(jaraklurus(node,node2,nodes)))))))
        print()

def matriksjarakjalan(arrnode, nodes, edges):
    costs = {}
    route = {}
    print(" ",end=" ")
    for node in arrnode:
        costs[node] = {}
        route[node] = {}
        print(str(node),end=" "*(8-len(str(node))))
    print()
    for node in arrnode:
        print(node,end =" ")
        for node2 in arrnode:
            x,y = jarakjalanan(node,node2,edges,nodes)
            costs[node][node2] = x
            route[node][node2] = y
            print(int(x),end=(" "*(8-len(str(int(x))))))
        print()
    return costs,route
    



#milestone2
#matriksnya direpresentasikan dictionary
def reduceMatrix(matriksreduks):
    matriks = matriksreduks[0]
    cost = 0
    # for node in matriks.keys():
    #     ada = False
    #     mini = 9999999
    #     for node2 in matriks[node].keys():
    #         if matriks[node][node2] == 0:
    #             ada = True
    #         else:
    #             if matriks[node][node2] < mini and matriks[node][node2] != -1:
    #                 mini = matriks[node][node2]
    #     if not ada:
    #         cost += mini
    #         for node2 in matriks[node].keys() :
    #             if matriks[node][node2] != -1:
    #                 matriks[node][node2] -= mini
    
    # for node in matriks.keys():
    #     ada = False
    #     mini = 9999999
    #     for node2 in matriks[node].keys():
    #             if matriks[node2][node] == 0:
    #                 ada = True
    #             else:
    #                 if matriks[node2][node] < mini and matriks[node2][node] != -1:
    #                     mini = matriks[node2][node]
    #     if not ada:
    #         cost += mini
    #         for node2 in matriks[node].keys() :
    #             if matriks[node2][node] != -1:
    #                 matriks[node2][node] -= mini
            
    
    return matriks,matriksreduks[1], cost

def printMatriks(matriks):
    print(" "*4,end="")
    for node in matriks.keys():
        print(str(node),end=" "*(8-len(str(node))))
    print()
    for node in matriks.keys():
        print(node,end =" "*(4-len(str(node))))
        for node2 in matriks[node].keys():
            x = matriks[node][node2]
            print(int(x),end=(" "*(8-len(str(int(x))))))
        print()


def multiAgent(arrnode, kantor, kurir, matriksreduks,edges,nodecc):
    matriks = matriksreduks[0]
    rute = [[[kantor],[kantor],0] for i in range(kurir)]
    visited = set([])
    while len(visited) < len(matriks) - 1:
        # print(visited)
        for kurirs in rute:
            mini = -1
            pos = kurirs[0][len(kurirs[0])-1]
            for nodes in arrnode:
                if nodes not in visited:
                    if mini == -1 and matriks[pos][nodes] != -1:
                        mini = nodes
                    else:
                        if matriks[pos][nodes] < mini and matriks[pos][nodes] != -1:
                            mini = nodes
            if mini != -1:
                real = True
                for kurirs2 in rute: #multiAgent([8,9,5],0,3,x),nodes,edges
                    if kurirs2 != kurirs:
                        pos2 = kurirs2[0][len(kurirs2[0]) - 1]
                        if matriks[pos2][mini] < matriks[pos][mini] and matriks[pos2][mini] != -1:
                            # print(pos)
                            # print(pos2)
                            # print(mini)
                            # print("sss")
                            real = False
                if real:        
                    # print("hellor")
                    kurirs[0].append(mini)
                    # print(kurirs)
                    # kurirs[1].append([int(i) ])
                    for i in matriksreduks[1][pos][mini].split(',')[1:]:
                        kurirs[1].append(int(i))
                    # print(rute)
                    kurirs[2] += matriks[pos][mini]
                    visited.add(mini) 
    hasil = 0
    for rutes in rute:
        hasil += rutes[2]
    
    realrute = []
    for kurirs in rute:
        route = []
        # print(kurirs)
        pulang = jarakjalanan(kurirs[1][len(kurirs[1])-1],kantor,edges,nodecc)
        hasil += pulang[0]
        for routes in kurirs[1]:
            route.append(routes)
        for i in pulang[1].split(',')[1:]:
            route.append(int(i))
        realrute.append(route)
    # print(realrute)
    return realrute, hasil
        
#milestone 3
#([[5, 2, 0], [5, 7, 11, 37]], 1526.751068)
def scale(routes):
    # print(routes)
    maxx = -99999999
    maxy = -99999999
    minx = 999999999
    miny = 999999999
    for route in routes:
        for steps in route:
            x,y = nodes[steps]
            if x < minx :
                minx = x
            if x > maxx:
                maxx = x
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y
    scale = minx, maxx, miny, maxy
    # print(scale)
    return scale


def scaleit(xi,xa,x):
    return (x - xi) / (xa-xi) * 700

def visualize(arrnode, hasil, nodes, edges):
    cost = hasil[1]
    routes = hasil[0]
    colors = ['orange','brown','green','gray','cyan','teal']

    
    
    xi,xa,yi,ya = scale(routes)

    xscale = xa - xi
    yscale = ya - yi

    win = GraphWin("Graph",800,800) 

    # text = Text(Point(600,50),"Tes")
    # text.draw(win)

    kankur = Circle(Point(scaleit(xi,xa,nodes[routes[0][0]][0])+50,scaleit(yi,ya,nodes[routes[0][0]][1])+50),0.5)
    text = Text(Point(scaleit(xi,xa,nodes[routes[0][0]][0])+50,scaleit(yi,ya,nodes[routes[0][0]][1])+50),f"{routes[0][0]}")
    text.setFill('blue')
    text.draw(win)
    # kankur = Circle(Point(450,450),2)
    kankur.setFill("blue")
    kankur.draw(win)

    text = Text(Point(650,30),f"Kantor kurir")
    text.setFill("blue")
    text.draw(win)
    text = Text(Point(650,60),f"Pelanggan")
    text.setFill("red")
    text.draw(win)
    text = Text(Point(650,700),f"Jarak total : {cost}")
    text.draw(win)

    for j,route in enumerate(routes):
        text = Text(Point(300,60+30*((j+1)%6)),f"Kurir {j+1}, rute = {'-'.join([str(i) for i in route])}")
        text.setFill(colors[j%6])
        text.draw(win)
        for i in range(len(route)-1):
            pos1 = Point(scaleit(xi,xa,nodes[route[i]][0])+50,scaleit(yi,ya,nodes[route[i]][1])+50)
            pos2 = Point(scaleit(xi,xa,nodes[route[i+1]][0])+50,scaleit(yi,ya,nodes[route[i+1]][1])+50)
            # pos2 = Point(nodes[route[i+1]][0],nodes[route[i+1]][1])
            # print(pos1)
            # print(pos2)
            line = Line(pos1,pos2)
            line.setFill(colors[j % 6])
            # node = Circle(pos1,2)
            if (route[i+1] != route[0]):
                text = Text(pos2,f"{route[i+1]}")
                if (route[i+1] in arrnode): 
                    text.setFill('red')
                text.draw(win)
            node2 = Circle(pos2,0.5)
            if route[i+1] in arrnode:
                node2.setFill('red')
            line.draw(win)
            # node.draw(win)
            node2.draw(win)
    
    win.getMouse()
    win.close()


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) < 2:
        print("USAGE : py main.py [nodesfile] [edgesfile]")
    else:
        # print(argv)
        nodes,edges = load(argv[1],argv[2])
        # x = reduceMatrix(matriksjarakjalan([6,5,8,9],nodes,edges))
        # printMatriks(x[0])
        # print(jarakjalanan(9,8,edges,nodes))
        kantor = int(input("Masukkan node kantor : "))
        kurir = int(input("Masukkan jumlah kurir : "))
        nodeses = input("Masukkan list node, dipisahkan , : ")
        arrnode = [int(i) for i in nodeses.split(',')]
        arrsem = copy.deepcopy(arrnode)
        arrsem.append(kantor)
        x = reduceMatrix(matriksjarakjalan(arrsem,nodes,edges))
        visualize(arrnode,multiAgent(arrnode,kantor,kurir,x,edges,nodes),nodes,edges)

