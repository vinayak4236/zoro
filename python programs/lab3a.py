x=input("Enter a sentence: ")
y=x
print("there are",len(x.split()),"word in the sentence: ")
digits,upper,lower=0,0,0
for i in x:
    if i.isdigit():
        digits+=1
    elif i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print ("There are {0} digits,\n {1} upper case characters and \n{2} lower case characters in the sentence".format(digits,upper,lower))