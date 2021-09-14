class RubikCube:

    TOP = 0
    BOTTOM = 1
    FRONT = 2
    RIGHT = 3
    REAR = 4
    LEFT = 5

    CLOCKWISE = 0
    COUNTERCLOCKWISE = 1

    FACE = {TOP: 'top', BOTTOM: 'bottun', FRONT: 'front', RIGHT: 'right', REAR: 'rear', LEFT: 'left'}
    DIRECTION = {CLOCKWISE: 'clockwise', COUNTERCLOCKWISE: 'counterclockwise'}

    RED = 0
    ORANGE = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4
    WHITE = 5
    GOAL = [[[0,0,0],[0,0,0],[0,0,0]], \
            [[1,1,1],[1,1,1],[1,1,1]], \
            [[2,2,2],[2,2,2],[2,2,2]], \
            [[3,3,3],[3,3,3],[3,3,3]], \
            [[4,4,4],[4,4,4],[4,4,4]], \
            [[5,5,5],[5,5,5],[5,5,5]]]
    
    ACTIONS = [(RubikCube.TOP, RubikCube.CLOCKWISE), (RubikCube.TOP, RubikCube.COUNTERCLOCKWISE), \
    (RubikCube.BOTTOM, RubikCube.CLOCKWISE), (RubikCube.BOTTOM, RubikCube.COUNTERCLOCKWISE), \
    (RubikCube.FRONT, RubikCube.CLOCKWISE), (RubikCube.FRONT, RubikCube.COUNTERCLOCKWISE), \
    (RubikCube.REAR, RubikCube.CLOCKWISE), (RubikCube.REAR, RubikCube.COUNTERCLOCKWISE), \
    (RubikCube.LEFT, RubikCube.CLOCKWISE), (RubikCube.LEFT, RubikCube.COUNTERCLOCKWISE), \
    (RubikCube.RIGHT, RubikCube.CLOCKWISE), (RubikCube.RIGHT, RubikCube.COUNTERCLOCKWISE)]
    
    def __init__(self, initial_cube=GOAL):
        self.cube = initial_cube

    # self.cube[i][j][k] denotes the square at the ith face, j row and k column.
    def __eq__(self, other):
        for i in range(6):
            for j in range(N_layer):
                for k in range(N_layer):
                    if not self.cube[i][j][k] == other.cube[i][j][k]:
                        return False
        return True

    def __str__(self):
        return str(self.cube)

    def __hash__(self):
        return (self.__str__()).__hash__()

    def deep_copy(self):
        # Performs an appropriately deep copy of a state,
        # for use by operators in creating new states.
        cube_copy = []
        for i in range(6):
            row = []
            for j in range(3):
                col = []
                for k in range(3):
                    col.append(self.cube[i][j][k])
                row.append(col)
            cube_copy.append(row)
        return RubikCube(cube_copy)

    def step(self, action):
        face, direction = action
        new_state = self.deep_copy()  # start with a deep copy.
        # move the upper face in clockwise direction
        if face == self.TOP and direction == self.CLOCKWISE:   
            temp = new_state.cube[self.LEFT][0]
            new_state.cube[self.LEFT][0] = new_state.cube[self.FRONT][0]
            new_state.cube[self.FRONT][0] = new_state.cube[self.RIGHT][0]
            new_state.cube[self.RIGHT][0] = new_state.cube[self.REAR][0]
            new_state.cube[self.REAR][0] = temp
            new_state.move_clockwise(self.TOP)

        # move the upper face in counter-clockwise direction
        if face == self.TOP and direction == self.COUNTERCLOCKWISE:
            temp = new_state.cube[self.LEFT][0]
            new_state.cube[self.LEFT][0] = new_state.cube[self.REAR][0]
            new_state.cube[self.REAR][0] = new_state.cube[self.RIGHT][0]
            new_state.cube[self.RIGHT][0] = new_state.cube[self.FRONT][0]
            new_state.cube[self.FRONT][0] = temp
            new_state.move_counter_clockwise(self.TOP)

        # move the down face in clockwise direction
        if face == self.BOTTOM and direction == self.CLOCKWISE:
            temp = new_state.cube[self.LEFT][2]
            new_state.cube[self.LEFT][2] = new_state.cube[self.REAR][2]
            new_state.cube[self.REAR][2] = new_state.cube[self.RIGHT][2]
            new_state.cube[self.RIGHT][2] = new_state.cube[self.FRONT][2]
            new_state.cube[self.FRONT][2] = temp
            new_state.move_clockwise(self.BOTTOM)

        # move the down face in counter-clockwise direction
        if face == self.BOTTOM and direction == self.COUNTERCLOCKWISE:
            temp = new_state.cube[self.LEFT][2]
            new_state.cube[self.LEFT][2] = new_state.cube[self.FRONT][2]
            new_state.cube[self.FRONT][2] = new_state.cube[self.RIGHT][2]
            new_state.cube[self.RIGHT][2] = new_state.cube[self.REAR][2]
            new_state.cube[self.REAR][2] = temp
            new_state.move_counter_clockwise(self.BOTTOM)

        # move the front face in clockwise direction
        if face == self.FRONT and direction == self.CLOCKWISE:
            for i in range(3):
                temp = new_state.cube[self.TOP][2][i]
                new_state.cube[self.TOP][2][i] = new_state.cube[self.LEFT][2 - i][2]
                new_state.cube[self.LEFT][2 - i][2] = new_state.cube[self.BOTTOM][0][2 - i]
                new_state.cube[self.BOTTOM][0][2 - i] = new_state.cube[self.RIGHT][i][0]
                new_state.cube[self.RIGHT][i][0] = temp
            new_state.move_clockwise(self.FRONT)

        # move the front face in counter-clockwise direction
        if face == self.FRONT and direction == self.COUNTERCLOCKWISE:
            for i in range(3):
                temp = new_state.cube[self.TOP][2][i]
                new_state.cube[self.TOP][2][i] = new_state.cube[self.RIGHT][i][0]
                new_state.cube[self.RIGHT][i][0] = new_state.cube[self.BOTTOM][0][2 - i]
                new_state.cube[self.BOTTOM][0][2 - i] = new_state.cube[self.LEFT][2 - i][2]
                new_state.cube[self.LEFT][2 - i][2] = temp
            new_state.move_counter_clockwise(self.FRONT)

        # move the back face in clockwise direction
        if face == self.REAR and direction == self.CLOCKWISE:
            for i in range(3):
                temp = new_state.cube[self.TOP][0][i]
                new_state.cube[self.TOP][0][i] = new_state.cube[self.RIGHT][i][2]
                new_state.cube[self.RIGHT][i][2] = new_state.cube[self.BOTTOM][2][2 - i]
                new_state.cube[self.BOTTOM][2][2 - i] = new_state.cube[self.LEFT][0][2 - i]
                new_state.cube[self.LEFT][0][2 - i] = temp
            new_state.move_clockwise(self.REAR)

        # move the back face in counter-clockwise direction
        if face == self.REAR and direction == self.COUNTERCLOCKWISE:
            for i in range(3):
                temp = new_state.cube[self.TOP][0][i]
                new_state.cube[self.TOP][0][i] = new_state.cube[self.LEFT][0][2 - i]
                new_state.cube[self.LEFT][0][2 - i] = new_state.cube[self.BOTTOM][2][2 - i]
                new_state.cube[self.BOTTOM][2][2 - i] = new_state.cube[self.RIGHT][i][2]
                new_state.cube[self.RIGHT][i][2] = temp
            new_state.move_counter_clockwise(self.REAR)

        # move the left face in clockwise direction
        if face == self.LEFT and direction == self.CLOCKWISE:
            for i in range(3):
                temp = new_state.cube[self.FRONT][0][i]
                new_state.cube[self.FRONT][0][i] = new_state.cube[self.TOP][0][i]
                new_state.cube[self.TOP][0][i] = new_state.cube[self.REAR][2 - i][2]
                new_state.cube[self.REAR][2 - i][2] = new_state.cube[self.BOTTOM][0][i]
                new_state.cube[self.BOTTOM][0][i] = temp
            new_state.move_clockwise(self.LEFT)

        # move the left face in counter-clockwise direction
        if face == self.LEFT and direction == self.COUNTERCLOCKWISE:
            for i in range(3):
                temp = new_state.cube[self.FRONT][0][i]
                new_state.cube[self.FRONT][0][i] = new_state.cube[self.BOTTOM][0][i]
                new_state.cube[self.BOTTOM][0][i] = new_state.cube[self.REAR][2 - i][2]
                new_state.cube[self.REAR][2 - i][2] = new_state.cube[self.TOP][0][i]
                new_state.cube[self.TOP][0][i] = temp
            new_state.move_counter_clockwise(self.LEFT)

        # move the right face in clockwise direction
        if face == self.RIGHT and direction == self.CLOCKWISE:
            for i in range(3):
                temp = new_state.cube[self.FRONT][i][2]
                new_state.cube[self.FRONT][i][2] = new_state.cube[self.BOTTOM][i][2]
                new_state.cube[self.BOTTOM][i][2] = new_state.cube[self.REAR][2 - i][0]
                new_state.cube[self.REAR][2 - i][0] = new_state.cube[self.TOP][i][0]
                new_state.cube[self.TOP][i][0] = temp
            new_state.move_clockwise(self.RIGHT)

        # move the right face in counter-clockwise direction
        if face == self.RIGHT and direction == self.COUNTERCLOCKWISE:
            for i in range(3):
                temp = new_state.cube[self.FRONT][i][2]
                new_state.cube[self.FRONT][i][2] = new_state.cube[self.TOP][i][0]
                new_state.cube[self.TOP][i][0] = new_state.cube[self.REAR][2 - i][0]
                new_state.cube[self.REAR][2 - i][0] = new_state.cube[self.BOTTOM][i][2]
                new_state.cube[self.BOTTOM][i][2] = temp
            new_state.move_counter_clockwise(self.RIGHT)
        reward = 0
        if goal_test(new_state):
            reward = 1
        return new_state, reward  # return new state
    
    def move_clockwise(self, face):
        temp = self.cube[face][0][2]
        self.cube[face][0][2] = self.cube[face][0][0]
        self.cube[face][0][0] = self.cube[face][2][0]
        self.cube[face][2][0] = self.cube[face][2][2]
        self.cube[face][2][2] = temp

        temp = self.cube[face][0][1]
        self.cube[face][0][1] = self.cube[face][1][0]
        self.cube[face][1][0] = self.cube[face][2][1]
        self.cube[face][2][1] = self.cube[face][1][2]
        self.cube[face][1][2] = temp 

    def move_counter_clockwise(self, face):
        temp = self.cube[face][0][2]
        self.cube[face][0][2] = self.cube[face][2][2]
        self.cube[face][2][2] = self.cube[face][2][0]
        self.cube[face][2][0] = self.cube[face][0][0]
        self.cube[face][0][0] = temp

        temp = self.cube[face][0][1]
        self.cube[face][0][1] = self.cube[face][1][2]
        self.cube[face][1][2] = self.cube[face][2][1]
        self.cube[face][2][1] = self.cube[face][1][0]
        self.cube[face][1][0] = temp

    def goal_test(state):
        for i in range(6):
            color = state.cube[i][0][0]
            for j in range(3):
                for k in range(3):
                    if state.cube[i][j][k] != color: 
                        return False
        return True
    

