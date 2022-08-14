#Counts the number of lines in a file and displays it 
print(len([k for k in open("class.txt","r").read().split("\n") if len(k)>0]))
