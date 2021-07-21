import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか？
        frame.grid()

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # height : 高さの設定
        # bg : 背景色の設定
        # 色について　: https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label1 = tk.Label(frame, text="label1", width=10, height=10, bg="red")

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # height : 高さの設定
        # bg : 背景色の設定
        # 色について　: https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label2 = tk.Label(frame, text="label2", width=10, height=10, bg="green")

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # height : 高さの設定
        # bg : 背景色の設定
        # 色について　: https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label3 = tk.Label(frame, text="labal3", width=10, height=10, bg="yellow")

        # frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか？
        label1.grid()
        # frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか？
        label2.grid()
        # frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか？
        label3.grid()

if __name__ == "__main__":
    # Windowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
