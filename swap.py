def swapText():
     file1=input("Enter a file ")
     file2=input("Enter second file ")
     a=open(file1,'r')
     b=open(file2,'r')
     data_a=a.read()
     data_b=b.read()
     a.write(data_b)
     b.write(data_a)
     #with open(file1,'r') as a:
      #   data_a=a.read()
    #with open(file2,'r') as b:
         
      #  data_b=b.read()

    
swapText()