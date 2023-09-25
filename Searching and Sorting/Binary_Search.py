def search(list,n):
    start = 0
    end = len(list)    

    while(start <= end):
        mid=(start + end)//2
        if(list[mid] == n):
            return True
        else:
            if(list[mid] < n):
                start = mid
            else:
                end = mid

list=[4,7,88,10,15,45]
n = 15
if search(list,n):
    print("Element found")
else:
    print("Element not found")