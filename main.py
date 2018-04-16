from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
palos = (255,255,255)
fondo = (0,0,0)
pink = (255,105,180)
pell = (171,128,55)
cap_difunto = (255,0,255)

def base():
    G = green
    Y = yellow
    B = blue
    O = fondo
    w = palos
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, w, w, w, O, O, O, O,
    ]
    return logo

def fallo_1():
    G = green
    R = red
    O = fondo
    w = palos
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, w, w, w, O, O, O, O,
    ]
    return logo

def fallo_2():
    w = palos
    O = fondo

    logo = [
    O, O, O, O, O, O, O, O,
    O, O, w, w, w, w, O, O,
    O, O, w, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, w, w, w, O, O, O, O,
    ]
    return logo



def cabeza():
    O = fondo
    w = palos
    C = pell
    logo = [ 
    O, O, O, O, O, O, O, O,
    O, O, w, w, w, w, O, O,
    O, O, w, O, O, C, O, O,
    O, O, w, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, w, w, w, O, O, O, O,
    ]
    return logo
    
def torso():
    O = fondo
    w = palos
    C = pell
    B = blue
    logo = [ 
    O, O, O, O, O, O, O, O,
    O, O, w, w, w, w, O, O,
    O, O, w, O, O, C, O, O,
    O, O, w, O, O, B, O, O,
    O, O, w, O, O, B, O, O,
    O, O, w, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, w, w, w, O, O, O, O,
    ]
    return logo
    
def bras_1():
    O = fondo
    w = palos
    C = pell
    B = blue
    logo = [ 
    O, O, O, O, O, O, O, O,
    O, O, w, w, w, w, O, O,
    O, O, w, O, O, C, O, O,
    O, O, w, O, C, B, O, O,
    O, O, w, O, O, B, O, O,
    O, O, w, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, w, w, w, O, O, O, O,
    ]
    return logo
    
def bras_2():
    O = fondo
    w = palos
    C = pell
    B = blue
    logo = [ 
    O, O, O, O, O, O, O, O,
    O, O, w, w, w, w, O, O,
    O, O, w, O, O, C, O, O,
    O, O, w, O, C, B, C, O,
    O, O, w, O, O, B, O, O,
    O, O, w, O, O, O, O, O,
    O, O, w, O, O, O, O, O,
    O, w, w, w, O, O, O, O,
    ]
    return logo
    
def cama_1():
    O = fondo
    w = palos
    C = pell
    B = blue
    logo = [ 
    O, O, O, O, O, O, O, O,
    O, O, w, w, w, w, O, O,
    O, O, w, O, O, C, O, O,
    O, O, w, O, C, B, C, O,
    O, O, w, O, O, B, O, O,
    O, O, w, O, C, O, O, O,
    O, O, w, O, O, O, O, O,
    O, w, w, w, O, O, O, O,
    ]
    return logo
    
def cama_2():
    O = fondo
    w = palos
    C = pell
    B = blue
    logo = [ 
    O, O, O, O, O, O, O, O,
    O, O, w, w, w, w, O, O,
    O, O, w, O, O, C, O, O,
    O, O, w, O, C, B, C, O,
    O, O, w, O, O, B, O, O,
    O, O, w, O, C, O, C, O,
    O, O, w, O, O, O, O, O,
    O, w, w, w, O, O, O, O,
    ]
    return logo
    

def muerto():
    O = fondo
    w = palos
    C = pell
    R = red
    L = cap_difunto
    logo = [ 
    O, O, O, O, O, O, O, O,
    O, O, w, w, w, w, O, O,
    O, O, w, O, O, L, O, O,
    O, O, w, O, R, R, R, O,
    O, O, w, O, O, R, O, O,
    O, O, w, O, R, O, R, O,
    O, O, w, O, O, O, O, O,
    O, w, w, w, O, O, O, O,
    ]
    return logo

images = [base, fallo_1, fallo_2, cabeza, torso, bras_1, bras_2, cama_1, cama_2, muerto]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
