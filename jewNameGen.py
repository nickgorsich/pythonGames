'''
    Jewish Name Generator
'''

import random

male_names = [
    "Aaron", "Abba", "Abraham", "Adam", "Aharon", "Akiva", "Alter", "Amos",
    "Ari", "Aryeh", "Asher", "Avi", "Avigdor", "Aviv", "Avner", "Avraham",
    "Azriel", "Baruch", "Benjamin", "Berel", "Betzalel", "Binyamin", "Boaz",
    "Chaim", "Dan", "Daniel", "David", "Dov", "Efraim", "Eitan", "Elazar",
    "Eli", "Eliezer", "Elijah", "Elimelech", "Elisha", "Ephraim", "Ezekiel",
    "Ezra", "Feivel", "Gabriel", "Gad", "Gavriel", "Gedaliah", "Gershon",
    "Gideon", "Hershel", "Hillel", "Isaac", "Isaiah", "Israel", "Issachar",
    "Itzhak", "Jacob", "Jeremiah", "Joel", "Jonah", "Jonathan", "Joseph",
    "Joshua", "Judah", "Kalman", "Lazar", "Leib", "Levi", "Malachi", "Meir",
    "Menachem", "Mendel", "Micah", "Mordechai", "Moshe", "Nachman", "Nachum",
    "Naftali", "Nathan", "Nathaniel", "Nehemiah", "Noah", "Ovadia", "Pinchas",
    "Rafael", "Reuven", "Ruben", "Samuel", "Saul", "Shalom", "Shaul", "Shimon",
    "Shlomo", "Shmuel", "Shraga", "Simcha", "Solomon", "Tobias", "Tuvia",
    "Tzvi", "Uri", "Uriel", "Velvel", "Yaakov", "Yair", "Yechiel", "Yehuda",
    "Yisroel", "Yitzchak", "Yoel", "Yonatan", "Yosef", "Zalman", "Zev",
]

female_names = [
    "Adina", "Aliza", "Ariella", "Aviva", "Ayelet", "Batsheva", "Batya",
    "Beila", "Bluma", "Bracha", "Chana", "Chava", "Chaya", "Dalia", "Devorah",
    "Dina", "Edna", "Eliana", "Eliora", "Elisheva", "Esther", "Faige",
    "Frayda", "Gittel", "Golda", "Hadassah", "Hannah", "Hinda", "Ilana",
    "Kayla", "Leah", "Liba", "Malka", "Michal", "Miriam", "Naomi", "Nechama",
    "Noa", "Orly", "Penina", "Perel", "Rachel", "Raizel", "Rebekah", "Rivka",
    "Rochel", "Ruth", "Sarah", "Shayna", "Shifra", "Shira", "Shoshana",
    "Sima", "Tamar", "Tova", "Tzipporah", "Yael", "Yaffa", "Yehudit",
    "Yocheved", "Zahava", "Zisel",
]

last_name_bit1 = [
    "Adel", "Apfel", "Berg", "Bern", "Birn", "Blum", "Braun", "Breit",
    "Buch", "Edel", "Eisen", "Fein", "Feld", "Finkel", "Fisch", "Frei",
    "Fried", "Glass", "Gold", "Gott", "Green", "Gross", "Hammer", "Herz",
    "Hirsch", "Holz", "Honig", "Kauf", "Kirsch", "Klein", "Kupfer", "Land",
    "Lang", "Licht", "Lieber", "Loew", "Mandel", "Morgen", "Nadel", "Nuss",
    "Perl", "Rapp", "Reich", "Rein", "Rosen", "Roth", "Rubin", "Sand",
    "Schiff", "Schoen", "Schul", "Schwartz", "Seiden", "Silber", "Spiel",
    "Stein", "Stern", "Suss", "Tannen", "Tauber", "Teitel", "Traub", "Wachs",
    "Wald", "Wasser", "Weber", "Wein", "Weiss", "Wolf", "Zucker",
]

last_name_bit2 = [
    "bach", "baum", "berg", "blatt", "bloom", "farb", "feld", "garten",
    "gold", "hart", "heim", "hertz", "hof", "holz", "horn", "kind", "korn",
    "man", "mann", "reich", "sohn", "son", "sky", "ski", "stadt", "stein",
    "stock", "thal", "wald", "witz", "zweig",
]

last_name_solo = [
    "Abrams", "Abulafia", "Adler", "Amsalem", "Ashkenazi", "Azoulay",
    "Barak", "Baron", "Ben-David", "Ben-Ami", "Benveniste", "Berkowitz",
    "Bernstein", "Blumenthal", "Brodsky", "Cardozo", "Caro", "Chazan",
    "Cohen", "Cordovero", "Dayan", "Diamant", "Dreyfus", "Eisenberg",
    "Elbaz", "Epstein", "Eshkol", "Farkas", "Feldman", "Friedman", "Gantz",
    "Ginsburg", "Glaser", "Goldberg", "Goldman", "Gutman", "Halevi",
    "Halpern", "Hershkowitz", "Horowitz", "Jaffe", "Kagan", "Kahn", "Kaplan",
    "Katz", "Kaufman", "Kimchi", "Klein", "Kohn", "Landau", "Lebowitz",
    "Levi", "Levin", "Levine", "Levy", "Lieberman", "Luria", "Maimon",
    "Margolis", "Mizrahi", "Moskowitz", "Nachmani", "Nathanson", "Ohana",
    "Pereira", "Peretz", "Rabin", "Rabinowitz", "Rothschild", "Rubin",
    "Sarfati", "Sassoon", "Schneider", "Schwartz", "Segal", "Shapiro",
    "Shalom", "Shulman", "Sofer", "Spektor", "Toledano", "Wasserman",
    "Weiss", "Wiesel", "Yaari", "Zilberman", "Zohar",
]


def get_last_name():
    x = random.randint(0, 2)  # 0 = solo last name, 1 or 2 = bit1 + bit2
    if x == 0:
        return random.choice(last_name_solo)
    return random.choice(last_name_bit1) + random.choice(last_name_bit2)


def generate_name(gender):
    if gender.lower() in {'b', 'boy', 'male'}:
        first = random.choice(male_names)
    elif gender.lower() in {'g', 'girl', 'female'}:
        first = random.choice(female_names)
    else:
        raise ValueError("Gender must be 'b' or 'g'.")

    return f"{first} {get_last_name()}"


print("\nHello Goyim!!")
print("Welcome to the Jewish Name Generator!\n")

def option():
    while True:
        choice = input("Boy or Girl? (b/g): ").strip().lower()
        if choice in {'b', 'boy', 'male'}:
            print(f"Your Jewish name is: {generate_name('boy')}\n")
            break
        if choice in {'g', 'girl', 'female'}:
            print(f"Your Jewish name is: {generate_name('girl')}\n")
            break
        print("Please enter 'b' for boy or 'g' for girl.\n")


def speedgen(): # generates a name no input
    gender = random.choice(['b', 'g'])
    print(f"Your Jewish name is: {generate_name(gender)}\n")


# option()

speedgen()