terminals_manual = [' 127.0.0. 1 ', ' 127.0.0. 2 ', ' 127.0.0. 3']
terminals_invalid = [
    '127.0.0.1, http://127.0.0.1/python',
    '127.0.0.2, http://127.0.0.2/python',
    '127.0.0.3, http://127.0.0.3/python'
]

controllers_manual = [' 192.168. 1.10:1 ', '192.168. 2.10:2 ', ' 192. 168.3.10 :3']
controllers_invalid = ['192.168.1.10:1', '192.168.2.10:2', '192.168.3.10:3']

terminals = []

# remove all spaces
for terminal in terminals_manual:
    terminals.append(terminal.replace(' ', ''))

# add only ip adresses without http
for terminal in terminals_invalid:
    terminals.append(terminal.split(',')[0])

# remove duplicates
terminals = list(dict.fromkeys(terminals))

# sort terminals
terminals.sort()

controllers = []

for controller in controllers_manual:
    controllers.append(controller.replace(' ', ''))

for controller in controllers_invalid:
    controllers.append(controller)

controllers = list(dict.fromkeys(controllers))
controllers.sort()


print(controllers)
print(terminals)
