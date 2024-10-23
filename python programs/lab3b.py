if __name__=='__main__':
    x=input("Enter first String: ")
    y=input("Enter second String: ")

    x=x.strip()
    y=y.strip()
    sim=0
    if len(x)>len(y):
        xx=x
        yy=y
    else:
        xx=x
        yy=x
    j=0
    for i in yy:
        if i==xx[j]:
            sim+=1
        else:
            pass
        j+=1
        similarity=(sim/len(xx))*100
        print(f"The similarity between the two given strings is {similarity:.2f}%")