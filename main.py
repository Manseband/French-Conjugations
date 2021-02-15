import data
import dictionary
import out
import update
import user_input

def main():

    data.output

    change = input('Would you like to update the verb list? (y/n): ')

    if change == 'y':
        update.newUrl()

main()