def learn_about_cultures(cultures, learned_cultures):
    print("Select a culture to learn about by writing the name:")
    # Print the culture names with numbered options
    for i, culture_name in enumerate(cultures.keys(), start=1):
        print(f"{i}. {culture_name}")
    choice = input("Enter your choice: ").upper()
    if choice in cultures:
        print(f"\n{cultures[choice]}\n")
        learned_cultures.append(choice)
    else:
        print("Invalid choice. Please enter a valid choice.")
    new_choice = input("Do you want to learn about another culture? Enter 'y' for yes and 'n' for no: ")
    while new_choice == 'y':
        print("Select a culture to learn about:")
        # Print the culture names with numbered options
        for i, culture_name in enumerate(cultures.keys(), start=1):
            print(f"{i}. {culture_name}")
        new_choice_input = input("Enter your choice: ").upper()
        if new_choice_input in cultures:
            print()
            print(cultures[new_choice_input])
            print()
            learned_cultures.append(new_choice_input)
        else:
            print("Invalid choice. Please enter a valid choice.")
        new_choice = input("Do you want to learn about another culture? Enter 'y' for yes and 'n' for no: ")
    print(f"You have learned about the following cultures: {learned_cultures}")
    print()

def take_quiz(quiz_questions, learned_cultures):
    while True:
        print("Enter 'quiz' to take the quiz or 'exit' to end learning and take the quiz.")
        quiz_choice = input("Enter your choice: ")

        if quiz_choice == "quiz":
            break
        elif quiz_choice == "exit":
            break

    print("\nYou have learned about the following cultures:")
    for culture in learned_cultures:
        print(culture)

    score = 0
    total_questions = 0

    if learned_cultures:
        print("\nNow, let's test your knowledge with a quiz!")
        for culture in learned_cultures:
            if culture.upper() in quiz_questions:
                total_questions += 1
                print(quiz_questions[culture.upper()]["question"])
                answer = input("Enter your answer: ")
                if answer.lower() == quiz_questions[culture.upper()]["answer"].lower():
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Incorrect!\nThe correct answer is {quiz_questions[culture.upper()]['answer']}\n")
        print(f"You scored {score} out of {total_questions} questions.")

    else:
        print("\nSince you did not learn about any culture, there is no quiz for you to take.")

    print("\nThank you for learning and playing our African Culture Quiz Program!")

def main():
    cultures = {
        "YORUBA": "Yoruba culture is one of the most vibrant cultures in Nigeria, known for its rich folklore, "
                  "colorful festivals, and unique religious practices.",

        "MAASAI": "The Maasai people of East Africa are known for their distinctive customs and dress, and for their"
                  " close relationship with the natural world.",

        "ZULU": "The Zulu people of South Africa have a rich history and cultural heritage, including a unique system "
                "of government, art, music, and dance.",

        "BERBER": "The Berber people of North Africa have a rich and ancient culture, known for their distinctive "
                  "language, architecture, music, and traditional crafts.",

        "KIKUYU": "The Kikuyu people are the largest ethnic group in Kenya and have a rich cultural heritage. "
                  "They are known for their music, dance, and storytelling traditions.",

        "SWAHILI": "The Swahili people are a diverse group found along the East African coast, including in Kenya, "
                   "Tanzania, and Mozambique. They have a unique blend of African, Arab, and Indian influences and are "
                   "known for their language, music, and cuisine.",

        "TUAREG": "The Tuareg people are a nomadic group found in the Sahara Desert. They are known for their " 
                  "distinctive blue clothing and jewelry, and have a rich tradition of music and poetry.",

        "IGBO": "The Igbo people have a rich cultural heritage, including a unique religion, art, music, and dance. "
                "They have a strong emphasis on community and are known for their entrepreneurial spirit.",

        "AMHARA": "The Amhara people are one of the largest ethnic groups in Ethiopia and have a rich cultural "
                  "heritage, including a unique language, music, and dance.",

        "HAUSA": "The Hausa people are a large ethnic group found in Nigeria and Niger. They have a rich "
                 "cultural heritage, including a unique language, music, and dance.",

        "SAN": "The San people are one of the oldest ethnic groups in Southern Africa and have a unique "
               "cultural heritage, including a distinctive language, art, music, and dance.",

        "NDEBELE": "The Ndebele people of Zimbabwe and South Africa are known for their distinctive art and "
                   "architecture, including brightly painted houses and bead-work.",

        "WOLOF": "The Wolof people are one of the largest ethnic groups in Senegal and have a rich cultural heritage, "
                 "including a unique language, music, and dance.",

        "ASHANTI": "The Ashanti people of Ghana are known for their rich cultural traditions, including their use of "
                   "kente cloth, traditional dance and music, and elaborate funerals to honor their ancestors.",

        "FULA": "The Fula people are a large ethnic group found across West and Central Africa. "
                "They have a rich cultural heritage, including a unique language, music, and dance.",

    }

    quiz_questions = {
        "YORUBA": {"question": "What country is the Yoruba culture from?", "answer": "Nigeria"},

        "MAASAI": {"question": "What animals are the Maasai people known for herding?", "answer": "Cattle"},

        "ZULU": {"question": "What is the traditional weapon of the Zulu people?", "answer": "Spear"},

        "BERBER": {"question": "What is the traditional music of the Berber people called?", "answer": "Amazigh"},

        "KIKUYU": {"question": "What are the Kikuyu people known for in terms of culture?",
                   "answer": "Music, dance, storytelling"},

        "SWAHILI": {"question": "What makes the Swahili people's culture unique?",
                    "answer": "Blend of African, Arab, and Indian influences"},

        "TUAREG": {"question": "What is the distinctive clothing worn by the Tuareg people?",
                   "answer": "Blue clothing and jewelry"},

        "IGBO": {"question": "The Igbo people have a strong emphasis on what?", "answer": "Community"},

        "AMHARA": {"question": "The Amhara people are one of the largest ethnic groups in?",
                   "answer": "Ethiopia"},

        "HAUSA": {"question": "Where are the two places where the Hausa people are found?",
                  "answer": "Nigeria and Niger"},

        "SAN": {"question": "The San people are one of the oldest ethnic groups in?", "answer": "Southern Africa"},

        "NDEBELE": {"question": "What is the distinctive art form of the Ndebele people?",
                    "answer": "Painted houses and bead-work"},

        "WOLOF": {"question": "The Wolof people are in which country?",
                  "answer": "Senegal"},

        "ASHANTI": {"question": "What is the traditional cloth used by the Ashanti people?", "answer": "Kente cloth"},

        "FULA": {"question": "What is the unique cultural heritage of the Fula people?",
                 "answer": "Language, music, and dance"}
    }

    print("Welcome to the African Culture Learning and Quiz Program!")
    learned_cultures = []
    learn_about_cultures(cultures, learned_cultures)
    take_quiz(quiz_questions, learned_cultures)

main()
