from random import choice


class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, walk_points=5000):
        """initializing all walk attributes"""
        self.walk_points = walk_points

        # since all walks start at (0, 0)
        self.x_axis = [0]
        self.y_axis = [0]

    def fill_walks(self):
        """a method to calculate all walks"""

        while len(self.x_axis) < self.walk_points:
            """setting a limit to the walk points"""

            # deciding which direction to go and what distance
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # preventing the code from returning zero movement
            if x_step == 0 and y_step == 0:
                continue

            x = self.x_axis[-1] + x_step
            y = self.y_axis[-1] + y_step

            self.x_axis.append(x)
            self.y_axis.append(y)
