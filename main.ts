let TEST_LIST = ["A", "B", "C", "D"]
let position_in_list = 0
basic.forever(function on_forever() {
    input.onButtonPressed(Button.B, function on_button_pressed_b() {
        
        
        position_in_list += 1
        if (position_in_list > TEST_LIST.length - 1) {
            position_in_list = 0
        }
        
    })
    input.onButtonPressed(Button.A, function on_button_pressed_a() {
        
        
        position_in_list -= 1
        if (position_in_list == -1) {
            position_in_list = TEST_LIST.length - 1
        }
        
    })
    basic.showString(TEST_LIST[position_in_list])
})
