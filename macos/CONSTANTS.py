__all__ = [
    "SOUNDS_SUBMARINE_SOUND",
     'SOUNDS_PING_SOUND',
     'SOUNDS_FUNK_SOUND',
     'SOUNDS_POP_SOUND',
     'SOUNDS_BLOW_SOUND',
     'SOUNDS_GLASS_SOUND', 
        'BLUE_COLOR', 
        'RED_COLOR',
        'GREEN_COLOR', 
        'BLACK_COLOR', 
        'YELLOW_COLOR'
]


# Sounds list


SOUNDS_SUBMARINE_SOUND = 'Submarine'

SOUNDS_POP_SOUND = 'Pop'


SOUNDS_FUNK_SOUND = 'Funk'


SOUNDS_GLASS_SOUND = 'Glass'

SOUNDS_PING_SOUND = 'Ping'


SOUNDS_BLOW_SOUND = 'Blow'


"""Taken from Pyautogui Documentation"""

KeyHexType = {
    'a': 0x00, # kVK_ANSI_A
    's': 0x01, # kVK_ANSI_S
    'd': 0x02, # kVK_ANSI_D
    'f': 0x03, # kVK_ANSI_F
    'h': 0x04, # kVK_ANSI_H
    'g': 0x05, # kVK_ANSI_G
    'z': 0x06, # kVK_ANSI_Z
    'x': 0x07, # kVK_ANSI_X
    'c': 0x08, # kVK_ANSI_C
    'v': 0x09, # kVK_ANSI_V
    'b': 0x0b, # kVK_ANSI_B
    'q': 0x0c, # kVK_ANSI_Q
    'w': 0x0d, # kVK_ANSI_W
    'e': 0x0e, # kVK_ANSI_E
    'r': 0x0f, # kVK_ANSI_R
    'y': 0x10, # kVK_ANSI_Y
    't': 0x11, # kVK_ANSI_T
    '1': 0x12, # kVK_ANSI_1
    '!': 0x12, # kVK_ANSI_1
    '2': 0x13, # kVK_ANSI_2
    '@': 0x13, # kVK_ANSI_2
    '3': 0x14, # kVK_ANSI_3
    '#': 0x14, # kVK_ANSI_3
    '4': 0x15, # kVK_ANSI_4
    '$': 0x15, # kVK_ANSI_4
    '6': 0x16, # kVK_ANSI_6
    '^': 0x16, # kVK_ANSI_6
    '5': 0x17, # kVK_ANSI_5
    '%': 0x17, # kVK_ANSI_5
    '=': 0x18, # kVK_ANSI_Equal
    '+': 0x18, # kVK_ANSI_Equal
    '9': 0x19, # kVK_ANSI_9
    '(': 0x19, # kVK_ANSI_9
    '7': 0x1a, # kVK_ANSI_7
    '&': 0x1a, # kVK_ANSI_7
    '-': 0x1b, # kVK_ANSI_Minus
    '_': 0x1b, # kVK_ANSI_Minus
    '8': 0x1c, # kVK_ANSI_8
    '*': 0x1c, # kVK_ANSI_8
    '0': 0x1d, # kVK_ANSI_0
    ')': 0x1d, # kVK_ANSI_0
    ']': 0x1e, # kVK_ANSI_RightBracket
    '}': 0x1e, # kVK_ANSI_RightBracket
    'o': 0x1f, # kVK_ANSI_O
    'u': 0x20, # kVK_ANSI_U
    '[': 0x21, # kVK_ANSI_LeftBracket
    '{': 0x21, # kVK_ANSI_LeftBracket
    'i': 0x22, # kVK_ANSI_I
    'p': 0x23, # kVK_ANSI_P
    'l': 0x25, # kVK_ANSI_L
    'j': 0x26, # kVK_ANSI_J
    "'": 0x27, # kVK_ANSI_Quote
    '"': 0x27, # kVK_ANSI_Quote
    'k': 0x28, # kVK_ANSI_K
    ';': 0x29, # kVK_ANSI_Semicolon
    ':': 0x29, # kVK_ANSI_Semicolon
    '\\': 0x2a, # kVK_ANSI_Backslash
    '|': 0x2a, # kVK_ANSI_Backslash
    ',': 0x2b, # kVK_ANSI_Comma
    '<': 0x2b, # kVK_ANSI_Comma
    '/': 0x2c, # kVK_ANSI_Slash
    '?': 0x2c, # kVK_ANSI_Slash
    'n': 0x2d, # kVK_ANSI_N
    'm': 0x2e, # kVK_ANSI_M
    '.': 0x2f, # kVK_ANSI_Period
    '>': 0x2f, # kVK_ANSI_Period
    '`': 0x32, # kVK_ANSI_Grave
    '~': 0x32, # kVK_ANSI_Grave
    ' ': 0x31, # kVK_Space
    'space': 0x31,
    '\r': 0x24, # kVK_Return
    '\n': 0x24, # kVK_Return
    'enter': 0x24, # kVK_Return
    'return': 0x24, # kVK_Return
    '\t': 0x30, # kVK_Tab
    'tab': 0x30, # kVK_Tab
    'backspace': 0x33, # kVK_Delete, which is "Backspace" on OS X.
    '\b': 0x33, # kVK_Delete, which is "Backspace" on OS X.
    'esc': 0x35, # kVK_Escape
    'escape': 0x35, # kVK_Escape
    'command': 0x37, # kVK_Command
    'shift': 0x38, # kVK_Shift
    'shiftleft': 0x38, # kVK_Shift
    'capslock': 0x39, # kVK_CapsLock
    'option': 0x3a, # kVK_Option
    'optionleft': 0x3a, # kVK_Option
    'alt': 0x3a, # kVK_Option
    'altleft': 0x3a, # kVK_Option
    'ctrl': 0x3b, # kVK_Control
    'ctrlleft': 0x3b, # kVK_Control
    'shiftright': 0x3c, # kVK_RightShift
    'optionright': 0x3d, # kVK_RightOption
    'ctrlright': 0x3e, # kVK_RightControl
    'fn': 0x3f, # kVK_Function
    'f17': 0x40, # kVK_F17
    'volumeup': 0x48, # kVK_VolumeUp
    'volumedown': 0x49, # kVK_VolumeDown
    'volumemute': 0x4a, # kVK_Mute
    'f18': 0x4f, # kVK_F18
    'f19': 0x50, # kVK_F19
    'f20': 0x5a, # kVK_F20
    'f5': 0x60, # kVK_F5
    'f6': 0x61, # kVK_F6
    'f7': 0x62, # kVK_F7
    'f3': 0x63, # kVK_F3
    'f8': 0x64, # kVK_F8
    'f9': 0x65, # kVK_F9
    'f11': 0x67, # kVK_F11
    'f13': 0x69, # kVK_F13
    'f16': 0x6a, # kVK_F16
    'f14': 0x6b, # kVK_F14
    'f10': 0x6d, # kVK_F10
    'f12': 0x6f, # kVK_F12
    'f15': 0x71, # kVK_F15
    'help': 0x72, # kVK_Help
    'home': 0x73, # kVK_Home
    'pageup': 0x74, # kVK_PageUp
    'pgup': 0x74, # kVK_PageUp
    'del': 0x75, # kVK_ForwardDelete
    'delete': 0x75, # kVK_ForwardDelete
    'f4': 0x76, # kVK_F4
    'end': 0x77, # kVK_End
    'f2': 0x78, # kVK_F2
    'pagedown': 0x79, # kVK_PageDown
    'pgdn': 0x79, # kVK_PageDown
    'f1': 0x7a, # kVK_F1
    'left': 0x7b, # kVK_LeftArrow
    'right': 0x7c, # kVK_RightArrow
    'down': 0x7d, # kVK_DownArrow
    'up': 0x7e, # kVK_UpArrow
    'yen': 0x5d, # kVK_JIS_Yen
    'underscore' : 0x5e, # kVK_JIS_Underscore (only applies to Japanese keyboards)
    'comma': 0x5f, # kVK_JIS_KeypadComma (only applies to Japanese keyboards)
    'eisu': 0x66, # kVK_JIS_Eisu
    'kana': 0x68, # kVK_JIS_Kana
}

RED_COLOR = 'red'

GREEN_COLOR = 'green'

YELLOW_COLOR = 'yellow'

BLUE_COLOR = 'blue'

BLACK_COLOR = 'black'

# END FILE
