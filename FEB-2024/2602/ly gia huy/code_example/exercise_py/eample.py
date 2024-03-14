class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.directions = ['north', 'east', 'south', 'west']

    def turn_right(self):
        dir_index = self.directions.index(self.direction)
        self.direction = self.directions[(dir_index + 1) % 4]

    def turn_left(self):
        dir_index = self.directions.index(self.direction)
        self.direction = self.directions[(dir_index - 1) % 4]

    def advance(self):
        if self.direction == 'north':
            self.y += 1
        elif self.direction == 'east':
            self.x += 1
        elif self.direction == 'south':
            self.y -= 1
        elif self.direction == 'west':
            self.x -= 1

    def move(self, instructions):
        try:
            for instruction in instructions:
                if instruction == 'R':
                    self.turn_right()
                elif instruction == 'A':
                    self.advance()
                elif instruction == 'L':
                    self.turn_left()
                else:
                    raise ValueError(f"Invalid instruction: '{instruction}'")
        except ValueError as error:
            print(f"An error occurred while processing the instructions: {error}")

    def __repr__(self):
        return f"Robot(position=({self.x}, {self.y}), direction='{self.direction}')"


# Example usage
try:
    # Instantiate the robot at position {7, 3} facing north
    robot = Robot(7, 3, 'north')

    # The instructions for the robot to move
    instructions = "RAALAL"

    # Move the robot based on the instructions
    robot.move(instructions)

    # Output the final position and direction of the robot
    print(robot)
except Exception as e:
    print(f"An error occurred: {e}")
