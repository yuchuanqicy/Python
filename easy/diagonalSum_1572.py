class Solution:
    # 方法一，求出主对角线和副对角线和，在减去重叠部分的值，n阶矩阵，当n是奇数时，存在重叠，是偶数时，不存在重叠，使用(n-1)&1 判断是否是奇数，n-1是因为数组下标从0开始
    def diagonalSum_1(self, mat) -> int:
        sum=0
        l=len(mat)
        mid=l//2
        for i in  range(l):
            sum+=mat[i][i]+mat[i][l-i-1]

        return sum-mat[mid][mid]*(l&1)



