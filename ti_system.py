import pygame
import time

_current_key = 0
# Keymap, more will be added as needed
keymap = {
    pygame.K_LEFT: 24,
    pygame.K_RIGHT: 26,
    pygame.K_UP: 25,
    pygame.K_DOWN: 34,
    pygame.K_RETURN: 105,
    pygame.K_1: 11,
    pygame.K_2: 12,
    pygame.K_3: 13,
    pygame.K_4: 14,
    pygame.K_5: 15
}

def check():
    if not pygame.get_init() or pygame.display.get_surface() is None:
        pygame.init()
        if not pygame.display.get_init():
            pygame.display.init()

def handle_event(event, keymap):
    global _current_key
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    elif event.type == pygame.KEYDOWN:
        if event.key in keymap:
            _current_key = keymap[event.key]

def getKey(idk):
    global _current_key
    check()
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in keymap:
                _current_key = keymap[event.key]
    
    if idk == 0:
        key = _current_key
        _current_key = 0 # single press
        return key
    return wait_key()
def get_key(idk):
    return getKey(idk)
def sleep(seconds):
    time.sleep(seconds)
def wait(seconds):
    time.sleep(seconds)
def wait_key():
    while True:
        event = pygame.event.wait()
        handle_event(event, keymap)
        if _current_key != 0:
            return getKey(0)
# useless stubs, submit PR if you want lol
def disp_at(row, col, text):
    pass
def disp_clr():
    pass
def disp_cursor(idk):
    pass
def disp_wait():
    pass
def escape():
    pass
def recall_RegEQ():
    pass
def recall_list():
    pass
def store_list():
    pass
