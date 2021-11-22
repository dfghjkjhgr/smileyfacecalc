TEST_LIST = ["A", "B", "C", "D"]
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

    input.on_button_pressed(Button.B, on_button_pressed_b)
    input.on_button_pressed(Button.A, on_button_pressed_a)
    basic.show_string(TEST_LIST[position_in_list])
basic.forever(on_forever)
