color_encoded = {
"black": 0, 
"brown": 1, 
"red": 2, 
"orange": 3, 
"yellow": 4, 
"green": 5, 
"blue": 6, 
"violet": 7, 
"grey": 8, 
"white": 9}

def color_code(color):
    # for color_found, code in color_encoded:
    #     if color == color_found:
    #         return code
    return color_encoded[color]


def colors():
    return list(color_encoded.keys())
