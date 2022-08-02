import pyttsx3
friend = pyttsx3.init()

friend.say("Say, What do you want to hear: ")
friend.runAndWait()

speech = input("Say, What do you want to hear: ")

friend.say(speech)
friend.runAndWait()

print("\n")
print("Awesome...!")
