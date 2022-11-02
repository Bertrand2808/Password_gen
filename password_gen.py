import random

print('Bienvenue dans votre générateur de mot de passe.')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*().,?'

site = input('Saisissez le site pour lequel vous voulez enregistrer le mot de passe : ') 

mail = input('Saisissez votre adresse mail : ')

# number = input('Saisissez le nombre de mot de passe à générer : ')
# number = int(number)
number = 1
length = input('Entrez la longueur du mot de passe : ')
length = int(length)

print('\nVoici votre mot de passe pour le site : ' + site)

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
    