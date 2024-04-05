import curses
import random
from time import sleep

random.seed()
stdscr = curses.initscr()
h, w = stdscr.getmaxyx()
"""Keep it tidy and global, not having to refer to
class, which would be longer to type."""


class TerminalControl:
    def __init__(self):
        curses.start_color()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        curses.curs_set(False)

    def stop_control(self):
        curses.nocbreak()
        stdscr.keypad(False)
        curses.curs_set(True)
        curses.echo()
        curses.endwin()


def wait():
    stdscr.getch()
    stdscr.clear()


def print_c_rows(arr):
    for idx, row in enumerate(arr):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(arr) // 2 + idx
        stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_c_str(txt):
    stdscr.addstr(h // 2, w // 2 - len(txt) // 2, txt)
    stdscr.refresh()


def print_c_moving_str(txt):
    for i, sentence in enumerate(txt):
        stdscr.move(h // 2, w // 2 - len(sentence) // 2)
        stdscr.refresh()
        for char in sentence:
            stdscr.addch(char)
            stdscr.refresh()
            sleep(0.1)
        wait()


def print_s(a=0, b=0, txt=""):
    stdscr.addstr(a, b, txt)
    stdscr.refresh()


class Game:
    def ui(self):
        self.actions = ["(A)ttack", "(H)eal"]
        self.enemy_desc_str = f"Enemy HP: {self.eHP}"
        self.stats = f"HP: {self.pHP} -|- Score: {self.pScore}"
        print_c_rows(self.actions)
        print_s(h // 4, w // 2 - len(self.enemy_desc_str) // 2,
                self.enemy_desc_str)
        print_s(h - 1, w // 2 - len(self.stats) // 2, self.stats)

    def damage_calc(self, roll):
        self.damage = int(-((roll) * (roll - 10)))
        if self.damage < 0:
            self.damage = 0

    def enemy_encounter(self):
        self.random_encounter = [
            "an enemy",
            "a flying beast",
            "a sleeping beast who just woke up",
            "a highwayman",
        ]
        self.enemy = self.random_encounter[
            random.randint(0, len(self.random_encounter) - 1)
        ]
        self.enemy = f"You encountered {self.enemy}!"
        print_c_str(self.enemy)
        wait()
        self.fight = True
        self.eHP = random.randint(1, 20)

    def prologue(self):
        self.prolog = [
            "Darkness has befallen the world.",
            "You are the last hope.",
            "You are on your own, entirely.",
            "And so begins the eternal golden dawn.",
        ]
        self.logo = [
            " ▄▄▄  ▄▄▄  ▄▄▄▄▄▄▄▄  ▄▄        ▄▄▄▄▄▄▄▄  ▄▄▄▄▄       ▄▄▄▄   ▄▄      ▄▄ ▄▄▄   ▄▄ ",
            " ███  ███  ██▀▀▀▀▀▀  ██        ▀▀▀██▀▀▀  ██▀▀▀██    ██▀▀██  ██      ██ ███   ██ ",
            " ████████  ██        ██           ██     ██    ██  ██    ██ ▀█▄ ██ ▄█▀ ██▀█  ██ ",
            " ██ ██ ██  ███████   ██           ██     ██    ██  ██    ██  ██ ██ ██  ██ ██ ██ ",
            " ██ ▀▀ ██  ██        ██           ██     ██    ██  ██    ██  ███▀▀███  ██  █▄██ ",
            " ██    ██  ██▄▄▄▄▄▄  ██▄▄▄▄▄▄     ██     ██▄▄▄██    ██▄▄██   ███  ███  ██   ███ ",
            " ▀▀    ▀▀  ▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀     ▀▀     ▀▀▀▀▀       ▀▀▀▀    ▀▀▀  ▀▀▀  ▀▀   ▀▀▀ ",
        ]
        print_c_moving_str(self.prolog)
        stdscr.clear()
        print_c_rows(self.logo)
        wait()

    def short_intro(self):
        self.intro = [
            "You start with 20 HP.",
            "You will cause random damage when (A)ttacking.",
            "Using (H)eal will restore your HP in random manner.",
            "And remember, try not to die. Last as long as you can.",
        ]
        for i, txt in enumerate(self.intro):
            print_c_str(txt)
            wait()
        stdscr.clear()

    def kill_success(self):
        self.pScore += random.randint(1, 10)
        self.killstr = ("You have slain the enemy!" 
                        f" Total score now: {self.pScore}")
        stdscr.clear()
        print_c_str(self.killstr)
        wait()
        self.fight = False

    def enemy_action(self):
        if self.eHP <= 0:
            self.kill_success()
        else:
            eDMG = random.randint(0, 10)
            self.pHP -= eDMG
            print_s(
                txt=(f"Enemy caused {eDMG} damage!"
                    f" Your current HP is now {self.pHP}")
            )
            self.ui()
            wait()

    def player_action(self):
        self.ui()
        while True:
            key = stdscr.getkey().lower()
            if key == "a":
                self.damage_calc(random.randint(0, 10))
                self.eHP -= self.damage
                stdscr.clear()
                print_s(0, 0, f"You caused {self.damage} to the enemy!")
                self.ui()
                wait()
                break
            elif key == "h":
                self.restore = random.randint(1, 10)
                self.pHP += self.restore
                print_s(0, 0, f"{self.restore} HP gained!")
                self.ui()
                wait()
                if self.pHP > 30:
                    self.pHP = 30
                    print_s(txt="Fully healed!")
                    self.ui()
                    wait()
                break
            else:
                pass

    def gameover(self):
        self.endtext = [
            "You have been slain, unfortunately.",
            f"You survived {self.day} days.",
            f"You achieved a score of {self.pScore}.",
            "The sun has finally set. Rest well, hero.",
        ]
        stdscr.clear()
        print_c_rows(self.endtext)
        wait()

    def thanks(self):
        print_c_str("Thank you for playing!")
        wait()

    def gameplay(self):
        while self.pHP > 0:
            if not (self.fight):
                self.day += 1
                self.enemy_encounter()
            self.player_action()
            self.enemy_action()
        self.gameover()

    def __init__(self):
        self.day = 0
        self.pScore = 0
        self.pHP = 20
        self.fight = False
        stdscr.clear()
        wait()
        self.prologue()
        self.short_intro()
        self.gameplay()


class Start:
    def credits_menu(self):
        self.credits_text = [
            "This game is",
            "dedicated for the open-source",
            "community and for revitalizing my skills.",
            "Written and developed",
            "by Eddie, 2024.",
        ]
        stdscr.clear()
        print_c_rows(self.credits_text)
        stdscr.refresh()

    def print_menu(self):
        stdscr.clear()
        print_c_rows(self.prompt)
        stdscr.refresh()

    def prompt_menu(self):
        while True:
            self.print_menu()
            key = stdscr.getkey()
            if key.lower() == "e":
                break
            elif key.lower() == "c":
                self.credits_menu()
                wait()
                self.print_menu()
            elif key.lower() == "p":
                Game()

    def __init__(self):
        self.entry = ["Meltdown", "Press any key to start."]
        self.prompt = ["(P)lay", "(C)redits", "(E)xit"]
        print_c_rows(self.entry)
        wait()
        self.prompt_menu()


vtcontrol = TerminalControl()
try:
    Start()
except KeyboardInterrupt:
    pass
vtcontrol.stop_control()
