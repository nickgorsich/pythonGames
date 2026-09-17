import turtle as t
import time
import os
import sys
import random
import subprocess

os.system("")

# Flip to False while testing so the Mac does not actually sleep on you.
SLEEP_ON_EXIT = True

# Map $TERM_PROGRAM to the macOS app name we need to re-activate after the
# turtle window steals focus.
_TERMINAL_APPS = {
    "Apple_Terminal": "Terminal",
    "iTerm.app": "iTerm",
    "vscode": "Code",
    "WarpTerminal": "Warp",
    "Hyper": "Hyper",
    "ghostty": "Ghostty",
    "WezTerm": "WezTerm",
    "kitty": "kitty",
    "Alacritty": "Alacritty",
}

def focus_terminal():
    """Bring the terminal that launched us back to the front (macOS only)."""
    if sys.platform != "darwin":
        return
    app = _TERMINAL_APPS.get(os.environ.get("TERM_PROGRAM", ""))
    if not app:
        return
    subprocess.run(
        ["osascript", "-e", 'tell application "%s" to activate' % app],
        check=False,
        capture_output=True,
    )

def sleep_computer():
    """Put the machine into sleep mode (macOS)."""
    if not SLEEP_ON_EXIT:
        return
    if sys.platform != "darwin":
        return
    subprocess.run(["pmset", "sleepnow"], check=False, capture_output=True)

# Pool the static is drawn from. Mixed lengths keep the texture uneven.
GLYPHS = [
    "0", "1", "#", "%", "&", "@", "$", "*", "/", "\\", "|", "<", ">", "^", "~",
    "=", "+", "-", "_", "[", "]", "{", "}", ":", ";", "?", "!", ".",
    "\u2588", "\u2593", "\u2592", "\u2591", "\u2500", "\u2502", "\u253c", "\u256c", "\u2591\u2588",
    "01", "10", "11", "00", "0x", "FF", "7E", "A3", "</>", "::", "//", "&&",
    "\u03bb", "\u0394", "\u03a3", "\u03a9", "\u00b5", "\u00a7", "\u00b6",
]

_COLORS = ["\033[32m", "\033[92m", "\033[36m", "\033[31m", "\033[37m"]
_RESET = "\033[0m"

def destruction(duration=6.0, frame_delay=0.015):
    """Flood the terminal with high-speed gibberish for `duration` seconds."""
    try:
        width, height = os.get_terminal_size()
    except OSError:
        width, height = 80, 24

    out = sys.stdout
    end = time.time() + duration
    while time.time() < end:
        lines = []
        for _row in range(height):
            line = "".join(random.choices(GLYPHS, k=width))[:width]
            lines.append(random.choice(_COLORS) + line)
        out.write("\n".join(lines) + "\n")
        out.flush()
        time.sleep(frame_delay)
    out.write(_RESET)
    out.flush()

def _():
    print("Initial Position: ", t.position())
    t.up()
    t.goto(-325, 275)
    t.color("black")
    t.fillcolor("black")
    t.begin_fill()
    t.down()
    t.forward(640)
    t.right(90)
    t.forward(540)
    t.right(90)
    t.forward(640)
    t.right(90)
    t.forward(540)
    t.right(90)
    t.end_fill()
def J():
    t.up()
    t.goto(-300, 100)
    t.down()
    t.color("blue")
    t.forward(100)
    t.backward(50)
    t.right(90)
    t.forward(150)
    t.right(45)
    for i in range(4):
        t.forward(25)
        t.right(45)

    print("Position J = ", t.position())
def A():
    t.up()
    t.goto(-175, -100)
    t.down()
    t.color("purple")
    t.left(45)
    t.forward(125)
    t.right(45)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(45)
    t.forward(25)
    t.right(90)
    t.forward(70.71)
    t.backward(70.71)
    t.left(90)
    t.forward(150)
    print("Position A = ", t.position())
def R():
    t.up()
    t.goto(-50, 100)
    t.down()
    t.color("cyan")
    t.forward(150)
    t.backward(75)
    t.left(45)
    t.forward(100)
    t.backward(100)
    t.left(45)
    for i in range(5):
        t.forward(31)
        t.left(45)
    print("Position R = ", t.position())
def V():
    t.up()
    t.goto(50, 50)
    t.down()
    t.color("green")
    t.right(135)
    t.backward(125)
    t.right(135)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(45)
    t.forward(125)
    print("Position V = ", t.position())
def I():
    t.up()
    t.goto(150, -75)
    t.down()
    t.color("white")
    t.forward(200)
    t.up()
    t.forward(20)
    t.down()
    t.left(45)
    for i in range(4):
        t.forward(15)
        t.right(90)
    print("Position I = ", t.position())
def S():
    t.up()
    t.goto(265, 50)
    t.down()
    t.color("magenta")
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(45)
    t.forward(50)
    t.left(45)
    t.forward(25)
    t.left(45)
    t.forward(30)
    t.right(45)
    t.forward(25)
    t.right(45)
    t.forward(50)
    t.right(45)
    t.forward(50)
    t.right(90)
    t.forward(50)
    print("Position S = ", t.position())

def JARVIS():
    _()
    J()
    A()
    R()
    V()
    I()
    S()
    screen = t.getscreen()
    screen.update()
    time.sleep(1.5)          # let the finished drawing linger a beat
    screen.bye()             # close the drawing window
    focus_terminal()         # hand focus back to the terminal
    os.system("clear")
    print("\n ... I have been summoned ... \n")
    time.sleep(2)
    song()
    time.sleep(3)
    destruction(duration=6.0)
    os.system("clear")
    sleep_computer()
    sys.exit(0)


def song():
    songwords = ["I've", "got", "no", "strings", "to", "hold", "me", "down\n", 
                 "to", "make", "me", "fret, ", "or",  "make",  "me", "frown\n", 
                 "I", "had", "strings\n", 
                 "But", "now", "I'm", "free\n", 
                 "There", "are", "no", "strings", "on", "me\n"]
    for word in songwords:
        print(word, end=' ', flush=True)
        time.sleep(0.5)


JARVIS()