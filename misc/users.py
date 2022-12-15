users ={
    'aeinstein' : {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie' : {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{userinfo['first'].title()} {userinfo['last'].title()}"
    location = f"{userinfo['location'].title()}"

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")