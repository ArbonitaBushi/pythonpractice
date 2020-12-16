## Make a function that takes in a list of numbers and adds them together. 

arr = [10, 20, 30, 40, 5, 6, 7, 8, 9, 30, 50, 3]

def loop(arr):
    count = 0
    for i in arr:
        count += i
    return count

##print(loop(arr))

## Loop funcion but with index instead of value 

def new_loop(arr):
    count = 0
    for i in range(len(arr)):
        count += arr[i]
    return count

print(new_loop(arr))


    

