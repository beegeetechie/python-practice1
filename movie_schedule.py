#movie schedule using Dictionary set(key, Value pair)
current_movies={'Leo':'11.00AM',
                'Beast':'2PM',
                'Kaidhi':'5PM',
                'Vikram':'8PM'}
print("We are showing the below movies :\n")
for key in current_movies:
  print(key)

user_select = input("Which movie are you interested to book: ")
show_time=current_movies.get(user_select)
if show_time == None:
  print("Selected movie is not in the list")
else:
  print("Your Movie time is",show_time)