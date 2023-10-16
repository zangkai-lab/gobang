'''
Tkinter 是 Python 的标准 GUI（图形用户界面）库，用于创建桌面应用程序。它是 Tcl/Tk 的 Python 接口。因为它是 Python 的一部分，所以通常无需额外安装。Tkinter 提供了各种控件（widgets）如按钮、标签和文本框，用于构建应用程序。

优点：

简单易用，适合初学者。
跨平台，可在 Windows、Linux 和 macOS 上运行。
缺点：

相较于其他更现代的 GUI 库，界面略显陈旧。
可定制性相对较低。
适用场景：快速原型开发、小型项目、教学目的。
'''

import tkinter as tk
from tkinter import messagebox

class GomokuBoard:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, bg='white', width=620, height=620)
        # 填充棋盘边缘
        self.canvas.pack(padx=10, pady=10)
        self.draw_board()
        self.canvas.bind("<Button-1>", self.place_piece)
        self.current_color = 'black'  # 初始棋子颜色为黑色
        self.grid = [['' for _ in range(16)] for _ in range(16)]  # 初始化棋盘状态

    def draw_board(self):
        for i in range(16):
            self.canvas.create_line(40 * i, 0, 40 * i, 600, width=1, fill='black')
            self.canvas.create_line(0, 40 * i, 600, 40 * i, width=1, fill='black')

    def place_piece(self, event):
        x, y = event.x, event.y

        # 确保找到最近的鼠标位置
        if (x % 40) > 20:
            x += 40
        if (y % 40) > 20:
            y += 40
        col = x // 40
        row = y // 40

        # 如果当前位置没有棋子
        if not self.grid[row][col]:
            self.canvas.create_oval(col * 40 - 15, row * 40 - 15, col * 40 + 15, row * 40 + 15, fill=self.current_color, outline='black')
            self.grid[row][col] = self.current_color

            if self.check_win(row, col):
                messagebox.showinfo("五子棋", "游戏结束！{}方胜利！".format(self.current_color))
                self.reset_game()
                return

            self.switch_color()

    # 判断游戏是否有人获胜
    def check_win(self, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            for i in range(1, 5):
                if 0 <= row + i * dy < 16 and 0 <= col + i * dx < 16 and self.grid[row + i * dy][col + i * dx] == self.current_color:
                    count += 1
                else:
                    break
            for i in range(1, 5):
                if 0 <= row - i * dy < 16 and 0 <= col - i * dx < 16 and self.grid[row - i * dy][col - i * dx] == self.current_color:
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False

    def reset_game(self):
        for i in range(16):
            for j in range(16):
                self.grid[i][j] = ''
        self.canvas.delete("all")
        self.draw_board()
        self.current_color = 'black'

    def switch_color(self):
        if self.current_color == 'black':
            self.current_color = 'white'
        else:
            self.current_color = 'black'

if __name__ == "__main__":
    root = tk.Tk()
    root.title("五子棋")
    board = GomokuBoard(root)
    root.mainloop()
