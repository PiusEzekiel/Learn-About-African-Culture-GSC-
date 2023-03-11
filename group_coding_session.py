countries_culture = ["Zulu culture of South Africa",
                     "Maasai culture of Kenya and Tanzania",
                     "Berber culture of North Africa",
                     "Yoruba culture of Nigeria",
                     "Kikuyu culture of Kenya",
                     "Swahili culture of East Africa",
                     "Tuareg culture of the Sahara Desert",
                     "Igbo culture of Nigeria",
                     "Amhara culture of Ethiopia",
                     "Hausa culture of Nigeria and Niger",
                     "San culture of Southern Africa",
                     "Ndebele culture of Zimbabwe and South Africa",
                     "Ndebele culture of Zimbabwe and South Africa",
                     "Wolof culture of Senegal",
                     "Ashanti culture of Ghana",
                     "Fula culture of West and Central Africa",
                     ]

valid_choices = []
for i in range(1, len(countries_culture) + 1):
    valid_choices.append(str(i))
print("These are the options you have: {}".format(valid_choices))
current_choice = "-"

while current_choice != '0':
    if current_choice == '1':
        print("You're reading about option {}".format(current_choice))
        print("Zulu culture of South Africa: The Zulu people have a strong warrior tradition and are known"
              " for their dance, music, and art. They have a hierarchical social structure, "
              "with the king at the top.")
    elif current_choice == '2':
        print("You're reading about option {}".format(current_choice))
        print("Maasai culture of Kenya and Tanzania: The Maasai people are known for their distinctive dress,"
              " which includes brightly colored shukas (cloth wraps) and beaded jewelry. "
              "They are semi-nomadic herders and have a strong connection to their cattle.")
    elif current_choice == '3':
        print("You're reading about option {}".format(current_choice))
        print("Berber culture of North Africa: Berber culture is a diverse set of cultures found across North Africa, "
              "including in Morocco, Algeria, Tunisia, and Libya. The Berber people have a rich history and are known "
              "for their music, dance, and art.")
    elif current_choice == '4':
        print("You're reading about option {}".format(current_choice))
        print("Yoruba culture of Nigeria: The Yoruba people have a rich cultural heritage, including a unique religion,"
              " art, music, and dance. They have a strong emphasis on family and community.")
    elif current_choice == '5':
        print("You're reading about option {}".format(current_choice))
        print("Kikuyu culture of Kenya: The Kikuyu people are the largest ethnic group in Kenya and have a rich"
              " cultural heritage. They are known for their music, dance, and storytelling traditions.")
    elif current_choice == '6':
        print("You're reading about option {}".format(current_choice))
        print("Swahili culture of East Africa: The Swahili people are a diverse group found along the"
              " East African coast, including in Kenya, Tanzania, and Mozambique. They have a unique blend of African,"
              " Arab, and Indian influences and are known for their language, music, and cuisine.")
    elif current_choice == '7':
        print("You're reading about option {}".format(current_choice))
        print("Tuareg culture of the Sahara Desert: The Tuareg people are a nomadic group found in the Sahara Desert."
              " They are known for their distinctive blue clothing and jewelry, and have a rich tradition of"
              " music and poetry.")
    elif current_choice == '8':
        print("You're reading about option {}".format(current_choice))
        print("Igbo culture of Nigeria: The Igbo people have a rich cultural heritage, including a unique religion,"
              " art, music, and dance. They have a strong emphasis on community and are known for"
              " their entrepreneurial spirit.")
    elif current_choice == '9':
        print("You're reading about option {}".format(current_choice))
        print("Amhara culture of Ethiopia: The Amhara people are one of the largest ethnic groups in Ethiopia and"
              " have a rich cultural heritage, including a unique language, music, and dance.")
    elif current_choice == '10':
        print("You're reading about option {}".format(current_choice))
        print("Hausa culture of Nigeria and Niger: The Hausa people are a large ethnic group found in"
              " Nigeria and Niger. They have a rich cultural heritage, including a unique language, music, and dance.")
    elif current_choice == '12':
        print("You're reading about option {}".format(current_choice))
        print("San culture of Southern Africa: The San people are one of the oldest ethnic groups in"
              " Southern Africa and have a unique cultural heritage, including a distinctive"
              " language, art, music, and dance.")
    elif current_choice == '13':
        print("You're reading about option {}".format(current_choice))
        print("Ndebele culture of Zimbabwe and South Africa: The Ndebele people are known for their distinctive"
              " art and architecture, including brightly painted houses and bead-work.")
    elif current_choice == '14':
        print("You're reading about option {}".format(current_choice))
        print("Wolof culture of Senegal: The Wolof people are one of the largest ethnic groups in Senegal and"
              " have a rich cultural heritage, including a unique language, music, and dance.")
    elif current_choice == '15':
        print("You're reading about option {}".format(current_choice))
        print("Ashanti culture of Ghana: The Ashanti people are known for their rich cultural traditions,"
              " including their use of kente cloth, traditional dance and music, and elaborate"
              " funerals to honor their ancestors.")
    elif current_choice == '16':
        print("You're reading about option {}".format(current_choice))
        print("Fula culture of West and Central Africa: The Fula people are a large ethnic group found across"
              " West and Central Africa. They have a rich cultural heritage, including a unique"
              " language, music, and dance.")
    else:
        print("You have to choose a culture to learn about from the list below:")
        for number, culture in enumerate(countries_culture):
            print("{0}: {1}".format(number + 1, culture))
    current_choice = input()

print("Thanks for exploring African culture with us! Rerun the program to start again.")
