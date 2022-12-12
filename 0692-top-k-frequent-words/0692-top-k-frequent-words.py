from queue import PriorityQueue
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        q,ans = PriorityQueue(),[]
        temp = [(freq,st) for st,freq in Counter(words).items()]
        temp.sort( key=lambda i: (-i[0],i[1]))
        for freq,st in temp:
            temp = (freq,st)           
            if q.qsize()>k-1: 
                pop = q.get()
                if pop[0]>temp[0] or (pop[0]==temp[0] and temp[1]>pop[1]):
                    temp = pop              
            q.put(temp)

        while not q.empty():
            ans.append(q.get())
        ans.sort( key=lambda i: i[0],reverse=True)   
        return [st for fre,st in ans]

        