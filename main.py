TEST_LIST = [
    "0", 
    "1", 
    "2", 
    "3", 
    "4", 
    "5",
    "6",
    "7",
    "8",
    "9",
    "+",
    "-",
    "*",
    "/",
    "E"]
expression = [""]
position_in_list = 0
def on_forever():
    def on_button_pressed_a():
        global position_in_list
        global TEST_LIST
        position_in_list -= 1
        if position_in_list == -1:
            position_in_list = len(TEST_LIST) - 1

    def on_button_pressed_b():
        global position_in_list
        global TEST_LIST
        position_in_list += 1
        if position_in_list > len(TEST_LIST) - 1:
            position_in_list = 0

    def on_button_pressed_ab():
        global expression
        global TEST_LIST
        global position_in_list
        if TEST_LIST == [""]:
            expression.append(TEST_LIST[position_in_list])
    input.on_button_pressed(Button.B, on_button_pressed_b)
    input.on_button_pressed(Button.A, on_button_pressed_a)
    input.on_button_pressed(Button.AB, on_button_pressed_ab)
    basic.show_string(TEST_LIST[position_in_list])
basic.forever(on_forever)
