state = 'stopped'
while True:
    input1 = input('>').lower()
    if input1 == 'help':
        print('''
Choose:
    start
    stop
    quit
        ''')
    elif input1 == 'start':
        if state == 'stopped':
            print('Car started')
            state = 'started'
        else:
            print('Already started')
    elif input1 == 'stop':
        if state == 'started':
            print('Car stopped')
            state = 'stopped'
        else:
            print('Already stopped')
    elif input1 == 'quit':
        break
    else:
        print("I don't understand")
