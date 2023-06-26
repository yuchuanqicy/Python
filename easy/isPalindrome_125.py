class Solution:
    # 将给出的字符串 大写变成小写， 去除中间其他字符和空格，验证其是否是回文字符串
    # 方法一，遍历字符串，通过isalnum函数判断每个字符是否为数字和字母，然后将大写字母转换为小写字母，追加为新的字符串，通过切片反转字符串，比较两个字符串是否相等，即可
    def isPalindrome(self, s: str) -> bool:
        if s =="":
            return True
        newString=''.join(ch.lower() for  ch in s if ch.isalnum())
        if newString==newString[::-1]:
            return True
        else:
            return False
    # 方法二  双指针，在方法一上 不用反转字符串，直接左右同时移动
    def isPalindrome2(self, s: str) -> bool:
        if s =="":
            return True
        newString=''.join(ch.lower() for  ch in s if ch.isalnum())
        left,right=0,len(newString)-1
        while left<right:
            if  newString[left] !=newString[right]:
                return False
            if s[left]==s[right]:
                left=left+1
                right=right-1
            return True
    # 方法三 在原字符串上进行筛选，直接使用双指针，进行判断
    def isPalindrome3(self, s: str) -> bool:
        if s =="":
            return True
        left=0
        right=len(s)-1
        while left<right:
            while left<right and  not s[left].isalnum():
                left=left+1
            while left<right and not  s[right].isalnum():
                right=right-1
            if  left<right:
                if s[left].lower()!=s[right].lower():
                    return False
                if s[left]==s[right]:
                    left+=1
                    right-=1
            return True