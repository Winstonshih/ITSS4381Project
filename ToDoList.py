# Using the datetime module for keeping track of current time
from datetime import datetime




reset = open("ToDoList.txt", "w")
reset.write("")




# ToDo List Class - Handles the tasks information by either adding, deleting, and sorting the different tasks based on
# importance, date, and when it is due
class To_Do_List:
   # Initialization Method - Assign an empty list to store the task objects
   def __init__(self):
       self.TaskList = []


   # Add task to to-do list
   def addTask(self, Name, Importance, DueDate):
       # Prompt the User for the Task Information
       # Create a new task instance
       task = Task(Name, Importance, DueDate)
       # Add the task object to the To Do List (Task List)
       self.TaskList.append(task)
       print("Successfully Added Task!")
       ToDoList.viewTasks()


   # Deletes task from to-do list
   def delTask(self, Value):
       self.TaskList.pop(int(Value))
       ToDoList.viewTasks()


   # Sort tasks by importance
   def sortByImportance(self):
       self.TaskList.sort(key=lambda x: x.taskImportance, reverse=True)


   # Sort tasks by most recent date
   def sortByRecentDate(self):
       self.TaskList.sort(key=lambda x: x.taskDateAdded, reverse=True)


   # Sort tasks by closest due date
   def sortByDueDate(self):
       self.TaskList.sort(key=lambda x: x.taskDueDate)


   # Sorts alphabetically
   def sortAlpha(self):
       self.TaskList.sort(key=lambda x: x.taskName.lower())


   # Displays tasks by alphabetical order
   def displayTaskAlphabetically(self):
       print("List in alphabetical order")
       self.sortAlpha()
       ToDoList.viewTasks()


   # Displays list by order of importance from 5 (most important) to 1 (least).
   def displayTaskByImportance(self):
       print("List by importance:")
       self.sortByImportance()
       ToDoList.viewTasks()


   # Displays list by order of time added.
   def displayTaskByTimeAdded(self):
       print("List by recent date:")
       self.sortByRecentDate()
       ToDoList.viewTasks()


   # Displays tasks by earliest due date to latest.
   def displayTaskByTimeDue(self):
       print("List by due date:")
       self.sortByDueDate()
       ToDoList.viewTasks()


   # Display the Tasks
   def viewTasks(self):
       # Iterates through the list of tasks, writing the whole thing to ToDoList.txt and then displaying the txt file
       # This function is now ran everytime the list is updated so that the current list is always displayed.


       task_file = open("ToDoList.txt", "w")
       for tasks in self.TaskList:
           task_file.write("\n| Task Name: " + str(tasks.taskName) + " | Importance Level: " + str(
               tasks.taskImportance) + " | Task Date Added: " + str(tasks.taskDateAdded) + " | Task Due Date: " + str(
               tasks.taskDueDate))
       task_file.close()
       task_file = open("ToDoList.txt", "r")
       return task_file.read()




# Tasks Class - Holds all the information for each tasks including: Name, Importance (1-5), Date, and Due Date
class Task:
   # Initialization Method - Stores the task information
   def __init__(self, taskName, taskImportance, taskDueDate):
       self.taskName = taskName
       self.taskImportance = taskImportance
       # .strftime formats the date to be more readable.
       # Stores the current time using the datetime module
       self.taskDateAdded = datetime.now().strftime("%m-%d-%Y, %H:%M:%S")
       self.taskDueDate = taskDueDate




class ImportanceNotAIntError(Exception):
   def __init__(self, message="Importance must be an integer number."):
       self.message = message


   def __str__(self):
       return self.message




class DueDateIncorrectFormatError(Exception):
   def __init__(self, message="Due Date is in the incorrect format."):
       self.message = message


   def __str__(self):
       return self.message


# Create a To-Do List




ToDoList = To_Do_List()
