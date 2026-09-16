# NOTE calculator

def AlphaCalculator():
    a = input("-->")

    # shatttt this may be difficult

    a.strip()

    # cooked

    # good thing someone else invented the calculator 

def LiturgyOfTheHoursWeekFinder():
    a = input('What week in Ordinary Time is it? ')
    a = int(a)
    week = (a % 4)
    if (a % 4) == 0:
        week = 4
    print()
    print(f'It is Week {week} for Liturgy of the Hours')

def BetaCalculator():
    print('-----------------------------------------------')
    b = input('1st number: ')
    c = input('Operation (+, -, x, /, ^): ')
    d = input('2nd number: ')

    b = float(b)
    d = float(d)
    
    print()

    if c == '+':
        print(str(b) +' '+ str(c) +' '+ str(d) +' = '+ str(b+d))
    elif c == '-':
        print(str(b) +' '+ str(c) +' '+ str(d) +' = '+ str(b-d))
    elif c == 'x':
        print(str(b) +' '+ str(c) +' '+ str(d) +' = '+ str(b*d))
    elif c == '/':
        print(str(b) +' '+ str(c) +' '+ str(d) +' = '+ str(b/d))
    elif c == '^':
        print(str(b) +' '+ str(c) +' '+ str(d) +' = '+ str(b**d))

    else:
        print('Invalid Input')

    print() 

    BetaCalculator()
    

#################################################

# AlphaCalculator()

# BetaCalculator()  

# LiturgyOfTheHoursWeekFinder()

#################################################





