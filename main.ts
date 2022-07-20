input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    led.stopAnimation()
    if (index < 10) {
        index += 1
    } else {
        basic.showString("Game Over!")
    }
})
let index = 0
let Superheroes = [
"Hulk",
"Captain America",
"Iron Man",
"Spider-man",
"Wonder Woman",
"Batman",
"Antman ",
"Robin",
"Captain Marvel",
"Flash",
"Doctor Strange"
]
index = 0
basic.showString("" + (Superheroes[index]))
basic.forever(function () {
    basic.showString("" + (Superheroes[index]))
})
