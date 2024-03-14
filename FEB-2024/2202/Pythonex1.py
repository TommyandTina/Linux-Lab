class Robot:
    def __init__(self, x_coordinate, y_coordinate, first_direction):
        self.x = x_coordinate
        self.y = y_coordinate
        self.direction = first_direction

    def head_to_right(self): #add self to change its parameter
        base_direction = ['N', 'E', 'S', 'W']
        new_index_of_direction_after_turn = (base_direction.index(self.direction)+1%4)
        self.direction = base_direction[new_index_of_direction_after_turn]
        """here we change the index so robot can change its direction"""
    
    def head_to_left(self): #add self to change its parameter
        base_direction = ['N', 'E', 'S', 'W']
        new_index_of_direction_after_turn = (base_direction.index(self.direction)-1%4)
        self.direction = base_direction[new_index_of_direction_after_turn]
        """same with above"""
    
    def advance(self): #go ahead
        match self.direction:
            case 'N':
                self.y += 1 #North in positive y-axis
            case 'E':
                self.x += 1
            case 'S':
                self.y -= 1
            case 'W':
                self.x -= 1
    
    def robot_follow_instruction(self, instructions):
        for action in instructions:
            try:
                if action == 'R':
                    self.head_to_right()
                elif action == 'L':
                    self.head_to_left()
                elif action == 'A':
                    self.advance()
                else:
                    print("Your instruction is invalid")
            except Exception:
                print(f"We have problem: {Exception}")

    def current_position(self):
        return self.x, self.y, self.direction

# example
myRobot = Robot(7, 3, 'N')

# Execute the instructions
myRobot.robot_follow_instruction('RAALAL')

# Print the final position of the robot
print(myRobot.current_position())




