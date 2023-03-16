import time
class Solution:
    def dayOfYear1(self, date: str) -> int:
         return time.strptime(date, "%Y-%m-%d")[-2]
    def dayOfYear2(self,date:str):
        days=[31,28,31,30,31,30,31,31,30,31,30,31]
        string=date.split("-")
        year=int(string[0])
        print(year)

