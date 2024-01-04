import numpy as np

#参量
x = 3 #x方向网格数
y = 2 #y方向网格数
delta_x = 3 #x方向网格间距
delta_y = 3 #y方向网格间距

#坐标
coordinate = np.zeros([x+1, y+1]) #初始化坐标矩阵, x+1行y+1列
for i in range(x+1):
    for j in range(y+1):
        coordinate[i][j] = i*delta_x + j*delta_y

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

print(coordinate)