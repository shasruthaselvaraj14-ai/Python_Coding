import tkinter as tk
import random

# Window setup
window = tk.Tk()
window.title("Car Racing Game")

WIDTH = 400
HEIGHT = 600

# Canvas
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="gray")
canvas.pack()

# Player car
car = canvas.create_rectangle(180, 500, 220, 580, fill="blue")

# Enemy car
enemy = canvas.create_rectangle(180, 0, 220, 80, fill="red")

# Score
score = 0

# ---------------- CAR MOVEMENT ---------------- #

def move_left(event):
    pos = canvas.coords(car)

    if pos[0] > 0:
        canvas.move(car, -20, 0)

def move_right(event):
    pos = canvas.coords(car)

    if pos[2] < WIDTH:
        canvas.move(car, 20, 0)

window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

# ---------------- GAME LOOP ---------------- #

def game_loop():
    global score

    # Move enemy down
    canvas.move(enemy, 0, 10)

    enemy_pos = canvas.coords(enemy)
    car_pos = canvas.coords(car)

    # Reset enemy when it goes outside
    if enemy_pos[3] > HEIGHT:
        x = random.randint(50, 320)

        canvas.coords(enemy, x, 0, x + 40, 80)

        score += 1
        window.title(f"Car Racing Game - Score: {score}")

    # Collision detection
    if (
        car_pos[2] > enemy_pos[0] and
        car_pos[0] < enemy_pos[2] and
        car_pos[3] > enemy_pos[1] and
        car_pos[1] < enemy_pos[3]
    ):

        canvas.create_text(
            200,
            300,
            text="GAME OVER",
            fill="white",
            font=("Arial", 30, "bold")
        )

        return

    # Repeat loop
    window.after(50, game_loop)

# Start game
game_loop()

# Run window
window.mainloop()
