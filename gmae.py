import random

num=random.randint(10000,99999)
numstr=str(num)
yournum=0
print("I have a 5 digit number for you can you guess it?")
while(yournum!=num):

    yournumstr=input("Give number: ")

    try:
        yournum=int(yournumstr)

        while(yournum>99999 or yournum<10000):
            if yournum>99999:
                yournum=yournum/10
            elif yournum<10000:
                yournum*=10

        yournumstr=str(yournum)  
        closeness=0
        finalstring=""
        for index in range(0,len(yournumstr)):
            if(str(numstr[index])==str(yournumstr[index])):
                finalstring+="\033[1;32;40m"+yournumstr[index] +"\033[0m"
                closeness+=3
            elif(yournumstr[index] in numstr):
                finalstring+="\033[1;33;40m"+yournumstr[index] +"\033[0m"    
                closeness+=1
            else:
                finalstring+="\033[1;31;40m"+yournumstr[index] +"\033[0m"
                
        print(finalstring)

        if(closeness>9 and closeness!=15):
            print("Nearly there")
        elif(closeness==15):
            print("You guessed correct. Congrats")
        elif(closeness>5):
            print("You are doing good, keep it up")
        else:
            print("Don't give up, you can do it")
        
    except:
        print("Give valid input :(")