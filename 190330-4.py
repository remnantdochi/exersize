class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if rooms==[]: return
        xcord=len(rooms)
        ycord=len(rooms[0])
        indexstack=[(i,j) for i in range(len(rooms)) for j in range(len(rooms[0])) if rooms[i][j] == 0]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        gatenum=1
        while indexstack != []:
            newindex=[]
            for item in indexstack:
                for mapdir in direction:
                    xpoint=item[0]+mapdir[0]
                    ypoint=item[1]+mapdir[1]
                    if 0<=xpoint <len(rooms) and 0<=ypoint<len(rooms[0]):
                        if rooms[xpoint][ypoint]==pow(2,31)-1:
                            rooms[xpoint][ypoint]=gatenum
                            newindex.append((xpoint,ypoint))
            indexstack=newindex
            gatenum+=1
        ''''
        for item in index_0:
            for mapdir in direction:
                xpoint=item[0]+mapdir[0]
                ypoint=item[1]+mapdir[1]
                if xpoint <len(rooms) and ypoint<len(rooms[0]):
                    if rooms[xpoint][ypoint]==pow(2,31)-1:
                        rooms[xpoint][ypoint]=1
                        index_1.append((xpoint,ypoint))
        for item in index_1:
            for mapdir in direction:
                xpoint=item[0]+mapdir[0]
                ypoint=item[1]+mapdir[1]
                if xpoint <len(rooms) and ypoint<len(rooms[0]):
                    if rooms[xpoint][ypoint]==pow(2,31)-1:
                        rooms[xpoint][ypoint]=2
                        index_2.append((xpoint,ypoint))
        for item in index_2:
            for mapdir in direction:
                xpoint=item[0]+mapdir[0]
                ypoint=item[1]+mapdir[1]
                if xpoint <len(rooms) and ypoint<len(rooms[0]):
                    if rooms[xpoint][ypoint]==pow(2,31)-1:
                        rooms[xpoint][ypoint]=3
                        index_3.append((xpoint,ypoint))
        for item in index_3:
            for mapdir in direction:
                xpoint=item[0]+mapdir[0]
                ypoint=item[1]+mapdir[1]
                if xpoint <=len(rooms) and ypoint<=len(rooms[0]):
                    if rooms[xpoint][ypoint]==pow(2,31)-1:
                        rooms[xpoint][ypoint]=4
                        #index_3.append((xpoint,ypoint))'''
