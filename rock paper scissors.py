import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="indigo")
        self.canvas.pack()

        self.game_label = tk.Label(root, text="Rock Paper Scissors Game", font=("Sohne", 20), bg="gray")
        self.game_label.place(relx=0.5, rely=0.1, anchor="center")

        self.user_score = 0
        self.comp_score = 0

        self.score_label = tk.Label(root, text="", font=("Sohne", 14), bg="indigo")
        self.score_label.place(relx=0.5, rely=0.2, anchor="center")
        self.display_scores()

        self.buttons_frame = tk.Frame(root, bg="indigo")
        self.buttons_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.rock_button = tk.Button(self.buttons_frame, text="Rock", font=("Sohne", 12), command=lambda: self.make_choice("Rock"))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.buttons_frame, text="Paper", font=("Sohne", 12), command=lambda: self.make_choice("Paper"))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors", font=("Sohne", 12), command=lambda: self.make_choice("Scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.result_label = tk.Label(root, text="", font=("Sohne", 14), bg="indigo")
        self.result_label.place(relx=0.5, rely=0.7, anchor="center")

        self.quit_replay_frame = tk.Frame(root, bg="indigo")
        self.quit_replay_frame.place(relx=0.5, rely=0.9, anchor="center")

        self.quit_button = tk.Button(self.quit_replay_frame, text="Quit", font=("Sohne", 12), command=self.end_game)
        self.quit_button.pack(side="left", padx=10)

        self.replay_button = tk.Button(self.quit_replay_frame, text="Replay", font=("Sohne", 12), command=self.reset_game)
        self.replay_button.pack(side="right", padx=10)
        self.replay_button.config(state="disabled")

    def make_choice(self, choice):
        self.user_choice = choice
        self.play_game()

    def play_game(self):
        comp_choice = random.choice(["Rock", "Paper", "Scissors"])
        self.result_label.config(text=f"Computer's choice: {comp_choice}")
        result = self.get_result(self.user_choice, comp_choice)
        if result == "You Win!":
            self.user_score += 1
        elif result == "Computer Wins!":
            self.comp_score += 1
        self.display_scores()
        self.result_label.config(text=f"Computer's choice: {comp_choice}\n{result}")

    def get_result(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            return "It's a Draw"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
(user_choice == "Paper" and comp_choice == "Rock") or \
            (user_choice == "Scissors" and comp_choice == "Paper"):
            return "You Win!"
        else:
            return "Computer Wins!"

    def display_scores(self):
        self.score_label.config(text=f"Scores: User: {self.user_score}   Computer: {self.comp_score}")

    def end_game(self):
        self.result_label.config(text=f"Final Scores:\nUser: {self.user_score}   Computer: {self.comp_score}\n")
        if self.user_score > self.comp_score:
            winner = "You Win!"
        elif self.user_score < self.comp_score:
            winner = "Computer Wins!"
        else:
            winner = "It's a Draw!"
        self.result_label.config(text=f"Final Scores:\nUser: {self.user_score}   Computer: {self.comp_score}\n{winner}")
        self.replay_button.config(state="normal")
        self.disable_buttons()

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.result_label.config(text="")
        self.display_scores()
        self.replay_button.config(state="disabled")
        self.enable_buttons()

    def disable_buttons(self):
        self.rock_button.config(state="disabled")
        self.paper_button.config(state="disabled")
        self.scissors_button.config(state="disabled")

    def enable_buttons(self):
        self.rock_button.config(state="normal")
        self.paper_button.config(state="normal")
        self.scissors_button.config(state="normal")

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
