'''Problem Statement

You are provided with:
A list of employee identifiers.
A list of attribute keys that each employee has (e.g. name, ID, salary).
For each employee, a corresponding list of attribute values.
Write a program that constructs and outputs a nested dictionary (or map) where each employee identifier maps to an inner dictionary of attribute-key:attribute-value pairs.
Input Format

An integer N, the number of employees.
A line containing N space-separated strings: the employee identifiers.
An integer M, the number of attribute keys.
A line containing M space-separated strings: the attribute keys.
N more lines, each containing M space-separated strings: the attribute values for each employee in the same order.
Output Format

Print the resulting nested dictionary in the following format (keys and values enclosed in single quotes, nested without extra spaces):
{'emp1':{'e_name':'John','e_id':'SG101','e_sal':'$10,000'},...}
Constraints

1 ≤ N ≤ 1000
1 ≤ M ≤ 100
Each string has length between 1 and 50 characters.

Hints

Read all inputs and store employee IDs, keys, and values in lists.
Use zip to pair each employee ID with its list of values.
For each employee, zip the attribute-key list with its corresponding values to form an inner dictionary.
Assemble an outer dictionary mapping each ID to its inner dictionary.
Print the final nested dictionary string exactly, including single quotes and commas, without extra spaces.
Sample Test Cases

Example 1

Input:
3
emp1 emp2 emp3
3
e_name e_id e_sal
John SG101 $10,000
Smith SG102 $9,000
Peter SG103 $9,500
Output:
{'emp1':{'e_name':'John','e_id':'SG101','e_sal':'$10,000'},'emp2':{'e_name':'Smith','e_id':'SG102','e_sal':'$9,000'},'emp3':{'e_name':'Peter','e_id':'SG103','e_sal':'$9,500'}}
Example 2

Input:
2
a b
2
k1 k2
v1 v2
v3 v4
Output:
{'a':{'k1':'v1','k2':'v2'},'b':{'k1':'v3','k2':'v4'}}
Example 3

Input:
1
userX
1
age
30
Output:
{'userX':{'age':'30'}}
Example 4

Input:
2
empA empB
1
role
manager developer
Output:
{'empA':{'role':'manager'},'empB':{'role':'developer'}}
Example 5
'''

e_count = 2 #int(input())
emps = ["a","b"] #input().split()

att_key_count = 2 #int(input())
att_keys = ["k1", "k2"] #input().split()

emp_value = []

while e_count>0:
    emp_value.append(input().split())
    e_count-=1
    if len(emp_value[0])>len(att_keys):
        break

if len(emp_value) == 1 and len(emp_value[0]) > len(att_keys):
    val = emp_value[0]
    emp_value = [val[i:i+att_key_count] for i in range(0, len(val),att_key_count)]   


emp_attr_list = [dict(zip(att_keys, values)) for values in emp_value]

final_emp_dict = dict(zip(emps, emp_attr_list))

out = "{"
pairs = []

for emp, attrs in final_emp_dict.items():
    attr_parts = []
    for k, v in attrs.items():
        attr_parts.append(f"'{k}':'{v}'")
    attr_str = "{" + ",".join(attr_parts) + "}"
    pairs.append(f"'{emp}':{attr_str}")

out += ",".join(pairs) + "}"
print(out)