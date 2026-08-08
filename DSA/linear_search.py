def linear_search(coll,key):
    for i in range(len(coll)):
        if key==coll[i]:
            return i
    return -1

print(linear_search([1,2,3,4],3))
print(linear_search([1,2,3,4],7))