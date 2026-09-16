import random

def generatePassword():
    lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '123456789012345678901234567890'
    specials = '@#$%&*()?!^:"~-'
    
    password = ''
    chars = ''

    print('Welcome to password generator')
    a = input('Enter number of characters: ')
    if a == '0':
        print('bruh')
        quit()
    elif a[0] not in '1234567890':
        print('Invalid input. enter in digits')
        quit()


    b = input('Include lowercase letters? [Y] or [N]: ')
    c = input('Include uppercase letters? [Y] or [N]: ')
    d = input('Include numbers? [Y] or [N]: ')
    e = input('Include special characters? [Y] or [N]: ')


    if b.upper() == 'Y':
        chars += lower
    if c.upper() == 'Y':
        chars += upper
    if d.upper() == 'Y':
        chars += digits
    if e.upper() == 'Y':
        chars += specials
    
    if b.upper() != 'Y' and c.upper() != 'Y' and d.upper() != 'Y' and e.upper() != 'Y':
        print('You selected No for all 4 options, that leaves you with no password idiot.')
        quit()

    
    chars = list(chars)

    while len(password) < int(a):
        z = len(chars)
        x = random.randint(0, z-1)
        password += chars[x]
    
    print(password)
    return


generatePassword()

