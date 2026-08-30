password = "bbc"
words = ["a", "b", "c"]

def find(password, words, attemps=""):

    if len(attemps) == len(password):
        if attemps == password:
            return attemps
        return None 
    
    for word in words:
        result = find(password, words, attemps + word)

        if result == password:
            return result

    print(result)

found = find(password, words)

if found:
    print(f"Пароль успешно найден: {found}")
else:
    print("Пароль не найден.")
