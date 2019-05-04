import sys
del sys.argv[0]
option = ''
if sys.argv[0] == '-option':
    del sys.argv[0]
    option = '-option'

la = sys.argv
la = [int(x) for x in la]
text = ''
nbr_actions = 0
lb = []
nbra = len(la)
nbrb = len(lb)

# [1, 2, 3, 4, 5] => [2, 1, 3, 4, 5]
def sa():
    global text
    global nbr_actions
    nbr_actions = nbr_actions +1
    text = text + 'sa '
    la[0], la[1] = la[1], la[0]
def sb():
    global text
    global nbr_actions
    nbr_actions = nbr_actions +1
    text = text + 'sb '
    first = lb[1]
    lb.insert(0, first)
    del lb[2]
def sc():
    global text
    global nbr_actions
    nbr_actions = nbr_actions +1
    text = text + 'sc '
    sa()
    sb()
# lb-[2, 3, 4, 5] la-[1]
def pa():
    global nbr_actions
    global text
    nbr_actions = nbr_actions +1
    text = text + 'pa '
    first = lb[0]
    del lb[0]
    la.insert(0, first)
# la-[2, 3, 4, 5] lb-[1]
def pb():
    global nbr_actions
    global text
    nbr_actions = nbr_actions +1
    text = text + 'pb '
    first = la[0]
    del la[0]
    lb.insert(0, first)
# [1, 2, 3, 4, 5] => [2, 3, 4, 5, 1]
def ra():
    global nbr_actions
    global text
    nbr_actions = nbr_actions +1
    text = text + 'ra '
    first = la[0]
    la.insert(len(la), first)
    del la[0]
def rb():
    global nbr_actions
    nbr_actions = nbr_actions +1
    global text
    text = text + 'rb '
    first = lb[0]
    lb.insert(len(lb), first)
    del lb[0]
def rr():
    global nbr_actions
    nbr_actions = nbr_actions +1
    global text
    text = text + 'rr '
    ra()
    rb()
# [1, 2, 3, 4, 5] => [5, 1, 2, 3, 4]
def rra():
    global text
    global nbr_actions
    nbr_actions = nbr_actions +1
    text = text + 'rra '
    last = la[(len(la)-1)]
    la.insert(0, last)
    del la[(len(la)-1)]
def rrb():
    global text
    global nbr_actions
    nbr_actions = nbr_actions +1
    text = text + 'rrb '
    last = lb[(len(lb)-1)]
    lb.insert(0, last)
    del lb[(len(lb)-1)]
def rrr():
    global text
    global nbr_actions
    nbr_actions = nbr_actions +1
    text = text + 'rrr '
    rra()
    rrb()



if len(la) > 1 and sorted(la) != la:
    if len(la) == 2 and la != sorted(la):
        sa()
    if len(la) == 3 and la != sorted(la):
        if max(la) == la[(len(la)-1)]:
            sa()
        else:
            index = la.index(max(la))
            if index == 0:
                ra()
            else:
                rra()
                if min(la) != la[0]:
                    sa()
    else:    
        while len(la) > 0:
            for X in la:
                if X == min(la):
                    if (len(la)/2) <= la.index(X):
                        while la.index(X) != 0:
                            rra()
                    if (len(la)/2) > la.index(X):
                        while la.index(X) != 0:
                            ra()
                    pb()
        while len(lb) != 0:
            pa()

if la == sorted(la) and len(la) > 0 and option != '-option':
    text = text.strip()
    print(text)

if option == '-option':
    if la == sorted(la) and len(la) > 0:
        print('List A : ' + str(la))
        if nbr_actions >= 100:
            print("\033[1;31;40m\033[1;05;40m" + 'actions: ' + str(nbr_actions))
        if nbr_actions > 50 and nbr_actions < 100:
            print("\033[1;33;40m" + 'actions: ' + str(nbr_actions))
        if nbr_actions == 1 or nbr_actions == 0:
            print("\033[1;32;40m" + 'action: ' + str(nbr_actions))
        if nbr_actions < 30 and nbr_actions > 1:
            print("\033[1;32;40m" + 'actions: ' + str(nbr_actions))