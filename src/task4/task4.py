secret_list = ["Apple", "Banana", "Some", "word", "excel"]

isActive = True
while isActive:
    value = input("Enter some word that you wanna check in my secret list:")
    if secret_list.__contains__(value):
        print("Congratulations! You have guessed the secret!")
        isActive = False
    else:
        print("Try another one ;(")


