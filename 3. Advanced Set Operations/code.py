friends = {'bob','rolf','anne'}
abroad = {'bob','anne'}

local_friends = friends.difference(abroad)
print(local_friends)

local_friends = abroad.difference(friends)
print(local_friends)

local = {'rolf'}
abroad = {'bob','anne'}

friends = local.union(abroad)
print(friends)

arts = {'bob','jen','rolf','anne'}
science = {'bob','jen','adam','charlie'}

friends = arts.intersection(science)
print(friends)