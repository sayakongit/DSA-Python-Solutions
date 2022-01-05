max = int(input("Enter the max number: "))
odd = []
if max <=0:
    raise Exception("Max less than 1 error")
for i in range(1,max+1):
    if i % 2 != 0:
        odd.append(i)

print(f'The odd numbers between 1 and {max} are:\n'
      f'{odd}')
