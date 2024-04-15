def minRectanglesToCoverPoints( points, w):
        """
        :type points: List[List[int]]
        :type w: int
        :rtype: int
        """
        X=[]
        for e in points:
            X.append(e[0])
        X=sorted(X)

        if w==0: return len(set(X))
        
        counter=0
        while X:
            counter+=1
            xmin=X[0]
            while X:
                if X[0]<=xmin+w:
                    X.pop(0)
                else:
                    break
        return counter
            
        
        


def tests():
    assert minRectanglesToCoverPoints([[2,3],[1,2]], 0) ==2
    assert minRectanglesToCoverPoints([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]], 2) ==3
    assert minRectanglesToCoverPoints([[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]], 1) ==2
    assert minRectanglesToCoverPoints([[2,1],[1,0],[1,4],[1,8],[24,5],[25,6]], 1) ==2

#print(minRectanglesToCoverPoints([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]], 2))
print(minRectanglesToCoverPoints([[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]], 1))
tests()
