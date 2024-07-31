import tkinter as tk

# ウィンドウを作成
root = tk.Tk()
root.title("キーイベント検知アプリ")

# ラベルを作成して配置
label = tk.Label(root, text="ここにキーイベントが表示されます", font=("Helvetica", 16))
label.pack(pady=20)

def key_press(event):
    """
    キーが押されたときに呼ばれる関数
    event.char: 押されたキーの文字
    event.keysym: 押されたキーのシンボル名
    """
    label.config(text=f"キーが押されました: {event.keysym}")

def key_release(event):
    """
    キーが離されたときに呼ばれる関数
    event.char: 離されたキーの文字
    event.keysym: 離されたキーのシンボル名
    """
    label.config(text=f"キーが離されました: {event.keysym}")

# キーが押されたときのイベントをバインド
root.bind("<KeyPress>", key_press)

# キーが離されたときのイベントをバインド
root.bind("<KeyRelease>", key_release)

# メインループを開始
root.mainloop()
