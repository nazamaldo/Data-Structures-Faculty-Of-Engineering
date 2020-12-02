import random

"""  * QUICKSORT * """
def q_sort(list,l,r):
    if (l<r):
        #Partition with a randomized pivot
        pivot = random.randint(0,len(list)-1)
        list[pivot], list[r] = list[r], list[pivot] #swap
        middle = q_partition(list,l,r)
        q_sort(list,l,middle-1)
        q_sort(list,middle+1,r)

def q_partition(list,l,r):
    #Pivot will be the last item
    pivot = list[r]
    i = l-1
    #i --> last item less than pivot
    #k --> scanner
    for j in range(l,r):
        if list[j] <= pivot:
            i+=1
            list[i], list[j] = list[j], list[i]

    #Change de pivot to the middle
    list[i+1], list[r] = list[r], list[i+1]
    #And return the middle index
    return i+1


if __name__ == "__main__":
    principal_list = [1,3,5,2,1,3]
    q_sort(principal_list,0,len(principal_list)-1)
    print(principal_list)
    
    
