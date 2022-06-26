#Problem Code:NUM239
# def prettyNum(l,r):
#     count = 0
#     for i in range(l,r+1):
#         if i%10 in (2,3,9):
#             count += 1
#     return count

# n = int(input())
# for i in range(n):
#     l, r = list(map(int, input().split()))
#     print(prettyNum(l,r))
# Problem Code: DOLL
# def AliAndGiHun(n, h):
#     count = 0
#     l = list(map(int, input().split()))
#     for i in l:
#         if i > h:
#             count += 1
#     return count

# n = int(input())
# for i in range(n):
#     c, h = list(map(int, input().split()))
#     print(AliAndGiHun(c,h))
#Problem Code: JOHNY
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     start = arr[0]
#     left = list(filter(lambda x: x < start, arr))
#     center = [i for i in arr if i == start]
#     right = list(filter(lambda x: x > start, arr))
#     return quick_sort(left) + center + quick_sort(right)

# def newPlace(q, arr, k):
#     value = arr[k-1]
#     sorted_arr = quick_sort(arr)
#     return sorted_arr.index(value) + 1

# n = int(input())
# for i in range(n):
#     q = int(input())
#     arr = list(map(int, input().split()))
#     k = int(input())
#     print(newPlace(q, arr, k))
#Problem Code: EID
# def lessDiff(q, arr):
#     arr = quick_sort(arr)
#     min_value = max(arr)
#     for i in range(len(arr)-1):
#         if min_value > arr[i+1] - arr[i]:
#             min_value =  arr[i+1] - arr[i]
#     return min_value

# t = int(input())
# for i in range(t):
#     n = int(input())
#     l = list(map(int, input().split()))
#     print(lessDiff(n, l))


def myset(orig, unique = None):
    if unique == None:
        unique = list()
    if len(orig) == 1:
        return unique
    elem = orig[0]
    for i in range(len(orig)-1):
        if elem == orig[i+1]:
            if orig[i+1] not in unique:
                unique.append(orig[i+1])
    orig.pop(0)
    return myset(orig, unique)

print(myset([1,2,1,3,3,4,5,6,9]))