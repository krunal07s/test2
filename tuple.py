t = tuple()

n = int(input("enter limit:"))
for i in range(n):
    i = int(input())
    t = t + (i,)
    
print(t)
print("Maximum number in tuple t: ",max(t))
print("Minimum number in tuple t: ",min(t))

print("Repeted num in tuple t:")
for i in range(n):
    for j in range(i+1,n):
        if(t[i]==t[j]):
            print(t[i])
            
arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def number_2_word(n):
    if (n == 0):
        return ""
    else:
        small_ans = arr[n % 10]
        ans = number_2_word(int(n / 10)) + small_ans + " "
    return ans

print("Enter number:")
num = int(input())
print("Number Entered was : ", num)
print("Converted to word it becomes: ", end="")
print(number_2_word(num))


