def sort_stack(stack):
    tmp_stack=[]

    while stack:
        temp=stack.pop()
        while tmp_stack and tmp_stack[-1]>temp:
            stack.append(tmp_stack.pop())
        tmp_stack.append(temp)
    return tmp_stack

stack=[34,3,31,98,92,23]
print("intput-->",stack)
print("output-->",sort_stack(stack))