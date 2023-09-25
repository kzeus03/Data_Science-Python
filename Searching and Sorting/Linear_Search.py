def search(list , n):
    pos = -1
    found = False
    for x in range(n):
        if(list[x]==n):
            pos = x+1
            found = True
            break
        else:
            pass
    if(found == False):
        print("Element not found")
    else:        
        print("Element ",n," found at position : ",pos)

list = [2,5,9,8,4]
search_ele = 9
search(list,search_ele)