'''Write a Python program that reads a list of 2-element integer tuples from STDIN 
and prints a new list sorted in 
increasing order by each tuple’s last element. 
You are not allowed to use any built-in sorting utilities (sorted(), list.sort(), or key=).
Use only loops, conditionals, and basic list operations. '''

#[(5,4),(9,1),(2,3),(5,9),(7,6),(5,5)]

# inp = input() 
inp = "[(5,4),(9,1),(2,3),(5,9),(7,6),(5,5)]"
tp = eval(inp)
li = list(tp)

for i in range(len(li)):
    for j in range(len(li)-1-i):
        if li[j][1]>li[j+1][1]:
            li[j],li[j+1] = li[j+1],li[j]

out = "[" +",".join(f"({x[0]},{x[1]})" for x in li)+"]"

   
print(out)