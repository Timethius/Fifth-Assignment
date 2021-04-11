'''
Implement the following functions based on the question. Retain the name of the functions, and parameters as is in the question. 
=================
1. create_new_file(name_list, address_list, phone_list) --> 30% 
Get the names, addresses, phone of 10 different people as a list and write it to a file called 'contacts.txt' 
Input:
name_list = ['Joe', 'Max' ...]
address_list = ['Addr 1', 'Addr 2' ..]
phone_list = ['4041234567', '6161234567'..]
Output:
contacts.txt file
]
------------------------------------------------
2. compile_poem(file_list) --> 40%
 
Write a function that reads the 4 different paragraphs of road not taken, and combine it into a single file called 'road_not_taken.txt'. 
Input:
file_list = ['two_roads_1.txt', 'two_roads_2.txt', 'two_roads_3.txt', 'two_roads_4.txt']
Output:
road_not_taken.txt
----------------------------------------------------------------
3. write_custom_parser(file_name) --> 30% 
You're using a tool that outputs final grade of student in the format given in 'parsed_file.txt'.
Write a file parser that parses this document and gives output in format below.
Input:
file_name = 'parsed_file.txt'
Output:
result_list = [
    {
        'student': 'John,
        'year': 2019,
        'grade': B+
    }, ....
]
'''


import csv
import pprint

#COMPLETE

#1
def create_new_file(name_list, address_list, phone_list):
    result_list = []
    for i in range(len(name_list)):
        temp_dict = {
            "name": name_list[i],
            "address": address_list[i],
            "phone": phone_list[i]
            }
        result_list.append(temp_dict)
    keys = result_list[0].keys()
    with open('contacts.txt', 'w', newline = '') as output:
        dict_writer = csv.DictWriter(output, keys)
        dict_writer.writeheader()
        dict_writer.writerows(result_list)

if __name__ == "__main__":
    name_list = ['Joe', 'Max', 'Sally', 'Bianca', 'Alex', 'Ryoichi', 'Esther', 'Meerae', 'Samarth', 'Yuxuan']
    address_list = ["Addr 1", "Addr 2", "Addr 3", "Addr 4", "Addr 5", "Addr 6", "Addr 7", "Addr 8", "Addr 9", "Addr 10"]
    phone_list = ["40412334567", "61612334567", "4561234357", "4788458886", "4344567788", "4365567788", "9876673357", "4042245679", "7708708890", "55555555556"]
    create_new_file(name_list, address_list, phone_list)




#COMPLETE

#2
def compile_poem(file_list):
    with open('road_not_taken.txt', 'w') as Whole:
        for files in file_list:
            with open(files) as Parts:
                values = Parts.read()
                Whole.write(values)

if __name__ == "__main__":
    file_list = ['two_roads_1.txt', 'two_roads_2.txt', 'two_roads_3.txt', 'two_roads_4.txt']
    compile_poem(file_list)



#COMPLETE

#3
def write_custom_parser(file_name):
    result_list = []
    each_dict = {}
    with open(file_name, "r") as files:  
        for entries in files:
            entry = entries.split(':', 1)
            if len(entry) == 2:
                if entry[0] == 'Student' and each_dict:
                    result_list.append(each_dict)
                    each_dict = {}
                each_dict[entry[0]] = entry[1].rstrip()
        if each_dict:
            result_list.append(each_dict)
    return result_list


if __name__ == "__main__":
    pprint.pprint(write_custom_parser('parsed_file.txt'))
Write a file parser that parses this document and gives output in format below.

Input:
file_name = 'parsed_file.txt'
Output:
result_list = [
    {
        'student': 'John,
        'year': 2019,
        'grade': B+
    }, ....
]


'''
