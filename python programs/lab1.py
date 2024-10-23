def test_score():
    while True:
        try:
            score=float(input("Enter the score:"))
            if 0<=score<=100:
                return score
            else:
                print("Please enter the valid score btw 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter valid input")
            
score=[]
for i in range(3):
    score.append(test_score())
score.sort(reverse=True)
average=sum(score[:2])/2
print(f"The average of best two test score is {average:.2f}")