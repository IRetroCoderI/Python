unconfirmed_users = ['alice', 'brian', 'candace', 'jesus', 'angie']
confirmed_users = []

while len(unconfirmed_users)!=0:
    confirmed_users.append(unconfirmed_users.pop())

print(f"Confirmed Users: {confirmed_users}")
print(f"Unconfirmed Users: {unconfirmed_users}")