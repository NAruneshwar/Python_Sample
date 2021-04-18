class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dist = list()
        dist.append(sqrt((p1[1]-p2[1])**2+(p1[0]-p2[0])**2))
        dist.append(sqrt((p2[1]-p3[1])**2+(p2[0]-p3[0])**2))
        dist.append(sqrt((p3[1]-p4[1])**2+(p3[0]-p4[0])**2))
        dist.append(sqrt((p1[1]-p3[1])**2+(p1[0]-p3[0])**2))
        dist.append(sqrt((p2[1]-p4[1])**2+(p2[0]-p4[0])**2))
        dist.append(sqrt((p1[1]-p4[1])**2+(p1[0]-p4[0])**2))
        
        dist.sort()
        if 0 in dist:
            return False
        print(dist)
        if dist.pop() != dist.pop():
            return False
        if dist.pop() == dist.pop() == dist.pop() == dist.pop():
            return True
        else:
            return False