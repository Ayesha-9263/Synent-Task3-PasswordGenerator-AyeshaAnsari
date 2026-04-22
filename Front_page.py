import tkinter as tk

def type_writer(label, text, delay=70):
    def type_char(index=0):
        if index <= len(text):
            label.config(text=text[:index])
            label.after(delay, type_char, index+1)
    type_char()


def loading_bar(canvas, bar, root):
    width = 0

    def load():
        nonlocal width
        if width < 300:
            width += 5
            canvas.coords(bar, 0, 0, width, 20)
            root.after(50, load)
        else:
            start_btn.config(state="normal")

    load()


def launch_project():
    root.destroy()
    print("Project Started...")


# Window
root = tk.Tk()
root.title("Internship Project")
root.geometry("800x500")
root.configure(bg="#d14a24")

# Heading
heading = tk.Label(root, font=("Helvetica", 24, "bold"), fg="white", bg="#14e79a")
heading.pack(pady=20)
type_writer(heading, ">>> SYNENT TECHNOLOGIES <<<")

# Subheading
sub = tk.Label(root, font=("Arial", 14), fg="#38bdf8", bg="#0f172a")
sub.pack()
type_writer(sub, "Python Development Internship", 40)

# Frame (Card)
frame = tk.Frame(root, bg="#1e293b", bd=3, relief="ridge")
frame.pack(pady=30, padx=60, fill="both", expand=True)

# Info Labels (animated)
name_label = tk.Label(frame, font=("Arial", 12), fg="white", bg="#1e293b")
name_label.pack(pady=5)

project_label = tk.Label(frame, font=("Arial", 12), fg="white", bg="#1e293b")
project_label.pack(pady=5)

company_label = tk.Label(frame, font=("Arial", 12), fg="white", bg="#1e293b")
company_label.pack(pady=5)

type_writer(name_label, "Student Name  →  AYESHA   ANSARI")
type_writer(project_label, "Project  →TASK 3:- PASSWORD GENRATOR")
type_writer(company_label, "Company  →  Synent Technologies")

mode_label = tk.Label(frame, font=("Arial", 12), fg="white", bg="#1e293b")
mode_label.pack(pady=5)



# Loading Bar
canvas = tk.Canvas(root, width=300, height=20, bg="white")
canvas.pack(pady=20)
bar = canvas.create_rectangle(0, 0, 0, 20, fill="#38bdf8")

# Button
start_btn = tk.Button(
    root,
    text="Start Project",
    font=("Arial", 12, "bold"),
    bg="#22c55e",
    fg="white",
    state="disabled",
    command=launch_project
)
start_btn.pack(pady=20)

# Start animation
loading_bar(canvas, bar, root)

root.mainloop()