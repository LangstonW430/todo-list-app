# Todo List App

A simple and efficient desktop to-do list application built with Python and Tkinter. Organize and track your daily tasks with an intuitive graphical interface that automatically saves your progress locally.

## Features

- Add new tasks with due dates
- Delete existing tasks
- Mark tasks as completed or pending
- Tasks automatically persist to `tasks.json` and `done_task.json`
- Lightweight with no database required
- Cross-platform support (Windows, macOS, Linux)

## Quick Start

### Prerequisites

- Python 3.10 or higher
- Tkinter (usually comes pre-installed with Python)

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/LangstonW430/todo-list-app.git
   cd todo-list-app
   ```

2. Run the application
   ```bash
   python gui.py
   ```

The app will launch and automatically create a `tasks.json` file for storing your tasks.

## How to Use

1. **Add a Task**: Type the task name in the input field and click "Add"
2. **Mark as Complete**: Click on any task to toggle between completed and pending status
3. **Delete a Task**: Select a task and click the "Delete" button
4. **Exit**: Close the window - your tasks are automatically saved to `tasks.json`

When you reopen the application, all your tasks will be automatically restored.

## Project Structure

```
todo-list-app/
│
├── gui.py              # Main GUI implementation using Tkinter
├── task.py             # Task class definition
├── task_manager.py     # Task storage and management logic
├── constants.py        # Application constants
├── tasks.json          # Auto-generated task storage file
├── done_task.json      # Auto-generated finished task storage file
└── README.md           # This file
```

## Data Format

Tasks are stored in JSON format in the `tasks.json` file:

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

## Future Enhancements

Potential features for future versions:

- Sort and filter tasks by due date or status
- Add categories and priority levels
- Task reminders and notifications
- Cloud synchronization
- Mobile companion app
- Dark mode support
- Task statistics and productivity insights

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Author

**Langston Woods**

Computer Science Student at the University of Rochester

Portfolio: [langstonw430.github.io](https://langstonw430.github.io/langstonw430/)
