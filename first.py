def selection(array):
    for i in range(0, len(array) - 2, 1):
        min = i
        for j in range(i+1, len(array) - 1):
            if array[j] < array[min]:
                min = j
        temp = array[i]
        array[i] = array[min]
        array[min] = temp
    return array; 

def insert(array1):
    for j in range(2, len(array1)):
        key = array1[j]
        i = j - 1
        while i >= 0 and array1[i] > key:
            array1[i+1] = array1[i]
            i = i-1 
            array1[i+1] = key
    return array1;

array = [102, 192, 368, 558, 142, 771, 793, 51, 469, 222, 802, 389, 257, 722, 893]
selection(array)
print(array)
array1 = [440, 739, 110, 703, 242, 976, 758, 283, 820, 55, 586, 484, 35, 761, 433]
insert(array1)
print(array1)
