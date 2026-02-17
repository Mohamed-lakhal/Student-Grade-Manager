import os
import time

# GLOBAL VARIABLES : 
STD_NAME = []
STD_GRADE = []

# FUNCTION'S MENU :
def MENU():
    print ("\n"+"="*50)
    print ("STUDENT_GRADE_MANAGER ")
    print ("="*50)
    print ("[1] ADD NEW STUDENT !")
    print ("[2] VIEW ALL STUDENTS")
    print ("[3] SEARCH STUDENT ")
    print ("[4] CALCULATE CLASS AVERAGE")
    print ("[5] STUDENTS STATISTICS")
    print ("[6] FIND TOP STUDENT ")
    print ("[7] SAVE_FILE ")
    print ("[8] LOAD_FILE")
    print ("[0] EXIT ")
    print ("="*50)
    USERCHOICE = int(input ("Your choice please :"))
    return USERCHOICE

#                                          ADD_NEW

# [1] ADD A NEW STUDENT AND HIS GRADES IF GRADES DOES NOT EXIST ROLLBACK !

def ADD_NEW(listname,listgrade):
    while True:
        name = input ("STUDENT NAME (Exit => done): ").strip()
        # CHEK IF NAME IS EMPTY :
        if not name :
            print("error : name can not be empty !")
            continue 
        # CHECK IF NAME IS "DONE"
        if name.upper() == "DONE":
             break
        # Check if contains only letters and spaces
        # Remove spaces, then check if rest is alphabetic
        name_w_space = name.replace(" ","")
        if not name_w_space :
            print ("Name can not be only spaces : ")
            continue 
        if not name_w_space.isalpha():
            print ("Only alphabetic characters and spaces are allowed! ")
            continue
        # IF NAME IS REALLY HERE :
        if name.upper() in listname :
            print ("NAME ALREADY EXIST CHOSE OTHER ONE!")
            continue
    # grade part :
        grades = [] # each student has 3 grades  that's mean a list of grade 
        cpt = 3
        while cpt > 0 :
                while True:
                    
                    # verification if grade is number :
                    try :
                         value = float (input("ENTER grade :"))
                    except ValueError:
                        print ("unaccepted grade must be a value!")
                        continue
                
                    # IF GRADE WAS ILLOGIC DONT ADD IT TO THE LIST OF GRADES :
                    if value > 20 or value < 1 :
                        print ("Grade allowed are between 1 and 20 :")
                        continue 
                    grades.append(value)
                    cpt-=1
                    if cpt == 0 :
                         break
        
        # ADD THE STUDENT TO THE LIST[] AFTER VERIFICATION OF ALL CONDITIONS :
        DECISION =input ("DROP (E) TO  FINISH OR (C) TO CANCEL : ")
        while DECISION.upper() != "E" and DECISION.upper() != "C":
            DECISION = input ("Invalid options only (E/C) :")
        # COMMIT TRANSACTION : 
        if DECISION.upper() == "E":
            listname .append(name.upper()) # STUDENT NAME 
            listgrade.append(grades) # STUDENT GRADES 
            print("SUCCESS !")
            print(f"NAME : {name}")
            print (f"GRADES :{grades}")
        else : # RollBACK 
                print ("MISSION HAS BEEN CANCELED !")
#                                                    SHOW_ALL_STUDENTS
# [2]show all students function :

def SHOW_ALL(listname,listgrade):
    if not STD_NAME:
         print('='*50)
         print("Error:No data to show it!")
         print('='*50)
         return
    print ("[D] for detail list")
    print ("[Q] for Quick list ")
    choice = input("ENTER [D]OR [Q] : ")
    while choice.upper() not in ["D","Q"]:
        choice= input  ("Error : chose only [Q] or [D]:")
    
    # Calculation 
    for i in range (len(listname)):
            name = listname[i] #  GET STUDENT NAME !
            result = list (listgrade[i]) # GET STUDENT GRADES!
            total = sum (result) # SUM OF STUDENT GRADES !
            average = total / len(result)
            DECISION = "PASS" if average >= 10 else "FAIL"
            # [D] detailed list :
            if choice.upper() == "D": 
                print(f"\nNAME:    {name}")
                print(f"GRADES:  {result}")
                print(f"AVERAGE: {average:.2f}/20")  # Fixed: .2f for 2 decimals
                print(f"STATUS:  {DECISION}")
                print("-" * 40)
            else :
                print(f"{name:15} → {average:4.2f}/20 → {DECISION}")
#                                                     LOOKING_FOR_STUDENT
#[3] SEARCH A STUDENT :
def SEARCH_STD(listname,listgrade):
    if not listname:
        print ("Sorry no data to look for!")
        return
    student = input ("STUDENT NAME : ").strip()
    while True:
        name_wo_spaces = student.replace(" ", "")
        if not name_wo_spaces:
             student = input ("Error : name cannot be empty or only spaces : ")
             continue
        # looking for the student in the data base :
        if student.upper() not in listname:
            student = input (f"student {student} not found (Cancel => E):").strip()
            if student.upper() == "E":
                print ("SEARCH CANCELLED !")
                return
            continue
        else:
            found_index =-1
            for i in range (len(listname)):
                        if listname[i] == student.upper():
                            found_index = i 
                            break 
            if found_index != -1:
                        name = student.upper()
                        grade = listgrade[found_index]
                        average = sum(grade) / len(grade)
                        status = "PASS" if average >=10 else "FAIL!" 
                        print(F"NAME : {name}")
                        print(F"GRADE : {grade}")
                        print(F"AVERAGE : {average:.2f}")
                        print(F"STATUS : {status}")
                        return
#                                                         CLASS_AVERAGE

def AVERAGE(listname,listgrade):
     TOTAL_AVG = 0 
     if not listname:
          print ("we're sorry no data to work on it !")
          return
     elif len (listname) < 2:
          print (f"we're sorry need 2 student at less you have {len(listname)}")
          return
     else :
          for i in range (len(listname)):
               std_average = sum(listgrade[i])/ len (listgrade[i]) # calculate each student average
               TOTAL_AVG +=std_average # affect each student average to TOTAL_AVG :
          CLASS_AVERAGE = TOTAL_AVG / len(listname) # Class average must be outside of the  for loop 
          if CLASS_AVERAGE >= 16:
                        note = "Excellent class performance! 🎉"
          elif CLASS_AVERAGE >= 14:
                        note = "Very good results! 👍"
          elif CLASS_AVERAGE >= 12:
                        note = "Good performance overall."
          elif CLASS_AVERAGE >= 10:
                        note = "Satisfactory results."
          else:
                        note = "Needs improvement. 📚"
          print("\n"+"="*50) 
          print("STUDENT AVRAGE ")  
          print("\n"+"="*50) 
          print(f"TOTAL STUDENT : {len(listname)}")
          print(f"CLASS AVERAGE : {CLASS_AVERAGE:.2f}/20")
          print(f"NOTE : {note}")
          print("\n"+"="*50)

#                                                            STATISTICS

def STATISTICS(listname,listgrade):
      pass_list = []
      fail_list = []
      std_pass = 0
      std_fail = 0
      if len (listname) < 2:
            print ("We're sorry no data to work on!")
            return
      else :
            for i in range(len (listname)):
                  average = sum(listgrade[i])/len(listgrade[i])
                  if average >= 10:
                        pass_list.append(listname[i])
                        std_pass += 1
                  else:
                        fail_list.append(listname[i])
                        std_fail += 1
            pass_static = (std_pass*100)/len(listname) # PERCENTAGE OF STUDENT WHO PASSED 
            fail_static = (std_fail*100)/len(listname) # PERCENTAGE OF STUDENT WHO FAILED
            print ("="*50)
            print ("CLASS STATISTICS ")
            print ("="*50)
            print (f"TOTAL STUDENTS : {len(listname)}")
            print ("\n\n")
            print (F"PASSED ({std_pass} - {pass_static:.1f}%) :")
            if pass_list: 
                for n in range(0,(len(pass_list)),3):
                    line = pass_list[n:n+3] 
                    print(" "+" - ".join(line))
            print ("\n\n")
            print (F"FAILED ({std_fail} - {fail_static:.1f}%) :")
            if fail_list:
                for n in range(0,(len(fail_list)),3):
                    line = fail_list[n:n+3] 
                    print(" "+" - ".join(line))
            print ("\n\n")
            if (len(pass_list) - len (fail_list))/4 >=3/4:
                  note = "GOOD JOB PROFESSOR!"
            elif (len(pass_list) - len (fail_list))/4 >= 2/4 + 1:
                  note = "ACCEPTABLE WORK!"
            elif (len(pass_list) - len (fail_list))/4 == 2/4:
                 note = "NEED SOME EFFORT!"
            elif (len(pass_list) - len (fail_list))/4 < 2/4:
                  note = "NEED BIG SUPPORT!"
            else:
                  note = "CLASS HAVE TO RPEAT THE COURSE !"
            print(f"NOTE : {note}")
            print ("\n\n")
            print("="*50)

#                                                                TOP STUDENTS 
def TOP_STD(listname,listgrade):
      if len(listname) < 2 :
            print("We're sorry no data to work on it!")
            return
      AVG_LIST = []
      TOP1_l = []
      TOP2_l = []
      TOP3_l = []
      # 1 . CALCULATE EACH STUDENT AVG AND AND PUT IT ON A LIST :
      for i in range (len (listname)):
            average = round(sum(listgrade[i])/ len(listgrade[i]),2)
            AVG_LIST.append(average)
      max_avg = max(AVG_LIST)
      for i in range (len (listname)):
            if max_avg == AVG_LIST[i]:
                  TOP1_l.append(listname[i])
        # WORKING ON A COPY OF THE AVG LIST TO FIND THE SECOND MAX AFTER DELETING THE TOP ONE AVG :
      COPY_AVG = AVG_LIST.copy()
      
      while max_avg in  (COPY_AVG):

        COPY_AVG.remove(max_avg)

      # LOOKING FOR THE NEXT MAX:
      if COPY_AVG :
            max2_avg = max(COPY_AVG)
            for i in range (len (listname)):
                if max2_avg == AVG_LIST[i]:
                  TOP2_l.append(listname[i])

            #  DELETING THE MAX2 TO LOOK FOR  MAX3

            while max2_avg in  (COPY_AVG):
                  
                COPY_AVG.remove(max2_avg)

      # LOOKING FOR THE THIRD ONE 
      if COPY_AVG:
        max3_avg = max(COPY_AVG)
        for i in range (len (listname)):
            if max3_avg == AVG_LIST[i]:
                  TOP3_l.append(listname[i])
      # INTERFACE PART :
      print("="*50)
      print("TOP STUDENTS ")
      print("="*50)
      print("\n\n")
      print("FIRST PLACE :")
      for i in range(0,len(TOP1_l),3):
            line = TOP1_l[i:i+3]
            print (" "+" - ".join(line)+f" - {max_avg}/20")
      print("\n\n")
      if TOP2_l:
        print("SECOND PLACE :")
        for i in range(0,len (TOP2_l),3):
            line = TOP2_l[i:i+3]
            print (" "+" - ".join(line)+F" - {max2_avg}/20")
        print("\n\n")
      else:
        print("NO SECOND PLACE !")
      if TOP3_l:
            print("THIRD PLACE :")
            for i in range(0,len(TOP3_l),3):
                line = TOP3_l[i:i+3]
                print (" "+" - ".join(line)+F" - {max3_avg}/20")
      else :
                  print ("NO THIRD PLACE !")
      print("\n\n")
      print("="*50)
      from datetime import datetime
      date = datetime.now().strftime("%d-%m-%Y")
      print(f"Total Students: {len(listname)} | Date: [{date}]")
      print("="*50)


#                                                 (SAVE / LOAD) FUNCTIONS 
def LOAD_DATA(listname , listgrade):
            LOADS_ERROR = 0
            LOADS_SUCCESS= 0
            file_L_name = input ("Enter Name of the file (Make  the file in programme folder): ")
            file_L_name = file_L_name.replace(" ","") 
            if not file_L_name:
                  print("Sorry : file name can't be spaces ")
                  return
            # CHECKING FOR EXIST OR NOT :
            
            if not os.path.exists(file_L_name):
                  print("Error : file does not exist!")
                  return
            def IS_FILE_EMPTY(DATA):
                  """CHECK IF FILE IS EMPTY BY SIZE """
                  return os.path.getsize(DATA) == 0
            if IS_FILE_EMPTY(file_L_name):
                  print(f"Error : No data in '{file_L_name}'")
                  return
            
            # AUTOMATICALLY CLEAR OLD DATA
            if listname:
                  print("the program will delete old DATA")
                  choice= input("Do you agree ? (y/n): ")
                  if choice.upper()=="Y":
                    listname.clear()
                    listgrade.clear()
                  elif choice.upper() == "N":
                        print("The program will save old student data after (3s)")
                        time.sleep(3)
                        SAVE_DATA(listname,listgrade)
                        listname.clear()
                        listgrade.clear()
                  else :
                        print("invalide choice")
                        return
            # LOAD DATA FROM FILE
            with open(file_L_name,'r',encoding='utf-8') as file :
                      for line_number,line in enumerate(file,1):
                            line = line.strip()
                            if not line :
                                LOADS_ERROR+=1
                                continue
                            # split by '|'
                            parts = line.split('|')
                            if  (len(parts)) != 4:
                                  print(f"Error:Invalid format at line{line_number},skipping.")
                                  LOADS_ERROR+=1
                                  continue 
                            # Check if grade contain a  character 
                            if parts[1].isalpha() or parts[2].isalpha() or parts[3].isalpha():
                                  print(f"There is a character on grade place at line {line_number},skipping.")
                                  LOADS_ERROR+=1
                                  continue
                            #Converting grades from 'str' into 'int'
                            name = parts[0]
                            grade1 = int( parts[1] )
                            grade2 = int( parts[2] )
                            grade3 = int( parts[3] )
                            # Check if 1<=grade[i]<=20
                            if not (1 <= grade1 <= 20 and 1 <= grade2 <= 20 and 1 <= grade3 <= 20):
                                  print(f"Error : grade invalid at line{line_number},skipping.")
                                  LOADS_ERROR+=1
                                  continue
                            # Add to lists
                            if name not in listname:
                                    listname.append (name)
                                    listgrade.append([grade1,grade2,grade3])
                                    LOADS_SUCCESS+=1
                            else :
                                    print(f"Error : duplicate student at {line_number},skipping")
                                    LOADS_ERROR+=1
            if len(STD_NAME) >=2:
                print("Perfect,Now you can treat this data choose any choice in the menu and have a best day ")
                print("\n")
                print(f"loading success:{round(LOADS_SUCCESS*100/(LOADS_SUCCESS+LOADS_ERROR),1)} %")
                print(f"loading fail : {round(LOADS_ERROR*100/(LOADS_SUCCESS+LOADS_ERROR),1)} %")
def SAVE_DATA(listname,listgrade):
     try :
        file_name = input ("Enter a file name [default: student.txt]: ").strip() # .strip()to delete space before and after name 
        if not file_name:#if the user don't enter the of the file will be default name students.txt
         file_name = "STUDENT.txt"
        with open (file_name,'w',encoding='utf-8') as file: #Turn the file name into a real file 
                        # Each student data !
            for i in range (len(listname)):
                name = listname[i]
                grades = listgrade[i]
                                # FORMAT ALI|12|14|15
                line = f"{name}|{grades[0]}|{grades[1]}|{grades[2]}"
                file.write(line + "\n") # Add new line 
            print (f"Success : saved {len(listname)} to '{file_name}'")
     except Exception as e :
        print (f"Error: cold not save file .reason {e}")
# Calling all the functions:
welcome = 0
while True :
        if welcome == 0:
            welcome = 1
            print("==================================================")
            print("    Welcome back")
            print("==================================================")
            print("If you have old data drop [8] to upload it :")

        USERCHOICE = MENU()
        if USERCHOICE == 0 :
            decision= input("Do you want to save modification(y/n):").lower()
            if decision == 'y':
                  SAVE_DATA(STD_NAME,STD_GRADE)
                  print("Data saved!")
            else:  
                break
        if USERCHOICE == 1 :
            ADD_NEW(STD_NAME,STD_GRADE)
            continue
        elif USERCHOICE == 2:
            SHOW_ALL(STD_NAME,STD_GRADE)
            continue
        elif USERCHOICE == 3 :
            SEARCH_STD(STD_NAME,STD_GRADE)
            continue                                    
        elif USERCHOICE == 4 :                                    
            AVERAGE(STD_NAME,STD_GRADE)
            continue                                  
        elif USERCHOICE == 5 :                                    
            STATISTICS(STD_NAME,STD_GRADE)
            continue                                    
        elif USERCHOICE == 6 :                                    
            TOP_STD(STD_NAME,STD_GRADE)
            continue                                    
        elif USERCHOICE == 7 :                                    
            SAVE_DATA(STD_NAME,STD_GRADE)
            continue
        elif USERCHOICE == 8 :
              LOAD_DATA(STD_NAME,STD_GRADE)                                    
        else :                                                                   
             print("Error :Choice not in  MENU programme will end after{5s}") 
             time.sleep(5)
             break

