class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        判断两个字符串是否为同构字符串，即判断两个字符串的每位字符映射关系是唯一的，即双射
        :param s:S字符串
        :param t:t字符串
        :return:bool类型
        """
        return all(s.index(s[i])==t.index(t[i]) for i in range(len(s)))
