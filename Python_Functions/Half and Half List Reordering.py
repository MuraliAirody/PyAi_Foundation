'''
Implement a function half_and_half that takes a list of integers and rearranges it so that the second half of the list appears before the first half. If the list has an odd length, keep the middle element exactly between the two halves.
How It Works

Let n be the length of the list.
Compute half = n // 2.
If n is even:
First half = lst[:half]
Second half = lst[half:]
Result = second_half + first_half
If n is odd:
First half = lst[:half]
Middle element = lst[half]
Second half = lst[half+1:]
Result = second_half + [middle] + first_half
'''

num = int(input())

li = list(map(int,input().split()))

def half_and_half(li):
    mid = len(li)//2
    if len(li)%2==0:
        return li[mid:len(li)]+li[:mid]
    else:
        return li[mid+1:len(li)]+li[mid:mid+1]+li[:mid]    

print(" ".join(map(str,half_and_half(li))))        