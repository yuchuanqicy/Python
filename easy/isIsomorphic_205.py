class Solution:
    def isIsomorphic_1(self, s: str, t: str) -> bool:
        """
        判断两个字符串是否为同构字符串，即判断两个字符串的每位字符映射关系是唯一的，即双射；
        使用index函数遍历字符第一次出现的下标，然后判断S与t的每个字符的下标是否相等。确定时间复杂度高为O(n^2)
        :param s:S字符串
        :param t:t字符串
        :return:bool类型
        """
        return all(s.index(s[i])==t.index(t[i]) for i in range(len(s)))

    def isIsomorphic_2(self, s: str, t: str) ->bool:
        """
        使用hash表做法，map1的key对应唯一t中的字符串，map2同样
        :param s:
        :param t:
        :return:
        """
        mp1={}
        mp2={}
        for a,b in zip(s,t):
            if a in mp1 and mp1[a]!=b:
                return False
            if b in mp2 and mp2[b]!=a:
                return False
            mp1[a]=b
            mp2[b]=a
        return True