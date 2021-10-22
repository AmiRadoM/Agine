import pygame
from .Objects2D import Vector2D



KeyPressed = {"a": False, "b": False, "c": False, "d": False, "e": False, "f": False, "g": False, "h": False, "i": False, "j": False, "k": False, "l": False, "m": False, "n": False, "o": False, "p": False, "q": False, "r": False, "s": False, "t": False, "u": False, "v": False, "w": False, "x": False, "y": False, "z": False, "1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False, "0": False, "KP1": False, "KP2": False, "KP3": False, "KP4": False, "KP5": False, "KP6": False, "KP7": False, "KP8": False, "KP9": False, "KP0": False, "space": False, "lshift": False, "lctrl": False, "lalt": False, "rshift": False, "rctrl": False, "ralt": False,"up": False, "down": False,"left": False,"right": False, }
KeyDown = {"a": False, "b": False, "c": False, "d": False, "e": False, "f": False, "g": False, "h": False, "i": False, "j": False, "k": False, "l": False, "m": False, "n": False, "o": False, "p": False, "q": False, "r": False, "s": False, "t": False, "u": False, "v": False, "w": False, "x": False, "y": False, "z": False, "1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False, "0": False, "KP1": False, "KP2": False, "KP3": False, "KP4": False, "KP5": False, "KP6": False, "KP7": False, "KP8": False, "KP9": False, "KP0": False, "space": False, "lshift": False, "lctrl": False, "lalt": False, "rshift": False, "rctrl": False, "ralt": False,"up": False, "down": False,"left": False,"right": False, }
KeyUp = {"a": False, "b": False, "c": False, "d": False, "e": False, "f": False, "g": False, "h": False, "i": False, "j": False, "k": False, "l": False, "m": False, "n": False, "o": False, "p": False, "q": False, "r": False, "s": False, "t": False, "u": False, "v": False, "w": False, "x": False, "y": False, "z": False, "1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False, "0": False, "KP1": False, "KP2": False, "KP3": False, "KP4": False, "KP5": False, "KP6": False, "KP7": False, "KP8": False, "KP9": False, "KP0": False, "space": False, "lshift": False, "lctrl": False, "lalt": False, "rshift": False, "rctrl": False, "ralt": False,"up": False, "down": False,"left": False,"right": False, }

MousePressed = {"button0" : False, "button1" : False, "button2": False}
MouseDown = {"button0" : False, "button1" : False, "button2": False}
MouseUp = {"button0" : False, "button1" : False, "button2": False}

mousePos = Vector2D(0,0)


def inputSystem():

    #KEYBOARD
    #Pressed
    keyPressed = pygame.key.get_pressed()

    #Letters
    KeyPressed["a"] = keyPressed[pygame.K_a]
    if KeyPressed["a"]:
        KeyDown["a"] = False
    else:
        KeyUp["a"] = False
    KeyPressed["b"] = keyPressed[pygame.K_b]
    if KeyPressed["b"]:
        KeyDown["b"] = False
    else:
        KeyUp["b"] = False
    KeyPressed["c"] = keyPressed[pygame.K_c]
    if KeyPressed["c"]:
        KeyDown["c"] = False
    else:
        KeyUp["c"] = False
    KeyPressed["d"] = keyPressed[pygame.K_d]
    if KeyPressed["d"]:
        KeyDown["d"] = False
    else:
        KeyUp["d"] = False
    KeyPressed["e"] = keyPressed[pygame.K_e]
    if KeyPressed["e"]:
        KeyDown["e"] = False
    else:
        KeyUp["e"] = False
    KeyPressed["f"] = keyPressed[pygame.K_f]
    if KeyPressed["f"]:
        KeyDown["f"] = False
    else:
        KeyUp["f"] = False
    KeyPressed["g"] = keyPressed[pygame.K_g]
    if KeyPressed["g"]:
        KeyDown["g"] = False
    else:
        KeyUp["g"] = False
    KeyPressed["h"] = keyPressed[pygame.K_h]
    if KeyPressed["h"]:
        KeyDown["h"] = False
    else:
        KeyUp["h"] = False
    KeyPressed["i"] = keyPressed[pygame.K_i]
    if KeyPressed["i"]:
        KeyDown["i"] = False
    else:
        KeyUp["i"] = False
    KeyPressed["j"] = keyPressed[pygame.K_j]
    if KeyPressed["j"]:
        KeyDown["j"] = False
    else:
        KeyUp["j"] = False
    KeyPressed["k"] = keyPressed[pygame.K_k]
    if KeyPressed["k"]:
        KeyDown["k"] = False
    else:
        KeyUp["k"] = False
    KeyPressed["l"] = keyPressed[pygame.K_l]
    if KeyPressed["l"]:
        KeyDown["l"] = False
    else:
        KeyUp["l"] = False
    KeyPressed["m"] = keyPressed[pygame.K_m]
    if KeyPressed["m"]:
        KeyDown["m"] = False
    else:
        KeyUp["m"] = False
    KeyPressed["n"] = keyPressed[pygame.K_n]
    if KeyPressed["n"]:
        KeyDown["n"] = False
    else:
        KeyUp["n"] = False
    KeyPressed["o"] = keyPressed[pygame.K_o]
    if KeyPressed["o"]:
        KeyDown["o"] = False
    else:
        KeyUp["o"] = False
    KeyPressed["p"] = keyPressed[pygame.K_p]
    if KeyPressed["p"]:
        KeyDown["p"] = False
    else:
        KeyUp["p"] = False
    KeyPressed["q"] = keyPressed[pygame.K_q]
    if KeyPressed["q"]:
        KeyDown["q"] = False
    else:
        KeyUp["q"] = False
    KeyPressed["r"] = keyPressed[pygame.K_r]
    if KeyPressed["r"]:
        KeyDown["r"] = False
    else:
        KeyUp["r"] = False
    KeyPressed["s"] = keyPressed[pygame.K_s]
    if KeyPressed["s"]:
        KeyDown["s"] = False
    else:
        KeyUp["s"] = False
    KeyPressed["t"] = keyPressed[pygame.K_t]
    if KeyPressed["t"]:
        KeyDown["t"] = False
    else:
        KeyUp["t"] = False
    KeyPressed["u"] = keyPressed[pygame.K_u]
    if KeyPressed["u"]:
        KeyDown["u"] = False
    else:
        KeyUp["u"] = False
    KeyPressed["v"] = keyPressed[pygame.K_v]
    if KeyPressed["v"]:
        KeyDown["v"] = False
    else:
        KeyUp["v"] = False
    KeyPressed["w"] = keyPressed[pygame.K_w]
    if KeyPressed["w"]:
        KeyDown["w"] = False
    else:
        KeyUp["w"] = False
    KeyPressed["x"] = keyPressed[pygame.K_x]
    if KeyPressed["x"]:
        KeyDown["x"] = False
    else:
        KeyUp["x"] = False
    KeyPressed["y"] = keyPressed[pygame.K_y]
    if KeyPressed["y"]:
        KeyDown["y"] = False
    else:
        KeyUp["y"] = False
    KeyPressed["z"] = keyPressed[pygame.K_z]
    if KeyPressed["z"]:
        KeyDown["z"] = False
    else:
        KeyUp["z"] = False

    #numbers
    KeyPressed["1"] = keyPressed[pygame.K_1]
    if KeyPressed["1"]:
        KeyDown["1"] = False
    else:
        KeyUp["1"] = False
    KeyPressed["2"] = keyPressed[pygame.K_2]
    if KeyPressed["2"]:
        KeyDown["2"] = False
    else:
        KeyUp["2"] = False
    KeyPressed["3"] = keyPressed[pygame.K_3]
    if KeyPressed["3"]:
        KeyDown["3"] = False
    else:
        KeyUp["3"] = False
    KeyPressed["4"] = keyPressed[pygame.K_4]
    if KeyPressed["4"]:
        KeyDown["4"] = False
    else:
        KeyUp["4"] = False
    KeyPressed["5"] = keyPressed[pygame.K_5]
    if KeyPressed["5"]:
        KeyDown["5"] = False
    else:
        KeyUp["5"] = False
    KeyPressed["6"] = keyPressed[pygame.K_6]
    if KeyPressed["6"]:
        KeyDown["6"] = False
    else:
        KeyUp["6"] = False
    KeyPressed["7"] = keyPressed[pygame.K_7]
    if KeyPressed["7"]:
        KeyDown["7"] = False
    else:
        KeyUp["7"] = False
    KeyPressed["8"] = keyPressed[pygame.K_8]
    if KeyPressed["8"]:
        KeyDown["8"] = False
    else:
        KeyUp["8"] = False
    KeyPressed["9"] = keyPressed[pygame.K_9]
    if KeyPressed["9"]:
        KeyDown["9"] = False
    else:
        KeyUp["9"] = False
    KeyPressed["0"] = keyPressed[pygame.K_0]
    if KeyPressed["0"]:
        KeyDown["0"] = False
    else:
        KeyUp["0"] = False
    #KeyPad
    KeyPressed["KP1"] = keyPressed[pygame.K_KP1]
    if KeyPressed["KP1"]:
        KeyDown["KP1"] = False
    else:
        KeyUp["KP1"] = False
    KeyPressed["KP2"] = keyPressed[pygame.K_KP2]
    if KeyPressed["KP2"]:
        KeyDown["KP2"] = False
    else:
        KeyUp["KP2"] = False
    KeyPressed["KP3"] = keyPressed[pygame.K_KP3]
    if KeyPressed["KP3"]:
        KeyDown["KP3"] = False
    else:
        KeyUp["KP3"] = False
    KeyPressed["KP4"] = keyPressed[pygame.K_KP4]
    if KeyPressed["KP4"]:
        KeyDown["KP4"] = False
    else:
        KeyUp["KP4"] = False
    KeyPressed["KP5"] = keyPressed[pygame.K_KP5]
    if KeyPressed["KP5"]:
        KeyDown["KP5"] = False
    else:
        KeyUp["KP5"] = False
    KeyPressed["KP6"] = keyPressed[pygame.K_KP6]
    if KeyPressed["KP6"]:
        KeyDown["KP6"] = False
    else:
        KeyUp["KP6"] = False
    KeyPressed["KP7"] = keyPressed[pygame.K_KP7]
    if KeyPressed["KP7"]:
        KeyDown["KP7"] = False
    else:
        KeyUp["KP7"] = False
    KeyPressed["KP8"] = keyPressed[pygame.K_KP8]
    if KeyPressed["KP8"]:
        KeyDown["KP8"] = False
    else:
        KeyUp["KP8"] = False
    KeyPressed["KP9"] = keyPressed[pygame.K_KP9]
    if KeyPressed["KP9"]:
        KeyDown["KP9"] = False
    else:
        KeyUp["KP9"] = False
    KeyPressed["KP0"] = keyPressed[pygame.K_KP0]
    if KeyPressed["KP0"]:
        KeyDown["KP0"] = False
    else:
        KeyUp["KP0"] = False

    #Left
    KeyPressed["lshift"] = keyPressed[pygame.K_LSHIFT]
    if KeyPressed["lshift"]:
        KeyDown["lshift"] = False
    else:
        KeyUp["lshift"] = False
    KeyPressed["lctrl"] = keyPressed[pygame.K_LCTRL]
    if KeyPressed["lctrl"]:
        KeyDown["lctrl"] = False
    else:
        KeyUp["lctrl"] = False
    KeyPressed["lalt"] = keyPressed[pygame.K_LALT]
    if KeyPressed["lalt"]:
        KeyDown["lalt"] = False
    else:
        KeyUp["lalt"] = False

    #Space
    KeyPressed["space"] = keyPressed[pygame.K_SPACE]
    if KeyPressed["space"]:
        KeyDown["space"] = False
    else:
        KeyUp["space"] = False

    #Right
    KeyPressed["rshift"] = keyPressed[pygame.K_RSHIFT]
    if KeyPressed["rshift"]:
        KeyDown["rshift"] = False
    else:
        KeyUp["rshift"] = False
    KeyPressed["rctrl"] = keyPressed[pygame.K_RCTRL]
    if KeyPressed["rctrl"]:
        KeyDown["rctrl"] = False
    else:
        KeyUp["rctrl"] = False
    KeyPressed["ralt"] = keyPressed[pygame.K_RALT]
    if KeyPressed["ralt"]:
        KeyDown["ralt"] = False
    else:
        KeyUp["ralt"] = False

    #Arrows
    KeyPressed["up"] = keyPressed[pygame.K_UP]
    if KeyPressed["up"]:
        KeyDown["up"] = False
    else:
        KeyUp["up"] = False
    KeyPressed["down"] = keyPressed[pygame.K_DOWN]
    if KeyPressed["down"]:
        KeyDown["down"] = False
    else:
        KeyUp["down"] = False
    KeyPressed["left"] = keyPressed[pygame.K_LEFT]
    if KeyPressed["left"]:
        KeyDown["left"] = False
    else:
        KeyUp["left"] = False
    KeyPressed["right"] = keyPressed[pygame.K_RIGHT]
    if KeyPressed["right"]:
        KeyDown["right"] = False
    else:
        KeyUp["right"] = False

    #Down
    event = pygame.event.get(pygame.KEYDOWN)
    for e in event:
        #letters
        KeyDown["a"] = e.key == pygame.K_a
        KeyDown["b"] = e.key == pygame.K_b
        KeyDown["c"] = e.key == pygame.K_c
        KeyDown["d"] = e.key == pygame.K_d
        KeyDown["e"] = e.key == pygame.K_e
        KeyDown["f"] = e.key == pygame.K_f
        KeyDown["g"] = e.key == pygame.K_g
        KeyDown["h"] = e.key == pygame.K_h
        KeyDown["i"] = e.key == pygame.K_i
        KeyDown["j"] = e.key == pygame.K_j
        KeyDown["k"] = e.key == pygame.K_k
        KeyDown["l"] = e.key == pygame.K_l
        KeyDown["m"] = e.key == pygame.K_m
        KeyDown["n"] = e.key == pygame.K_n
        KeyDown["o"] = e.key == pygame.K_o
        KeyDown["p"] = e.key == pygame.K_p
        KeyDown["q"] = e.key == pygame.K_q
        KeyDown["r"] = e.key == pygame.K_r
        KeyDown["s"] = e.key == pygame.K_s
        KeyDown["t"] = e.key == pygame.K_t
        KeyDown["u"] = e.key == pygame.K_u
        KeyDown["v"] = e.key == pygame.K_v
        KeyDown["w"] = e.key == pygame.K_w
        KeyDown["x"] = e.key == pygame.K_x
        KeyDown["y"] = e.key == pygame.K_y
        KeyDown["z"] = e.key == pygame.K_z


        KeyDown["space"] = e.key == pygame.K_SPACE

    #Up
    event = pygame.event.get(pygame.KEYUP)
    for e in event:
        # letters
        KeyDown["a"] = e.key == pygame.K_a
        KeyDown["b"] = e.key == pygame.K_b
        KeyDown["c"] = e.key == pygame.K_c
        KeyDown["d"] = e.key == pygame.K_d
        KeyDown["e"] = e.key == pygame.K_e
        KeyDown["f"] = e.key == pygame.K_f
        KeyDown["g"] = e.key == pygame.K_g
        KeyDown["h"] = e.key == pygame.K_h
        KeyDown["i"] = e.key == pygame.K_i
        KeyDown["j"] = e.key == pygame.K_j
        KeyDown["k"] = e.key == pygame.K_k
        KeyDown["l"] = e.key == pygame.K_l
        KeyDown["m"] = e.key == pygame.K_m
        KeyDown["n"] = e.key == pygame.K_n
        KeyDown["o"] = e.key == pygame.K_o
        KeyDown["p"] = e.key == pygame.K_p
        KeyDown["q"] = e.key == pygame.K_q
        KeyDown["r"] = e.key == pygame.K_r
        KeyDown["s"] = e.key == pygame.K_s
        KeyDown["t"] = e.key == pygame.K_t
        KeyDown["u"] = e.key == pygame.K_u
        KeyDown["v"] = e.key == pygame.K_v
        KeyDown["w"] = e.key == pygame.K_w
        KeyDown["x"] = e.key == pygame.K_x
        KeyDown["y"] = e.key == pygame.K_y
        KeyDown["z"] = e.key == pygame.K_z

        KeyUp["space"] = e.key == pygame.K_SPACE








    #MOUSE

    from .Agine_main import gameDisplay
    #Mouse Position
    mousePos.x = pygame.mouse.get_pos()[0] - gameDisplay.display.get_width() / 2
    mousePos.y = -pygame.mouse.get_pos()[1]  + gameDisplay.display.get_width() / 2



    #Pressed
    mousePressed = pygame.mouse.get_pressed()

    MousePressed["button0"] = mousePressed[0]
    MousePressed["button0"] = MouseDown["button0"]
    if MousePressed["button0"]:
        MouseDown["button0"] = False
    else:
        MouseUp["button0"] = False



    #Down
    event = pygame.event.get(pygame.MOUSEBUTTONDOWN)
    for e in event:
        MouseDown["button0"] = e.button == pygame.BUTTON_LEFT
        MouseDown["button1"] = e.button == pygame.BUTTON_MIDDLE
        MouseDown["button2"] = e.button == pygame.BUTTON_RIGHT


    # Up
    event = pygame.event.get(pygame.MOUSEBUTTONUP)
    for e in event:
        MouseUp["button0"] = e.button == pygame.BUTTON_LEFT
        MouseUp["button1"] = e.button == pygame.BUTTON_MIDDLE
        MouseUp["button2"] = e.button == pygame.BUTTON_RIGHT


