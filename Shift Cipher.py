alphabet = "abcdefghijklmnopqrstuvwxyz"
partialOne = ""
partialTwo = ""
newAlphabet = ""
newMessage = ""

message = input("Input a Messsage ").lower();
key = int(input("Please enter a number to shift by: "))%26



if key == 0:
    newAlphabet = alphabet
    
else:
    if key < 0:
        key = key + 26
    p1 = alphabet[:key]
    p2 = alphabet[key:]
    newAlphabet = p2 + p1
for i in range(0, len(message)):
    index = alphabet.find(message[i])
    if index < 0:
        newMessage += message[i]
    else: 
        newMessage += newAlphabet[index]


print (newMessage)
