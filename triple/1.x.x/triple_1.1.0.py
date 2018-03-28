#TRIPLE-LANG
print 'TRIPLE-LANG TRANSPILER IN PYTHON\n'
while True:
    dic = []
    commands = ['PUT', 'END', 'ADD', 'SUB', 'MUL', 'DIV', 'GET', 'LSS', 'GRT', 'EQL', 'LEQ', 'GEQ']
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8, -9]
    string = ''
    usrinput = raw_input()
    usrarray = usrinput.split()
    x = 0
    while len(dic) < len(usrarray):
        dic.append(usrarray[x])
        x += 1
    if 'ADD' in dic:
        if dic[0] == 'PUT':
            torun = 'print ' + dic[1] + ' + ' + dic[3]
            exec(torun)
        else:
            torun = dic[0] + ' + ' + dic[2]
            exec(torun)
    elif 'SUB' in dic:
        if dic[0] == 'PUT':
            torun = 'print ' + dic[1] + ' - ' + dic[3]
            exec(torun)
        else:
            torun = dic[0] + ' - ' + dic[2]
            exec(torun)
    elif 'MUL' in dic:
        if dic[0] == 'PUT':
            torun = 'print ' + dic[1] + ' * ' + dic[3]
            exec(torun)
        else:
            torun = dic[0] + ' * ' + dic[2]
            exec(torun)
    elif 'DIV' in dic:
        if dic[0] == 'PUT':
            torun = 'print ' + dic[1] + ' / ' + dic[3]
            exec(torun)
        else:
            torun = dic[0] + ' / ' + dic[2]
            exec(torun)
    elif dic[0] == 'END':
        break
    elif dic[0] == 'PUT':
        if len(dic) > 2:
            if dic[2] == 'LSS':
                torun = 'print ' + dic[1] + ' < ' + dic[3]
            elif dic[2] == 'GRT':
                torun = 'print ' + dic[1] + ' > ' + dic[3]
            elif dic[2] == 'EQL':
                torun = 'print ' + dic[1] + ' = ' + dic[3]
            elif dic[2] == 'LEQ':
                torun = 'print ' + dic[1] + ' <= ' + dic[3]
            elif dic[2] == 'GEQ':
                torun = 'print ' + dic[1] + ' >= ' + dic[3]
        else:
            string = ' \''
            command = ''
            string += ' '.join(dic[1:])
            command = commands[0]
            string += '\''
            torun = command + string
        exec(torun)
    elif dic[0] == 'GET':
        command = 'raw_input()'
        torun = 'print ' + command
        exec(torun)
    elif dic[0] in num:
        if dic[1] == 'LSS':
            torun = dic[0] + ' < ' + dic[2]
        elif dic[1] == 'GRT':
            torun = dic[0] + ' > ' + dic[2]
        elif dic[1] == 'EQL':
            torun = dic[0] + ' = ' + dic[2]
        elif dic[1] == 'LEQ':
            torun = dic[0] + ' <= ' + dic[2]
        elif dic[1] == 'GEQ':
            torun = dic[0] + ' >= ' + dic[2]
        exec(torun)
    else:
        torun = 'ERROR: does not understand command'
        exec(torun)
exit()