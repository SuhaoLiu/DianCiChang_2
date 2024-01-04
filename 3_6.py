import numpy as np

#坐标
coordinate = np.zeros([10, 7])

#节点坐标
points = {
    'p1': (3, 0), 'p2': (6, 0), 'p3': (3, 3), 'p4': (6, 3), 
    'p5': (3, 6), 'p6': (6, 6), 'p7': (0, 0), 'p8': (0, 3), 
    'p9': (0, 6), 'p10': (9, 0), 'p11': (9, 3), 'p12': (9, 6)
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