import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, balls):
        drawn_balls = []
        if balls > len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
        else:
            for i in range(balls):
                ball_index = random.randint(0, len(self.contents) - 1)
                drawn_balls.append(self.contents.pop(ball_index))
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for i in range(num_experiments):
        hat_copy = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        drawn_balls = hat_copy.draw(num_balls_drawn)

        match = True
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                match = False
                break

        if match:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability
