import numpy as np
from matplotlib import pyplot as plt


#参量
x = 3 #x方向网格数
y = 2 #y方向网格数
delta_x = 3 #x方向网格间距
delta_y = 3 #y方向网格间距

#坐标
coordinate = np.zeros([x+1, y+1]) #初始化坐标矩阵, x+1行y+1列

#节点矩阵坐标
points = {
    'p1': (1, 0), 'p2': (2, 0), 'p3': (1, 1), 'p4': (2, 1), 
    'p5': (1, 2), 'p6': (2, 2), 'p7': (0, 0), 'p8': (0, 1), 
    'p9': (0, 2), 'p10': (3, 0), 'p11': (3, 1), 'p12': (3, 2)
}

#三角形单元&顶点编号
triangles = {
    't1': [1, 3, 7], 't2': [3, 8, 7], 't3': [3, 9, 8], 't4': [3, 5, 9], 
    't5': [3, 6, 5], 't6': [3, 4, 6], 't7': [1, 4, 3], 't8': [1, 2, 4], 
    't9': [2, 10, 4], 't10': [4, 10, 11], 't11': [4, 11, 12], 't12': [4, 12, 6]
}

#边界值
coordinate[points['p7']] = coordinate[points['p8']] = coordinate[points['p9']]  = 0
coordinate[points['p10']] = coordinate[points['p11']] = coordinate[points['p12']] = 100

#单元分析
def analysis(triangles, points):
    global x, y, delta_x, delta_y
    K = np.zeros([(x+1) * (y+1), (x+1) * (y+1)]) #初始化刚度矩阵
    for triangle in triangles:
        #顶点坐标
        p1 = points['p' + str(triangles[triangle][0])]
        p2 = points['p' + str(triangles[triangle][1])]
        p3 = points['p' + str(triangles[triangle][2])]

        #bi = yj - ym（逆时针）, ci = xm - xj（顺时针）
        b1 = delta_y * (p2[1] - p3[1])
        b2 = delta_y * (p3[1] - p1[1])
        b3 = delta_y * (p1[1] - p2[1])

        c1 = delta_x * (p3[0] - p2[0])
        c2 = delta_x * (p1[0] - p3[0])
        c3 = delta_x * (p2[0] - p1[0])

        #fourDelta = 2 * (b1c2 - b2c1)
        fourDelta = 2 * (b1 * c2 - b2 * c1)

        #Kij = (bibj + cicj) / fourDelta
        K11 = (b1 * b1 + c1 * c1) / fourDelta
        K12 = (b1 * b2 + c1 * c2) / fourDelta
        K13 = (b1 * b3 + c1 * c3) / fourDelta
        K22 = (b2 * b2 + c2 * c2) / fourDelta
        K23 = (b2 * b3 + c2 * c3) / fourDelta
        K33 = (b3 * b3 + c3 * c3) / fourDelta

        #K = K + Kij
        K[triangles[triangle][0]-1, triangles[triangle][0]-1] += K11
        K[triangles[triangle][0]-1, triangles[triangle][1]-1] += K12
        K[triangles[triangle][0]-1, triangles[triangle][2]-1] += K13
        K[triangles[triangle][1]-1, triangles[triangle][1]-1] += K22
        K[triangles[triangle][1]-1, triangles[triangle][2]-1] += K23
        K[triangles[triangle][2]-1, triangles[triangle][2]-1] += K33
    
    K = K.T + K - np.diag(np.diag(K)) #对称化
    return K

#刚度矩阵
K = analysis(triangles, points)
K11 = K[0:6, 0:6]
K12 = K[0:6, 6:12]

#计算位向量
A = np.zeros((x+1) * (y+1)) #初始化位向量
for i in range(1, (x+1) * (y+1) + 1):
    A[i-1] = coordinate[points['p' + str(i)]]

A_unknown = np.dot(np.linalg.inv(K11), -1 * np.dot(K12, A[6:12]))

A = np.concatenate((A_unknown, A[6:12]), axis=0)

#回填坐标
for i in range(1, (x+1) * (y+1) + 1):
    coordinate[points['p' + str(i)]] = A[i-1]

#输出&作图
print(coordinate)
plt.imshow(coordinate)
plt.colorbar()
#TODO: 规范作图
plt.savefig('/home/lsh/workspace/DianCiChang_2/test.png')