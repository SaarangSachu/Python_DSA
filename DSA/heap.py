import heapq

l=[23,31,4,54,234,5,3,1,1,43,34]
heapq.heapify(l)
print(l)
heapq.heappop(l)
heapq.heappop(l)
print(l)
heapq.heappush(l,2)
print(l)
pop=heapq.heapreplace(l,1)
print(pop)
print(l)
print(heapq.nsmallest(4,l))