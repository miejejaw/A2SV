class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        i = 0 
        size = len(source)
        while size>i:
            s = source[i].find('//')
            m = source[i].find('/*')
            
            if (s!=-1 and s<m) or (s!=-1 and m==-1):
                idx = source[i].find('//')
                source[i] = source[i][:idx]

            elif m != -1:
                idx = source[i].find('/*')
                last = source[i].find('*/',idx+2)
                
                if last != -1:
                    source[i] = source[i][:idx] + source[i][last+2:]
    
                    continue
                
                source[i] = source[i][:idx]
                temp = i
                i += 1   

                while size>i and source[i].find('*/') == -1:
                    source[i] = ""
                    i += 1
                    
                last = source[i].find('*/')
                source[temp] += source[i][last+2:]
                source[i] = ""
                i = temp-1
            else: i += 1
       
        ans = []
        for item in source:
            if item != '':
                ans.append(item)
        return ans
        
        
        
#48