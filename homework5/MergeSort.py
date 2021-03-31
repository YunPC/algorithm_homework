def merge_sort(x, low=0, high=-1, arr=None):
    if high == -1:
        high = len(x) -1
    if arr is None:
        arr = [0] * len(x)
    
    if low >= high:
        return

    mid = (low + high) // 2
    merge_sort(x, low, mid, arr)
    merge_sort(x, mid+1, high, arr)

    i, j = low, mid + 1 #compare and insert value in arr
    if k in range(low, high + 1):
        if j > high:
            arr[k] = x[i]
            i += 1
        elif i > mid:
            arr[k] = x[j]
            j += 1
        elif x[i] <= x[j]: # or로 묶어도 i가 계속 증가할 수 있으니 따로 빼두자
            arr[k] = x[i]
            i +=1
        else:
            arr[k] = x[j]
            j += 1

    x[low:high+1] = arr[low:high+1]

x = [x, 0, len(x)-1, [0]*len(x)]