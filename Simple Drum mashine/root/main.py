import tkinter as tk

def main():
    # Create a window
    window = tk.Tk()
    window.title("Basic App")

    # Add widgets or functionality to the window
    label = tk.Label(window, text="Hello, World!")
    label.pack()

    # Run the application
    window.mainloop()

if __name__ == "__main__":
    main()