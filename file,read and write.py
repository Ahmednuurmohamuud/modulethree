def write(filename, data):
  
    with open(filename, 'w') as file:
        for name, phone in data:
            file.write(f"{name}\t{phone}\n")


def read(filename):
   
    data_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            name, phone = line.strip().split('\t')
            data_dict[name] = phone
    return data_dict


# List of names and phone numbers
data = [
    ("hassam", "6176376382"),
    ("ahmed", "614567893"),
    ("muse", "6183929209"),
    ("yaxye", "612789383"),
    ("noor", "6127382487")
]

# Filename to write to and read from
filename = "filetest.txt"

# Write data to file
write(filename, data)

# Read data from file and store in dictionary
dict = read(filename)

# Print the dictionary
print(dict)
