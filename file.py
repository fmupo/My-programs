fhand = open('mbox.txt')
print(fhand)
# using the newlne character that is called backslash-n
hello_text= 'hello\nworld!\nlove'
print(hello_text)
hello_length=len(hello_text) 
print("hello length is ", hello_length)
#\n is treated as a single character
# reading files
my_file = open('shortfile.txt')
my_lines = my_file.readlines()
print(type(my_lines))
print("this is my line ",my_lines)
count = 0
for line in my_lines:
    count+= 1
    print(line)
print('line count is ,', count) 
mbox_file= open ("mbox.txt")
mbox_content = mbox_file.read()
print(len(mbox_content))
# Reading the file content and printing its length
print(mbox_content[:20])  # Print the first 20 characters of the file content
# we can search through a file and find a specific line that contains a specific word
# we use the command startswith
# Loop through each line in the file and print lines that start with 'From:'
print("this is bofore for loop")
for line in my_lines:
    if line.__contains__('From:'):
        print(line)
print("after the for loop")
test_file = open('shortfile.txt')
print(test_file.readline())  # Read and print the first line of the file
print(test_file.readline())  # Read and print the second line of the file

with open ('names_of_schools', 'w') as file:
    file.write("Kriste mambo\n")
    file.write("School B\n")
    file.write("School C\n")
    file.close()  # Close the file after writing



with open ('email_adresses', 'w') as file:
    for line in my_lines:

        if line.__contains__('From:'):
            # Extract the email address from the line
          email_address = line.split()[1]
          file.write(email_address +'\n')
    file.close()  # Close the file after writing
 