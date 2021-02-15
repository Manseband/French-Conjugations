import requests

PROJECT_TOKEN = 'ta4TO7wT8gFJ'

def newUrl():

    verb = input("Enter name of new verb: ")

    nUrl = 'https://conjugator.reverso.net/conjugation-french-verb-' + str(verb) + '.html\n'

    with open('cahier.csv','a') as f:
        f.write(newUrl())
        f.close

    requests.post('https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/run')
