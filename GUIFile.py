import tkinter as tk
from ToDoList import ToDoList
from tkinter import messagebox


MainWindow = tk.Tk()
# create the text file


# add task window construction




def add_task():
   add_task_window = tk.Toplevel()
   name_req = tk.Label(add_task_window, text="Enter the task Name")
   name_req.pack()
   name_ent = tk.Entry(add_task_window)
   name_ent.pack()


   imp_req = tk.Label(add_task_window, text="Enter Task Importance")
   imp_req.pack()
   imp_ent = tk.Entry(add_task_window)
   imp_ent.pack()


   due_req = tk.Label(add_task_window, text="Enter Task Due Date")
   due_req.pack()
   due_ent = tk.Entry(add_task_window)
   due_ent.pack()


   def close_window():
       # Check if the importance input is an integer
       try:
           imp_input = int(imp_ent.get())


       except ValueError:
           tk.messagebox.showerror("Error", "Importance must be an integer")
           return


       if 5 < imp_input or 1 > imp_input:
           tk.messagebox.showerror("Error", "Importance should be a integer 1-5")
           return None


       ToDoList.addTask(str(name_ent.get()), str(imp_ent.get()), str(due_ent.get()))
       add_task_window.destroy()


   add_btn = tk.Button(add_task_window, text="Add Task", command=lambda: close_window())
   add_btn.pack()


   add_task_window.mainloop()


# delete task window construction




def del_task():
   deltask_window = tk.Toplevel()
   task_num = tk.Label(deltask_window, text="What is the index of the task you want to delete?")
   task_num.pack()
   task_num_ent = tk.Entry(deltask_window)
   task_num_ent.pack()


   del_btn = tk.Button(deltask_window, text="Delete Task", command=lambda: close_window(task_num_ent.get()))
   del_btn.pack()


   def close_window(value):
       if 0 > int(value) or len(ToDoList.TaskList) < int(value)+1:
           tk.messagebox.showerror("Error", "The index of the task should be a number from 0 to " +
                                   str(len(ToDoList.TaskList)-1))
           return None
       ToDoList.delTask(value)
       deltask_window.destroy()


# sort window construction




def sortby():
   sort_win = tk.Toplevel()


   ask_label = tk.Label(sort_win, text="What do you want to sort by?")
   ask_label.pack()


   imp_btn = tk.Button(sort_win, text="Importance", command=lambda: impSort())
   imp_btn.pack()


   add_btn = tk.Button(sort_win, text="Newest added", command=lambda: addSort())
   add_btn.pack()


   alph_btn = tk.Button(sort_win, text="Alphabetically", command=lambda: alphSort())
   alph_btn.pack()


   due_btn = tk.Button(sort_win, text="Earliest Due", command=lambda: dueSort())
   due_btn.pack()


   def alphSort():
       ToDoList.displayTaskAlphabetically()
       sort_win.destroy()


   def impSort():
       ToDoList.displayTaskByImportance()
       sort_win.destroy()


   def addSort():
       ToDoList.displayTaskByTimeAdded()
       sort_win.destroy()


   def dueSort():
       ToDoList.displayTaskByTimeDue()
       sort_win.destroy()


# main window construction




addTask_btn = tk.Button(MainWindow, text="Add Task", command=lambda: add_task())
addTask_btn.pack()




delTask_btn = tk.Button(MainWindow, text="Delete Task", command=lambda: del_task())
delTask_btn.pack()




sort_btn = tk.Button(MainWindow, text="sort list", command=lambda: sortby())
sort_btn.pack()




list_label = tk.Label(MainWindow)
list_label.pack()


# This method refreshes the list every .25 seconds




def update_list():
   with open("ToDoList.txt", "r") as f:
       contents = f.read()
   list_label.config(text=contents)


   # Schedule the next update in .25 seconds
   MainWindow.after(250, update_list)




# Call update_list() once to start the update loop
update_list()




MainWindow.mainloop()


