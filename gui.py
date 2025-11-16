from task_manager import TaskManager
import tkinter as tk
import tkinter.font as tkFont
from task import Task
from contants import WINDOW_WIDTH, WINDOW_HEIGHT, COLORS
from datetime import date, datetime

def run_gui():
    task_list = TaskManager()
    done_list = TaskManager()
    showing_done = False

    # Load saved data
    task_list.load_from_file()
    done_list.load_from_file("done_tasks.json")

    def button_add_task():
        """Add a new task to the list"""
        title = title_input_entry.get().strip()
        due_date = due_date_input_entry.get().strip()
        
        if not parse_date(due_date):
            return

        if not title:
            title = "Untitled Task"
        
        new_task = Task(title, parse_date(due_date))
        new_task.title = title
        
        task_list.add_task(new_task)
        title_input_entry.delete(0, 'end')
        due_date_input_entry.delete(0, 'end')
        title_input_entry.focus()
        refresh()

    def add_to_list(task):
        """Create a task widget and add it to the container"""
        def cycle_status():
            if task.status == "not started":
                task.status = "in progress"
                status_button.config(bg=COLORS['in_progress'])
            elif task.status == "in progress":
                task.status = "done"
                status_button.config(bg=COLORS['done'])
                done_list.add_task(task)
                task_list.remove_task(task)
                refresh()
                return
            else:
                task.status = "not started"
                done_list.remove_task(task)
                task_list.add_task(task)
                refresh()
                return
            status_button.config(text=task.status.title())

        def delete_task():
            if showing_done:
                done_list.remove_task(task)
            else:
                task_list.remove_task(task)
            refresh()

        # Task card frame
        task_frame = tk.Frame(task_container,
                              bg=COLORS['bg_secondary'], 
                              highlightbackground=COLORS['border'], 
                              highlightthickness=1)
        task_frame.pack(fill="x", pady=5, padx=10)
        
        # Configure grid
        task_frame.grid_columnconfigure(0, weight=1)
        task_frame.grid_columnconfigure(1, weight=0)
        task_frame.grid_columnconfigure(2, weight=0)
        task_frame.grid_columnconfigure(3, weight=0)

        # Title
        title_label = tk.Label(task_frame,
                               text=task.title, 
                               font=("Segoe UI", 11, "bold"),
                               bg=COLORS['bg_secondary'], 
                               fg=COLORS['text_primary'],
                               anchor="w",
                               padx=15,
                               pady=12)
        title_label.grid(row=0, column=0)

        # Due date
        due_date_label = tk.Label(task_frame, 
                                  text=task.due_date if task.due_date else "No due date",
                                  font=("Segoe UI", 10),
                                  bg=COLORS['bg_secondary'], 
                                  fg=COLORS['text_secondary'],
                                  anchor="center",
                                  padx=10,
                                  pady=12)
        due_date_label.grid(row=0, column=1)

        # Status button
        status_bg = {
            "not started": COLORS['not_started'],
            "in progress": COLORS['in_progress'],
            "done": COLORS['done']
        }.get(task.status, COLORS['not_started'])
        
        status_button = tk.Button(task_frame,
                                  text=task.status.title(),
                                  font=("Segoe UI", 9, "bold"),
                                  bg=status_bg, 
                                  fg=COLORS['text_primary'],
                                  relief="flat",
                                  cursor="hand2",
                                  padx=10,
                                  pady=8,
                                  width=12,
                                  command=cycle_status)
        status_button.grid(row=0, column=2, padx=5)

        # Delete button
        delete_btn = tk.Button(task_frame,
                               text="✕",
                               font=("Segoe UI", 12, "bold"),
                               bg=COLORS['bg_secondary'], 
                               fg=COLORS['danger'],
                               relief="flat",
                               cursor="hand2",
                               padx=10,
                               pady=8,
                               command=delete_task)
        delete_btn.grid(row=0, column=3, padx=(0, 5))

    def resize_canvas(event):
        """Adjust canvas width on window resize"""
        new_width = window.winfo_width() - 20
        task_list_canvas.itemconfig(canvas_window_id, width=new_width)
    
    def refresh():
        """Refresh the task list display"""
        for widget in task_container.winfo_children():
            widget.destroy()
        
        current_list = done_list if showing_done else task_list
        
        if len(current_list.tasks) == 0:
            empty_label = tk.Label(task_container, 
                                   text="No tasks yet!" if not showing_done else "No completed tasks!",
                                   font=("Segoe UI", 12),
                                   fg=COLORS['text_secondary'],
                                   bg=COLORS['bg_primary'],
                                   pady=50)
            empty_label.pack(fill="both", expand=True)
        else:
            for task in current_list:
                add_to_list(task)
        
        task_list_canvas.update_idletasks()
        task_list_canvas.configure(scrollregion=task_list_canvas.bbox("all"))

    def toggle_list():
        """Toggle between active and completed tasks"""
        nonlocal showing_done
        showing_done = not showing_done
        toggle_btn.config(text="📋 Active Tasks" if showing_done else "✓ Completed Tasks")
        refresh()

    def sort_list_button():
        """Sort the current list"""
        current_list = done_list if showing_done else task_list
        current_list.sort_list(not current_list.is_sorted(False))
        refresh()

    def on_close():
        task_list.save_to_file()
        done_list.save_to_file("done_tasks.json")
        window.destroy()
    
    def on_focus_in(event, placeholder=""):
        entry = event.widget
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(event, placeholder=""):
        entry = event.widget
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg="grey")

    def parse_date(date_str):
        try:
            return datetime.strptime(date_str, "%m/%d/%Y")
        except ValueError:
            return None

    # Main window setup
    window = tk.Tk()
    window.title("To-Do List Manager")
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    window.configure(bg=COLORS['bg_primary'])

    # Configure grid weights
    window.grid_rowconfigure(0, weight=0)
    window.grid_rowconfigure(1, weight=0)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=0)
    window.grid_columnconfigure(0, weight=1)

    # Header
    header_frame = tk.Frame(window, bg=COLORS['accent'], height=80)
    header_frame.grid(row=0, column=0, sticky="ew")
    header_frame.grid_propagate(False)

    title_font = tkFont.Font(family="Segoe UI", size=20, weight="bold")
    title_label = tk.Label(header_frame,
                           text="📝 My To-Do List", 
                           font=title_font,
                           bg=COLORS['accent'], 
                           fg="white",
                           pady=25)
    title_label.pack()

    # Control buttons frame
    control_frame = tk.Frame(window, bg=COLORS['bg_primary'])
    control_frame.grid(row=1, column=0, sticky="ew", pady=10, padx=10)

    control_frame.grid_columnconfigure(0, weight=1, uniform="buttons")
    control_frame.grid_columnconfigure(1, weight=1, uniform="buttons")
    control_frame.grid_columnconfigure(2, weight=1, uniform="buttons")

    sort_btn = tk.Button(control_frame,
                         text="⇅ Sort by Date",
                         font=("Segoe UI", 10),
                         bg=COLORS['bg_secondary'], 
                         fg=COLORS['text_primary'],
                         relief="flat",
                         cursor="hand2",
                         padx=20,
                         pady=10,
                         command=sort_list_button)
    sort_btn.grid(row=0, column=0, padx=5, sticky="ew")

    toggle_btn = tk.Button(control_frame,
                           text="✓ Completed Tasks",
                           font=("Segoe UI", 10),
                           bg=COLORS['bg_secondary'], 
                           fg=COLORS['text_primary'],
                           relief="flat",
                           cursor="hand2",
                           padx=20,
                           pady=10,
                           command=toggle_list)
    toggle_btn.grid(row=0, column=1, padx=5, sticky="ew")

    time_and_date_button = tk.Button(control_frame,
                                   text=date.today().strftime("%B %d, %Y"),
                                   font=("Segoe UI", 10),
                                   bg=COLORS['bg_secondary'], 
                                   fg=COLORS['text_primary'],
                                   relief="flat",
                                   cursor="arrow",
                                   padx=20,
                                   pady=10,
                                   state="disabled",
                                   disabledforeground=COLORS['text_primary'])
    
    time_and_date_button.grid(row=0, column=2, padx=5, sticky="ew")

    # Main scrollable frame
    main_frame = tk.Frame(window, bg=COLORS['bg_primary'])
    main_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=(0, 10))

    task_list_canvas = tk.Canvas(main_frame, bg=COLORS['bg_primary'], 
                                 highlightthickness=0)
    task_list_canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(main_frame,
                             orient="vertical", 
                             command=task_list_canvas.yview)
    scrollbar.pack(side="right", fill="y")
    
    task_list_canvas.configure(yscrollcommand=scrollbar.set)

    task_container = tk.Frame(task_list_canvas, bg=COLORS['bg_primary'])
    canvas_window_id = task_list_canvas.create_window(
        (0, 0), window=task_container, anchor="nw", width=WINDOW_WIDTH-20
    )

    window.bind("<Configure>", resize_canvas)

    # Input frame
    input_frame = tk.Frame(window,
                           bg=COLORS['bg_secondary'], 
                           highlightbackground=COLORS['border'],
                           highlightthickness=1)
    input_frame.grid(row=3, column=0, sticky="ew", padx=10, pady=(0, 10))

    input_frame.grid_columnconfigure(0, weight=2)
    input_frame.grid_columnconfigure(1, weight=2)
    input_frame.grid_columnconfigure(2, weight=0)

    # Title input
    title_input_frame = tk.Frame(input_frame, bg=COLORS['bg_secondary'])
    title_input_frame.grid(row=0, column=0, sticky="ew", padx=15, pady=15)

    title_input_label = tk.Label(title_input_frame,
                                 text="Task Title",
                                 font=("Segoe UI", 9),
                                 bg=COLORS['bg_secondary'],
                                 fg=COLORS['text_secondary'])
    title_input_label.pack(anchor="w")

    title_input_entry = tk.Entry(title_input_frame, 
                                font=("Segoe UI", 11),
                                relief="flat",
                                bg=COLORS['bg_primary'])
    title_input_entry.pack(fill="x", ipady=8)

    # Due date input
    due_date_input_frame = tk.Frame(input_frame, bg=COLORS['bg_secondary'])
    due_date_input_frame.grid(row=0, column=1, sticky="ew", padx=15, pady=15)

    due_date_input_label = tk.Label(due_date_input_frame,
                                    text="Due Date",
                                    font=("Segoe UI", 9),
                                    bg=COLORS['bg_secondary'],
                                    fg=COLORS['text_secondary'])
    due_date_input_label.pack(anchor="w")
    

    due_date_input_entry = tk.Entry(due_date_input_frame,
                                    font=("Segoe UI", 11),
                                    relief="flat",
                                    bg=COLORS['bg_primary'])
    due_date_input_entry.pack(fill="x", ipady=8)
    due_date_input_entry.bind("<FocusIn>", lambda e: on_focus_in(e, "MM/DD/YYYY"))
    due_date_input_entry.bind("<FocusOut>", lambda e: on_focus_out(e, "MM/DD/YYYY"))

    # Add button
    add_task_button = tk.Button(input_frame,
                                text="+ Add Task",
                                font=("Segoe UI", 11, "bold"),
                                bg=COLORS['accent'], 
                                fg="white",
                                relief="flat",
                                cursor="hand2",
                                padx=30,
                                command=button_add_task)
    add_task_button.grid(row=0, column=2, sticky="ns", padx=15, pady=15)

    # Bind Enter key to add task
    window.bind('<Return>', lambda e: button_add_task())

    # Initial refresh
    refresh()
    title_input_entry.focus()

    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()