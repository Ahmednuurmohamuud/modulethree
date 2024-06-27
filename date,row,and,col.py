def read_file(file):
    with open(file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)

def split_file(file):
    with open(file, 'r') as file:
        data = file.read()
        print(data)
        new = data.split(",")
        print(new[3:7])
        


file= "Data analaysis sample.csv"


read_file(file)

split_file(file)













































         
#file = open("Data analaysis sample.csv", 'r')
#lines = file.readlines()
#for line in lines:
    #print(line
