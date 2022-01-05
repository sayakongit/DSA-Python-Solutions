array = [2200, 2350, 2600, 2130, 2190]

# Question 1
print(f'In Feb, how many dollars you spent extra compare to January?\n'
      f'${array[1] - array[0]}')

# Question 2
print(f'Find out your total expense in first quarter (first three months) of the year.\n'
      f'${sum(array[:3])}')

# Question 3
print("Find out if you spent exactly 2000 dollars in any month.")
flag = 0
for i in array:
    if i == 2000:
        flag = 1
        break
if flag == 1:
    print("Yes")
else:
    print("No")

# Question 4
print(f'June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list')
array.append(1980)
print(array)

# Question 5
print(f'You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your '
      f'monthly expense list based on this')
array.insert(3, array[3]-200)
print(array)
