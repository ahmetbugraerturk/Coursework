users = {
    "id1": {"name": "Alice", "age": 30, "city": "New York", "friends": ["id2", "id3", "id5", "id6"]},
    "id2": {"name": "Bob", "age": 25, "city": "New York", "friends": ["id1", "id5", "id6", "id7"]},
    "id3": {"name": "Charlie", "age": 35, "city": "Los Angeles", "friends": ["id1", "id7", "id8", "id12"]},
    "id4": {"name": "Diana", "age": 23, "city": "Chicago", "friends": ["id9", "id10","id11", "id12"]},
    "id5": {"name": "Eve", "age": 27, "city": "New York", "friends": ["id1", "id2", "id10", "id11"]},
    "id6": {"name": "Frank", "age": 40, "city": "Miami", "friends": ["id1", "id2", "id10", "id12"]},
    "id7": {"name": "Grace", "age": 29, "city": "Los Angeles", "friends": ["id2", "id3", "id8", "id11"]},
    "id8": {"name": "Hank", "age": 33, "city": "Los Angeles", "friends": ["id3", "id7", "id9", "id10"]},
    "id9": {"name": "Ivy", "age": 26, "city": "Chicago", "friends": ["id4", "id8", "id11", "id12"]},
    "id10": {"name": "Jack", "age": 41, "city": "Chicago", "friends": ["id4", "id5", "id6", "id8"]},
    "id11": {"name": "Karen", "age": 24, "city": "Miami", "friends": ["id4", "id9", "id5", "id7"]},
    "id12": {"name": "Leo", "age": 37, "city": "Miami", "friends": ["id3", "id4", "id6", "id9"]},
}

# Function to find pairs of people most likely to be friends based on mutual friends
def most_likely_to_be_friends(users):
    """Function to find pairs of people most likely to be friends based on mutual friends"""
    if not users:
        return []
    
    mutual_friends = []
    for ids, user in users.items():
        for i in users.keys()-(user["friends"]+[ids]):
            mutual_friends.append((user["name"], users[i]["name"], len(intersection(users[i]["friends"], user["friends"]))))
    mutual_friends = sorted(mutual_friends, key=lambda x: x[2])[::-1]
    maxV = mutual_friends[0][2]
    if maxV==0:
        return []
    for i in range(len(mutual_friends)):
        if mutual_friends[i][2] < maxV:
            mutual_friends = mutual_friends[:i]
            break
    mutual_friends = [mutual_friends[i] for i in range(len(mutual_friends)) if i%2==1]
    return mutual_friends[::-1]
        
    
def intersection(l1, l2):
    inter = []
    for i in l1:
        for j in l2:
            if i == j:
                inter.append(i)
    return inter
    
