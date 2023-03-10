class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dic = defaultdict(int)
        ans = []
        self.trav(root)
        
        for key,value in self.dic.items():
            while ans and self.dic[ans[-1]] < value:
                ans.pop()
            if not ans or self.dic[ans[-1]] == value:
                ans.append(key)
        return ans
    
    def trav(self,curr):
        if curr:
            self.trav(curr.left)
            self.dic[curr.val] += 1
            self.trav(curr.right)