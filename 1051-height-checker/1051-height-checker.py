class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        b=heights.copy()
        for i in range(len(b)):
            for j in range(i,len(b)):
                if b[i] > b[j]:
                    b[i] , b[j]= b[j] , b[i] 
        count=0
        for k in range(len(heights)):
            if b[k] != heights[k]:
                count+=1

        return(count)