def write(textfile, a):
    try:
        with open(textfile, 'w') as file:
            file.write(a)
            print("Content written to the file successfully!")
    except IOError:
        print("Error: Could not write to the file.")

def read(textfile):
    try:
        with open(textfile, 'r') as file:
            a= file.read()
            print("Content read from the file:")
            print(a)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Could not read from the file.")

def a():
  f=open("song titanic.txt","r")
  data=f.read()
  print(data)
  f.close()
  
def length():
  f=open("song titanic.txt","r")
  data=f.read()
  l=len(data)
  print(l)
  f.close()

def T():
  f=open("song titanic.txt","r")
  data=f.readlines()
  count=0
  for line in data:
    if line[0]=="T":
      count+=1
  f.close()
  print("The no. if line starting with T ", count)

def uppercheck():
  f=open("song titanic.txt","r")
  data=f.read()
  count=0
  for i in data:
    if i.islower():
      count+=1
  f.close()
  print("The no. uppercase letters are ", count)

def main():
    textfile = "test.txt"
    a = "Hello, this is a file handling example.\nHave a nice day!"

    write(textfile, a)
    read(textfile)
main()
a()
length()
T()
