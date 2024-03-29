import tkinter as tk
import time
from PIL import Image, ImageTk

# Main Window
root = tk.Tk()
root.title("Justin's Quiz Game")
root.geometry("600x650")  # Sets the GUI width and height
root.configure(bg="#A4D2CF")  # Sets the background color of the quiz program

# Photo Images
logo = ImageTk.PhotoImage(file="logo.png")
easy = ImageTk.PhotoImage(file="Easy Mode.png")
hard = ImageTk.PhotoImage(file="Hard Mode.png")
easyv2 = ImageTk.PhotoImage(file="Easy Mode 2.png")
hardv2 = ImageTk.PhotoImage(file="Hard Mode 2.png")
arrow = ImageTk.PhotoImage(file="Arrow.png")
arrowv2 = ImageTk.PhotoImage(file="Arrow 2.png")
help_icon = ImageTk.PhotoImage(file="Help Icon.png")
help_iconv2 = ImageTk.PhotoImage(file="Help Icon 2.png")
confetti = ImageTk.PhotoImage(file="Confetti.png")
confettiv2 = ImageTk.PhotoImage(file="Confetti 2.png")

# Easy Mode Flags
canada_flag = ImageTk.PhotoImage(file="Canada.png")
america_flag = ImageTk.PhotoImage(file="America.png")
south_africa_flag = ImageTk.PhotoImage(file="South Africa.png")
switzerland_flag = ImageTk.PhotoImage(file="Switzerland.png")
turkey_flag = ImageTk.PhotoImage(file="Turkey.png")
united_kingdom_flag = ImageTk.PhotoImage(file="United Kingdom.png")
south_korea_flag = ImageTk.PhotoImage(file="South Korea.png")
japan_flag = ImageTk.PhotoImage(file="Japan.png")
france_flag = ImageTk.PhotoImage(file="France.png")
new_zealand_flag = ImageTk.PhotoImage(file="New Zealand.png")

# Hard Mode Flags
sweden_flag = ImageTk.PhotoImage(file="Sweden.png")
jamaica_flag = ImageTk.PhotoImage(file="Jamaica.png")
romania_flag = ImageTk.PhotoImage(file="Romania.png")
azerbaijan_flag = ImageTk.PhotoImage(file="Azerbaijan.png")
laos_flag = ImageTk.PhotoImage(file="Laos.png")
tanzania_flag = ImageTk.PhotoImage(file="Tanzania.png")
benin_flag = ImageTk.PhotoImage(file="Benin.png")
togo_flag = ImageTk.PhotoImage(file="Togo.png")
ghana_flag = ImageTk.PhotoImage(file="Ghana.png")
mali_flag = ImageTk.PhotoImage(file="Mali.png")

# Global Variables
score = 0
total_questions = 9

# List for the country flags in easy mode
# Flag questions list
flags_list_easymode = [america_flag, south_africa_flag, switzerland_flag, turkey_flag, united_kingdom_flag,
                       south_korea_flag, japan_flag, france_flag, new_zealand_flag]
# Multiple choice answers list
options_easymode = [["Germany", "France", "Spain", "America"], ["Australia", "Russia", "South Africa", "Brazil"],
                    ["Ireland", "Switzerland", "Cambodia", "China"],
                    ["Thailand", "Indonesia", "Turkey", "Saudi Arabia"],
                    ["United Kingdom", "Australia", "New Zealand", "Norway"],
                    ["Greece", "Vietnam", "Japan", "South Korea"],
                    ["Cuba", "Japan", "Egypt", "China"], ["Egypt", "Iceland", "India", "France"],
                    ["Australia", "America", "New Zealand", "Austria"]]
# Correct answers list
correct_answers_easymode = ["America", "South Africa", "Switzerland", "Turkey", "United Kingdom", "South Korea",
                            "Japan", "France", "New Zealand"]

# List for the country flags in hard mode
# Flag questions list
flags_list_hardmode = [jamaica_flag, romania_flag, azerbaijan_flag, laos_flag, tanzania_flag, benin_flag, togo_flag,
                       ghana_flag, mali_flag]
# Answers list
correct_answers_hardmode = ["Jamaica", "Romania", "Azerbaijan", "Laos", "Tanzania", "Benin", "Togo", "Ghana", "Mali"]

Q_number = 0

# Welcome Screen
def welcome_screen():
    welcome_label = tk.Label(root, text="Welcome to Justin's Quiz Game!", font=("Helvetica", 22, "bold"),
                             bg="#A4D2CF")  # Sets the background color of the label and makes the text bold
    welcome_label.place(x=300, y=100, anchor="center")  # Sets the x and y position of the label in the welcome screen

    # Help window
    def open_help_window():
        # Opens new window with same geometry
        help_window = tk.Toplevel(root)
        help_window.title("How To Play Justin’s Quiz Game")
        help_window.geometry("600x650")
        help_window.configure(bg="#A4D2CF")

        title_label = tk.Label(help_window, text="How To Play Justin’s Quiz Game", font=("Helvetica", 16, "bold"),
                               bg="#A4D2CF", fg="#000000")
        title_label.pack(pady=10)

        info_frame = tk.Frame(help_window, bg="#1CB9F6", bd=2, relief=tk.SOLID)
        info_frame.pack(pady=10, padx=20)

        info_label = tk.Label(info_frame, text="Hello, Player!\n\n"
                                               "• This Quiz program was created by Justin Park\n\n"
                                               "• In this quiz game, a set of questions will show up for you to answer\n\n"
                                               "• You will have the choice to either play easy mode\n or hard mode depending on your knowledge of country flags.\n\n"
                                               "• In Easy Mode, you will be given multiple choice questions.\n\n"
                                               "• In Hard mode, you must type in the answer and you will be given no hints\n\n"
                                               "• To play the quiz game, choose the correct country flag\n"
                                               "which is shown in the centre of the screen.\n",
                              font=("Helvetica", 12), bg="#1CB9F6", fg="#000000")
        info_label.pack(padx=10, pady=10)

        close_label = tk.Label(help_window, text="You may close this when you are ready to play!",
                               font=("Helvetica", 12), bg="#A4D2CF", fg="#000000")
        close_label.pack(pady=10)

    # Help icon Button
    help_icon_button = tk.Button(root, image=help_icon, bg="#A4D2CF", relief=tk.FLAT, command=open_help_window)
    help_icon_button.place(x=10, y=10)
    # Hover effect of the help button
    help_icon_button.bind("<Enter>", lambda event: help_icon_button.config(image=help_iconv2))
    help_icon_button.bind("<Leave>", lambda event: help_icon_button.config(image=help_icon))

    # Quiz logo
    quiz_logo = tk.Label(root, image=logo, bg="#A4D2CF")  # Image of quiz logo
    quiz_logo.place(x=146, y=170)  # Centres the logo

    # Play button
    play_button = tk.Button(root, text="PLAY", font=("Helvetica", 16, "bold"), bg="#1CB9F6", fg="#000000",
                            command=rules_screen, relief=tk.SOLID, bd=2,
                            cursor="hand2")  # Sets the background color, text color, and font for the play button
    play_button.place(x=200, y=550, width=200,
                      height=50)  # Sets the x and y position of the play button in the welcome screen

# Rules Screen
def rules_screen():
    clear_screen()  # Clears the screen

    rules_frame = tk.Frame(root, bg="#A4D2CF")  # Create the frame for the rules screen with the background color
    rules_frame.pack(fill=tk.BOTH, expand=True)

    rules_label = tk.Label(rules_frame, text="Rules of the Quiz Game", font=("Helvetica", 18, "bold"), bg="#A4D2CF",
                           fg="#000000")  # Sets the background color of the rules label and makes the title text bold
    rules_label.pack(pady=10)

    rules_box = tk.Frame(rules_frame, bg="#1CB9F6", bd=2,
                         relief=tk.SOLID)  # Creates a frame for the rules box with a border
    rules_box.pack(pady=10, padx=20)

    rules_title = tk.Label(rules_box, text="Hello, Player", font=("Helvetica", 14, "bold"), bg="#1CB9F6", fg="#000000")
    rules_title.pack(pady=5)

    rules_content = tk.Label(rules_box,
                             text="• Do not cheat\n• Do not google the answers\n• Your answers will be recorded\n• Statistics of your quiz will be shown at the end\n• You will have the option to export your statistics to a text file\n• Have fun!",
                             font=("Helvetica", 14), bg="#1CB9F6", fg="#000000")  # Lists the rules of the quiz game
    rules_content.pack(padx=10, pady=5)

    # Help window
    def open_help_window():
        # Opens new window with same geometry
        help_window = tk.Toplevel(root)
        help_window.title("How To Play Justin’s Quiz Game")
        help_window.geometry("600x650")
        help_window.configure(bg="#A4D2CF")

        title_label = tk.Label(help_window, text="How To Play Justin’s Quiz Game", font=("Helvetica", 16, "bold"),
                               bg="#A4D2CF", fg="#000000")
        title_label.pack(pady=10)

        info_frame = tk.Frame(help_window, bg="#1CB9F6", bd=2, relief=tk.SOLID)
        info_frame.pack(pady=10, padx=20)

        info_label = tk.Label(info_frame, text="Hello, Player!\n\n"
                                               "• This Quiz program was created by Justin Park\n\n"
                                               "• In this quiz game, a set of questions will show up for you to answer\n\n"
                                               "• You will have the choice to either play easy mode\n or hard mode depending on your knowledge of country flags.\n\n"
                                               "• In Easy Mode, you will be given multiple choice questions.\n\n"
                                               "• In Hard mode, you must type in the answer and you will be given no hints\n\n"
                                               "• To play the quiz game, choose the correct country flag\n"
                                               "which is shown in the centre of the screen.\n",
                              font=("Helvetica", 12), bg="#1CB9F6", fg="#000000")
        info_label.pack(padx=10, pady=10)

        close_label = tk.Label(help_window, text="You may close this when you are ready to play!",
                               font=("Helvetica", 12), bg="#A4D2CF", fg="#000000")
        close_label.pack(pady=10)

    # Help Icon Button
    help_icon_button = tk.Button(root, image=help_icon, bg="#A4D2CF", relief=tk.FLAT, command=open_help_window)
    help_icon_button.place(x=10, y=10)
    # Hover effect of help button
    help_icon_button.bind("<Enter>", lambda event: help_icon_button.config(image=help_iconv2))
    help_icon_button.bind("<Leave>", lambda event: help_icon_button.config(image=help_icon))

    guide_label = tk.Label(rules_frame, text="Quiz Modes", font=("Helvetica", 18, "bold"), bg="#A4D2CF",
                           fg="#000000")  # Creates the label for the game modes guide
    guide_label.pack(pady=10)

    guide_box = tk.Frame(rules_frame, bg="#1CB9F6", bd=2,
                         relief=tk.SOLID)  # Creates a frame for the game modes guide box with a black border
    guide_box.pack(pady=10, padx=20)

    guide_text = tk.Label(guide_box,
                          text="You will have the choice to \nplay between two different quiz game modes",
                          font=("Helvetica", 14, "bold"), bg="#1CB9F6", fg="#000000")  # Title of the game modes guide
    guide_text.pack(padx=10, pady=5)

    easy_mode_label = tk.Label(guide_box, text="⋆ EASY MODE: \n• Multiple choice answers for the quiz.",
                               font=("Helvetica", 14, "bold"), bg="#1CB9F6", fg="green")  # Easy mode description
    easy_mode_label.pack(padx=10, pady=5)

    hard_mode_label = tk.Label(guide_box,
                               text="⋆ HARD MODE: \n• Type in the name of the country in the textbox. \n• 10-second time limit for each question.",
                               font=("Helvetica", 14, "bold"), bg="#1CB9F6", fg="red")  # Hard mode description
    hard_mode_label.pack(padx=10, pady=5)

    ok_button = tk.Button(rules_frame, text="Okay", font=("Helvetica", 16, "bold"), bg="#1CB9F6", fg="#000000",
                          relief=tk.SOLID, bd=2, padx=10, pady=5,
                          command=game_screen)  # Goes to game screen when the button is clicked
    ok_button.pack(pady=20)


# Game Screen
def game_screen():
    clear_screen()

    # Easy mode
    easy_button = tk.Button(root, text="Easy", command=easy_mode, font=("Helvetica", 20, "bold"), bg="#A4D2CF",
                            fg="#000000", relief=tk.RAISED, bd=2, padx=20, pady=10, cursor="hand2")
    easy_button.config(image=easy)  # Set the initial image
    easy_button.bind("<Enter>", lambda event: easy_button.config(image=easyv2))  # Change image on mouse enter
    easy_button.bind("<Leave>",
                     lambda event: easy_button.config(image=easy))  # Change back to original image on mouse leave
    easy_button.pack(fill=tk.BOTH, expand=True)

    # Hard mode
    hard_button = tk.Button(root, text="Hard", command=hard_mode, font=("Helvetica", 20, "bold"), bg="#A4D2CF",
                            fg="#000000", relief=tk.RAISED, bd=2, padx=20, pady=10, cursor="hand2")
    hard_button.config(image=hard)  # Set the initial image
    hard_button.bind("<Enter>", lambda event: hard_button.config(image=hardv2))  # Change image on mouse enter
    hard_button.bind("<Leave>",
                     lambda event: hard_button.config(image=hard))  # Change back to original image on mouse leave
    hard_button.pack(fill=tk.BOTH, expand=True)

# Go to the next question
def next_question():
    global Q_number
    children_list = []
    for each_children in root.winfo_children():
        children_list.append(each_children)
    deleting_frame = children_list[2]
    deleting_frame.destroy()

    if Q_number < len(flags_list_easymode):
        EasyQuestions(flags_list_easymode[Q_number], options_easymode[Q_number][0], options_easymode[Q_number][1],
                      options_easymode[Q_number][2],
                      options_easymode[Q_number][3], correct_answers_easymode[Q_number])
        Q_number += 1
    else:
        # Congratulations screen
        clear_screen()
        congratulations_screen(time_taken)

# Saving data to a text file
def export_data():
    num_correct_answers = score
    accuracy_percentage = int((num_correct_answers / total_questions) * 100)
    print("Your statistics have been successfully exported as a text file to your designated file location!")
    # Creates a text file to the file path put here
    file_path = "C:/Users/justin.park/Downloads/Quiz Game Statistics.txt" # Change this to where you want your file to be downloaded
    with open(file_path, "w") as file:
        file.write("Congratulations on finishing my quiz game!\n")
        file.write("You took " + str(time_taken) + " to finish the quiz!\n")
        file.write("You got " + str(num_correct_answers) + " questions correct!\n")
        file.write("You scored a " + str(accuracy_percentage) + "% accuracy!\n\n")
        file.write("-----Here are the Answers of the quiz:-----\n\n")
        file.write("* Easy Mode *\n")
        file.write("1. Canada\n")
        file.write("2. America\n")
        file.write("3. South Africa\n")
        file.write("4. Switzerland\n")
        file.write("5. Turkey\n")
        file.write("6. United Kingdom\n")
        file.write("7. South Korea\n")
        file.write("8. Japan\n")
        file.write("9. France\n")
        file.write("10. New Zealand\n\n")
        file.write("* Hard Mode *\n")
        file.write("1. Sweden\n")
        file.write("2. Jamaica\n")
        file.write("3. Romania\n")
        file.write("4. Azerbaijan\n")
        file.write("5. Laos\n")
        file.write("6. Tanzania\n")
        file.write("7. Benin\n")
        file.write("8. Togo\n")
        file.write("9. Ghana\n")
        file.write("10. Mali\n")

# Congratulations screen
def congratulations_screen(time_set):
    clear_screen()
    root.configure(bg="#FFFF00")  # Change background color to yellow

    congratulations_label = tk.Label(root, text="CONGRATULATIONS!", font=("Helvetica", 22, "bold"),
                                     bg="#FFFF00", fg="#000000")
    congratulations_label.place(x=300, y=100, anchor="center")

    confetti_label = tk.Label(root, image=confetti, bg="#FFFF00")
    confetti_label.place(x=0, y=650, relwidth=0.5, anchor="sw")

    confetti2_label = tk.Label(root, image=confettiv2, bg="#FFFF00")
    confetti2_label.place(x=600, y=650, relwidth=0.5, anchor="se")

    # Create a colored frame
    frame = tk.Frame(root, bg="#1CB9F6", bd=2, relief=tk.SOLID)
    frame.place(x=100, y=150, width=400, height=200)

    # Calculate time taken
    time_taken = time_set

    # Calculate score and accuracy percentage
    num_correct_answers = score
    accuracy_percentage = int((num_correct_answers / total_questions) * 100)

    # Label containing the statistics
    content_label = tk.Label(frame, text=f"Congratulations on completing the quiz!\n"
                                         f"You took {time_taken} to finish the quiz!\n"
                                         f"You got {num_correct_answers}/{total_questions} questions correct!\n"
                                         f"You scored a {accuracy_percentage}% accuracy!",
                             font=("Helvetica", 16), bg="#1CB9F6", fg="#000000")
    content_label.pack(pady=20)

    # Exports the statistics to a text file 
    export_button = tk.Button(frame, text="Export Statistics", font=("Helvetica", 14), bg="#A4D2CF", fg="#000000",
                              relief=tk.SOLID, bd=2, padx=10, pady=5, command=export_data)
    export_button.pack()


# Creating the questions using classes for easy mode
class EasyQuestions:

    # Checks the answer and says if its correct or incorrect
    def checker(self, answer, selected_button):
        global score
        if selected_button['text'] == answer:
            selected_button.configure(bg="green")  # Highlight the selected button in green
            correct_answer_label = tk.Label(self.question_ans_frame, text="Correct!", font=("Helvetica", 16),
                                            bg="#A4D2CF", fg="green")
            correct_answer_label.pack(pady=10)
            self.option_four['state'] = "disabled" # Disable the answer button after user has clicked an answer
            self.option_three['state'] = "disabled"
            self.option_two['state'] = "disabled"
            self.option_one['state'] = "disabled"
            self.arrow_button['state'] = 'normal' # Enable the arrow_button
            score +=1
        else:
            selected_button.configure(bg="red")  # Highlight the selected button in red
            incorrect_answer_label = tk.Label(self.question_ans_frame, text="Incorrect!", font=("Helvetica", 16),
                                              bg="#A4D2CF", fg="red")
            incorrect_answer_label.pack(pady=10)
            self.option_four['state'] = "disabled" # Disable the answer button after user has clicked an answer
            self.option_three['state'] = "disabled"
            self.option_two['state'] = "disabled"
            self.option_one['state'] = "disabled"
            self.arrow_button['state'] = 'normal' # Enable the arrow_button

    def __init__(self, flag1, option_one, option_two, option_three, option_four, correct_answer, master=root,
                 question="What flag is this?", arrow=arrow):
        self.width_frame = '600'
        self.bg_frame = "#A4D2CF"
        self.question = question
        self.flag1 = flag1
        self.option_one = option_one
        self.option_two = option_two
        self.option_three = option_three
        self.option_four = option_four
        self.correct_answer = correct_answer  # Set the correct answer for the question

        self.question_ans_frame = tk.Frame(master, width=self.width_frame, bg='#A4D2CF', height="640")
        self.question_ans_frame.pack()

        self.question_frame = tk.Frame(self.question_ans_frame, bg="#1CB9F6", padx=10, pady=10, borderwidth=2,
                                       relief=tk.SOLID, bd=2)
        self.question_frame.pack(pady=10)

        self.question_label = tk.Label(self.question_frame, text=self.question, font=("Helvetica", 22, "bold"),
                                       bg="#1CB9F6", fg="#000000", width=15)
        self.question_label.pack(padx=100)

        # Sets the flag image in centre
        self.flag_image = tk.Label(self.question_ans_frame, image=self.flag1, background=self.bg_frame)
        self.flag_image.pack(pady=(10, 20))

        # Arrow button
        self.arrow_button = tk.Button(self.question_ans_frame, image=arrow, bg="#A4D2CF", relief=tk.FLAT,
                                      command=next_question,
                                      state='disabled')  # Set the image and add command for the button
        self.arrow_button.place(x=450, y=170)  # Adjust the coordinates according to your desired position
        self.arrow_button.bind("<Enter>",
                               lambda event: self.arrow_button.config(image=arrowv2))  # Change image on mouse enter
        self.arrow_button.bind("<Leave>", lambda event: self.arrow_button.config(
            image=arrow))  # Change back to original image on mouse leave

        # Multiple choice answers
        self.options_frame_one = tk.Frame(self.question_ans_frame, background=self.bg_frame)
        self.options_frame_one.pack(pady=(0, 20))

        self.option_one = tk.Button(self.options_frame_one, text=self.option_one, font=("Helvetica", 22, "bold"),
                                    bg="#1CB9F6", fg="#000000", width=13,
                                    command=lambda: self.checker(self.correct_answer,
                                                                 self.option_one))  # Pass the button as an argument
        self.option_one.pack(side='left', padx=(50, 10), ipady=1)

        self.option_two = tk.Button(self.options_frame_one, text=self.option_two, font=("Helvetica", 22, "bold"),
                                    bg="#1CB9F6", fg="#000000", width=13,
                                    command=lambda: self.checker(self.correct_answer, self.option_two))
        self.option_two.pack(side='left', padx=(10, 50), ipady=1)

        self.options_frame_two = tk.Frame(self.question_ans_frame, background=self.bg_frame)
        self.options_frame_two.pack()

        self.option_three = tk.Button(self.options_frame_two, text=self.option_three, font=("Helvetica", 22, "bold"),
                                      bg="#1CB9F6", fg="#000000", width=13,
                                      command=lambda: self.checker(self.correct_answer, self.option_three))
        self.option_three.pack(side='left', padx=(50, 10), ipady=1)

        self.option_four = tk.Button(self.options_frame_two, text=self.option_four, font=("Helvetica", 22, "bold"),
                                     bg="#1CB9F6", fg="#000000", width=13,
                                     command=lambda: self.checker(self.correct_answer, self.option_four))
        self.option_four.pack(side='left', padx=(10, 50), ipady=1)

        # From here, this code makes the options the same in width, as they are not from the start
        self.option_one.update()
        self.option_two.update()
        self.option_three.update()
        self.option_four.update()

        self.option_one_width = self.option_one.winfo_width()
        self.option_two_width = self.option_two.winfo_width()
        self.option_three_width = self.option_three.winfo_width()
        self.option_four_width = self.option_four.winfo_width()

        self.biggest_options_width = [self.option_one_width, self.option_two_width, self.option_three_width,
                                      self.option_four_width]

        self.biggest_width_found = max(self.biggest_options_width)
        self.turn_width_into_pixel = str(int(self.biggest_width_found / 18))

        self.option_one.configure(width=self.turn_width_into_pixel)
        self.option_two.configure(width=self.turn_width_into_pixel)
        self.option_three.configure(width=self.turn_width_into_pixel)
        self.option_four.configure(width=self.turn_width_into_pixel)

# Creating the questions using classes for hard mode
hard_Q_number = 0
class HardQuestions:
    def __init__(self, flag1, correct_answer, question="What flag is this?", arrow=arrow, master=root):
        self.width_frame = '600'
        self.bg_frame = "#A4D2CF"
        self.question = question
        self.flag1 = flag1
        self.correct_answer = correct_answer  # Set the correct answer for the question

        self.question_ans_frame = tk.Frame(master, width=self.width_frame, bg='#A4D2CF', height="640")
        self.question_ans_frame.pack()

        self.question_frame = tk.Frame(self.question_ans_frame, bg="#1CB9F6", padx=15, pady=10, borderwidth=2,
                                       relief=tk.SOLID, bd=2)
        self.question_frame.pack(pady=10)

        self.question_label = tk.Label(self.question_frame, text=self.question, font=("Helvetica", 22, "bold"),
                                       bg="#1CB9F6", fg="#000000", width=15)
        self.question_label.pack(padx=100)

        # Sets the flag image in centre
        self.flag_image = tk.Label(self.question_ans_frame, image=self.flag1, background=self.bg_frame)
        self.flag_image.pack(pady=(10, 20))

        # Arrow button
        self.arrow_button = tk.Button(self.question_ans_frame, image=arrow, bg="#A4D2CF", relief=tk.FLAT,
                                      command=self.next_question, state='disabled')  # Set the image and add command for the button
        self.arrow_button.place(x=387, y=170)  # Adjust the coordinates according to your desired position
        self.arrow_button.bind("<Enter>",
                               lambda event: self.arrow_button.config(image=arrowv2))  # Change image on mouse enter
        self.arrow_button.bind("<Leave>", lambda event: self.arrow_button.config(
            image=arrow))  # Change back to original image on mouse leave

        # Text box to take in answers
        self.entry = tk.StringVar()
        self.text_entry = tk.Entry(self.question_ans_frame, textvariable=self.entry, font=("Helvetica", 16), width=35,
                                   bd=2, relief=tk.SOLID)
        self.text_entry.pack(pady=(10, 20))

        # Submit button to check answer
        self.submit_button = tk.Button(self.question_ans_frame, text="Submit Answer", font=("Helvetica", 24),
                                       bg="#1CB9F6", fg="#000000", command=self.check_in_process)
        self.submit_button.pack()

    # Checks the answer and says if its correct or incorrect
    def check_in_process(self):
        global write_some_label
        if len(self.entry.get()) > 0:
            self.check_answer()
        else:
            pass

    def check_answer(self):
        global score
        user_answer = self.text_entry.get().strip()  # Get the user's answer from the textbox

        # Check if the user's answer contains only alphabetic characters
        if user_answer.isalpha():
            if user_answer == self.correct_answer:
                self.text_entry.configure(bg="green", state='disabled', highlightbackground='green')
                correct_answer_label = tk.Label(self.question_ans_frame, text="Correct!", font=("Helvetica", 16),
                                                bg="#A4D2CF", fg="green")
                correct_answer_label.pack(pady=10)
                self.submit_button['state'] = "disabled"
                self.arrow_button['state'] = "normal"
                score += 1
            else:
                self.text_entry.configure(bg="red", state='disabled')
                incorrect_answer_label = tk.Label(self.question_ans_frame, text="Incorrect!", font=("Helvetica", 16),
                                                  bg="#A4D2CF", fg="red")
                incorrect_answer_label.pack(pady=10)
                self.submit_button['state'] = "disabled"
                self.arrow_button['state'] = "normal"
        else:
            # States that you can only enter in alphabetic characters
            invalid_answer_label = tk.Label(self.question_ans_frame,
                                            text="Invalid answer! Please enter only alphabetic characters.",
                                            font=("Helvetica", 16), bg="#A4D2CF", fg="red")
            invalid_answer_label.pack(pady=10)
            self.text_entry ['state'] = "disabled"
            self.submit_button['state'] = "disabled"
            self.arrow_button['state'] = "normal"

    # Goes to the next question
    def next_question(self):
        global hard_Q_number
        if self.text_entry['state'] == 'disabled':
            self.question_ans_frame.destroy()
            if hard_Q_number < len(flags_list_hardmode):
                HardQuestions(flags_list_hardmode[hard_Q_number], correct_answers_hardmode[hard_Q_number])
                hard_Q_number += 1
            else:
                # Congratulations screen
                clear_screen()
                congratulations_screen(time_taken)
        else:
            pass


# Easy Mode
def easy_mode():
    global total_questions
    total_questions += 1
    clear_screen()

    timer_label = tk.Label(root, text="0:00", font=("Helvetica", 24, "bold"), bg="#A4D2CF", fg="#000000")
    timer_label.pack(pady=10)

    title_frame = tk.Frame(root, bg="#1CB9F6", padx=10, pady=10, borderwidth=2, relief=tk.SOLID, bd=2)
    title_frame.pack(pady=10)

    title_label = tk.Label(title_frame, text="You are currently playing Easy Mode!", font=("Helvetica", 22, "bold"),
                           bg="#1CB9F6", fg="#000000")  # Title of easy mode
    title_label.pack()

    # The countdown timer
    countdown_text_label = tk.Label(root, text="Your game will start in...", font=("Helvetica", 32, "bold"),
                                    bg="#A4D2CF", fg="#000000")
    countdown_text_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    countdown_text_label.after(1000, lambda: countdown_text_label.config(text=""))  # Hides the text after 1 second

    countdown_label = tk.Label(root, text="", font=("Helvetica", 150, "bold"), bg="#A4D2CF", fg="#000000")
    countdown_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    root.update()  # Update the GUI to show the countdown labels

    # Starts the quiz after countdown finishes
    def start_countdown(i):
        if i < 0:
            countdown_label.destroy()
            title_frame.destroy()
            Q1 = EasyQuestions(canada_flag, "Canada", "India", "Japan", "China", "Canada")
        elif i > 0:
            countdown_label.config(text=str(i))  # Update the countdown text
            countdown_label.after(1000, start_countdown,
                                  i - 1)  # Call the function again after 1 second with the next number
        elif i == 0:
            countdown_label.config(text="GO!", fg="green")  # Display "GO!" when the countdown finishes
            countdown_label.config(font=("Helvetica", 144, "bold"))  # Change the countdown font
            start_game(countdown_label, timer_label)  # Start the game
            countdown_label.after(1000, start_countdown,
                                  i - 1)  # Call the function again after 1 second with the next number

    countdown_text_label.after(1000, start_countdown, 3)  # Start the countdown after 1 second


# Hard Mode
def hard_mode():
    global total_questions
    total_questions += 1
    clear_screen()

    timer_label = tk.Label(root, text="0:00", font=("Helvetica", 24, "bold"), bg="#A4D2CF", fg="#000000")
    timer_label.pack(pady=10)

    title_frame = tk.Frame(root, bg="#1CB9F6", padx=10, pady=10, borderwidth=2, relief=tk.SOLID, bd=2)
    title_frame.pack(pady=10)

    title_label = tk.Label(title_frame, text="You are currently playing Hard Mode!", font=("Helvetica", 22, "bold"),
                           bg="#1CB9F6", fg="#000000")
    title_label.pack()

    # The countdown timer
    countdown_text_label = tk.Label(root, text="Your game will start in...", font=("Helvetica", 32, "bold"),
                                    bg="#A4D2CF", fg="#000000")
    countdown_text_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    countdown_text_label.after(1000, lambda: countdown_text_label.config(text=""))  # Hides the text after 1 second

    countdown_label = tk.Label(root, text="", font=("Helvetica", 150, "bold"), bg="#A4D2CF", fg="#000000")
    countdown_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    root.update()  # Update the GUI to show the countdown labels

    # Starts the quiz after countdown finishes
    def start_countdown(i):
        if i < 0:
            countdown_label.destroy()
            title_frame.destroy()
            Q1 = HardQuestions(sweden_flag, 'Sweden')
        elif i > 0:
            countdown_label.config(text=str(i))  # Update the countdown text
            countdown_label.after(1000, start_countdown,
                                  i - 1)  # Call the function again after 1 second with the next number
        elif i == 0:
            countdown_label.config(text="GO!", fg="green")  # Display "GO!" when the countdown finishes
            countdown_label.config(font=("Helvetica", 144, "bold"))  # Change the countdown font
            start_game(countdown_label, timer_label)  # Start the game
            countdown_label.after(1000, start_countdown,
                                  i - 1)  # Call the function again after 1 second with the next number

    countdown_text_label.after(1000, start_countdown, 3)  # Start the countdown after 1 second


# Starts the quiz game
def start_game(countdown_label, timer_label):
    seconds = 0
    update_timer(timer_label, seconds)  # Start the timer at 0 seconds


# Update the timer label
def update_timer(timer_label, seconds):
    global time_taken
    minutes = seconds // 60
    seconds_remaining = seconds % 60
    timer_label.config(text=f"{minutes}:{seconds_remaining:02d}")
    time_taken = f"{minutes}:{seconds_remaining:02d}"
    seconds += 1
    timer_label.after(1000, update_timer, timer_label, seconds)  # Update the timer after 1 second

# Clears the screen
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# Wrong Answer
def wrong_answer():
    clear_screen()  # Clear the screen
    score_label = tk.Label(root, text="Incorrect!", font=("Helvetica", 16))
    score_label.pack()

# Correct Answer
def correct_answer():
    global score
    score += 1
    clear_screen()  # Clear the screen
    score_label = tk.Label(root, text="Correct!", font=("Helvetica", 16))
    score_label.pack()

# Run the quiz game
welcome_screen()
root.mainloop()
