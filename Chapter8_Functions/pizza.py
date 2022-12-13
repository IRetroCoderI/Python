
def makePizza(*toppings):
    for tops in toppings:
        print(f"Adding {tops.upper()} to your pizza!")
    print("Your pizza is finished, please let me go home")

def build_profile(first, last, **userinfo):
    userinfo['firstName'] = first
    userinfo['lastName'] = last
    return userinfo

def make_car(make, model, **carInfo):
    carInfo['make'] = make
    carInfo['model'] = model
    return carInfo


user_profile = build_profile('jesus','ramirez',location='reda',field='compSci')


car = make_car("nissan","cube", color = 'black')
print(car)