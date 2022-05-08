import re
from geopy.geocoders import Nominatim


def parse(path):
    data = parse_by_newlines(read_file(path))
    starting_info = {"протопресвітерат": "Льввівський",
           "деканат": re.findall('.* деканат', data[0][0])[0][:-8]}
    res1 = parse_decande(starting_info, data[1:])
    res = {"протопресвітерат": "Льввівський",
           "деканат": re.findall('.* деканат', data[0][0])[0][:-8],
           "населений пункт": {
               "назва": "ТЕРНОПІЛЬ",
               "location": {
                   "lat": 49.56667,
                   "lng": 25.60000
               }
           },
           "церкви": [{
               "назва": "Різдва Христ.",
               "тип": "мур.",
               "рік": "1600",
               "відн.": "1925",
               "Дн.": "Дн."
           },
               {
                   "назва": "Воздвиження Чесн. Хр.",
                   "тип": "мур.",
                   "рік": "1400",
                   "відн.": "1921",
                   "Дн.": "Дн."
               },
               {
                   "назва": "Н. Серця Ісуса.",
                   "тип": "мур.",
                   "прил.": "Гаї великі",
                   "рік": "1910",
                   "відн.": "1921",
                   "Дн.": "Дн."
               },
               {
                   "назва": "Пр. Д. М.",
                   "тип": "мур.",
                   "прил.": "Янівці",
                   "рік": "1905",
                   "Дн.": "Дн."
               }
           ],

           "надає": {
               "тип": "організація",
               "назва": "Місцева Мійська Рада"
           },
           "персонал": {
               "парох": {
                   "тип": "о.",
                   "ім'я": "Володимир",
                   "прізвище": "Громницький",
                   "р.": "1862",
                   "o.": "1885",
                   "стан": "ж.",
                   "інше": "поч. крил. М. К., декан, ком. і орд. дел. до кв. ісп. нар. учит.,поч. горож. м. Тернополя, чл. Ш. Р. О., чл. Мійськ. і Повіт. Ради"
               },
               "сотрудники": [{
                   "тип": "о.",
                   "ім'я": "Степан",
                   "прізвище": "Ратич",
                   "р.": "1890",
                   "o.": "1919",
                   "стан": "ж."
               },
                   {
                       "тип": "о.",
                       "ім'я": "Степан",
                       "прізвище": "Колянковський",
                       "р.": "1896",
                       "o.": "1923",
                       "стан": "ж."
                   },
                   {
                       "тип": "о.",
                       "ім'я": "Омелян",
                       "прізвище": "Ваврик",
                       "р.": "1901",
                       "o.": "1926",
                       "стан": "ж."
                   }
               ]
           },
           "душ": [{
               "грк.": "8742",
               "лат.": "9246",
               "інш.": "13933"
           },
               {
                   "прил.": "Загробеля",
                   "грк.": "491",
                   "лат.": "1160",
                   "інш.": "260"
               },
               {
                   "прил.": "Янівці",
                   "грк.": "180",
                   "лат.": "610"
               },
               {
                   "інше": "костел і лат. парох, кост. ОО. Єзуїтів, кост. ОО. Домініканів, лат. капл. в вязниці. і шпиталі, лат. СС. Служ., СС. Мил. Вінк. П."
               }
           ],
           "дот.": {
               "п.": {
                   "ha": "41",
                   "a": "61",
                   "m2": "75"
               },
               "дім": "нові.",
               "буд.": "нові",
               "Дн.": "Дн."
           },
           "навчальні заклади": [{
               "шк.": [{
                   "кл.": "7",
                   "мова": "укр.",
                   "кількість": "2",
                   "тип": "муж."
               },
                   {
                       "кл.": "7",
                       "мова": "укр.",
                       "кількість": "2",
                       "тип": "дів."
                   },
                   {
                       "кл.": "4",
                       "мова": "укр.",
                       "кількість": "2",
                       "тип": "муж."
                   },
                   {
                       "кл.": "4",
                       "мова": "укр.",
                       "кількість": "2",
                       "тип": "дів."
                   }
               ],
               "учит. семінарія": [{
                   "кількість": "1",
                   "тип": "муж."
               },
                   {
                       "кількість": "2",
                       "власність": "прив."
                   }
               ],
               "гімн.": [{
                   "мова": "укр.",
                   "кількість": "1",
                   "власність": "держ."
               },
                   {
                       "мова": "пол.",
                       "кількість": "3"
                   },
                   {
                       "мова": "укр.",
                       "кількість": "1",
                       "власність": "прив.",
                       "тип": "дів."
                   },
                   {
                       "мова": "пол.",
                       "кількість": "1",
                       "власність": "прив.",
                       "тип": "дів."
                   }
               ],
               "школа пром.": [{
                   "мова": "пол.",
                   "кількість": "1",
                   "спец.": "слюсарська."
               }],
               "інше": "6 сталих: катехитів, філ. і чит. »Просв.« філ. УПТ., 8 коопер., грк. СС. Служ. (8)."
           }],
           "стар.": [{
               "Стар.": "Тернопіль"
           },
               {
                   "пч.": "Тернопіль"
               },
               {
                   "тел.": "Тернопіль"
               },
               {
                   "зал.": "Тернопіль"
               }
           ]
           }
    return res1


def parse_decande(starting_info, data):
    json = []
    for place in data:
        json.append(parse_living_place(starting_info, place).copy())
    return json


def parse_living_place(starting_info, data):
    json = starting_info
    name = data[0].split(',')[0].strip()
    json["населений пункт"] = place_info(name)
    data[0] = ''.join(data[0].split(',')[1:])
    json["церкви"] = parse_churches(data[0])
    data = data[1:]
    for part in data:
        if 'Надає: ' in part:
            type = "організація" if part.split(': ')[1:][0].count(' ')>1 else "особа"
            json["надає"] = {"тип": type, "назва": part.split(': ')[1:][0]}
            continue
        if 'Парох: ' in part:
            json["персонал"] = {
                "парох": parse_paroch(part, ''),
            }
            continue
        if "Сотр." in part:
            if "сотрудники" in json['персонал'].keys():
                json['персонал']["сотрудники"].append(worker(part))
            else:
                json['персонал']["сотрудники"] = [worker(part)]
            continue
        if "Душ:" in part:
            json["душ"] = parse_population(part)
        if "Дот.: " in part:
            json["дот."] = parse_dot(part)


    # # try:
    # #     if bool(re.match('Надає: ', data[1])):
    # #         json["надає"] = {"тип": "організація", "назва": data[1].split(': ')[1:][0]}
    # #     json["персонал"] = {
    # #         "парох": parse_paroch(data[2], ' '.join(data[3].split('\n'))),
    # #         "сотрудники":[]
    # #
    # #     }
    # except IndexError:
    #     pass
    return json


def parse_dot(data):
    data = data.replace('\n', ' ')
    data = data.replace(';', ',')
    data = data.split(',')
    res = {}
    res['п.'] = {
        "ha": re.search('[0-9]+ .а',data[0]).group()[:-3],
        "a": re.search('[0-9]+ а',data[0]).group()[:-2],
        "m2": re.search('[0-9]+ т.',data[0]).group()[:-3]
    }
    data = data[1:]
    for dot in data:
        if len(re.findall('[0-9]+', dot)) < 2:
            dot_parts = dot.split(' ')
            if len(dot_parts) == 2 and "Дн." not in dot:
                res[dot_parts[0]] = dot_parts[1]
        else:
            try:
                res[re.search('\S+\.',dot).group()] = {
                    "ha": re.search('[0-9]+ .а', dot).group()[:-3],
                    "a": re.search('[0-9]+ а', dot).group()[:-2],
                    "m2": re.search('[0-9]+ т.', dot).group()[:-3]
                }
            except ValueError:
                pass
    if "Дн." in data:
        res["Дн."] = "Дн."
    return res


def parse_population(data):
    populations = data.replace('\n', ' ').split(';')
    json = []
    for population in populations:
        if len(re.findall('[0-9]+', population)) < 2:
            res = {'інше': population}
        else:
            pairs = re.findall('\S{3,4}\. \S+', population)
            res = {}
            for pair in pairs:
                first = pair.split(' ')[0]
                second = pair.split(' ')[1]
                while second[-1] == '.' or second[-1] == ',' or second[-1] == ';':
                    second = second[:-1]
                res[first] = second
        json.append(res)
    return json


def worker(data):
    name = re.search('[А-Я][а-я]{2,} [А-Я][а-я]{2,}', data).group()
    years = re.findall('[0-9]{4}', data)
    json = {
        "тип": "о.",
        "ім'я": name.split(' ')[0],
        "прізвище": name.split(' ')[1],
        "р.": years[0],
        "o.": years[1],
        "стан": "ж."
    }
    return json


def parse_paroch(data, other):
    data = data.replace('Парох: ', '')
    data = data.replace(',', '').split(' ')
    json = {
        "тип": "о.",
        "ім'я": data[1],
        "прізвище": data[2],
        "р.": data[4],
        "o.": data[6],
        }
    if other:
        json["інше"] = other
    try:
        json["стан"] = data[7]
    except IndexError:
        pass
    return json


def parse_churches(data):
    try:
        churches = re.split('[0-9]\) ', data)
        res = []
        for church in churches:
            name = re.search('[А-Я]\S{2,}( [А-Я]\S+)*', church)
            church = church[name.end():]
            type = 'дер.' if 'дер.' in church else 'мур.'
            years = re.findall('[0-9]{4}', church)
            json = {"назва": name.group(),
                    "тип": type,
                    "рік": years[0],
                    }
            if len(years) > 1:
                json["відн."] = years[1]
            if 'Дн.' in church:
                json['Дн.'] = 'Дн.'
            res.append(json)
    except:
        pass
    return res


def place_info(place_name):
    geolocator = Nominatim(user_agent="my_user_agent")
    loc = geolocator.geocode(f'{place_name},Україна')
    if not loc:
        loc = geolocator.geocode(f'Україна')
    json = {
               "назва": place_name,
               "location": {
                   "lat": loc.latitude,
                   "lng": loc.longitude
               }
           }
    return json


def read_file(path):
    with open(path, "r") as file:
        content = file.read()
    return content


def parse_by_newlines(content):
    res = [i.split('\n\n') for i in re.split("[0-9][0-9]\)", content)]
    for i in res:
        while '' in i:
            i.remove('')
        while ' ' in i:
            i.remove(' ')

    return res


if __name__ == "__main__":
    print(parse("V_1364C_1924_0000-00253.txt"))

