class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.languages = []
        self.progress = {}

    def add_language(self, language_name):
        language = Language(language_name)
        self.languages.append(language)
        self.progress[language_name] = 0
        
    def update_progress(self, language, new_progress):
        self.progress[language] = new_progress


class Language:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)


class Course:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)


class Lesson:
    def __init__(self, topic, content):
        self.topic = topic
        self.content = content
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)


class Exercise:
    def __init__(self, question, answer_options, correct_answer):
        self.question = question
        self.answer_options = answer_options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer


class ProgressTracker:
    def __init__(self, user):
        self.user = user
        self.progress = {}

    def update_progress(self, language, course, lesson):
        if language in self.progress:
            if course in self.progress[language]:
                if lesson in self.progress[language][course]:
                    self.progress[language][course][lesson] += 1
                else:
                    self.progress[language][course][lesson] = 1
            else:
                self.progress[language][course] = {lesson: 1}
        else:
            self.progress[language] = {course: {lesson: 1}}



# main class

if __name__ == "__main__":
    # Create a user
    user = User("Ali-Ahmed", "AliAhmed@example.com")
    
    # Add predefined languages
    languages = ["German", "French", "Spanish", "Italian"]
    for language_name in languages:
        user.add_language(language_name)
    
    # Display available languages
    print("Available languages:")
    for i, language in enumerate(user.languages, start=1):
        print(f"{i}. {language.name}")
    
    # Prompt user to select a language
    selected_language_index = int(input("Enter the language code you want to learn: ")) - 1
    
    # Check if the selected language index is valid
    if 0 <= selected_language_index < len(user.languages):
        selected_language = user.languages[selected_language_index]
        
        # Check if the selected language is German
        if selected_language.name.lower() == "german":
            # Initialize progress tracker
            progress_tracker = ProgressTracker(user)
            
            # Start German course
            German_course = Course("German Basics", 1)
            selected_language.add_course(German_course)
            German_lesson1 = Lesson("Greetings", "Learn basic greetings in German")
            German_course.add_lesson(German_lesson1)
            German_exercise1 = Exercise("What is 'Danke' in English?", ["Hello", "Goodbye", "Thank you"], "Thank you")
            German_exercise2 = Exercise("What is 'Kaffee' in English?", ["Coffee", "Milk", "Water"], "Coffee")
            German_lesson1.add_exercise(German_exercise1)
            German_lesson1.add_exercise(German_exercise2)
            
            # Initialize lesson and exercise details
            selected_course = German_course
            selected_lesson = German_lesson1
            selected_exercise_index = 0
            print(f"Welcome to the {selected_language.name} course!")
            print(f"Lesson: {selected_lesson.topic}")
            print(f"Exercise: {selected_lesson.exercises[selected_exercise_index].question}")
            
            # Loop for answering exercises
            while True:
                user_answer = input("What is your answer? ").strip()
                current_exercise = selected_lesson.exercises[selected_exercise_index]
                if current_exercise.check_answer(user_answer):
                    print("Correct!")
                    # Update progress
                    progress_tracker.update_progress(selected_language.name, selected_course.name, selected_lesson.topic)
                    
                    # Check if there are more exercises in the lesson
                    if selected_exercise_index < len(selected_lesson.exercises) - 1:
                        selected_exercise_index += 1
                        next_exercise = selected_lesson.exercises[selected_exercise_index]
                        print(f"Next Exercise: {next_exercise.question}")
                    else:
                        print("No more exercises in this lesson. Moving to the next lesson...")
                        # Check if there are more lessons in the course
                        if len(selected_course.lessons) > 1:
                            next_lesson = selected_course.lessons[1]
                            print(f"Next Lesson: {next_lesson.topic}")
                            print(f"First Exercise of Next Lesson: {next_lesson.exercises[0].question}")
                        else:
                            print("No more lessons in this course. You've completed the course!")
                            break
                else:
                    print("Incorrect. Try again.")
        else:
            print("The selected language does not have a predefined course.")
    else:
        print("Invalid language selection. Please select a valid language code.")
