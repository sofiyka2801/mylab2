while True:
    def number(text):
        for letter in set(text):
            if letter.isalpha():
                x = text.count(letter)
                print(letter, "=", x)

    def words(text):
        res = []
        for word in text.split():
            if len(word) > 2:
                if word not in res:
                    res.append(word)
        Words = res
        Words.sort()
        resu = " ".join(Words)
        print(resu)

    print("""Menu: 




    1. Count letters




    2. Sort text




    3. Quit




    """)

    choice = input("Enter your choice: ")

    print()

    if choice == "1":

        text = input("Enter text: ")

        number(text)




    elif choice == "2":

        text = input("Enter text: ")

        words(text)




    elif choice == "3":

        break

    else:

        print("Incorrect input")
    print()