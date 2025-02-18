import sqlite3
import random

def init_db():
    conn = sqlite3.connect("flashcards.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_flashcard(question, answer):
    conn = sqlite3.connect("flashcards.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO flashcards (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    conn.close()

def view_flashcards():
    conn = sqlite3.connect("flashcards.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, question, answer FROM flashcards")
    flashcards = cursor.fetchall()
    conn.close()
    return flashcards

def delete_flashcard(card_id):
    conn = sqlite3.connect("flashcards.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM flashcards WHERE id = ?", (card_id,))
    conn.commit()
    conn.close()

def quiz():
    flashcards = view_flashcards()
    if not flashcards:
        print("No flashcards available. Add some first!")
        return
    
    score = 0
    random.shuffle(flashcards)
    for card in flashcards:
        print(f"Question: {card[1]}")
        user_answer = input("Your answer: ")
        if user_answer.strip().lower() == card[2].strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {card[2]}")
    
    print(f"Quiz complete! Your score: {score}/{len(flashcards)}")

def main():
    init_db()
    while True:
        print("\nFlashcard App")
        print("1. Add Flashcard")
        print("2. View Flashcards")
        print("3. Delete Flashcard")
        print("4. Quiz Mode")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            add_flashcard(question, answer)
            print("Flashcard added!")
        elif choice == "2":
            flashcards = view_flashcards()
            if not flashcards:
                print("No flashcards found.")
            else:
                for card in flashcards:
                    print(f"ID: {card[0]} | Question: {card[1]} | Answer: {card[2]}")
        elif choice == "3":
            card_id = input("Enter the ID of the flashcard to delete: ")
            delete_flashcard(card_id)
            print("Flashcard deleted!")
        elif choice == "4":
            quiz()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()