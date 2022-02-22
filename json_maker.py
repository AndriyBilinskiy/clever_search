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
            if line[ind_bracket - 1].isdecimal():
                res.append(previous)
                previous = []
        else:
            previous.append(line)
    for block in res:
        final.append(make_dict(block))
    return final


def make_dict(block: list):
    new_block = list(map(lambda x: x.split(","), block))
    dvokr_block = list(map(lambda x: x.split(":"), block))
    return new_block, dvokr_block

