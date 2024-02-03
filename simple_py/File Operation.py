#*********************************************
##########################################################################
#file create,open ,write,append,read  and closing function  

file1=open("Aro1.txt","w")
file1.write("welcome to python chiatol")
file1.close()


file1=open("Aro1.txt","a")
file1.write(" in oporajita school")
file1.close()



file1=open("Aro1.txt","r")
print(file1.read())
file1.close()

##########################################################################
#Program to check if a file is close

file1=open("Aro.txt","w")
print(file1.closed)
file1.close()
print(file1.closed)

#########################################################################
with open("Aro1.txt", "r") as file1:
    words = file1.read().split()
    max_len = max(len(word) for word in words)

print(max_len)

file1=open("Aro1.txt","r")
word=file1.read().split()
max_len = len(max(word,key=len))
print(max_len)


with open("Aro1.txt", "r") as file1:
    words = file1.read().split()
    longest_word = max(words, key=len)

print(longest_word)

with open("Aro1.txt","r") as file1:
    word=file1.read().split()
    longest_word  = (max(word,key=len))
    print(longest_word )

    

