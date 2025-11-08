from task_manager import TaskManager
import tkinter as tk
import tkinter.font as tkFont
from task import Task

def run_gui():
    task_list = TaskManager()
    done_list = TaskManager()

    showing_done = False

    

    
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    def button_add_task():
        new_task = Task()
        if not title_input_entry.get() == "":
            new_task.title = title_input_entry.get()

        if not due_date_input_entry.get() == "":
            new_task.due_date = due_date_input_entry.get()
        
        task_list.add_task(new_task)
        title_input_entry.delete(0, 'end')
        due_date_input_entry.delete(0, 'end')
        refresh()

    def add_to_list(task=Task()):

        def cycle_status():
            if task.status == "not started":
                task.status = "in progress"
            elif task.status == "in progress":
                task.status = "done"
            elif showing_done:
                task.status = "not started"
                done_list.remove_task(task)
                task_list.add_task(task)
                refresh()
            else:
                done_list.add_task(task)
                task_list.remove_task(task)
                refresh()
            task_list_status_button.config(text=task.status)

        new_task_frame = tk.Frame(task_container, bg="purple", height=50)
        new_task_frame.pack(fill="x", pady=2)
        
        new_task_frame.grid_rowconfigure(0, weight=1)
        new_task_frame.grid_columnconfigure(0, weight=1, uniform="col")
        new_task_frame.grid_columnconfigure(1, weight=1, uniform="col")
        new_task_frame.grid_columnconfigure(2, weight=1, uniform="col")

        task_list_title_label = tk.Label(new_task_frame, text=task.title, height=5, bg="lightgray")
        task_list_title_label.grid(row=0, column=0, sticky="nsew")

        task_list_due_date_label = tk.Label(new_task_frame, text= task.due_date, height=5, bg="lightgray")
        task_list_due_date_label.grid(row=0, column=1, sticky="nsew")

        task_list_status_button = tk.Button(new_task_frame, text=task.status, height=5, bg="lightgray", command=cycle_status)
        task_list_status_button.grid(row=0, column=2, sticky="nsew")


    def resize_canvas(event):
        new_width = window.winfo_width()
        task_list_canvas.itemconfig(canvas_window_id, width=new_width)
    
    def refresh():
        nonlocal showing_done
        for widget in task_container.winfo_children():
            widget.destroy()
        if showing_done:
            for task in done_list:
                add_to_list(task)
        else:
            for task in task_list:
                add_to_list(task)
        task_list_canvas.update_idletasks()
        task_list_canvas.configure(scrollregion=task_list_canvas.bbox("all"))

    def toggle_list():
        nonlocal showing_done
        showing_done = not showing_done
        refresh()

        
    def sort_list_button():
        if showing_done:
            if done_list.is_sorted(False):
                done_list.sort_list(True)
            else:
                done_list.sort_list(False)
        else:
            if task_list.is_sorted(False):
                task_list.sort_list(True)
            else:
                task_list.sort_list(False)
        refresh()
            
            

    window = tk.Tk()
    window.title("To-Do List")
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    window.grid_rowconfigure(0, weight=2)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=16)
    window.grid_rowconfigure(3, weight=2)
    window.grid_columnconfigure(0, weight=1)  

    title_frame = tk.Frame(window)
    title_frame.grid(row=0, column=0, sticky="nsew")

    title_font = tkFont.Font(family="Coutier", size= 24, weight="bold")
    title_label = tk.Label(title_frame, text="To-Do List App", font=title_font)
    title_label.pack(expand=True, fill="both")


    sort_by_frame = tk.Frame(window, bg="red")
    sort_by_frame.grid(row=1, column=0, sticky="nsew")

    


    main_frame = tk.Frame(window)
    main_frame.grid(row=2, column=0, sticky="nsew")

    task_list_canvas = tk.Canvas(main_frame)
    task_list_canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=task_list_canvas.yview)
    scrollbar.pack(side="right", fill="y")
    
    task_list_canvas.configure(yscrollcommand=scrollbar.set)

    task_container = tk.Frame(task_list_canvas)
    task_list_canvas.create_window((0, 0), window=task_container, anchor="nw", width=WINDOW_WIDTH)

    window.bind("<Configure>", resize_canvas)

    task_container.update_idletasks()
    task_list_canvas.configure(scrollregion=task_list_canvas.bbox("all"))
    
    canvas_window_id = task_list_canvas.create_window(
        (0, 0),
        window=task_container,
        anchor="nw",
        width=WINDOW_WIDTH
    )
    

    sort_by_frame.grid_rowconfigure(0, weight=1)
    sort_by_frame.grid_columnconfigure(0, weight=1, uniform="button")
    sort_by_frame.grid_columnconfigure(1, weight=1, uniform="button")
    sort_by_frame.grid_columnconfigure(2, weight=1, uniform="button")

    sort_alpha_button = tk.Button(sort_by_frame, text="sort", command=sort_list_button)
    sort_alpha_button.grid(row=0, column=0)

    toggle_list_button = tk.Button(sort_by_frame, text="toggle list", command=toggle_list)
    toggle_list_button.grid(row=0, column=1)




    input_frame = tk.Frame(window, bg="lightgray")
    input_frame.grid(row=3, column=0, sticky="nsew")

    input_frame.grid_rowconfigure(0, weight=1)
    input_frame.grid_columnconfigure(0, weight=2)
    input_frame.grid_columnconfigure(1, weight=2)
    input_frame.grid_columnconfigure(2, weight=1)

    title_input_frame = tk.Frame(input_frame, bg="orange")
    title_input_frame.grid(row=0, column=0, sticky="nsew")

    title_input_frame.grid_rowconfigure(0, weight=1)
    title_input_frame.grid_columnconfigure(0, weight=1)

    title_input_label = tk.Label(title_input_frame, text="Title")
    title_input_label.grid(row=0, column=0)

    title_input_entry = tk.Entry(title_input_frame)
    title_input_entry.grid(row=0, column=1)

    due_date_input_frame = tk.Frame(input_frame, bg="lime")
    due_date_input_frame.grid(row=0, column=1, sticky="nsew")

    due_date_input_frame.grid_rowconfigure(0, weight=1)
    due_date_input_frame.grid_columnconfigure(0, weight=1)

    due_date_input_label = tk.Label(due_date_input_frame, text="Due Date")
    due_date_input_label.grid(row=0, column=0)

    due_date_input_entry = tk.Entry(due_date_input_frame)
    due_date_input_entry.grid(row=0, column=1)


    add_task_button = tk.Button(input_frame, text="Add Task", command=button_add_task)
    add_task_button.grid(row=0, column=2)

    # tester_button = tk.Button(input_frame, text="test", command=print_list)
    # tester_button.grid(row=0, column=2, sticky="n")


    


     

    


    window.mainloop()