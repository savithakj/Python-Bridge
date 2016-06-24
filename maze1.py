import sys
sys.setrecursionlimit(5000)


class Maze(object):
    FLOOR = ' '
    WALLS = '*'
    PATH = '+'

    def __init__(self):
        self.cols = 0
        self.rows = 0
        self.maze = []

    def walk_forward(self, current_k, r, c):
        self.maze[r][c] = current_k
        next_k = current_k + 1
        # up
        if r > 1:
            up = self.maze[r - 1][c]
            if up != self.WALLS:
                if up == self.FLOOR or int(up) > current_k:
                    self.walk_forward(next_k, r - 1, c)
        # down
        if r < self.rows - 1:
            down = self.maze[r + 1][c]
            if down != self.WALLS:
                if down == self.FLOOR or int(down) > current_k:
                    self.walk_forward(next_k, r + 1, c)
        # left
        if c > 1:
            left = self.maze[r][c - 1]
            if left != self.WALLS:
                if left == self.FLOOR or int(left) > current_k:
                    self.walk_forward(next_k, r, c - 1)
        # right
        if c < self.cols - 1:
            right = self.maze[r][c + 1]
            if right != self.WALLS:
                if right == self.FLOOR or int(right) > current_k:
                    self.walk_forward(next_k, r, c + 1)

    def walk_backward(self, r, c):
        current_k = self.maze[r][c]
        if not isinstance(current_k, int):
            return False
        self.maze[r][c] = self.PATH

        up = self.maze[r - 1][c] if r > 0 else None
        down = self.maze[r + 1][c] if r < self.rows - 1 else None
        left = self.maze[r][c - 1] if c > 1 else None
        right = self.maze[r][c + 1] if c < self.cols else None

        passed = False
        if up and isinstance(up, int) and up == current_k - 1:
            self.walk_backward(r - 1, c)
            passed = True
        if down and isinstance(down, int) and down == current_k - 1:
            self.walk_backward(r + 1, c)
            passed = True
        if left and isinstance(left, int) and left == current_k - 1:
            self.walk_backward(r, c - 1)
            passed = True
        if right and isinstance(right, int) and right == current_k - 1:
            self.walk_backward(r, c + 1)

    def cleanup(self, cleanup_path=False):
        for r in range(0, self.rows):
            for c in range(0, self.cols):
                if isinstance(self.maze[r][c], int):
                    self.maze[r][c] = self.FLOOR
                if cleanup_path and self.maze[r][c] == self.PATH:
                    self.maze[r][c] = self.FLOOR

    def solve(self, start='up', show_path=True):
        # finding start and finish points
        upper = lower = None
        for c in range(0, self.cols):
            if self.maze[0][c] == self.FLOOR:
                upper = (0, c)
                break
        for c in range(0, self.cols):
            if self.maze[self.rows - 1][c] == self.FLOOR:
                lower = (self.rows - 1, c)
                break
        if start == 'up':
            start = upper
            finish = lower
        else:
            start = lower
            finish = upper

        self.cleanup(cleanup_path=True)
        self.walk_forward(1, start[0], start[1])
        length = self.maze[finish[0]][finish[1]]
        if not isinstance(length, int):
            length = 0
        if show_path:
            self.walk_backward(finish[0], finish[1])
            self.cleanup(cleanup_path=False)
        else:
            self.cleanup(cleanup_path=True)
        return length

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.writelines(str(self))

    def load_from_file(self, filename):
        self.maze = []
        with open(filename, 'r') as f:
            lines = f.readlines()
        for line in lines:
            row = []
            for c in line.strip():
                row.append(c)
            self.maze.append(row)
        self.rows = len(self.maze)
        self.cols = len(self.maze[0]) if self.rows > 0 else 0

    def get_maze(self):
        return copy(self.maze)

    def __str__(self):
        as_string = u''
        for row in self.maze:
            as_string += u''.join([str(s)[-1] for s in row]) + "\n"
        return as_string


maze = Maze()
maze.load_from_file(sys.argv[1])
maze.solve(show_path=True)
print(str(maze))