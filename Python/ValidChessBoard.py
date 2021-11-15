#Code to validate a chess board represented by a python dictionary
def isValidChessBoard(board):
    #w stands for white, b stands for black
    num_bking,num_wking=0,0
    num_bqueen,num_wqueen=0,0
    num_bpawn,num_wpawn,num_bknight,num_wknight=0,0,0,0
    num_bbishop,num_wbishop,num_brook,num_wrook=0,0,0,0

    for k,v in board.items():
        position=[]
        position[:0]=k
        #print(position[0])
        #print(position[1])
        if len(position)!=2:
            print('!!! INVALID POSITION COORDINATES ' +k)
        if (int(position[0])>8 or int(position[0])<1) or (position[1]>'h' or position[1]<'a'):
            print('INVALID PIECE POSITION '+k)
        if v=='wking':
            num_wking+=1
        if v=='bking':
            num_bking+=1
        if v=='wqueen':
            num_wqueen+=1
        if v=='bqueen':
            num_bqueen+=1
        if v=='bpawn':
            num_bpawn+=1
        if v=='wpawn':
            num_wpawn+=1
        if v=='bknight':
            num_bknight+=1
        if v=='wknight':
            num_wknight+=1
        if v=='bbishop':
            num_bbishop+=1
        if v=='wbishop':
            num_wbishop+=1
        if v=='brook':
            num_brook+=1
        if v=='wrook':
            num_wrook+=1
        piece=[]
        piece[:0]=v
        if (piece[0]!='w' and piece[0]!='b'):
            print("INVALID PIECE NAME " + v)
        piece_name=''
        for i in range(len(piece)):
            if (i>0):
                piece_name+=piece[i]
        #print(piece_name)
        if (piece_name!='king' and piece_name!='queen' and piece_name!='bishop' and piece_name!='rook' and piece_name!='knight'):
            print("INVALID PIECE NAME")

        if num_wking+num_wqueen+num_wpawn+num_wknight+num_wrook+num_wbishop>16:
            print("INVALID NUMBER OF PIECES: " + str(num_wking+num_wqueen+num_wpawn+num_wknight+num_wrook+num_wbishop))
        if num_bking+num_bqueen+num_bpawn+num_bknight+num_brook+num_bbishop>16:
            print("INVALID NUMBER OF PIECES: " + str(num_bking+num_bqueen+num_bpawn+num_bknight+num_brook+num_bbishop))
        if (num_wking>1 or num_bking>1):
            print("INVALID NUMBER OF PIECES FOR KING: BLACK " + str(num_bking) + " WHITE " + str(num_wking))


chess_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '2h': 'bbishop'}

isValidChessBoard(chess_board)
