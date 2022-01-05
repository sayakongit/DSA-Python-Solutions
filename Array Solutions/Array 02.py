heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# Question 1
print(f'Length of the list \n'
      f'{len(heroes)}')

# Question 2
print(f'Add \'black panther\' at the end of this list')
heroes.append("black panther")
print(heroes)

# Question 3
print("You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add "
      "it after 'hulk'")
heroes.remove("black panther")
heroes.append("hulk")
heroes.append("black panther")
print(heroes)

# Question 4
print("Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from "
      "list and replace them with doctor strange (because he is cool) Do that with one line of code.")
heroes = heroes[:1] + ["doctor strange"] + heroes[-4:]
print(heroes)

# Question 5
print("Sort the heros list in alphabetical order")
heroes = sorted(heroes)
print(heroes)
