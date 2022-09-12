def swpfile():

    file1 = "a.txt"
    file2 = "b.txt"

    with open(file1, "r")as a:
        dataA = a.read()

    with open(file2, "r")as b:
        dataB = b.read()     

    with open(file1, "w") as a:
        a.write (dataB)

    with open(file2,"w") as b:
        b.write (dataA)        

swpfile()       
