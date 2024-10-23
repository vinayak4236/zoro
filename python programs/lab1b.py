def p(num):
    num_str=str(num)
    return num_str==num_str[::-1]

def cd(num):
    dc=[0]*10
    while num>0:
        digits=num % 10
        dc[digits]+=1
        num//=10
    return dc
    
try:
    n=int(input("Enter a number:"))
    if n<0:
            print("Enter non negitive numbers")
    else:
        if p(n):
            print(f"{n} is a palindrome")
        else:
            print(f"{n} is not a palindrome")
        dc=cd(n)
        for digits, count in enumerate(dc):
            if count>0:
                print(f"Digits {digits} appears {count} times in the number")
except ValueError:
    print("Invalid input. please enter valid integer.")