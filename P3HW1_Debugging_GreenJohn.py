# I was supposed to put a comment here
# My Last Name

# system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    # TO DO: define the rest of the scores

    
score = int(input('Enter grade: '))

if score >= 90:
    print('Your grade is: A')
else:
    if (score >= 80) and (score <= 89):
        print('Your grade is: B')
    else:
        if (score >= 70) and (score <= 79):
            print('Your grade is: C')
        else: 
            if (score >= 60) and (score <= 69):
                print('Your grade is: D')
            else:
                print('Your grade is: F') # TO DO: finish this







# program start
main()
