def index_of_element(collection,key):
    for i in range(len(collection)):
        if collection[i]==key:
            print(i)

index_of_element([1,2,1,3,1,4],1)