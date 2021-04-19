# BeachHacks Project
# Student Schedule

####################

# Set a certain time frame within 24 hours
# Within time frame, assign work and study hours for time management
# Input different times and details
  # Possible alarm?

###################
main_loop = True
cont_loop = True

def menu_fun():
  print("Welcome to My Schedule")
  print("===========================")
  print("1. Add Schedule")
  print("2. Delete Schedule")
  print("3. See Schedule")
  print("4. Exit")

def cont_exit():
    print("Do you want to add another task? (Y/N) ")
    
schedule = [] # Empty schedule

while main_loop == True:
  menu_fun()
  number = int(input("Select a number between 1 and 4: "))
  while (number < 1) or (number > 4):
    print("Enter a valid input. ")
  while (1 <= number <= 4):
   
    # Add Schedule
    while cont_loop == True:
        if(number==1):
            timeframe = int(input("Enter a time in linear order. \n")) # 6 AM, 7 AM, 2 PM, 4 PM, etc...
            # 12 Hour or 24 Hour clock?
            # Floor Division // and Modulus % to determine AM and PM?
            while timeframe > 24:
                timeframe = int(input("Enter a time in linear order. \n")) # Time exceeds 24 hours?
            task = input("Enter a task you want to accomplish. \n")
            item = (timeframe, ":", task)
            schedule.append(item)

            cont_exit() # Input Y/N
            stayleave = input()
            if (stayleave == "Y"):
                cont_loop = True
            elif (stayleave == "N"):
                cont_loop = False
                # FIXME: While loop does not exit to main loop.
            else:
                print("Enter a valid input." )
                cont_exit
                stayleave = input()
                # How to create a new input? Add onto a list or something.
            

        ##Delete Schedule
        elif(number==2):
          # Delete from list > list.remove()
          schedule.remove()
          print(schedule)


        # ##See Schedule
        # elif(number==3):
          print(schedule)


        ##Exit
        else:
            print("See You!")
            cont_loop = False
            main_loop = False
            
            
            
