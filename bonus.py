if nbr_actions >= 100:
    print("\033[1;31;40m\033[1;05;40m" + 'actions: ' + str(nbr_actions))
if nbr_actions > 50 and nbr_actions < 100:
    print("\033[1;33;40m" + 'actions: ' + str(nbr_actions))
if nbr_actions == 1 or nbr_actions == 0:
    print("\033[1;32;40m" + 'action: ' + str(nbr_actions))
if nbr_actions < 30 and nbr_actions > 1:
    print("\033[1;32;40m" + 'actions: ' + str(nbr_actions))

if la == sorted(la) and len(la) > 0:
    print(la)