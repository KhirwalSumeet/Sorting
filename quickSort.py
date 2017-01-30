import random
count = 0
#Extract training datasets from file
def get_dataset_from_file(filename):
    file = open(filename, 'r')
    dataset = []
    for line in file:
        dataset.append(int(line.strip().rstrip('\n')))
    return dataset

# My own partitioning
# def partition(alist,i,j):
#     # a=random.randint(i,j) # Random pivot
#     # a=i # First element as pivot
#     # a=j #Last element as pivot
#     # a=(i+j)//2 # Middle element as pivot
#     # temp=alist[a]
#     # alist[a]=alist[i]
#     # alist[i]=temp
#     x=i
#     y=j
#     i+=1
#     temp=0
#     while(i<j):
#         if(alist[i]>alist[x] and temp == 0):
#             temp=1
#         elif(temp != 1):
#             i+=1
#         if(temp):
#             if(alist[j]<alist[x]):
#                 temp=alist[j]
#                 alist[j]=alist[i]
#                 alist[i]=temp
#                 temp=0
#             j-=1
#     temp=alist[x]
#     alist[x]=alist[j-1]
#     alist[j-1]=temp
#     if(alist[j]<alist[j-1]):
#         temp=alist[j]
#         alist[j]=alist[j-1]
#         alist[j-1]=temp
#     return j

# Coursera Partitioning
coun =0;
def partitionRoutine(A,l,r):
    # # Last element as pivot
    # temp=A[l]
    # A[l]=A[r-1]
    # A[r-1]=temp
    global coun
    coun =coun +1
    # Midlle element as pivot
    global count
    x= (l+r-1)//2
    if(coun < 5):
        print(str(x)+":"+str(l)+":"+str(r))
    # print(str(x)+":"+str(l)+":"+str(r))
    temp=A[l]
    A[l]=A[x]
    A[x]=temp
    p=A[l]
    i=l+1
    j=l+1
    while(j<r):
        count= count +1
        if(A[j] <p):
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
            i = i+1
        j = j+1
    temp = A[l]
    A[l] = A[i-1]
    A[i-1] = temp
    return i

def quickSort(alist, i, j):
    if (i>=j):
        return
    pos = partitionRoutine(alist, i, j)
    quickSort(alist, i, pos-1)
    quickSort(alist, pos , j)

alist = get_dataset_from_file("quickSortData.txt")
quickSort(alist, 0,len(alist))
print(len(alist))
print(count)
#162085
#164123