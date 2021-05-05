import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        # windowの初期設定を行う。
        super().__init__(master)

        # windowの画面サイズを設定する。
        self.master.geometry("300x200")

        # window内にframeを作成する。
        frame1 = tk.Frame(self.master)
        # frame1内にラベル1を作成する。
        label1 = tk.Label(frame1, text="1",
                          width=30, height=15, bg="orchid4")
        # frame1内にラベル2を作成する。
        label2 = tk.Label(frame1, text="2",
                          width=30, height=15, bg="dark turquoise")
        # frame1内にラベル3を作成する。
        label3 = tk.Label(frame1, text="3",
                          width=30, height=15, bg="MidnightBlue")
        # ラベルをフレームに配置
        label1.grid()
        label2.grid()
        label3.grid()
        # window上に配置
        frame1.grid()


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # windowをループさせて、継続的にwindow表示させる。
    app.mainloop()
