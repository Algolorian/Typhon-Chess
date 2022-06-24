import pyautogui

# I tried to make it play the stockfish website but retrieving the on screen board bp takes 50 sec
# an estimated 75 min game no way i can make it play 100,000 games maybe in the future I'll add
# multithreading and it'll be fast enough

directory = 'D:\\Pycharm_Database\\Typhon_Directory\\Stockfish Image Library\\'

bp = []

for j in range(8):
    for i in range(8):
        pic = pyautogui.locateOnScreen('blank_1.png',
                                       region=(339 + (i * 74), 794 - (j * 74), 10, 20),
                                       grayscale=True
                                       )
        if pic is not None:
            bp.append('0')
        pic = pyautogui.locateOnScreen('blank_2.png',
                                       region=(339 + (i * 74), 794 - (j * 74), 10, 20),
                                       grayscale=True
                                       )
        if pic is not None:
            bp.append('0')
        pic = pyautogui.locateOnScreen('white_pawn.png',
                                       region=(339 + (i * 74), 794 - (j * 74), 10, 20),
                                       grayscale=True
                                       )
        if pic is not None:
            bp.append('P')
        pic = pyautogui.locateOnScreen('black_pawn.png',
                                       region=(339 + (i * 74), 794 - (j * 74), 10, 20),
                                       grayscale=True
                                       )
        if pic is not None:
            bp.append('p')
        pic = pyautogui.locateOnScreen('white_rook.png',
                                       region=(339 + (i * 74), 794 - (j * 74), 10, 20),
                                       grayscale=True
                                       )
        if pic is not None:
            bp.append('R')
        pic = pyautogui.locateOnScreen('black_rook.png',
                                       region=(339 + (i * 74), 794 - (j * 74), 10, 20),
                                       grayscale=True
                                       )
        if pic is not None:
            bp.append('r')
        pic = pyautogui.locateOnScreen('white_byshop.png',
                                       region=(339 + (i * 74), 794 - (j * 74), 10, 20),
                                       grayscale=True
                                       )
        if pic is not None:
            bp.append('')
        pic = pyautogui.locateOnScreen('black_byshop.png',
                                       region=(339 + (i * 74), 794 - (j * 74), 10, 20),
                                       grayscale=True
                                       )
        if pic is not None:
            bp.append('0')
