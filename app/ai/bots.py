import random

class SnakeBot:
    def __init__(self, x=100, y=100):
        self.x = x
        self.y = y
        self.dx = 20
        self.dy = 0

    def move(self):
        move_choice = random.choice(['up', 'down', 'left', 'right'])
        if move_choice == 'up': self.dx, self.dy = 0, -20
        elif move_choice == 'down': self.dx, self.dy = 0, 20
        elif move_choice == 'left': self.dx, self.dy = -20, 0
        elif move_choice == 'right': self.dx, self.dy = 20, 0
        
        self.x += self.dx
        self.y += self.dy
        return {"x": self.x, "y": self.y}
