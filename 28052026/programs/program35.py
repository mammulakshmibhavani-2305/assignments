def split(arr,a):
    if a<=0 or a>=len(arr):
        return arr
    part1=arr[:a]
    part2=arr[a:]
    result=part2+part1
    return result
arr=[1,2,3,4,5]
a=3
result=split(arr,a)
print("Original Array:",arr)
print("Array after splitting and adding:",result)
