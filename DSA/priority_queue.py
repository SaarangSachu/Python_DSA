import heapq as hq
l=[(1,'anil'),(3,'saho'),(2,'apple'),(5,'lala')]
hq.heapify(l)
while l:
    item=hq.heappop(l)
    print(item[0],':',item[1])