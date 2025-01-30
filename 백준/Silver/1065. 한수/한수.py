def hansu(num):
    arr = list(map(int,str(num)))
    d = arr[1] - arr[0]
    for i in range(len(arr)-1,0,-1):
        tmp = arr[i] - arr[i-1]
        if tmp != d :
            return False
    return True

def main():
    n = int(input())
    count = 0

    for num in range(1,n+1):
        if num < 100 :
            count += 1
        else :
            result = hansu(num)
            if result == True:
                count += 1
    print(count)

main()