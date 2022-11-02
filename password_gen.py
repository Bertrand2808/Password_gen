import random

print('Bienvenue dans votre générateur de mot de passe.')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*().,?'
site = input('Saisissez le site pour lequel vous voulez enregistrer le mot de passe : ') 
mail = input('Saisissez votre adresse mail : ')
number = 1 # nombre de mot de passe à générer
length = input('Entrez la longueur du mot de passe : ')
length = int(length)

fichier = open("passwords.txt", "a")

print('\nVoici votre mot de passe pour le site : ' + site)

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
    fichier.write('\n' + site + '  :  ' + mail + '  :  ' + passwords)
    fichier.close()
    