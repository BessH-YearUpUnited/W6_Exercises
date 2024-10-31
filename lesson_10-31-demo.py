#loops
#dictionaries, lists, tuples in a list

movies = [
    ('The Minions', 'X-Men First Class', 'Kicking and Screaming'), 
    ('Her', 'Fall Guy', 'Prometheus', 'Wolf on Wall Street'), 
    ('Spiderman: Far from Home', 'Despicable Me 2', 'Freedom Writers Diary')
    ]

m1, m2, m3 = movies

change_m1 = list(m1)

change_m1.append('The Last Unicorn')

m1 = tuple(change_m1)

movies[0] = m1

change_m2 = list(m2)

change_m2[1] = 'The Fall Guy'

m2 = tuple(change_m2)

movies[1] = m2

print(movies)

for x in movies:
    for i in x:
        print(f'{i} is a great movie')