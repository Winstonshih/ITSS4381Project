# ITSS4381Project
Winston Shih, Ryan Hay, Sergei Wong, Seya Gadoo, Kevin Ly
ITSS 4381.001 Group 5

ITSS 4381 Group Project Option 1 Report
	Group 5’s program is supposed to help a user manage a to-do list by asking inputs for task name, importance, and due date and recording the date the task was added. After the inputs are collected, the contents of the to do list can be sorted in any order and displayed. Both functionalities are covered by the ToDoList.py and GUIFile.py. The ToDoList imports datetime module from a datetime file that can be used to track the time when a task is added. A variable called reset is created in the ToDoList file to open a text file called ToDoList.txt that allows user to write list of tasks in it through GUI open and write functions.ToDoList contains To_Do_List, Task, NameNotAStringError Exception, ImportanceNotAInt Exception, DueDateIncorrectFormat Exception, GreaterThanFiveError Exception, and LessThanOneError Exception classes. The GUIFile class will import tkinter to access GUI methods and ToDoList to access ToDoList method. 
	The first functionality of the program is the input, which is covered by the first 3 methods of the To_Do_List class in the ToDoList.py file. This class has an instance named TaskList, which is used to store input information about a task’s name, due date, importance, and time the task was added. The _init_method initializes the TaskList attribute by assigning self.TaskList to an empty list. The self parameter allows the method to access the TaskList attribute. The addTask  method adds a task to TaskList by prompting inputs for Name, Importance, and DueDate parameters when the method is called. After the method call, a new task instance is created and it is appended to the TaskList. The console prints the message “Successfully Added Task!” after the task is added and the viewTasks method is called to print out the current content of TaskList. The self parameter is used to access the append method when it needs to be called to add a task for the TaskList.The delTask method deletes tasks from the list by using the pop method and prompting an input for the index value of task. After the task is deleted, the viewTasks method is triggered. The self parameter is used to access the pop method when it needs to be triggered to remove a value from TaskList.
	The second functionality of the program, sorting and displaying the to-do list content, are covered by the remaining methods of the To_Do_List class. The sortByImportance method has a self parameter to allow it to access the sort method for the TaskList attribute to sort list by most important to least important (5 to 1). The method call uses lambda function as an anonymous function that will be used to pass the value of taskImportance to the key, so sort function knows what key to sort list by. Reverse is set to True so that the order of TaskList is sorted by importance from greatest value to lowest value. sortByRecentDate sorts list by recent date using the self parameter to access sort lambda function. Lambda function is used to pass the value of taskDateAdded to a key that will determine the order of the list. Reverse’s value is true so the order goes from the most recent date to the latest date. The sortByDueDate function sorts the list by proximity to the due date by using a lambda to pass the value of taskDueDate to the key that is used by the sort function to filter the list. It uses self to call the sort function for TaskList. sortAlpha organizes the list in alphabetical order by using a lambda function to pass the value of taskName.lower() to the key used to sort the list. Self is used to access the sort function for TaskList. displayTaskAlphabeutically displays a list in alphabetical order. It first prints the phrase: “List in alphabetical order:”. It uses the self parameter to access sortAlpha and calls the viewTasks method to display results of TaskList.  displayTaskByImportance prints list content in order of most important (5) to least important(1). It prints the statement: “List by importance:”. It then uses self to access the sortByImportance method and calls viewTasks to output the list sorted by importance. displayTaskByTimeAdded displays list by time the task is added. The method first prints, “List by recent date:”. It then uses the self parameter to call sortByRecentDate function to sort the list and ToDoList attribute to call viewTasks to display the rearranged list. displayTasks ByTimeDue displays list in order of earliest due date to latest. The function first prints: “List by due date:”. It then uses self to call sortByDueDate and ToDoList to call viewTasks, which will display a sorted list in order of due date. viewTasks is a method called when the contents of a to-do list needs to be printed. viewTasks uses the opem GUI method to set ToDoList.txt file to write only mode and iterate through a list by using the self parameter. In the for loop, each entry of ToDoList is added to text file with write GUI function. After the for loop is finished, close function is called to close GUI and the open function is used to set the text file to read only mode.
	The Task class holds all the information for each task entry in ToDoList list. It has attributes taskName, taskImportance, taskDueDate, and taskDateAdded. __init__ is the method that initializes all the attributes by assigning value of attribute to self.attribute.
	The NameNotAStringError class is triggered when the input for the task name is not a string. It has a __init__ method that initializes the message attribute. The self attribute is used to set the value of the message to “Name must be a String value.” The __str__ returns the message attribute’s value by using a self parameter to access the message attribute.
	The ImportanceNotAIntError class is triggered when the input for the importance value is not an integer. The self attribute is used to set the value of the message to “Importance must be an integer number.” The __str__ returns the message attribute’s value by using a self parameter to access the message attribute.
	The DueDateIncorrectForatError class is triggered when the due date is in the wrong format. The self attribute is used to set the value of the message to “Due date is in incorrect format.” The __str__ returns the message attribute’s value by using a self parameter to access the message attribute.
	The GreaterThanFiveError class is triggered when the input for the importance value is greater than five. The self attribute is used to set the value of the message to “The number cannot be greater than 5.” The __str__ returns the message attribute’s value by using a self parameter to access the message attribute.
	TheLessThanOneError class is triggered when the input for the importance value is less than 1. The self attribute is used to set the value of the message to “The number cannot be less than 1. The __str__ returns the message attribute’s value by using a self parameter to access the message attribute.
	The GUIFile class creates the GUI task windows that accepts input of task name , due date , and importance (add_task), deletes task by index (del_task), updates list (update_list), ends when close button is clicked (close_window), or sorts list by alphabetical order (alphsort), due date (duesort), importance (impsort), or time added (addsort).  MainWindow is a variable that is used to store value returned after tk object calls the Tk method to create a text file used to store to-do list contents. There are no attributes in this particular file. add_task, del_task, alphsort, duesort, impsort, and addsort utilize addTask, delTask, sortAlpha, sortByTimeDue, sortByImportance, amd sortByTimeAdded to be able to perform same function in GUI. Every method uses Label method from tk to label description in window and Entry method to create the window. The pack method is used to make the window widget show up, while the destroy method destroys the window widget after the user is done with the program. mainloop method is used to run the TKinter event loop. sortBy method constructs a window for sort functions to sort list by alphabetical order, date added, date due, or importance. closeWindow is called by add_task and del_task after the function of the method is complete. The main window is constructed by creating add_task, del_task, and sortBy buttons using lambda functions. update_list refreshes list every .25 seconds with a with-as statement that sets list to read only mode and uses config to make sure GUI list content is the same as text file content. The after method is used to schedule a list refresh to every .25 seconds. update_list is called once to start the update loop.
