#TRIPLE-LANG
print 'WELCOME TO THE TRIPLE CONSOLE\n'
while 1 == 1:
    dic = []
    commands = {'PRI': 'print', 'END': 'exit()', 'ADD': '+', 'SUB': '-', 'MUL': '*', 'DIV': '/', 'GET': 'raw_input()'}
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
        else:
            torun = dic[0] + ' + ' + dic[2]
            exec(torun)
    elif 'SUB' in dic:
        if dic[0] == 'PRI':
            torun = 'print ' + dic[1] + ' - ' + dic[3]
            exec(torun)
        else:
            torun = dic[0] + ' - ' + dic[2]
            exec(torun)
    elif 'MUL' in dic:
        if dic[0] == 'PRI':
            torun = 'print ' + dic[1] + ' * ' + dic[3]
            exec(torun)
        else:
            torun = dic[0] + ' * ' + dic[2]
            exec(torun)
    elif 'DIV' in dic:
        if dic[0] == 'PRI':
            torun = 'print ' + dic[1] + ' / ' + dic[3]
            exec(torun)
        else:
            torun = dic[0] + ' / ' + dic[2]
            exec(torun)
    elif dic[0] == 'END':
        break
    elif dic[0] == 'PRI':
        string = ' \''
        command = ''
        string += ' '.join(dic[1:])
        command = commands[dic[0]]
        string += '\''
        torun = command + string
        exec(torun)
    elif dic[0] == 'GET':
        command = 'raw_input()'
        string = dic[1] + ' = '
        torun = string + command
        exec(torun)
    else:
        torun = 'ERROR: does not understand command'
        exec(torun)
exit()