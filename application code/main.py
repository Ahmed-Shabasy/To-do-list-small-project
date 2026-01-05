from app_functions import *

task_list = []

def main():
  
  message = """
1 - Add A New Task To The List
2 - Mark Task As Completed
3 - View Tasks
4 - Quit"""

  
  while True:
      print(message)
      user_choice = input("Please Input Your Choice: ")

      # Let's Try To Use match case Instead of if statement
      match user_choice:
        case "1":
          add_task()
        case "2":
          mark_task_complete()
        case "3":
          view_tasks()
        case "4":
          print("App Ended")
          break
        case _:
          print("Invalid Choice, Please Input A Number Between 1-4")
  

if __name__ == "__main__":
    main()
