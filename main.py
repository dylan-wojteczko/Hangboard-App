from app.gui import HangboardApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = HangboardApp(root)
    app.show_home()
    root.mainloop()

if __name__ == "__main__":
    main()
