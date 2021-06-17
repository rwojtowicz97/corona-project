import json


with open('160221.json', 'r', encoding="utf8") as f:
    data = json.load(f)


nop_list = []
women_counter = 0
men_counter = 0
pomorskie_voivodeship = []
pomorskie_and_fever = 0

class Symptom:
    def __init__(self, name, *kwords):
        self.name = name
        self.kwords = kwords

reddening = Symptom('Zaczerwienienie i bolesność', 'zaczerwienienie i krótkotrwała bolesność')
fever = Symptom('Gorączka', 'temp', 'temperatura', 'gorączka')
seizures = Symptom('Drgawki', 'drgawki')
vomiting = Symptom('Wymioty', 'wymioty')
swoon = Symptom('Omdlenie', 'omdlenie, utrata przytomności')

class NOP:
    def __init__(self, date, voivodeship, region, gender, description):
        self.date = date
        self.voivodeship = voivodeship
        self.region = region
        self.gender = gender
        self.description = description

    symptoms_list = [reddening, fever, seizures, vomiting, swoon]


def count_voivodeship(voivodeship):
    counter = 0
    for nop in nop_list:
        if nop.voivodeship == voivodeship:
            counter += 1
        else:
            continue
    return counter


for x in data:
    nop_list.append(NOP(x["DATE"], x["VOIVODESHIP"], x["REGION"], x["GENDER"], x["DESCRIPTION"]))


for nop in nop_list:
    if 'K' in nop.gender:
        women_counter += 1
    elif 'M' in nop.gender:
        men_counter += 1
    else:
        print(f'else: {nop.gender}')


for nop in nop_list:
    if nop.voivodeship == 'pomorskie':
        if 'temp' in nop.description or 'gorączka' in nop.description or 'temperatura' in nop.description:
            pomorskie_and_fever += 1
        else:
            continue
    else:
        continue



count_voivodeship('lubelskie')

with open('odpowiedzi.txt', 'w') as file:
    file.write(f'Ilość wczytanych NOPów: {len(nop_list)}\n')
    file.write(f'Ilość Kobiet: {women_counter}\n')
    file.write(f'Ilość Mężczyzn: {men_counter}\n')
    file.write(f'Ilość osób z gorączką w województwie pomorskim: {pomorskie_and_fever}\n')


with open('zestawienie.txt', 'w') as file:
    file.write('dolnośląskie: ' + str(count_voivodeship('dolnośląskie')))
    file.write(f'\nkujawsko-pomorskie: '+ str(count_voivodeship('kujawsko-pomorskie')))
    file.write(f'\nlubelskie: '+str(count_voivodeship('lubelskie')))
    file.write(f'\nlubuskie: '+str(count_voivodeship('lubuskie')))
    file.write(f'\nłódzkie: '+str(count_voivodeship('łódzkie')))
    file.write(f'\nmałopolskie: '+str(count_voivodeship('małopolskie')))
    file.write(f'\nmazowieckie: '+str(count_voivodeship('mazowieckie')))
    file.write(f'\nopolskie: '+str(count_voivodeship('opolskie')))
    file.write(f'\npodkarpackie: '+str(count_voivodeship('podkarpackie')))
    file.write(f'\npodlaskie: '+str(count_voivodeship('podlaskie')))
    file.write(f'\npomorskie: '+str(count_voivodeship('pomorskie')))
    file.write(f'\nśląskie: '+str(count_voivodeship('śląskie')))
    file.write(f'\nświętokrzyskie: '+str(count_voivodeship('świętokrzyskie')))
    file.write(f'\nwarmińsko-mazurskie: '+str(count_voivodeship('warmińsko-mazurskie')))
    file.write(f'\nwielkopolskie: '+str(count_voivodeship('wielkopolskie')))
    file.write(f'\nzachodniopomorskie: '+str(count_voivodeship('zachodniopomorskie')))


for nop in nop_list:
    for symptom in nop.symptoms_list:
        if symptom.name in nop.description:
            print(nop.description)
        else:
            continue

with open('lubuskie.txt', 'w') as file:
    file.write('')


print(f'Ilość wczytanych NOPów: {len(nop_list)}')
print(f'Ilość Kobiet: {women_counter}')
print(f'Ilość Mężczyzn: {men_counter}')
print(f'Ilość osób z gorączką w województwie pomorskim: {pomorskie_and_fever}')

