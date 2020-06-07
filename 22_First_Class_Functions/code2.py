
def search(sequence, expected, finder):
    for i in sequence:
        if finder(i) == expected:
            return 'Found {}!!'.format(i['name'])
    raise RuntimeError("Couldn't not find an element with {e}".format(e=expected))

friends = [
    {'name':'bob','age':40},
    {'name':'mike','age':26},
    {'name':'phill','age':22}
]

def get_friend_name(friend):
    return friend['name']

print(search(friends,'bob',get_friend_name))
print(search(friends,'bob',lambda friend: friend['name']))