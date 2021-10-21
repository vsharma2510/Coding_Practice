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
            print('!!! INVALID POSITION COORDINATES ' + k)
        if (int(position[0])>8 or int(position[0])<1) or (position[1]>'h' or position[1]<'a'):
            print('INVALID PIECE POSITION '+k)
        


    return num_bking



chess_board={'9h':'bking','6c':'wqueen','2g':'bbishop','5h':'bqueen','3e':'wking'}

isValidChessBoard(chess_board)
