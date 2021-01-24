import pygame
from Objects2D import Vector2D



KeyPressed = {"a": False, "b": False, "c": False, "d": False, "e": False, "f": False, "g": False, "h": False, "i": False, "j": False, "k": False, "l": False, "m": False, "n": False, "o": False, "p": False, "q": False, "r": False, "s": False, "t": False, "u": False, "v": False, "w": False, "x": False, "y": False, "z": False, "1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False, "0": False, "KP1": False, "KP2": False, "KP3": False, "KP4": False, "KP5": False, "KP6": False, "KP7": False, "KP8": False, "KP9": False, "KP0": False, "space": False, "lshift": False, "lctrl": False, "lalt": False,"up": False, "down": False,"left": False,"right": False, }
KeyDown = {"a": False, "b": False, "c": False, "d": False, "e": False, "f": False, "g": False, "h": False, "i": False, "j": False, "k": False, "l": False, "m": False, "n": False, "o": False, "p": False, "q": False, "r": False, "s": False, "t": False, "u": False, "v": False, "w": False, "x": False, "y": False, "z": False, "1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False, "0": False, "KP1": False, "KP2": False, "KP3": False, "KP4": False, "KP5": False, "KP6": False, "KP7": False, "KP8": False, "KP9": False, "KP0": False, "space": False, "lshift": False, "lctrl": False, "lalt": False,"up": False, "down": False,"left": False,"right": False, }
InputMouse = {"click0" : False, "click1" : False, "click2": False}
mousePos = Vector2D(0,0)


def input():
    from Agine_main import gameDisplay, cameraPos
    mousePos.x = pygame.mouse.get_pos()[0] - gameDisplay.display.get_width() / 2 + cameraPos[0]
    mousePos.y = -pygame.mouse.get_pos()[1]  + gameDisplay.display.get_width() / 2 + cameraPos[0]

    keyPressed = pygame.key.get_pressed()
    mouseClicked = pygame.mouse.get_pressed()

    #keyboard
    #Pressed
    #Letters
    KeyPressed["a"] = keyPressed[pygame.K_a]
    KeyPressed["b"] = keyPressed[pygame.K_b]
    KeyPressed["c"] = keyPressed[pygame.K_c]
    KeyPressed["d"] = keyPressed[pygame.K_d]
    KeyPressed["e"] = keyPressed[pygame.K_e]
    KeyPressed["f"] = keyPressed[pygame.K_f]
    KeyPressed["g"] = keyPressed[pygame.K_g]
    KeyPressed["h"] = keyPressed[pygame.K_h]
    KeyPressed["i"] = keyPressed[pygame.K_i]
    KeyPressed["j"] = keyPressed[pygame.K_j]
    KeyPressed["k"] = keyPressed[pygame.K_k]
    KeyPressed["l"] = keyPressed[pygame.K_l]
    KeyPressed["m"] = keyPressed[pygame.K_m]
    KeyPressed["n"] = keyPressed[pygame.K_n]
    KeyPressed["o"] = keyPressed[pygame.K_o]
    KeyPressed["p"] = keyPressed[pygame.K_p]
    KeyPressed["q"] = keyPressed[pygame.K_q]
    KeyPressed["r"] = keyPressed[pygame.K_r]
    KeyPressed["s"] = keyPressed[pygame.K_s]
    KeyPressed["t"] = keyPressed[pygame.K_t]
    KeyPressed["u"] = keyPressed[pygame.K_u]
    KeyPressed["v"] = keyPressed[pygame.K_v]
    KeyPressed["w"] = keyPressed[pygame.K_w]
    KeyPressed["x"] = keyPressed[pygame.K_x]
    KeyPressed["y"] = keyPressed[pygame.K_y]
    KeyPressed["z"] = keyPressed[pygame.K_z]

    #numbers
    KeyPressed["1"] = keyPressed[pygame.K_1]
    KeyPressed["2"] = keyPressed[pygame.K_2]
    KeyPressed["3"] = keyPressed[pygame.K_3]
    KeyPressed["4"] = keyPressed[pygame.K_4]
    KeyPressed["5"] = keyPressed[pygame.K_5]
    KeyPressed["6"] = keyPressed[pygame.K_6]
    KeyPressed["7"] = keyPressed[pygame.K_7]
    KeyPressed["8"] = keyPressed[pygame.K_8]
    KeyPressed["9"] = keyPressed[pygame.K_9]
    KeyPressed["0"] = keyPressed[pygame.K_0]
    #KeyPad
    KeyPressed["KP1"] = keyPressed[pygame.K_KP1]
    KeyPressed["KP2"] = keyPressed[pygame.K_KP2]
    KeyPressed["KP3"] = keyPressed[pygame.K_KP3]
    KeyPressed["KP4"] = keyPressed[pygame.K_KP4]
    KeyPressed["KP5"] = keyPressed[pygame.K_KP5]
    KeyPressed["KP6"] = keyPressed[pygame.K_KP6]
    KeyPressed["KP7"] = keyPressed[pygame.K_KP7]
    KeyPressed["KP8"] = keyPressed[pygame.K_KP8]
    KeyPressed["KP9"] = keyPressed[pygame.K_KP9]
    KeyPressed["KP0"] = keyPressed[pygame.K_KP0]

    #Left
    KeyPressed["lshift"] = keyPressed[pygame.K_LSHIFT]
    KeyPressed["lctrl"] = keyPressed[pygame.K_LCTRL]
    KeyPressed["lalt"] = keyPressed[pygame.K_LALT]

    KeyPressed["space"] = keyPressed[pygame.K_SPACE]
    if KeyPressed["space"]:
        KeyDown["space"] = False

    #DOWN
    event = pygame.event.get(pygame.KEYDOWN)
    for e in event:
        KeyDown["space"] = e.key == pygame.K_SPACE

    #UP


