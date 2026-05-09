import random

# Ask user to type their username
username = input("Enter username: ")
# Ask user to type their password
password = input("Enter password: ")

if username == "mark" and password == "markie":
    print("Login successful!\n")
else:
    print("Login failed. Exiting program.")  # Login failed message
    exit()  # Stop the program here

class FlagQuiz:
    """A quiz game where you guess which country a flag belongs to"""
    
    def __init__(self):

        # All the flag questions
        self.all_questions = [
            {"description": "White background with a red circle in the middle", "answer": "japan", 
             "options": ["china", "japan", "south korea", "vietnam"]},
            {"description": "Red background with a white cross", "answer": "england", 
             "options": ["england", "denmark", "switzerland", "norway"]},
            {"description": "Green, white, and orange vertical stripes", "answer": "ireland", 
             "options": ["italy", "ireland", "ivory coast", "india"]},
            {"description": "Blue background with a white cross", "answer": "greece", 
             "options": ["greece", "finland", "iceland", "australia"]},
            {"description": "Red and white horizontal stripes (13 stripes) with a blue rectangle and white stars", "answer": "usa", 
             "options": ["usa", "united kingdom", "france", "russia"]},
            {"description": "Red background with a white circle and red maple leaf", "answer": "canada", 
             "options": ["canada", "denmark", "switzerland", "austria"]},
            {"description": "Green, yellow, and red horizontal stripes with a black star in the middle", "answer": "ghana", 
             "options": ["ethiopia", "ghana", "senegal", "cameroon"]},
            {"description": "Blue and white horizontal stripes with a sun in the middle", "answer": "argentina", 
             "options": ["argentina", "uruguay", "chile", "peru"]},
            {"description": "White background with a blue cross", "answer": "finland", 
             "options": ["finland", "norway", "sweden", "iceland"]},
            {"description": "Red background with a yellow hammer and sickle", "answer": "ussr", 
             "options": ["ussr", "china", "north korea", "vietnam"]},
            {"description": "Green background with a white crescent and star", "answer": "pakistan", 
             "options": ["pakistan", "turkey", "algeria", "malaysia"]},
            {"description": "Three horizontal stripes: black, red, and gold", "answer": "germany", 
             "options": ["belgium", "germany", "hungary", "yemen"]},
            {"description": "Three vertical stripes: blue, white, and red", "answer": "france", 
             "options": ["france", "netherlands", "russia", "serbia"]},
            {"description": "White background with a red cross", "answer": "switzerland", 
             "options": ["switzerland", "denmark", "norway", "england"]},
            {"description": "Green background with a yellow diamond and blue circle with white stars", "answer": "brazil", 
             "options": ["brazil", "venezuela", "colombia", "panama"]},
            {"description": "Red and white diagonal stripes with a blue square and white stars in the corner", "answer": "chile", 
             "options": ["chile", "cuba", "liberia", "togo"]},
            {"description": "White background with a red circle and red triangles on the edges", "answer": "bahrain", 
             "options": ["qatar", "bahrain", "kuwait", "oman"]},
            {"description": "Blue background with a yellow cross", "answer": "sweden", 
             "options": ["sweden", "norway", "finland", "denmark"]},
            {"description": "Red background with a yellow five-pointed star", "answer": "vietnam", 
             "options": ["vietnam", "china", "morocco", "somalia"]},
            {"description": "Green, white, and black horizontal stripes with a red vertical stripe on the left", "answer": "sudan", 
             "options": ["sudan", "jordan", "palestine", "kuwait"]}
        ]
        random.shuffle(self.all_questions)  # Mix up the order of questions
        self.questions = self.all_questions[:10]  # Pick 10 Questions for the quiz
        self.score = 0  # Start score at zero
    
    def ask_question(self, question_data):
        """Show one question to the player and check if their answer is right"""
        print("\n")
        print(f"Flag Description: {question_data['description']}")
        print("\nOptions:")
        letters = ['a', 'b', 'c', 'd']
        # Show each answer choice with a letter (a, b, c, d)
        for i, option in enumerate(question_data['options']):
            print(f"{letters[i]}. {option.title()}")
        
        # Keep asking until player enters a valid letter
        while True:
            user_answer = input("\nEnter your choice (a/b/c/d): ").strip().lower()
            if user_answer in letters:
                index = letters.index(user_answer)
                selected_option = question_data['options'][index]
                # Return True if answer is correct, False if wrong
                return selected_option == question_data['answer']
            else:
                print("Invalid input! Please enter a, b, c, or d.")
    
    def play(self):
        """Run the whole flag quiz game"""
        print("\n=== FLAG QUIZ ===")
        print("Guess the country based on the flag description.")
        
        # Go through each question one by one
        for i, q in enumerate(self.questions, 1):
            print(f"\nQuestion {i} of 10")
            if self.ask_question(q):
                print("Correct!")
                self.score += 1  # Add 1 point for correct answer
            else:
                print(f"Wrong! The correct answer is {q['answer'].title()}")
        
        # Show final score
        print(f"\nFlag Quiz completed! Your score: {self.score}/10")

class GeneralKnowledgeQuiz:
    """A quiz game with questions about geography and science"""
    
    def __init__(self):

        # All the general knowledge questions
        self.all_questions = [
            {"question": "What is the largest ocean on Earth?", "answer": "pacific", 
             "options": ["atlantic", "indian", "pacific", "arctic"]},
            {"question": "What is the longest river in the world?", "answer": "nile", 
             "options": ["amazon", "nile", "yangtze", "mississippi"]},
            {"question": "What is the capital of France?", "answer": "paris", 
             "options": ["london", "berlin", "madrid", "paris"]},
            {"question": "Which planet is known as the Red Planet?", "answer": "mars", 
             "options": ["jupiter", "mars", "venus", "saturn"]},
            {"question": "What is the tallest mountain in the world?", "answer": "everest", 
             "options": ["k2", "kangchenjunga", "everest", "makalu"]},
            {"question": "Which desert is the largest non-polar desert?", "answer": "sahara", 
             "options": ["gobi", "sahara", "arabian", "kalahari"]},
            {"question": "What is the capital of Japan?", "answer": "tokyo", 
             "options": ["seoul", "beijing", "tokyo", "bangkok"]},
            {"question": "Which gas do plants absorb from the air?", "answer": "carbon dioxide", 
             "options": ["oxygen", "nitrogen", "hydrogen", "carbon dioxide"]},
            {"question": "What is the hardest natural substance?", "answer": "diamond", 
             "options": ["gold", "iron", "diamond", "platinum"]},
            {"question": "Which animal is known as the 'Ship of the Desert'?", "answer": "camel", 
             "options": ["horse", "camel", "elephant", "donkey"]},
            {"question": "What is the largest continent?", "answer": "asia", 
             "options": ["africa", "asia", "north america", "europe"]},
            {"question": "Which country gifted the Statue of Liberty to the USA?", "answer": "france", 
             "options": ["england", "spain", "france", "germany"]},
            {"question": "What is the boiling point of water in Celsius?", "answer": "100", 
             "options": ["90", "100", "110", "120"]},
            {"question": "Which scientist developed the theory of relativity?", "answer": "einstein", 
             "options": ["newton", "galileo", "einstein", "tesla"]},
            {"question": "What is the capital of Egypt?", "answer": "cairo", 
             "options": ["alexandria", "cairo", "giza", "luxor"]},
            {"question": "Which is the fastest land animal?", "answer": "cheetah", 
             "options": ["lion", "cheetah", "leopard", "tiger"]},
            {"question": "What is the primary organ in the human circulatory system?", "answer": "heart", 
             "options": ["brain", "heart", "lungs", "liver"]},
            {"question": "Which country has the most natural lakes?", "answer": "canada", 
             "options": ["usa", "russia", "canada", "brazil"]},
            {"question": "What is the smallest planet in our solar system?", "answer": "mercury", 
             "options": ["mercury", "mars", "venus", "pluto"]},
            {"question": "Who painted the Mona Lisa?", "answer": "da vinci", 
             "options": ["van gogh", "picasso", "da vinci", "michelangelo"]}
        ]
        random.shuffle(self.all_questions)  # Mix up the order
        self.questions = self.all_questions[:10]  # Pick 10 questions for the quiz
        self.score = 0  # Start score at zero
    
    def ask_question(self, question_data):
        """Show one question and check if the answer is correct"""
        print("\n")
        print(f"Question: {question_data['question']}")
        print("\nOptions:")
        letters = ['a', 'b', 'c', 'd']

        # Show each answer choice with a letter
        for i, option in enumerate(question_data['options']):
            print(f"{letters[i]}. {option.title()}")
        
        # Keep asking till a valid letter was entered
        while True:
            user_answer = input("\nEnter your choice (a/b/c/d): ").strip().lower()
            if user_answer in letters:
                index = letters.index(user_answer)
                selected_option = question_data['options'][index]
                return selected_option == question_data['answer']
            else:
                print("Invalid input! Please enter a, b, c, or d.")
    
    def play(self):
        """Run the general knowledge quiz"""
        print("\n=== GENERAL KNOWLEDGE QUIZ ===")
        print("Topics: Geography and Science")
        
        # Go through each question
        for i, q in enumerate(self.questions, 1):
            print(f"\nQuestion {i} of 10")
            if self.ask_question(q):
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {q['answer'].title()}")
        
        # Show final score
        print(f"\nGeneral Knowledge Quiz completed! Your score: {self.score}/10")

class PeriodicTableQuiz:
    """A quiz about chemical elements - their symbols and atomic numbers"""
    
    def __init__(self):

        # List of elements
        self.all_elements = [
            {"name": "hydrogen", "symbol": "H", "number": 1},
            {"name": "helium", "symbol": "He", "number": 2},
            {"name": "lithium", "symbol": "Li", "number": 3},
            {"name": "beryllium", "symbol": "Be", "number": 4},
            {"name": "boron", "symbol": "B", "number": 5},
            {"name": "carbon", "symbol": "C", "number": 6},
            {"name": "nitrogen", "symbol": "N", "number": 7},
            {"name": "oxygen", "symbol": "O", "number": 8},
            {"name": "fluorine", "symbol": "F", "number": 9},
            {"name": "neon", "symbol": "Ne", "number": 10},
            {"name": "sodium", "symbol": "Na", "number": 11},
            {"name": "magnesium", "symbol": "Mg", "number": 12},
            {"name": "aluminum", "symbol": "Al", "number": 13},
            {"name": "silicon", "symbol": "Si", "number": 14},
            {"name": "phosphorus", "symbol": "P", "number": 15},
            {"name": "sulfur", "symbol": "S", "number": 16},
            {"name": "chlorine", "symbol": "Cl", "number": 17},
            {"name": "argon", "symbol": "Ar", "number": 18},
            {"name": "potassium", "symbol": "K", "number": 19},
            {"name": "calcium", "symbol": "Ca", "number": 20}
        ]
        random.shuffle(self.all_elements)  # Mix up the order
        self.questions = self.all_elements[:10]  # Pick 10 elements for the quiz
        self.score = 0  # Start score at zero
    
    def ask_number_question(self, element):
        """Ask what the atomic number is for a given element"""
        print("\n")
        print(f"Element: {element['name'].title()}")
        print("What is its atomic number?")
        
        correct_number = element['number']
        # Gather 3 wrong answers from other elements
        wrong_numbers = []
        for e in self.all_elements:
            if e['number'] != correct_number and e['number'] not in wrong_numbers:
                wrong_numbers.append(e['number'])
            if len(wrong_numbers) >= 3:
                break
        
        # Combine correct and wrong answers, then mix them up
        options = [correct_number] + wrong_numbers[:3]
        random.shuffle(options)
        
        # Show choices with letters
        letters = ['a', 'b', 'c', 'd']
        for i, option in enumerate(options):
            print(f"{letters[i]}. {option}")
        
        # Keep asking until valid input
        while True:
            user_answer = input("\nEnter your choice (a/b/c/d): ").strip().lower()
            if user_answer in letters:
                index = letters.index(user_answer)
                selected_option = options[index]
                return selected_option == correct_number
            else:
                print("Invalid input! Please enter a, b, c, or d.")
    
    def ask_symbol_question(self, element):
        """Ask what the chemical symbol is for a given element"""
        print("\n")
        print(f"Element: {element['name'].title()}")
        print("What is its atomic symbol?")
        
        correct_symbol = element['symbol']
        # Gather 3 wrong symbols from other elements
        wrong_symbols = []
        for e in self.all_elements:
            if e['symbol'] != correct_symbol and e['symbol'] not in wrong_symbols:
                wrong_symbols.append(e['symbol'])
            if len(wrong_symbols) >= 3:
                break
        
        # Combine correct and wrong answers, then mix them up
        options = [correct_symbol] + wrong_symbols[:3]
        random.shuffle(options)
        
        # Show choices with letters
        letters = ['a', 'b', 'c', 'd']
        for i, option in enumerate(options):
            print(f"{letters[i]}. {option}")
        
        # Keep asking until valid input
        while True:
            user_answer = input("\nEnter your choice (a/b/c/d): ").strip().lower()
            if user_answer in letters:
                index = letters.index(user_answer)
                selected_option = options[index]
                return selected_option == correct_symbol
            else:
                print("Invalid input! Please enter a, b, c, or d.")
    
    def play(self):
        """Run the periodic table quiz"""
        print("\n=== PERIODIC TABLE QUIZ ===")
        print("You will be asked for atomic numbers and symbols.")
        
        # Ask 10 questions, randomly mixing number questions and symbol questions
        for i in range(10):
            element = self.questions[i % len(self.questions)]
            print(f"\nQuestion {i+1} of 10")
            
            # Randomly choose whether to ask for number or symbol
            question_type = random.choice(["number", "symbol"])
            
            if question_type == "number":
                correct = self.ask_number_question(element)
                if correct:
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Wrong! The correct atomic number is {element['number']}")
            else:
                correct = self.ask_symbol_question(element)
                if correct:
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Wrong! The correct symbol is {element['symbol']}")
        
        # Show final score
        print(f"\nPeriodic Table Quiz completed! Your score: {self.score}/10")

def display_menu():
    """Show the main menu with all quiz options"""
    print("+---------------------------------+")
    print("|              MENU               |")
    print("+---------------------------------+")
    print("| 1. Flag Quiz                    |")
    print("| 2. General Knowledge Quiz       |")
    print("| 3. Periodic Table Quiz          |")
    print("| 4. Exit                         |")
    print("+---------------------------------+")

def main():
    """Main program that runs everything"""
    print("\n=== Welcome to Mark's Quiz Challenge! ===\n")
    
    # Keep showing menu until user chooses to exit
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        # Start the quiz the user picked
        if choice == '1':
            quiz = FlagQuiz()
            quiz.play()
        elif choice == '2':
            quiz = GeneralKnowledgeQuiz()
            quiz.play()
        elif choice == '3':
            quiz = PeriodicTableQuiz()
            quiz.play()
        elif choice == '4':
            print("\nThank you for playing! Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.")

# Start the program
if __name__ == "__main__":
    main()
