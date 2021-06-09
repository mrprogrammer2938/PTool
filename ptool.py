#!/usr/bin/python3
# This code write by (Mr.nope)
import os
import time
class color:
    green = '\033[92m'
    red = '\033[91m'
    white = '\033[0m'
PTool = color.green + "\nPTool>/ " + color.white
time.sleep(1)
os.system("clear")
print(color.green + """
      (                      
       )\ )  *   )    (   
      (()/(` )  /( (|  )\  
     /(_))( )(_)| ( ((_) 
    (_)) (_(_()))\   )\ _   
    | _ \|_   _((_) ((_) |  
    |  _/  | |/ _ \/ _ \ |  
    |_|    |_|\___/\___/_|""" + color.red + """
         (🅟🅣🅞🅞🅛) """ + color.white + "\n")
print("\t1.install package")
print("\t2.update package")
print("\t3.Help")
print("\t4.Exit")
choose = str(input(PTool))
if(str(choose) == '1'):
  time.sleep(1)
  os.system("clear")
  print(color.green)
  os.system("figlet PTool")
  print(color.white)
  print("1.python")
  print("2.python2")
  print("3.python3")
  print("4.php")
  print("5.java")
  print("6.c#")
  print("7.c")
  print("8.c++")
  print("9.installing All package")
  print("10.main menu")
  choose2 = str(input(PTool))
  if(str(choose2) == '1'):
    time.sleep(1)
    os.system("sudo apt install python")
    try3 = str(input("Do you want go to mein menu [y/n] "))
    if(str(try3) == 'y'):
      os.system("python3 ptool.py")
    elif(str(try3) == 'n'):
        time.sleep(1)
        os.system("clear")
        print("good bye")
        exit(1)
    else:
        time.sleep(1)
        os.system("clear")
        time.sleep(1)
        print(color.red + "Error PTool" + color.white)
        time.sleep(2)
        try4 = str(input("press Enter... "))
        if(str(try4) == ''):
          os.system("python3 ptool.py")
        else:
            os.system("python3 ptool.py")
  elif(str(choose2) == '2'):
      time.sleep(1)
      os.system("sudo apt install python2")
      time.sleep(1)
      try4 = str(input("Do you want go to mein menu [y/n] "))
      if(str(try4) == 'y'):
        os.system("python3 ptool.py")
      elif(str(try3) == 'n'):
          time.sleep(1)
          os.system("clear")
          print("good bye")
          exit(1)
      else:
          time.sleep(1)
          os.system("clear")
          time.sleep(1)
          print(color.red + "Error PTool" + color.white)
          time.sleep(2)
          try5 = str(input("press Enter... "))
          if(str(try5) == ''):
            os.system("python3 ptool.py")
          else:
              os.system("python3 ptool.py")
  elif(str(choose2) == '3'):
      time.sleep(1)
      os.system("sudo apt install python3")
      time.sleep(1)
      try7 = str(input("Do you want go to mein menu [y/n] "))
      if(str(try7) == 'y'):
        os.system("python3 ptool.py")
      elif(str(try7) == 'n'):
          time.sleep(1)
          os.system("clear")
          print("good bye")
          exit(1)
      else:
          time.sleep(1)
          os.system("clear")
          time.sleep(1)
          print(color.red + "Error PTool" + color.white)
          time.sleep(2)
          try10 = str(input("press Enter... "))
          if(str(try10) == ''):
            os.system("python3 ptool.py")
          else:
              os.system("python3 ptool.py")
  elif(str(choose2) == '4'):
      time.sleep(1)
      os.system("sudo apt install php")
      time.sleep(1)
      try8 = str(input("Do you want go to mein menu [y/n] "))
      if(str(try8) == 'y'):
        os.system("python3 ptool.py")
      elif(str(try8) == 'n'):
          time.sleep(1)
          os.system("clear")
          print("good bye")
          exit(1)
      else:
          time.sleep(1)
          os.system("clear")
          time.sleep(1)
          print(color.red + "Error PTool" + color.white)
          time.sleep(2)
          try9 = str(input("press Enter... "))
          if(str(try9) == ''):
            os.system("python3 ptool.py")
          else:
              os.system("python3 ptool.py") 
  elif(str(choose2) == '5'):
      time.sleep(1)
      os.system("sudo apt install java")
      time.sleep(1)
      try11 = str(input("Do you want go to mein menu [y/n] "))
      if(str(try11) == 'y'):
        os.system("python3 ptool.py")
      elif(str(try7) == 'n'):
          time.sleep(1)
          os.system("clear")
          print("good bye")
          exit(1)
      else:
          time.sleep(1)
          os.system("clear")
          time.sleep(1)
          print(color.red + "Error PTool" + color.white)
          time.sleep(2)
          try12 = str(input("press Enter... "))
          if(str(try12) == ''):
            os.system("python3 ptool.py")
          else:
              os.system("python3 ptool.py")  
  elif(str(choose2) == '6'):
      try13 = str(input("Do you want go to mein menu [y/n] "))
      if(str(try13) == 'y'):
        os.system("python3 ptool.py")
      elif(str(try13) == 'n'):
          time.sleep(1)
          os.system("clear")
          print("good bye")
          exit(1)
      else:
          time.sleep(1)
          os.system("clear")
          time.sleep(1)
          print(color.red + "Error PTool" + color.white)
          time.sleep(2)
          try14 = str(input("press Enter... "))
          if(str(try14) == ''):
            os.system("python3 ptool.py")
          else:
              os.system("python3 ptool.py")                
  elif(str(choose2) == '7'):
      time.sleep(1)
      os.system("sudo apt install c#")
      time.sleep(1)
      try14 = str(input("Do you want go to mein menu [y/n] "))
      if(str(try14) == 'y'):
        os.system("python3 ptool.py")
      elif(str(try7) == 'n'):
          time.sleep(1)
          os.system("clear")
          print("good bye")
          exit(1)
      else:
          time.sleep(1)
          os.system("clear")
          time.sleep(1)
          print(color.red + "Error PTool" + color.white)
          time.sleep(2)
          try15 = str(input("press Enter... "))
          if(str(try15) == ''):
            os.system("python3 ptool.py")
          else:
              os.system("python3 ptool.py")
  elif(str(choose2) == '7'):
      time.sleep(1)
      os.system("sudo apt install c")
      time.sleep(1)
      try16 = str(input("Do you want go to mein menu [y/n] "))
      if(str(try16) == 'y'):
        os.system("python3 ptool.py")
      elif(str(try7) == 'n'):
          time.sleep(1)
          os.system("clear")
          print("good bye")
          exit(1)
      else:
          time.sleep(1)
          os.system("clear")
          time.sleep(1)
          print(color.red + "Error PTool" + color.white)
          time.sleep(2)
          try17 = str(input("press Enter... "))
          if(str(try17) == ''):
            os.system("python3 ptool.py")
          else:
              os.system("python3 ptool.py")
  elif(str(choose2) == '8'):
      time.sleep(1)
      os.system("sudo apt install c++")
      time.sleep(1)
      try18 = str(input("Do you want go to mein menu [y/n] "))
      if(str(try18) == 'y'):
        os.system("python3 ptool.py")
      elif(str(try7) == 'n'):
          time.sleep(1)
          os.system("clear")
          print("good bye")
          exit(1)
      else:
          time.sleep(1)
          os.system("clear")
          time.sleep(1)
          print(color.red + "Error PTool" + color.white)
          time.sleep(2)
          try19 = str(input("press Enter... "))
          if(str(try19) == ''):
            os.system("python3 ptool.py")
          else:
              os.system("python3 ptool.py")
  elif(str(choose2) == '9'):
      time.sleep(1)
      os.system("sudo apt install python3 && sudo apt install python && sudo apt install python2 && sudo apt install php && sudo apt install java && sudo apt install c && sudo apt install c++")
      time.sleep(1)
      try20 = str(input("Do you want go to mein menu [y/n] "))
      if(str(try20) == 'y'):
        os.system("python3 ptool.py")
      elif(str(try7) == 'n'):
          time.sleep(1)
          os.system("clear")
          print("good bye")
          exit(1)
      else:
          time.sleep(1)
          os.system("clear")
          time.sleep(1)
          print(color.red + "Error PTool" + color.white)
          time.sleep(2)
          try21 = str(input("press Enter... "))
          if(str(try21) == ''):
            os.system("python3 ptool.py")
          else:
              os.system("python3 ptool.py")
  elif(str(choose2) == '10'):
      time.sleep(1)
      os.system("python3 ptool.py")
  elif(str(choose2) == ''):
      time.sleep(1)
      os.system("python3 ptool.py")
  elif(str(choose2) == ' '):
      time.sleep(1)
      os.system("python3 ptool.py")
  else:
      time.sleep(1)
      os.system("clear")
      time.sleep(1)
      print(color.red + "Error PTool!" + color.white)
      time.sleep(2)
      try24 = str(input("press Enter... "))
      if(str(try24) == ''):
        os.system("python3 ptool.py")
      else:
          os.system("python3 ptool.py")
elif(str(choose) == '2'):
    time.sleep(1)
    os.system("clear")
    time.sleep(1)
    print(color.green)
    os.system("figlet PTool")
    print(color.white)
    print("1.update system")
    print("2.upgrade system")
    print("3.mein menu")
    choose3 = str(input(PTool))
    if(str(choose3) == '1'):
      time.sleep(1)
      os.system("sudo apt update")
      time.sleep(1)
      try21 = str(input("Do you want go to mein menu [y/n] "))
      if(str(try21) == 'y'):
        os.system("python3 ptool.py")
      elif(str(try21) == 'n'):
          time.sleep(1)
          os.system("clear")
          print("good bye")
          exit(1)
      else:
          time.sleep(1)
          os.system("clear")
          time.sleep(1)
          print(color.red + "Error PTool" + color.white)
          time.sleep(2)
          try21 = str(input("press Enter... "))
          if(str(try21) == ''):
            os.system("python3 ptool.py")
          else:
              os.system("python3 ptool.py")
    elif(str(choose3) == '2'):
        time.sleep(1)
        os.system("sudo apt upgrade")
        time.sleep(1)
        try7 = str(input("Do you want go to mein menu [y/n] "))
        if(str(try22) == 'y'):
          os.system("python3 ptool.py")
        elif(str(try22) == 'n'):
            time.sleep(1)
            os.system("clear")
            print("good bye")
            exit(1)
        else:
            time.sleep(1)
            os.system("clear")
            time.sleep(1)
            print(color.red + "Error PTool" + color.white)
            time.sleep(2)
            try23 = str(input("press Enter... "))
            if(str(try23) == ''):
              os.system("python3 ptool.py")
            else:
                os.system("python3 ptool.py")
    elif(str(choose3) == '3'):
        time.sleep(1)
        os.system("python3 ptool.py")
    elif(str(choose3) == ''):
        time.sleep(1)
        os.system("python3 ptool.py")
    elif(str(choose3) == ' '):
        os.system("python3 ptool.py")
    else:
      time.sleep(1)
      os.system("clear")
      time.sleep(1)
      print(color.red + "Error PTool!" + color.white)
      time.sleep(2)
      try25 = str(input("press Enter... "))
      if(str(try25) == ''):
        os.system("python3 ptool.py")
      else:
          os.system("python3 ptool.py")
elif(str(choose) == '3'):
    os.system("clear")
    time.sleep(1)
    print("""
This code write by (Mr.nope)
usage:
     1 - and install pkg
     2 - and update your system
     3 - informtions package
     4 - Exit package :(
""")
    time.sleep(2)
    try26 = input("\npress Enter... ")
    if try26) == '':
      os.system("python3 ptool.py")
    else:
        os.system("python3 ptool.py")
elif(str(choose) == '4'):
    os.system("clear")
    time.sleep(1)
    print("Exiting...")
    exit()
elif(str(choose) == ''):
    os.system("python3 ptool.py")
elif(str(choose) == ' '):
    os.system("python3 ptool.py")
else:
    time.sleep(1)
    os.system("clear")
    time.sleep(1)
    print(color.red + "Error PTool!" + color.white)
    time.sleep(2)
    try27 = str(input("press Enter... "))
    if(str(try27) == ''):
      os.system("python3 ptool.py")
    else:
        os.system("python3 ptool.py")
# ptool
