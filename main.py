def on_button_pressed_a():
    global index
    basic.clear_screen()
    led.stop_animation()
    if index < 11:
        index += 1
    else:
        basic.show_string("Game Over!")
input.on_button_pressed(Button.A, on_button_pressed_a)

index = 0
Superheroes = ["Hulk",
    "Captain America",
    "Iron Man",
    "Spider-man",
    "Wonder Woman",
    "Batman",
    "Antman ",
    "Robin",
    "Captain Marvel",
    "Flash",
    "Doctor Strange"]
index = 0
basic.show_string("" + (Superheroes[index]))

def on_forever():
    basic.show_string("" + (Superheroes[index]))
basic.forever(on_forever)
