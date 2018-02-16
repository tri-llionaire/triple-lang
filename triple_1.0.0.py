#TRIPLE-LANG
print 'WELCOME TO THE TRIPLE CONSOLE\n'
while 1 == 1:
    dic = []
    commands = {'PRI': 'print', 'END': 'exit'}
    string = ''
    usrinput = raw_input()
    usrarray = usrinput.split()
    x = 0
    while len(dic) < len(usrarray):
        dic.append(usrarray[x])
        x += 1
    string = '\' '
    command = ''
    string += str(dic[1])
    command = commands[dic[0]]
    string += '\''
    torun = command + string
    exec(torun)