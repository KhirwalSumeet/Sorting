count = 0
#Extract training datasets from file
def get_dataset_from_file(filename):
    file = open(filename, 'r')
    dataset = []
    for line in file:
        dataset.append(line.strip().rstrip('\n'))
    return dataset

def mergeSort(alist):
    global count
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        i=0
        j=0
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        k=0

        # merging lefthalf and righthalf lists

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                count = count + 1
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            count = count +1
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


alist = get_dataset_from_file("integers.txt")
mergeSort(alist)
print(count)
