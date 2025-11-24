import random
import re

# ANSI colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

#def explanation():
#    explanation

# --------------------------------------------------------
# QUIZ ENGINE (shared logic for all quizzes)
# --------------------------------------------------------
def check_answers(user_input, required_answers):
    """
    Check if ALL required answers appear somewhere in the user's input.
    User may add extra text, but all keywords must be present.
    """
    text = user_input.lower()

    # Split into alphanumeric words
    words = re.split(r'\W+', text)

    # Check each required word
    for ans in required_answers:
        if ans.lower() not in words:
            return False

    return True


def run_quiz(questions, answers, quiz_title, multi=False, pretty_answers=None, explanation=None):

    qa_pairs = list(zip(questions, answers))
    random.shuffle(qa_pairs)

    if pretty_answers:
        pretty_pairs = list(zip(questions, pretty_answers))
    else:
        pretty_pairs = None

    guesses = []
    score = 0

    print(YELLOW + "===================================================" + RESET)
    print(BOLD + f"                 {quiz_title}" + RESET)
    print(YELLOW + "===================================================" + RESET)
    if explanation:
        print(BOLD + "Oppgave tekst:" + RESET)
        print(explanation)
        print()
    else:
        print()

    for question, valid_answers in qa_pairs:
        print("------------------------------")
        print(question)

        guess = input("Ditt svar: ").strip().lower()
        guesses.append(guess)

        # lowercase answers
        valid = [a.lower() for a in valid_answers]

        # Normal quiz (single-answer matching)
        if not multi:
            correct = guess in valid

        # Multi-answer mode (all required answers must appear)
        else:
            correct = all(req.lower() in guess for req in valid)

        if correct:
            score += 1
            print(GREEN + "Riktig!" + RESET)
        else:
            print(RED + "Feil ;(" + RESET)

            # Pretty formatted answer shown if available
            if pretty_pairs:
                for q, p in pretty_pairs:
                    if q == question:
                        print("Et riktig svar er:")
                        print(p)
                        break
            else:
                print(f"Et riktig svar er: {valid_answers[0]}")

        print()
        print()

    # Results page
    print(YELLOW + "---------------------------------------------------------------")
    print(BOLD + "                        |Resultatene|          " + RESET)
    print(YELLOW + "---------------------------------------------------------------" + RESET)

    #print("Svar: ", end="")
    #for _, a in qa_pairs:
    #    print(a[0], end=" ")
    #print()
    for question, valid_answers in qa_pairs:
        #Checking if pretty_pairs is available
        if pretty_pairs:
            for q, p in pretty_pairs:
                if q.strip() == question.strip(): #Matching the question
                    print(BOLD + question + RESET)
                    print(BOLD + "De riktige svarene er:\n" + RESET + p + "\n")
                    break 
        else:
            print(BOLD + question + RESET)
            print(BOLD + "De riktige svarene er:\n" + RESET + valid_answers[0])
            break
    print()



    print(BOLD + "Forsøk:\n" + RESET, end="")
    for g in guesses:
        print(g, end=" ")
    print()

    score_percent = int(score / len(qa_pairs) * 100)
    print(GREEN + f"\nDu hadde: {score_percent}% riktige" + RESET)
    print(YELLOW + "---------------------------------------------------------------" + RESET)
    print("\n")







def run_multiple_ans_quiz(questions, answers, quiz_title):
    guesses = []
    score = 0

    #Start page for quiz
    print(YELLOW + "===================================================" + RESET)
    print(BOLD + f"                 {quiz_title}" + RESET)
    print(YELLOW + "===================================================" + RESET)
    print()
    print(explanation)







    # Results / end page for quiz
    print(YELLOW + "---------------------------------------------------------------")
    print(BOLD + "                        |Resultatene|          " + RESET)
    print(YELLOW + "---------------------------------------------------------------" + RESET)

    print("Svar: ", end="")
    for _, a in qa_pairs:
        print(a[0], end=" ")
    print()

    print("Forsøk: ", end="")
    for g in guesses:
        print(g, end=" ")
    print()

    score_percent = int(score / len(qa_pairs) * 100)
    print(GREEN + f"\nDu hadde: {score_percent}% riktige" + RESET)
    print(YELLOW + "---------------------------------------------------------------" + RESET)
    print("\n")


# --------------------------------------------------------
# QUIZ 1: SPØRREORD
# --------------------------------------------------------
def quiz_sporreord():
    explanation = (
        "Oversett spørreordene"
    )

    questions = (
        "Hva?\n",
        "Hvordan?\n",
        "Hvor mye?\n",
        "Hvorfor?\n",
        "Når?\n",
        "Hvor?\n",
        "Hvilken/Hvilket\n",
        "Hvem?\n",
        "Hvor mange?\n"
    )

    answers = (
        ["che cosa", "che cosa?"],
        ["come", "come?"],
        ["quanto", "quanto?"],
        ["perché", "perché?"],
        ["quando", "cuando?"],
        ["dove", "dove?"],
        ["quale", "quale?"],
        ["chi", "chi?"],
        ["quanti", "quanti?"]
    )
    run_quiz(questions, answers, "Spørreord", explanation=explanation)


# --------------------------------------------------------
# QUIZ 2: COLOURS
# --------------------------------------------------------
def quiz_colours():
    explanation = (
        "Oversett fargene"
    )

    questions = (
        "Rød\n",
        "Blå\n",
        "Grønn\n",
        "Gul\n",
        "Svart\n",
        "Hvit\n",
        "Oransj\n",
        "Rosa\n",
    )

    answers = (
        ["rosso"],
        ["blu"],
        ["verde"],
        ["giallo"],
        ["nero"],
        ["bianco"],
        ["arancione"],
        ["Rosa"]
    )

    run_quiz(questions, answers, "Farger", explanation=explanation)


# --------------------------------------------------------
# QUIZ 3: RANDOM WORDS
# --------------------------------------------------------
def quiz_random():
    explanation = (
        "Oversett ordene"
    )

    questions = (
        "Hus\n",
        "Bok\n",
        "Mat\n",
        "Katt\n",
    )

    answers = (
        ["casa"],
        ["libro"],
        ["cibo"],
        ["gatto"]
    )

    run_quiz(questions, answers, "Tilfeldige ord", explanation=explanation)


# --------------------------------------------------------
# QUIZ 4: Compiti per casa 7
# --------------------------------------------------------
#MOST LIKELY I HAVE TO MAKE A FUNCTION FOR MULTIPLE ANSWER BY ITSELF!!!
def quiz_compiti_per_casa_7():
    explanation = (
        "I oppgaver med " + BOLD + "A" + RESET + 
            " skriv siste vokalen på adjektiver hvor du ser prikkene “. . .”\n"
        "I oppgaver med " + BOLD + "B" + RESET + " gjør det samme med fargene."
    )
    questions = (BOLD + "A\n" + RESET +
        "La stazione Termini di Roma è la più grand... stazione ferroviari... Italian...",
    )

    answers = (
        ["grande", "ferroviaria", "italiana"],   # words to check in ANY order
    )

    pretty_answers = (
        "La stazione Termini di Roma è la più " + GREEN + "grande" + RESET 
        + " stazione " + GREEN + "ferroviaria" + RESET + " "
        + GREEN + "Italiana" + RESET
    )

    run_quiz(
        questions, answers, "Compiti per casa 7", multi=True,
        pretty_answers=(pretty_answers,), explanation=explanation  # must be tuple
    )


# --------------------------------------------------------
# MAIN MENU
# --------------------------------------------------------
def main_menu():
    while True:
        print(YELLOW + "======================" + RESET)
        print(BOLD + "       Hovedmeny      " + RESET)
        print(YELLOW + "======================" + RESET)
        print("1. Spørreord")
        print("2. Farger")
        print("3. Tilfeldige ord")
        print("4. Hjemmelekse fra forelesning 7")
        print("5. Avslutt")
        print()

        choice = input("Velg et nummer: ")

        if choice == "1":
            quiz_sporreord()
        elif choice == "2":
            quiz_colours()
        elif choice == "3":
            quiz_random()
        elif choice == "4":
            quiz_compiti_per_casa_7()
        elif choice == "5":
            print(GREEN + "Ha det!" + RESET)
            break
        else:
            print(RED + "Ugyldig valg, prøv igjen.\n" + RESET)


# --------------------------------------------------------
# START PROGRAM
# --------------------------------------------------------
main_menu()
