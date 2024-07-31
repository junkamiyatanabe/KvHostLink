import tkinter as tk

class KeyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("キー入力検知アプリ")
        
        self.keys = ["↑", "↓", "←", "→", "Z", "X", "C", "スペース"]
        self.key_map = {
            "Up": "↑",
            "Down": "↓",
            "Left": "←",
            "Right": "→",
            "z": "Z",
            "x": "X",
            "c": "C",
            "space": "スペース"
        }
        
        self.create_widgets()
        self.bind_keys()
        
    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # キーの表示（コントローラーのような配置）
        self.key_labels = {}
        positions = {
            "Up": (1, 1),
            "Down": (3, 1),gi 
            "Left": (2, 0),
            "Right": (2, 2),
            "z": (2, 4),
            "x": (2, 5),
            "c": (2, 6),
            "space": (4, 1),
        }

        for key, (r, c) in positions.items():
            label = tk.Label(self.frame, text=self.key_map[key], font=("Helvetica", 24), width=4, relief="raised", bg="lightgrey")
            label.grid(row=r, column=c, padx=10, pady=10)
            self.key_labels[key] = label

        # 現在押されているまたは離されたキーの表示
        self.current_key_label = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.current_key_label.pack(pady=20)

    def bind_keys(self):
        for key in self.key_map.keys():
            self.root.bind(f'<KeyPress-{key}>', self.on_key_press)
            self.root.bind(f'<KeyRelease-{key}>', self.on_key_release)

    def on_key_press(self, event):
        key = event.keysym
        if key in self.key_map:
            self.current_key_label.config(text=f"{self.key_map[key]} が押されました")
            self.key_labels[key].config(bg="yellow")  # 押されたときに背景色を変更

    def on_key_release(self, event):
        key = event.keysym
        if key in self.key_map:
            self.current_key_label.config(text=f"{self.key_map[key]} が離されました")
            self.key_labels[key].config(bg="lightgrey")  # 離されたときに背景色を元に戻す

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyApp(root)
    root.mainloop()
