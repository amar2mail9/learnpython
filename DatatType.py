print("Hello")

# number 
x= 5 # int 

price = 26.5

num = 3e3 # large number e means power of 10 
# num = 3000

# complex number
z = 4+ 5j
print(z)

# check type

print(type(z))  # complex

print(type(num)) # float

print(abs(-5)) # get any number positive

print(pow(2,3)) # 8

print(round(4.75)) # 5
print(round(4.35)) # 4


nums = [1,8,8,5.5,78,9,79,789,8,98]

print(min(nums)) #1
print(max(nums)) #789


name  = 'amar kumar'

print(name[3])
print(name[-3])
print(name[1:4])


city  = "delhi"

country = '''India'''

# concatenation
first_name = "Amar"
last_name = "Kumar"

full_name = first_name + " " + last_name
print(full_name)

# find length
print(len(full_name))

print(full_name[1:3])
print(full_name[:3])
print(full_name[3:])
print(full_name[-3:])
print(full_name[1:7:2])
print(full_name[:])

# upper 
print(full_name.upper())
print(full_name.lower())
print(full_name.capitalize())

print(full_name.strip())
print(full_name.split())

str = "Welcome to python"

# replace method

str.replace("python", "Java",1)
print(str)
print(str.replace("python", "Java",1))


# escape character

print("Hello \n Amar kumar")
print("Hello \t Amar kumar")


# list data type 
# collection of elements
students  = ["Amar","Rohan","Mohan","Aryan"]

print(students)

