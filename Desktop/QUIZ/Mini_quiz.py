

questions = [
    {
        "prompt": "Qui a peint ''La nuit étoilée'' ?",
        "options": ["A. Pablo Picasson", "B.Vincent van Gogh","C. Claude Monet", "D. Salvador Dali"],
        "reponse": "B"
    },
    {
        "prompt": "Quelle est la planète la plus proche du soleil ?",
        "options": ["A. Vénus", "B. Terre", "C. Mars", "D. Mercure"],
        "reponse": "D"

    },
    {
        "prompt": "Quel est le plus grand désert du monde ?",
        "options": ["A. Sahara", "B. Désert d'Arabie", "C. Désert de Gobi", "D. Antarctique"],
        "reponse": "D"
    },
    {
        "prompt": "Quel est le plus long fleuve du monde ?",
        "options": ["A. Amazone","B. Nil", "C. Yangsté", "D. Mississippi"],
        "reponse": "A"

    }
]

def mini_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        reponse = input("Choisissez une réponse (A, B, C ou D): ").upper()
        if reponse == question["reponse"]:
            print("Bonne réponse !!\n")
            score += 1
        else:
            print("FAUX !! La bonne réponse était", question["reponse"], "\n")

    print((f"Vous avez un score de {score} sur {len(questions)}."))


mini_quiz(questions)

