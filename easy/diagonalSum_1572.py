class Solution:
    def diagonalSum_1(self, mat) -> int:
        sum=0
        l=len(mat)
        mid=l//2
        for i in  range(l):
            sum+=mat[i][i]+mat[i][l-i-1]

        return sum-mat[mid][mid]*(l&1)



