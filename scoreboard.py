from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # Attributes of the scoreboard class that determine how the score icon is visually presented on the turtle #
        self.color("white")
        self.score = 0
        with open("high_scores.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score = {self.score} // High Score = {self.high_score}", font=("Arial", 20, 'normal'), align="center")
        self.point()
        self.update_scoreboard()

    def point(self):
        # This function activates when the snake collides with the "food" object, giving you + 1 to your current score #
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score} // High Score = {self.high_score}", font=("Verdana", 20, 'normal'), align="center")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} // High Score = {self.high_score}", font=("Verdana", 20, 'normal'), align="center")


    def reset(self):
        # This function updates the high score
        if self.score > self.high_score:
            with open("high_scores.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()



