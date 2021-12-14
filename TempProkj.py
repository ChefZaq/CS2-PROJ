import glob
import shutil  #os features like copy photo
import os   
import random # randomized selected in list
import schedule #how to schedule tasks
import time  # minutes seconds days


def photo_copy():

    #Source Folder
    os.chdir('D:\\Users\\chese\\Desktop\\Jojo\\1. Phantom Blood')#file_sourcepath)#'D:\\Users\\chese\\Desktop\\Jojo\\1. Phantom Blood')
    
    #Destination Folder
    dst_dir = "D:/Users/chese/Desktop/VS Code/Python_Code/TempForProj" #file_destpath
    ImageList = os.listdir() 
    RandomImage = random.choice(ImageList)
    if not (already_exists(RandomImage)):
        shutil.copy(RandomImage,dst_dir)
    elif already_exists(RandomImage):
        pass
    else:
        print("All Photos Has Been Selected !")

# adjust by setting scheduled time
def schedule_select(ScheduleInput):
    if ScheduleInput == "M" or ScheduleInput == "m":
        print(ScheduleInput)
        schedule_by_minutes()
    elif ScheduleInput == "H" or ScheduleInput == "h":
        print(ScheduleInput)
        schedule_by_hours()
    elif ScheduleInput == "W" or ScheduleInput == "w":
        print(ScheduleInput)
        schedule_by_weekday()
    elif ScheduleInput == "D" or ScheduleInput == "d":
        print(ScheduleInput)
        schedule_by_daily()
    elif ScheduleInput == "T" or ScheduleInput == "t":
       print(ScheduleInput)
       schedule_by_time_and_day()
    else:
        print("Try Again Later , Please Enter The Correct Option Choice")
     #print(ScheduleInput)
    
def schedule_by_minutes ():
    print("Would You Like Schedule Every X Minute From Now or Every X Minute At a Specfied Second?\n") 
    print("\t 1 - Would You Like Schedule Every X Minute From Now\n") 
    print("\t 2 - Every X Minute At a Specfied Second?\n")
    VerifyOption = int(input("Enter The Following Choices Above: "))
    if VerifyOption == 1:
        print("Please Enter The Amount Of Minutes You Want To Schedule From 1-59 Minutes. ")
        AmountOfMinutes = int(input("Minutes: "))
        if AmountOfMinutes < 1 or AmountOfMinutes > 59:
            print("You Entered The Wrong Amount Of Time , Please Try Again Later.")
        else:
            schedule.every(AmountOfMinutes).minutes.do(photo_copy)
            while True:
                schedule.run_pending()
                time.sleep(1)
    elif VerifyOption == 2:
        print("Please Enter The Second on The Minute You Want To Schedule From 1-59 Seconds. ")
        AmountOfSeconds = int(input("Second: "))
        if AmountOfSeconds < 1 or AmountOfSeconds > 59:
            print("You Entered The Wrong Amount Of Time , Please Try Again Later.")
        else:
            print("Schedule Set For Every Minute At :{X} Second.".format(X = AmountOfSeconds))
            schedule.every().minute.at(":{X}".format(X = AmountOfSeconds)).do(photo_copy)
            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("You Have Incorrectly Typed The Code Try Again Later")
          
def schedule_by_hours ():
    print("Would You Like Schedule Every X Hour From Now or Every X Hour At a Specfied Minute?\n") 
    print("\t 1 - Would You Like Schedule Every X Hour From Now\n") 
    print("\t 2 - Every X Hour At a Specfied Minute?\n")
    VerifyOption = int(input("Enter The Following Choices Above: "))
    if VerifyOption == 1:
        print("Please Enter The Amount Of Hours You Want To Schedule From 1-24 Hours. ")
        AmountOfHours = int(input("Hours: "))
        if AmountOfHours < 1 or AmountOfHours > 24:
            print("You Entered The Wrong Amount Of Time , Please Try Again Later.")
        else:
            schedule.every(AmountOfHours).hours.do(photo_copy)
            while True:
                schedule.run_pending()
                time.sleep(1)
    elif VerifyOption == 2:
        print("Please Enter The Minute On The Hour You Want To Schedule From 1-59 Minutes. ")
        AmountOfMinutes = int(input("Minute: "))
        if AmountOfMinutes < 1 or AmountOfMinutes > 59:
            print("You Entered The Wrong Amount Of Time , Please Try Again Later.")
        else:
            print("Schedule Set For Every Hour At :{X} Minute.".format(X = AmountOfMinutes))
            schedule.every().hour.at(":{X}".format(X = AmountOfMinutes)).do(photo_copy)
            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("You Have Incorrectly Typed The Code Try Again Later")

def schedule_by_weekday ():

    print("\t 1 - Sunday\n") 
    print("\t 2 - Monday\n")
    print("\t 3 - Tuesday\n") 
    print("\t 4 - Wedsnesday\n")
    print("\t 5 - Thursday\n") 
    print("\t 6 - Friday\n")
    print("\t 7 - Saturday\n")
    VerifyOption = int(input("Please Selcet One Of The Following Number Choices Above: "))
    if VerifyOption == 1:
       schedule.every().sunday.do(photo_copy)
       while True:
            schedule.run_pending()
            time.sleep(1)

    elif VerifyOption == 2:
        schedule.every().monday.do(photo_copy)
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    elif VerifyOption == 3:
       schedule.every().tuesday.do(photo_copy)
       while True:
            schedule.run_pending()
            time.sleep(1)
      
    elif VerifyOption == 4:
       schedule.every().wednesday.do(photo_copy)
       while True:
            schedule.run_pending()
            time.sleep(1)
      
    elif VerifyOption == 5:
       schedule.every().thursday.do(photo_copy)
       while True:
            schedule.run_pending()
            time.sleep(1)
      
    elif VerifyOption == 6:
        schedule.every().friday.do(photo_copy)
        while True:
            schedule.run_pending()
            time.sleep(1)
      
    elif VerifyOption == 7:
       schedule.every().saturday.do(photo_copy)
       while True:
            schedule.run_pending()
            time.sleep(1)  
    else:
        print("You Have Incorrectly Typed The Code Try Again Later")
        
def schedule_by_daily ():
    print("Please Enter The Hour and Minute You Want To Schedule.\n")
    HourSelect = int(input("Hour: "))
    MinuteSelect = int(input("Minute: "))
    if MinuteSelect < 1 or MinuteSelect > 59 or HourSelect < 1 or HourSelect > 24:
        print("You Entered The Wrong Amount Of Time , Please Try Again Later.")
    else:
        print("Schedule Set For Every Day At {X}:{Y}.".format(X = HourSelect, Y= MinuteSelect))
        schedule.every().day.at("{X}:{Y}".format(X = HourSelect, Y= MinuteSelect)).do(photo_copy)
        while True:
            schedule.run_pending()
            time.sleep(1)
                
def schedule_by_time_and_day ():
    print("\t 1 - Sunday\n") 
    print("\t 2 - Monday\n")
    print("\t 3 - Tuesday\n") 
    print("\t 4 - Wednesday\n")
    print("\t 5 - Thursday\n") 
    print("\t 6 - Friday\n")
    print("\t 7 - Saturday\n")
    VerifyOption = int(input("Please Selcet One Of The Following Number Choices Above: "))
    if VerifyOption == 1:
        print("Please Enter The Hour and Minute You Want To Schedule On Sunday.\n")
        HourSelect = int(input("Hour: "))
        MinuteSelect = int(input("Minute: "))
        if MinuteSelect < 1 or MinuteSelect > 59 or HourSelect < 1 or HourSelect > 24:
            print("You Entered The Wrong Amount Of Time , Please Try Again Later.")
        else:
            print("Schedule Set For Every Sunday At {X}:{Y}.".format(X = HourSelect, Y= MinuteSelect))
            schedule.every().sunday.at("{X}:{Y}".format(X = HourSelect, Y= MinuteSelect)).do(photo_copy)
            while True:
                schedule.run_pending()
                time.sleep(1)
    
    elif VerifyOption == 2:
        print("Please Enter The Hour and Minute You Want To Schedule On Monday.\n")
        HourSelect = int(input("Hour: "))
        MinuteSelect = int(input("Minute: "))
        if MinuteSelect < 1 or MinuteSelect > 59 or HourSelect < 1 or HourSelect > 24:
            print("You Entered The Wrong Amount Of Time , Please Try Again Later.")
        else:
            print("Schedule Set For Every Monday At {X}:{Y}.".format(X = HourSelect, Y= MinuteSelect))
            schedule.every().monday.at("{X}:{Y}".format(X = HourSelect, Y= MinuteSelect)).do(photo_copy)
            while True:
                schedule.run_pending()
                time.sleep(1)
    
    elif VerifyOption == 3:
        print("Please Enter The Hour and Minute You Want To Schedule On Tuesday.\n")
        HourSelect = int(input("Hour: "))
        MinuteSelect = int(input("Minute: "))
        if MinuteSelect < 1 or MinuteSelect > 59 or HourSelect < 1 or HourSelect > 24:
            print("You Entered The Wrong Amount Of Time , Please Try Again Later.")
        else:
            print("Schedule Set For Every Tuesday At {X}:{Y}.".format(X = HourSelect, Y= MinuteSelect))
            schedule.every().tuesday.at("{X}:{Y}".format(X = HourSelect, Y= MinuteSelect)).do(photo_copy)
            while True:
                schedule.run_pending()
                time.sleep(1)
    
    elif VerifyOption == 4:
        print("Please Enter The Hour and Minute You Want To Schedule On Wednesday.\n")
        HourSelect = int(input("Hour: "))
        MinuteSelect = int(input("Minute: "))
        if MinuteSelect < 1 or MinuteSelect > 59 or HourSelect < 1 or HourSelect > 24:
            print("You Entered The Wrong Amount Of Time , Please Try Again Later.")
        else:
            print("Schedule Set For Every Wednesday At {X}:{Y}.".format(X = HourSelect, Y= MinuteSelect))
            schedule.every().wednesday.at("{X}:{Y}".format(X = HourSelect, Y= MinuteSelect)).do(photo_copy)
            while True:
                schedule.run_pending()
                time.sleep(1)
      
    elif VerifyOption == 5:
        print("Please Enter The Hour and Minute You Want To Schedule On Thursday.\n")
        HourSelect = int(input("Hour: "))
        MinuteSelect = int(input("Minute: "))
        if MinuteSelect < 1 or MinuteSelect > 59 or HourSelect < 1 or HourSelect > 24:
            print("You Entered The Wrong Amount Of Time , Please Try Again Later.")
        else:
            print("Schedule Set For Every Thursday At {X}:{Y}.".format(X = HourSelect, Y= MinuteSelect))
            schedule.every().thursday.at("{X}:{Y}".format(X = HourSelect, Y= MinuteSelect)).do(photo_copy)
            while True:
                schedule.run_pending()
                time.sleep(1)
      
    elif VerifyOption == 6:
        print("Please Enter The Hour and Minute You Want To Schedule On Friday.\n")
        HourSelect = int(input("Hour: "))
        MinuteSelect = int(input("Minute: "))
        if MinuteSelect < 1 or MinuteSelect > 59 or HourSelect < 1 or HourSelect > 24:
            print("You Entered The Wrong Amount Of Time , Please Try Again Later.")
        else:
            print("Schedule Set For Every Friday At {X}:{Y}.".format(X = HourSelect, Y= MinuteSelect))
            schedule.every().friday.at("{X}:{Y}".format(X = HourSelect, Y= MinuteSelect)).do(photo_copy)
            while True:
                schedule.run_pending()
                time.sleep(1)
      
    elif VerifyOption == 7:
        print("Please Enter The Hour and Minute You Want To Schedule On Saturday.\n")
        HourSelect = int(input("Hour: "))
        MinuteSelect = int(input("Minute: "))
        if MinuteSelect < 1 or MinuteSelect > 59 or HourSelect < 1 or HourSelect > 24:
            print("You Entered The Wrong Amount Of Time , Please Try Again Later.")
        else:
            print("Schedule Set For Every Saturday At {X}:{Y}.".format(X = HourSelect, Y= MinuteSelect))
            schedule.every().saturday.at("{X}:{Y}".format(X = HourSelect, Y= MinuteSelect)).do(photo_copy)
            while True:
                schedule.run_pending()
                time.sleep(1)
    
    else:
        print("You Have Incorrectly Typed The Code Try Again Later")  

def already_exists(RandomImage):
    exists = os.path.exists("D:/Users/chese/Desktop/VS Code/Python_Code/TempForProj/{x}".format(x = RandomImage))
    

print("Hello Welcome To Instabot!")
print("You Will Now Create Your Schedule For Your Instabot.")
#print("Please Enter From One Of The Following Options: M - Minutes , H - Hours , W - Weekday , D - Daily , T - Time On Weekday" )

OptionChoice = True
while OptionChoice:
    ScheduleOption = input("Please Enter From One Of The Following Options: M - Minutes , H - Hours , W - Weekday , D - Daily , T - Time On Weekday : ")
    print("You Have Selected: " + ScheduleOption)
    VerifyOption = input ("Is This Correct? (Y/N): ")
    if VerifyOption == "Y" or VerifyOption ==  "y":
        schedule_select(ScheduleOption)
        OptionChoice = False
    elif VerifyOption == "N" or VerifyOption ==  "n":
        continue
    else:
        print("Please Restart The Program And Try Again. ")
        OptionChoice = False




