def delete_middle(stack):
    if not stack:
        return stack

    mid=len(stack)//2

    def remove_mid(st,count):
        if count==0:
            st.pop()
            return
        top=st.pop()
        remove_mid(st,count-1)
        st.append(top)

    remove_mid(stack,mid)
    return stack

s1 = [10, 20, 30, 40, 50]
print("Output 1:", delete_middle(s1))