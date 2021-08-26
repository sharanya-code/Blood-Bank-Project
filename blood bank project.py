import pickle #IMPORTING PICKLE MODULE TO USE AND OPERATE BINARY FILE

f1=open('file name.txt','r') #OPENING A TEXT FILE TO LOOK AT NAMES OF THE FILES IN THE CURRENT SYSTEM
print(f1.read())
f1.close()
mn=('Name','PhoneNo','Address','Age','Gender','BloodGroup','Cholestrol')
name=input('Enter The Name Of City:  ')

j=name+'blood bank.dat' #TAKING THE INPUT FOR THE NAME AND USING FOR PROGRAM
L=[]
file=open(j,'wb') #OPENING THE BINARY FILE
pickle.dump(L,file)
file.close()

def append():
    print('\n')
    Name=input('Enter the name: ') #TAKING INPUTS
    phone=int(input('Enter The Phone Number: '))
    add=input('Enter The Address: ')
    age=int(input('Enter the age: '))
    gen=input('Enter the Gender: ')
    bg=input('Enter the BloodGroup: ')
    chol=int(input('Enter the Cholestrol level: '))
    
    data=[Name,phone,add,age,gen,bg,chol]
    while True:
        try: #CHECKING IF THE FILE EXISTS IN THE SYSTEM
            inFile=open(j,"rb")
            List=pickle.load(inFile)
            inFile.close()
            break
        except:
            List=[]
    List.append(data) #APPENDING DATA 
    outFile=open(j,"wb")
    pickle.dump(List,outFile) #WRITING INTO THE FILE
    outFile.close()
    
def Display():
    print("\n")
    inFile=open(j,"rb")
    List=pickle.load(inFile) #TO DISPLAY THE BINARY FILE
    inFile.close()
    print(List)
    
def Search():
    print('SEARCH MENU')
    print('\n') #TAKING INPUT
    print('1.Search by Blood Group')
    print('2.Search by Phone Number')
    ch=int(input('Enter The Choice: '))

    found=0

    if(ch==1):
        b=input("Enter Blood Group of the Person to be searched : ")
    else:
        p=int(input("Enter Phone Number of the Person to be searched: "))
        
    while True:
        try:
            inFile=open(j,"rb")
            List=pickle.load(inFile)
            inFile.close()
            break
        except:
            List=[]
            break
    print('Result')
    for L in List:
        if(ch==1 and b==L[5]): #CHECKING THE INPUT WITH DATA
             print(L)
             found=1
        elif(ch==2 and p==L[1]):
             print(L)
             found=1
    if (found==0):
         print('No Match Found')
         
def health():
    print('Checking Health status')
    while True:
        try:
            inFile=open(j,"rb")
            List=pickle.load(inFile)
            inFile.close()
            break
        except:
            List=[]
            break
    for i in List:
        if (int(i[6])>6): #CHECKING FOR HIGH CHOLESTROL
            print('High Cholestrol',i)
        elif (int(i[6]>4)) and (int(i[6])<2):
            print('Normal Cholestrol',i)

            
def modify():
     FoundIndex=-1
    
     print("1. Modify by Name.\n")
     print("2. Modify by Phone Number.\n")
     Ch=int(input("Enter your choice: "))

     if(Ch==1):
         Name=input("Enter Name of the Person to be modified: ")
     elif(Ch==2):
         PhoneNo=int(input("Enter Phone Number of the Person to be modified: "))

     while True:
         try:
             inFile=open(j,"rb")
             List=pickle.load(inFile)
             inFile.close()
             break
         except:
             List=[]
             break

     for i in range(len(List)):
         L=List[i]
         if (Ch==2 and PhoneNo==L[1]):#CHECKING IF THE INPUT EXISTS
             FoundIndex=i
             PhoneNo=List[i][1]
             newPhoneNo=int(input("Enter the Modified Phone Number of the Person: "))
             List[i][1]=newPhoneNo #CHANGING THE PHONE NUMBER
             print(PhoneNo," has been modified as ",newPhoneNo)
             break
         elif(Ch==1 and Name==L[0]):
             FoundIndex=i
             Name=List[i][0]
             newName=input("Enter the Modified Name of the Person: ")
             List[i][0]=newName #CHANGING THE NAME
             print(Name," has been modified as ",newName)
            

             break


     if(FoundIndex==-1):
         print("No Match Found!")
     else:
         outFile=open(j,"wb")
         pickle.dump(List,outFile)
         outFile.close()
        
def delete():
    
    FoundIndex=-1
    print("1. Delete by Address.\n")
    print("2. Delete by Phone Number.\n")
    Ch=int(input("Enter your choice: "))

    if(Ch==1):
        Add=input("Enter Address of the Person to be deleted: ")
    else:
        PhoneNo=int(input("Enter Phone Number of the Person to be deleted: "))

    while True:
        try:
            inFile=open(j,"rb")
            List=pickle.load(inFile)
            inFile.close()
            break
        except:
            List=[]
            break

    for i in range(len(List)):
        L=List[i]
        if (Ch==1 and Add==L[2]):
            FoundIndex=i
            break
        elif(Ch==2 and PhoneNo==L[1]):
            FoundIndex=i
            break


    if(FoundIndex==-1):
        print("No Match Found!")
    else:
        Data=List.pop(FoundIndex) #DELETING THE DATA FROM LIST
        print(Data," has been deleted!")
        outFile=open(j,"wb")
        pickle.dump(List,outFile) #COPYING THE NEW DATA TO FILE
        outFile.close()
        

while True: #MAIN MENU 
    print('\n\n')
    print('CITY SCALE BLOOD BANK DATA')
    print('DEVELOPED BY SHARANYA GUPTA AND SHASHANK GOSWAMI BY MODERN SCHOOL BARAKHAMBA ROAD')
    print('\n')
    print('THE FILE IS A BINARY FILE')
    print('\n')
    print('**********MAIN MENU**********')
    print('\n\n')
    print('DIRECTIONS FOR USING THE PROGRAM')
    print('\n\n')
    print('1. Append into the File')
    print('2. Display the File')
    print('3. Search Something from File')
    print('4. Health Check for Donors')
    print('5. Modify in the File')
    print('6. Delete from the File')
    Choice=int(input("Enter your choice: ")) #TAKING THE INPUT
    if (Choice==1): #CHECKING THE INPUT
        append()
    elif (Choice==2):
        Display()
    elif (Choice==3):
        Search()
    elif (Choice==4):
        health()
    elif (Choice==5):
        modify()
    elif (Choice==6):
        delete()
    else:
        break
    
    

