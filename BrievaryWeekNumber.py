# What week are we in darn it???

date = input("\nEnter a date (MM/DD/YYYY): ")
print()
month, day, year = map(int, date.split('/'))

def countDays(month, day, year):
    day_of_year = 0

    # LEAP YEAR
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        for m in range(1, month):
            if m in [1, 3, 5, 7, 8, 10, 12]:
                day_of_year += 31
            elif m in [4, 6, 9, 11]:
                day_of_year += 30
            elif m == 2:
                day_of_year += 29

    # NORMAL YEAR
    else:
        for m in range(1, month):
            if m in [1, 3, 5, 7, 8, 10, 12]:
                day_of_year += 31
            elif m in [4, 6, 9, 11]:
                day_of_year += 30
            elif m == 2:
                day_of_year += 28

    day_of_year += day
    return day_of_year

dayNumber = countDays(month, day, year)


# update before 2028
'''DAY ASSIGNMENTS'''
seasons2025 = {
    'Advent/Christmas': (1, 12),
    'Ordinary Time I': (13, 63),
    'Lent/Triduum/Easter': (64, 159),
    'Ordinary Time II': (159, 213),
    'Ordinary Time III': (214, 332),
    'Advent/Christmas II': (333, 365)
}
seasons2026 = {
    'Advent/Christmas I': (1, 11),
    'Ordinary Time I': (12, 48),
    'Lent/Triduum/Easter': (49, 144),
    'Ordinary Time II': (145, 213),
    'Ordinary Time III': (214, 332),
    'Advent/Christmas II': (333, 365)
}
seasons2027 = {
    'Advent/Christmas I': (1, 10),
    'Ordinary Time I': (11, 40),
    'Lent/Triduum/Easter': (41, 136),
    'Ordinary Time II': (137, 212),
    'Ordinary Time III': (213, 331),
    'Advent/Christmas II': (332, 365)
}


# 2025
if year == 2025:
    if dayNumber in range(seasons2025['Advent/Christmas'][0], seasons2025['Advent/Christmas'][1] + 1):
        week = (dayNumber - seasons2025['Advent/Christmas'][0]) // 7 + 1
        print(f"Week {week} of Advent/Christmas")
    elif dayNumber in range(seasons2025['Ordinary Time I'][0], seasons2025['Ordinary Time I'][1] + 1):
        week = (dayNumber - seasons2025['Ordinary Time I'][0]) // 7 + 1
        brievaryWeek = ((week - 1) % 4) + 1
        print(f"Week {week} of Ordinary Time I")
        print(f"Brievary week {brievaryWeek}")
    elif dayNumber in range(seasons2025['Lent/Triduum/Easter'][0], seasons2025['Lent/Triduum/Easter'][1] + 1):
        week = (dayNumber - seasons2025['Lent/Triduum/Easter'][0]) // 7 + 1
        print(f"Week {week} of Lent/Triduum/Easter")
    elif dayNumber in range(seasons2025['Ordinary Time II'][0], seasons2025['Ordinary Time II'][1] + 1):
        week = (dayNumber - seasons2025['Ordinary Time II'][0]) // 7 + 1
        brievaryWeek = ((week - 1) % 4) + 1
        print(f"Week {week} of Ordinary Time II")
        print(f"Brievary week {brievaryWeek}")
    elif dayNumber in range(seasons2025['Ordinary Time III'][0], seasons2025['Ordinary Time III'][1] + 1):
        week = (dayNumber - seasons2025['Ordinary Time III'][0]) // 7 + 1
        brievaryWeek = ((week - 1) % 4) + 1
        print(f"Week {week} of Ordinary Time III")
        print(f"Brievary week {brievaryWeek}")
    elif dayNumber in range(seasons2025['Advent/Christmas II'][0], seasons2025['Advent/Christmas II'][1] + 1):
        week = (dayNumber - seasons2025['Advent/Christmas II'][0]) // 7 + 1
        print(f"Week {week} of Advent/Christmas II")
    else:
        print("Invalid input")

# 2026
if year == 2026:
    if dayNumber in range(seasons2026['Advent/Christmas I'][0], seasons2026['Advent/Christmas I'][1] + 1):
        week = (dayNumber - seasons2026['Advent/Christmas I'][0]) // 7 + 1
        print(f"Week {week} of Advent/Christmas I")
    elif dayNumber in range(seasons2026['Ordinary Time I'][0], seasons2026['Ordinary Time I'][1] + 1):
        week = (dayNumber - seasons2026['Ordinary Time I'][0]) // 7 + 1
        brievaryWeek = ((week - 1) % 4) + 1
        print(f"Week {week} of Ordinary Time I")
        print(f"Brievary week {brievaryWeek}")
    elif dayNumber in range(seasons2026['Lent/Triduum/Easter'][0], seasons2026['Lent/Triduum/Easter'][1] + 1):
        week = (dayNumber - seasons2026['Lent/Triduum/Easter'][0]) // 7 + 1
        print(f"Week {week} of Lent/Triduum/Easter")
    elif dayNumber in range(seasons2026['Ordinary Time II'][0], seasons2026['Ordinary Time II'][1] + 1):
        week = (dayNumber - seasons2026['Ordinary Time II'][0]) // 7 + 1
        brievaryWeek = ((week - 1) % 4) + 1
        print(f"Week {week} of Ordinary Time II")
        print(f"Brievary week {brievaryWeek}")
    elif dayNumber in range(seasons2026['Ordinary Time III'][0], seasons2026['Ordinary Time III'][1] + 1):
        week = (dayNumber - seasons2026['Ordinary Time III'][0]) // 7 + 1
        brievaryWeek = ((week - 1) % 4) + 1
        print(f"Week {week} of Ordinary Time III")
        print(f"Brievary week {brievaryWeek}")
    elif dayNumber in range(seasons2026['Advent/Christmas II'][0], seasons2026['Advent/Christmas II'][1] + 1):
        week = (dayNumber - seasons2026['Advent/Christmas II'][0]) // 7 + 1
        print(f"Week {week} of Advent/Christmas II")
    else:
        print("Invalid input")

# 2027
if year == 2027:
    if dayNumber in range(seasons2027['Advent/Christmas I'][0], seasons2027['Advent/Christmas I'][1] + 1):
        week = (dayNumber - seasons2027['Advent/Christmas I'][0]) // 7 + 1
        print(f"Week {week} of Advent/Christmas I")
    elif dayNumber in range(seasons2027['Ordinary Time I'][0], seasons2027['Ordinary Time I'][1] + 1):
        week = (dayNumber - seasons2027['Ordinary Time I'][0]) // 7 + 1
        brievaryWeek = ((week - 1) % 4) + 1
        print(f"Week {week} of Ordinary Time I")
        print(f"Brievary week {brievaryWeek}")
    elif dayNumber in range(seasons2027['Lent/Triduum/Easter'][0], seasons2027['Lent/Triduum/Easter'][1] + 1):
        week = (dayNumber - seasons2027['Lent/Triduum/Easter'][0]) // 7 + 1
        print(f"Week {week} of Lent/Triduum/Easter")
    elif dayNumber in range(seasons2027['Ordinary Time II'][0], seasons2027['Ordinary Time II'][1] + 1):
        week = (dayNumber - seasons2027['Ordinary Time II'][0]) // 7 + 1
        brievaryWeek = ((week - 1) % 4) + 1
        print(f"Week {week} of Ordinary Time II")
        print(f"Brievary week {brievaryWeek}")
    elif dayNumber in range(seasons2027['Ordinary Time III'][0], seasons2027['Ordinary Time III'][1] + 1):
        week = (dayNumber - seasons2027['Ordinary Time III'][0]) // 7 + 1
        brievaryWeek = ((week - 1) % 4) + 1
        print(f"Week {week} of Ordinary Time III")
        print(f"Brievary week {brievaryWeek}")
    elif dayNumber in range(seasons2027['Advent/Christmas II'][0], seasons2027['Advent/Christmas II'][1] + 1):
        week = (dayNumber - seasons2027['Advent/Christmas II'][0]) // 7 + 1
        print(f"Week {week} of Advent/Christmas II")
    else:
        print("Invalid input")

print()