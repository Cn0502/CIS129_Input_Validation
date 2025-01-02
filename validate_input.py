isVoting = input("Hello are you planning on voting this November")

while isVoting != "yes" and isVoting != "no" :
    isVoting = input("there was a problem with your awnser try awnsering 'yes' or 'no' ")

if isVoting == "yes":
    print("thank you for voting this November")
elif isVoting == "no" :
    print("you should reconsider voting this November every voice counts")
else :
    print("there was an error")
