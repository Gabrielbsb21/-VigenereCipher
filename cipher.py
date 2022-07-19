from key_generator import key_generator

def cipher (password, message): 
    message = message.replace(',', "").replace('.', "").replace(" ", "").lower()
    size = len(message)
    key = key_generator(password, size)
    print(key)