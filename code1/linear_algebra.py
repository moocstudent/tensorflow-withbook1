import tensorflow as tf

# 创建两个矩阵
matrix1 = tf.constant([['1', 2], [3, 4],[5,6]])  # 3x2矩阵
print('matrix1',matrix1)
matrix2 = tf.constant([[7], [8]])  # 2x1矩阵
print('matrix2',matrix2)

# 矩阵相乘
result = tf.matmul(matrix1, matrix2)

print('result',result)
# 打印结果
print("矩阵相乘的结果:")
print(result.numpy())

# todo tensorflowjs showcase