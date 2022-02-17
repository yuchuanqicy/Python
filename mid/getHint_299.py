class Solution(object):
    def getHint(self, secret, guess):

        secret = list(secret)
        guess = list(guess)

        countBulls = 0
        removeList = []
        for (i, j) in zip(secret, guess):
            if i == j:
                countBulls += 1
                removeList.append(i)

        for i in removeList:
            secret.remove(i)
            guess.remove(i)

        countCows = 0
        for i in guess:
            if i in secret:
                countCows += 1
                secret.remove(i)

        return str(countBulls) + 'A' + str(countCows) + 'B'
s=Solution()
print(s.getHint('110002','1102'))