# this code brings in a library
# a collection of knowledge
# this code imports this knowledge
# of how to geocode
# detangling the complexities
# of place
# and spitting back
# a series of numbers

# it is customary to thank
# the library's creator
# thank you @deniscarriere
# it simplified this process
# it made the code easier
# to swallow
import geocoder

# this code asks the user to enter a place
# but even at this point
# it's not really a place
# it's just a string
# a series of characters
place = input("Please enter a place:\n")

# this code reaches out
# to a knowledge base called geocodefarm
# and returns a package
# of structured information
# about the place
# but it is not the place
# the place has been abstracted
# beyond recognition

# we should be so lucky
# that geocodefarm gives us this information
# for free
# originally i tried to use google
# but they asked for my credit card
# i almost gave it to them
# but switched to geocodefarm instead
# this information is free now
# but also not really
abstracted = geocoder.geocodefarm(place)

# this code will place a value judgement
# upon your place
# true or false
# if this code determines
# that your place is truly a place
# this code will try to tell you
# that your place is a series of numbers
# but it is not
if abstracted.ok == True:
    print(f"Congrats! Your place exists. Its coordinates are {abstracted.latlng}")

# this code determined
# that your place is false
# this code will try to tell you
# that your place does not exist
# but it does
# it exists outside of the confines
# of data
# it exists outside of the structures
# of power
# it exists outside of the technologies
# of mapping
else:
    print("Sorry, your place does not exist.")
