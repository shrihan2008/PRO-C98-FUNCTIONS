def swapText():
     file1=input("Enter First File - ")
     file2=input("Enter Second File - ")

     with open(file1, 'r') as a:
          data_a=a.read()

     with open(file2, 'r') as a:
          data_b=a.read()

     with open(file1, 'w') as a:
          a.write(data_b)
          print("Done swapping file1")

     with open(file2, 'w') as a:
          a.write(data_a)
          print("Done swapping file2")

swapText()