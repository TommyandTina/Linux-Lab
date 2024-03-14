# 1. The robot has three possible movements: turn right, turn left, advance
# 2. Robots are placed on a hypothetical infinite grid, facing a particular direction (north, east, south, or west) at a set of {x,y} coordinates, e.g., {3,8}, with coordinates increasing to the north and east.
# 3. Send to robot a number of instructions then robot will move like instructions
# Example: The letter-string ""RAALAL"" means:
# * Turn right
# * Advance twice
# * Turn left
# * Advance once
# * Turn left yet again
# => Suppose that a robot starts at {7, 3} facing north. Then running this stream of instructions should leave it at {9, 4} facing west.
# 4. Using try and except blocks in source code"

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
        elif self.direction == 'south':
            self.y -= 1
        elif self.direction == 'east':
            self.x += 1
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
                    raise ValueError(f"Điều hướng không hợp lệ: '{instruction}'")
        except ValueError as error:
            print(f"Lỗi trong quá trình điều hướng: {error}")

    def __repr__(self):
        return f"Robot(position=({self.x}, {self.y}), direction='{self.direction}')"


# MAIN
try:
    str_input = input("Nhập lệnh gồm các ký tự 'A','R','L' để điều khiển robot (vd RAALAL):  ")
    # khởi tạo vị trí robot
    robot = Robot(7, 3, 'north')
    print("Robot trước điều hướng: ", robot)
    # Nhập lệnh điều hướng
    # instructions = "RAALAL"
    instructions = str_input
    # Vận hành theo lệnh
    robot.move(instructions)

    # Robot sau điều hướng
    print("Robot sau điều hướng: ", robot)
except Exception as e:
    print(f"Phát sinh lỗi trong quá trình vận hành: {e}")
