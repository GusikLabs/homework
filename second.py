from datetime import datetime

try:
    f = open("ai183.txt", "r")
except IOError:
    print("Error!")
    exit()

test1, test2, test3 = False, False, False
array = []

while True:
    temp = f.read(1)
    if temp == "1":
        test1 = True
        temp = f.read(1)
        if temp == "3":
            test2 = True
            temp = f.read(1)
            if temp == ":":
               test3 = True
    if test1 == True and test2 == True and test3 == True:
        f.seek(f.tell() + 1)
        temp = f.read(1)
        while temp != "}":
            array.append(temp)
            temp = f.read(1)
        break

f.close()

arrayMerge = []
arrayQuick = []
arrayHeap = []

for i in range(len(array)):
    arrayMerge.append(array[i])
    arrayQuick.append(array[i])
    arrayHeap.append(array[i])

start_time = datetime.now()

def merge(arrayMerge):
    if len(arrayMerge) > 1:
        mid = len(arrayMerge) // 2
        left = arrayMerge[:mid]
        right = arrayMerge[mid:]

        mergeSort(left)
        mergeSort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arrayMerge[k] = left[i]
                i += 1
            else:
                arrayMerge[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arrayMerge[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arrayMerge[k] = right[j]
            j += 1
            k += 1

def quick(arrayQuick):
    less, equal, greater = [], [], []

    if len(arrayQuick) > 1:
        p = arrayQuick[0]
        for x in arrayQuick:
            if x < p:
                less.append(x)
            if x == p:
                equal.append(x)
            if x > p:
                greater.append(x)
        return quick(less) + equal + quick(greater)
    else:
        return arrayQuick

def heap(arrayHeap):
    def siftDown(parent, limit):
        item = arrayHeap[parent]
        while True:
            child = (parent << 1) + 1
            if child >= limit:
                break
            if child + 1 < limit and arrayHeap[child] < arrayHeap[child + 1]:
                child += 1
            if item < arrayHeap[child]:
                arrayHeap[parent] = arrayHeap[child]
                parent = child
            else:
                break
        arrayHeap[parent] = item

    length = len(arrayHeap)
    for index in range((length >> 1) - 1, -1, -1):
        siftDown(index, length)
    for index in range(length - 1, 0, -1):
        arrayHeap[0], arrayHeap[index] = arrayHeap[index], arrayHeap[0]
        siftDown(0, index)


start_time = datetime.now()
merge(arrayMerge)
end_time = datetime.now()
print("Merge sort:\n", arrayMerge)
print('Duration: {}'.format(end_time - start_time))

start_time = datetime.now()
quick(arrayQuick)
end_time = datetime.now()
print("\nQuick sort:\n", arrayQuick)
print('Duration: {}'.format(end_time - start_time))

start_time = datetime.now()
heap(arrayHeap)
end_time = datetime.now()
print("\nHeap sort:\n", arrayHeap)
print('Duration: {}'.format(end_time - start_time))
