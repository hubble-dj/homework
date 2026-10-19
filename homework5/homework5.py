# 2 vocab review 
# Git is the tool that saves coded work into remote repositories, and Github is the website interface. 
# Terminal is where you interact with your computer using shell commands, and the command line is where you write your commands. 
# Local is on your computure while remote is on the cloud
# Staging area is the files you've prepared to be put in the remote repository. 
# Git add adds something to the staging area
# Git commit commits the thigs in the staging area with a message
#Git push puts the staging area into the remote repository
# Git status tells the status of all files in your current directory, and whether they are staged 
# Git pull pulls the latest changes to the git repository
#print working directory 
# Shows files/directories in current position 
# cd change directory
#nano creates a text file
# touch creates a text file but doesn't enter it 
#mv move 
#remove 
#cat shows content of a file 

#2.2 Directory Tree 
#1. pwd
#2. ls
#3. git pull 
#4. mv homework.py homework/
#5. cd ../brianna_repo
#6. cat homework.py
#7. git add git commit -m "asifbuas" git push 
#8. git pull then do it again 


#3 
def dastardly(x):
    print(type(x))

def evenodd(x):
    if x%2 == 0:
        print("even")
    else:
        print("odd")

def summm(list):
    n=0
    for i in list:
        n += i
    return n

# 5 

def doublelist(list):
    list2= list * 2
    return list2

def square(num):
    new = num * num
    return new 

print(doublelist([1,5,10]))