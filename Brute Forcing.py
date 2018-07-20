alphabet = "abcdefghijklmnopqrstuvwxyz"

def decode(secretMessage):
    for key in range(0, len(alphabet)):
        newAlphabet = alphabet [key:] + alphabet [:key]
        attempt = ""

        for i in range(len(secretMessage)):
            index = alphabet.find(secretMessage[i])

            if index < 0:
                attempt += secretMessage[i]
            else:
                attempt += newAlphabet[index]

        print("key: " + str(key) + " - " + attempt)

secretMessage = input("What is your message?").lower();
decode(secretMessage)
