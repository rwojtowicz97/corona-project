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


with open('odpowiedzi.txt', 'w') as file:
    file.write(f'Ilość wczytanych NOPów: {len(nop_list)}\n')
    file.write(f'Ilość Kobiet: {women_counter}\n')
    file.write(f'Ilość Mężczyzn: {men_counter}\n')
    file.write(f'Ilość osób z gorączką w województwie pomorskim: {pomorskie_and_fever}\n')

print(f'Ilość wczytanych NOPów: {len(nop_list)}')
print(f'Ilość Kobiet: {women_counter}')
print(f'Ilość Mężczyzn: {men_counter}')
print(f'Ilość osób z gorączką w województwie pomorskim: {pomorskie_and_fever}')

