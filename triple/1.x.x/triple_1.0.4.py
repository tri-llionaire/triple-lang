#TRIPLE-LANG
print 'WELCOME TO THE TRIPLE CONSOLE\n'
while 1 == 1:
    dic = []
    commands = {'PRI': 'print', 'END': 'exit()', 'ADD': '+', 'SUB': '-'}
    string = ''
    usrinput = raw_input()
    usrarray = usrinput.split()
    x = 0
    while len(dic) < len(usrarray):
        dic.append(usrarray[x])
        x += 1
    if 'ADD' in dic:
        if dic[0] == 'PRI':
            torun = 'print ' + dic[1] + ' + ' + dic[3]
            exec(torun)
            break
        else:
            torun = dic[0] + ' + ' + dic[2]
            exec(torun)
            break
    elif 'SUB' in dic:
        if dic[0] == 'PRI':
            torun = 'print ' + dic[1] + ' - ' + dic[3]
            exec(torun)
            break
        else:
            torun = dic[0] + ' - ' + dic[2]
            exec(torun)
            break
    elif dic[0] == 'END':
        break
    else:
        string = ' \''
        command = ''
        string += str(dic[1])
        command = commands[dic[0]]
        string += '\''
        torun = command + string
        exec(torun)
exit()