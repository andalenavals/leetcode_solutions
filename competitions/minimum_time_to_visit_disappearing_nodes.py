def minimumTime(self, n, edges, disappear):
        """
        :type n: int
        :type edges: List[List[int]]
        :type disappear: List[int]
        :rtype: List[int]
        """

        times=[]
        for n,dl in enumerate(disappear):
            if n ==0: times.append(0)
            distances=[ ]
            


def tests():
    assert minimumTime(3,[[0,1,2],[1,2,1],[0,2,4]] ,[1,3,5])==[0,2,3]


print(minimumTime(3,[[0,1,2],[1,2,1],[0,2,4]] ,[1,3,5]))
tests()
