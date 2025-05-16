from evdev import ecodes

# Special handling for Enter key, used as terminator
BARCODE_END_KEY = ecodes.KEY_ENTER
GLYPH_NOT_FOUND = '□'

keymap = {
    # Numbers
    ecodes.KEY_0: '0',
    ecodes.KEY_1: '1',
    ecodes.KEY_2: '2',
    ecodes.KEY_3: '3',
    ecodes.KEY_4: '4',
    ecodes.KEY_5: '5',
    ecodes.KEY_6: '6',
    ecodes.KEY_7: '7',
    ecodes.KEY_8: '8',
    ecodes.KEY_9: '9',
    
    # Letters
    ecodes.KEY_A: 'A',
    ecodes.KEY_B: 'B',
    ecodes.KEY_C: 'C',
    ecodes.KEY_D: 'D',
    ecodes.KEY_E: 'E',
    ecodes.KEY_F: 'F',
    ecodes.KEY_G: 'G',
    ecodes.KEY_H: 'H',
    ecodes.KEY_I: 'I',
    ecodes.KEY_J: 'J',
    ecodes.KEY_K: 'K',
    ecodes.KEY_L: 'L',
    ecodes.KEY_M: 'M',
    ecodes.KEY_N: 'N',
    ecodes.KEY_O: 'O',
    ecodes.KEY_P: 'P',
    ecodes.KEY_Q: 'Q',
    ecodes.KEY_R: 'R',
    ecodes.KEY_S: 'S',
    ecodes.KEY_T: 'T',
    ecodes.KEY_U: 'U',
    ecodes.KEY_V: 'V',
    ecodes.KEY_W: 'W',
    ecodes.KEY_X: 'X',
    ecodes.KEY_Y: 'Y',
    ecodes.KEY_Z: 'Z',
    
    # Symbols
    ecodes.KEY_SPACE: ' ',
    ecodes.KEY_MINUS: '-',
    ecodes.KEY_EQUAL: '=',
    ecodes.KEY_LEFTBRACE: '[',
    ecodes.KEY_RIGHTBRACE: ']',
    ecodes.KEY_BACKSLASH: '\\',
    ecodes.KEY_SEMICOLON: ';',
    ecodes.KEY_APOSTROPHE: "'",
    ecodes.KEY_GRAVE: '`',
    ecodes.KEY_COMMA: ',',
    ecodes.KEY_DOT: '.',
    ecodes.KEY_SLASH: '/',
    ecodes.KEY_KPASTERISK: '*',
    ecodes.KEY_KPPLUS: '+',
    
    # Numeric keypad
    ecodes.KEY_KP0: '0',
    ecodes.KEY_KP1: '1',
    ecodes.KEY_KP2: '2',
    ecodes.KEY_KP3: '3',
    ecodes.KEY_KP4: '4',
    ecodes.KEY_KP5: '5',
    ecodes.KEY_KP6: '6',
    ecodes.KEY_KP7: '7',
    ecodes.KEY_KP8: '8',
    ecodes.KEY_KP9: '9',
    ecodes.KEY_KPMINUS: '-',
    ecodes.KEY_KPDOT: '.',
    
    # Extended symbols
    ecodes.KEY_LEFTCTRL: '%',
    ecodes.KEY_RIGHTCTRL: '$',
    ecodes.KEY_CAPSLOCK: '!',
    ecodes.KEY_TAB: '\t',
    ecodes.KEY_SYSRQ: '~',
    ecodes.KEY_SCROLLLOCK: '|',
    ecodes.KEY_102ND: '¬',
    
    # Function keys
    ecodes.KEY_F1: 'F1',
    ecodes.KEY_F2: 'F2',
    ecodes.KEY_F3: 'F3',
    ecodes.KEY_F4: 'F4',
    ecodes.KEY_F5: 'F5',
    ecodes.KEY_F6: 'F6',
    ecodes.KEY_F7: 'F7',
    ecodes.KEY_F8: 'F8',
    ecodes.KEY_F9: 'F9',
    ecodes.KEY_F10: 'F10',
    ecodes.KEY_F11: 'F11',
    ecodes.KEY_F12: 'F12'
}