


# durchschnittliche Zykluslänge berechnen (inkl. neuem / aktuellem Wert)

zyklen = [29,28,32,27,35,29]
total = 0
aktuell = input('dauer des letzten zyklus\'? (tage): ')
zyklen.append(aktuell)

for i in zyklen:
    total += (int(i))
    average = total / (len(zyklen))

print('durchschnittliche zykluslänge: ', average)

#KALENDER:

import calendar
c = calendar.TextCalendar(calendar.MONDAY)
for i in range(1,13):
    str = c.formatmonth(2020, i)
    print(str)

# file erstellen, zyklusdaten hineinschreiben, weitere daten hinzufügen:

with open('zyklen.txt', 'w') as f:
    f.write('zyklus nummer eins / ')

with open('zyklen.txt', 'a') as f:
    f.write('zyklus nummer zwei / ')

with open('zyklen.txt', 'a') as f:
    f.write('zyklus nummer drei / ')

with open('zyklen.txt', 'r') as f:
    print(f.read())

'''
# >>> als nächstes: daten als liste speichern und als liste wieder ins skript
    #speisen für neue berechnungen (wie neuer durchschnitt)

import pandas as pd
df = pd.read_txt('zyklen.txt')
df

#ModuleNotFoundError: No module named 'pandas'
'''


#Tage zwischen Daten ausrechnen (muss tag 1.a und tag1.b als eckpunkte
#angeben, weil exklusive zweitem datum gerechnet wird)


import datetime

start = datetime.date(2020, 1, 4)
end = datetime.date(2020, 2, 3)
days = (end - start).days

print(f'Tag Eins Jänner \'20: {start}')
print(f'Tag Eins Feber \'20: {end}')
print(f'Dauer des letzten Zyklus:{days} Tage ')


#resultat:
'''
    Start date: 2020-01-04
    End date: 2020-02-03
    Days between: 30
'''

#Welcher Tag im aktuellen Zyklus ist heute?

today = datetime.date.today()

tomorrow = today + datetime.timedelta(days=1)

days3 = (tomorrow - end).days

print(f'Heute ist Tag: {days3}')

#Juhuuuuuuu es funktioniert :)!!!!!!



zyklustag = datetime.date.today() + datetime.timedelta(days=1)

days3 = (zyklustag - end).days

print(f'Heute ist Tag: {days3}')






























 
