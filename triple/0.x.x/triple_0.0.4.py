#TRIPLE-LANG
print 'WELCOME TO THE TRIPLE CONSOLE\n'
while 1 = 1:
    dic = []
    commands = {'PRI': 'print'}
    string = ''
    usrinput = raw_input()
    usrarray = usrinput.split()
    x = 0
    while len(dic) < len(usrarray):
        dic.append(usrarray[x])
        x += 1
    string = '\''
    store = 0
    command = ''
    while store < len(dic):
        if dic[store] in commands:
            command += commands[dic[store]] + ' '
            store += 1
        else:
            if dic[store] not in commands:
                string += str(dic[store]) + ' '
            store += 1
    string += '\''
    torun = command + string
    exec(torun)