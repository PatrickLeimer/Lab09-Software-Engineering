# Patrick Leimer Lab 09
# There was no other partner to work with during the Lab, thus TA Sanjay told me to work with Andres Soto who was also working with another person,
# I just pulled his repository and worked on the decoder

def encode_password(password):
    newString = ''
    for num in password:
        newString += str((int(num) + 3) % 10)
    print('Your password has been encoded and stored!')
    return newString

if __name__ == '__main__':
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        try:
            choice = int(input("Please enter an option: "))
            if 1 > choice or choice > 3:
                raise ValueError("Please enter a valid option")
        except ValueError as error:
            print("Caught ValueError:", str(error))
        encoded_password = ''
        if choice == 1:
            password = list(input("Please enter your password to encode: "))
            encoded_password = encode_password(password)
    #   if choice == 2:

        if choice == 3:
            break
