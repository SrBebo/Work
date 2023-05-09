import os # library that let me interact with the OS and get the paths of files

name_file = input("Enter the name of file: \n") #We request the name of file 
print("The name of file is: ", name_file) #Print the name of file
print("\n")
file_path = os.path.abspath(name_file) #Get the path of file
print("The path of file is: ", file_path) #Print the path of file

file=open(name_file,"r") #Open the file and read the content
content=file.read() #Save the content of file in the variable "content"

words=content.split() #Separate the words with split

frequency = {} #We declare the dictionary

for word in words: #using a bucle for we count the repetitions of the words
    frequency[word] = frequency.get(word, 0) + 1

for word in sorted(frequency):
    print(word, "---", frequency[word])
