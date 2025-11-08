# 📝 To-Do List Application

A simple and efficient **to-do list desktop app** built in **Python**, designed to help you organize and track your daily tasks. The app supports adding, editing, deleting, and marking tasks as complete — and automatically saves your progress to a local JSON file so your tasks persist between sessions.

---

## 🚀 Features

- ✅ Add new tasks with optional due dates
- ✏️ Edit or delete existing tasks
- 🕓 Mark tasks as completed or pending
- 💾 Tasks are **saved automatically** in `tasks.json`
- 🪶 Lightweight and easy to use (no database required)

---

## 🧰 Technologies Used

- **Python 3.10+**
- **Tkinter** for the graphical user interface (GUI)
- **JSON** for persistent task storage

---

## 📂 Project Structure

```

todo-list/
│
├── gui.py              # Handles the graphical user interface
├── task.py             # Defines the Task class
├── task_manager.py     # Handles task storage, loading, and management
├── constants.py        # Contains constants used across files
├── tasks.json          # Automatically created file for task persistence
└── README.md           # Project documentation

```

---

## ⚙️ Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/todo-list.git
   cd todo-list
   ```

2. **Run the application:**

   ```bash
   python gui.py
   ```

3. The program will automatically create a `tasks.json` file in your project directory once you add or close tasks.

---

## 💡 Usage

- **Add a task:** Type the task name and click “Add”.
- **Mark as done:** Click on a task to toggle its completion status.
- **Delete a task:** Select it and click “Delete”.
- **Exit safely:** Closing the window automatically saves your current list to `tasks.json`.

When you reopen the program, your tasks will automatically be restored.

---

## 🧪 Example `tasks.json`

```json
[
  {
    "title": "Finish project report",
    "due_date": "2025-11-10",
    "status": "in progress"
  },
  {
    "title": "Buy groceries",
    "due_date": null,
    "status": "done"
  }
]
```

---

## 🧩 Possible Future Improvements

- Add sorting or filtering by due date or status
- Implement categories or priorities
- Add reminders or notifications
- Sync with cloud storage or a mobile version

---

## 🧑‍💻 Author

**Langston Woods**
Computer Science student at the University of Rochester
[Portfolio Website](https://langstonw430.github.io/langstonw430/)
