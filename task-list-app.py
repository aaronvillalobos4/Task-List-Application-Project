todo_list= []
while True:
  if todo_list == []:
    print("Your ToDo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index +=1
  print("Options:")
  print("1) Add Task")
  print("2) Remove Task")
  print("3) Quit")
  choice= input("Enter your choice (1, 2, or 3):")
  if choice == "1":
    new_task= input("What is your task?")
    todo_list.append(new_task)
    print("Your New Task Has Been Added")
  elif choice == "2":
    if todo_list ==[]:
      print("Your list is empty")
    else:
      removed_task= todo_list.pop()
  elif choice == "3":
    print("Quitting")
    break  