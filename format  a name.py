def namelist(names):
    nameString = ''

    if len(names) == 0:
        return ''
    if len(names) == 1:
        return names[0]['name']
    if len(names) == 2:
        return names[0]['name'] + ' & ' + names[1]['name']
    else:    
        for i in names[:-2]:
            nameString += i['name'] + ', '
        nameString += names[-2]['name'] + ' & ' + names[-1]['name']
        return nameString
