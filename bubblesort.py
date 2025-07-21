def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-1):
            if(l[i]<l[j]):
                l[i],l[j]=l[j],l[i]
    return l

l=[1,5,2,8,3,89,34]
print(bubble_sort(l))
