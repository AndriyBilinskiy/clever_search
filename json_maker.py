def reading_file(path):
	with open(path, "r") as file:
		content = []
		for line in file:
			content.append(line.rstrip())
	return content


def dct_maker(content: list):
	final = []
	res = []
	previous = []
	for line in content:
		if ")" in line:
			ind_bracket = line.find(")")
			if line[ind_bracket - 1].isdecimal() and ind_bracket in (1, 2):
				res.append(previous)
				previous = [line]
		else:
			previous.append(line)
	for ind, block in enumerate(res):
		cool_block = []
		pivot = ""
		for item in block:
			pivot += item
			if item == "":
				cool_block.append(pivot)
				pivot = ""
		print(cool_block)
		if ind >= 1:
			final.append(make_dict(cool_block))
	return final


def find_nas_punkt(block):
	return block[0][block[0].find(")") + 2:block[0].find(",")]


def find_nazva(line):
	s = ""
	splited = line.split()
	for item in splited:
		if item[0].isupper() or item == "св.":
			s += item + " "
	while s[-1] in (" ", ","):
		s = s[:-1]
	return s


def find_typ(line):
	splited = line.split(",")
	# print(splited)
	try:
		needed = splited[1][1:]
	except IndexError:
		return "мур."
	expected = needed.split()[0]
	while expected[-1].isdecimal():
		expected = expected[:-1]
	return needed.split()[0]

def make_dict(block: list):
	res = dict()

	nas_punkt = find_nas_punkt(block)
	# location = to_locate(nas_punkt)

	churches = []
	churches_str = block[0][block[0].find("ц."):]
	ch_ch = churches_str.split("ц. ")
	for church in ch_ch:
		if church != "":
			nazva = find_nazva(church)
			typ = find_typ(church)
			churches.append({"назва": nazva, "тип": typ, "рік": 1900})

def make_dict(block: list):
	res = dict()

	nas_punkt = find_nas_punkt(block)
	# location = to_locate(nas_punkt)

	churches = []
	churches_str = block[0][block[0].find("ц."):]
	ch_ch = churches_str.split("ц. ")
	for church in ch_ch:
		if church != "":
			nazva = find_nazva(church)
			typ = find_typ(church)
			churches.append({"назва": nazva, "тип": typ, "рік": 1900})

	res = {"протопресвітерат": "Тернопільський",
		"деканат": "Тернопільський",
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
	return res


if __name__ == "__main__":
	print(dct_maker(reading_file("file"))[1])
