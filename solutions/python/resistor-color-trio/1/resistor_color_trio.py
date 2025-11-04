color_code = {
"black": "0",
"brown": "1",
"red": "2",
"orange": "3",
"yellow": "4",
"green": "5",
"blue": "6",
"violet": "7",
"grey": "8",
"white": "9",
}        

def label(colors):
    if color_code[colors[0]] == "0" and color_code[colors[1]] == "0":
        return "0 ohms"
        
    resistor = ""
    index = 0
    if color_code[colors[0]] != "0":
        resistor = color_code[colors[0]]
    if color_code[colors[1]] != "0":
        resistor += color_code[colors[1]]
    else: index += 1
        
    index += int(color_code[colors[2]])
    prefix = ""

    if index > 8:
        index -= 9
        prefix = "giga"
    if index > 5:
        index -= 6        
        prefix = "mega"
    if index > 1:
        index -= 3
        prefix = "kilo"
    
    while index > 0:
        resistor += "0"
        print("while")
        print(resistor)
        index =- 1

    resistor += " " + prefix + "ohms"
    return resistor