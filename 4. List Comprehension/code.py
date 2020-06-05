numbers = [1,2,3]
doubled = [num * 2 for num in numbers]
print(doubled)

friends = ['rolf','sam','samantha','saurabh','jen']
starts_s = [friend for friend in friends if friend[0] == 's']
print(starts_s)

friends = ['sam','samantha','saurabh']
starts_s = [friend for friend in friends if friend[0] == 's']
print(friends)
print(starts_s)
print(friends is starts_s)
print(friends == starts_s)

print('\n\nFriends: ',id(friends),'Starts_S: ', id(starts_s))
print('Friends: ',id(friends[0]),'Starts_S: ', id(starts_s[0]))