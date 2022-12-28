class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for word in paths:
            path,*files = word.split()
            for file in files:
                i = file.index('(')
                file_name = file[i+1:]
                temp = path+"/"+file[:i]
                dic[file_name].append(temp) 
        ans = []
        for path in dic.values():
            if len(path) > 1:
                ans.append(path)
                
        return ans
        
        
# 55