def CountEvenNumbersInRange(array):
    count_array=[]
    CountOf_prefixEven=[1 if array[0]%2==0 else 0]
    
    for i in range(1,len(array)):
        if(array[i]%2==0):
            CountOf_prefixEven.append(CountOf_prefixEven[i-1]+1)
        else:
            CountOf_prefixEven.append(CountOf_prefixEven[i-1])
         
    for ranges in range_array:
        if   ranges[0]!=0:
            count_array.append(CountOf_prefixEven[ranges[1]] - CountOf_prefixEven[ranges[0] - 1]) 
        else:
            count_array.append(CountOf_prefixEven[ranges[1]])
    return count_array   
    
    
array=list(map(int,input("Enter the array of numbers: ").split()))
number_of_ranges=int(input("Enter the number of ranges: "))
range_array=[]
for i in range(number_of_ranges):
    range_input = list(map(int, input(f"Enter the start and end of range {i + 1}: ").split()))
    range_array.append(range_input)
    
print(CountEvenNumbersInRange(array))
