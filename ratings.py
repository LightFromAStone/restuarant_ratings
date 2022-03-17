"""Restaurant rating lister."""


# put your code here
def print_restuarant_ratings(dict):
    alphabetical = sorted(dict)
    for restuarant in alphabetical:
        print(f'{restuarant} is rated at {dict[restuarant]}.')


in_file = open('scores.txt')

restuarant_ratings = {}

for line in in_file:
    restuarant, _, rating = line.partition(':')
    rating = rating.strip()
    restuarant_ratings.update({restuarant : rating})

in_file.close()

user_restuarant = input('Please input a restuarant name: \n')
user_rating = input('What is the rating for that restuarant? \n')

restuarant_ratings.update({user_restuarant : user_rating})

print_restuarant_ratings(restuarant_ratings)

