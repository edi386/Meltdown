![image](https://github.com/edi386/Meltdown/assets/166058453/d69310a5-c5ea-47af-aded-1eb3cdedd597)

# Meltdown - A short, ncurses Python console game

A simple, rudimentary even, ncurses-based Python console game that you can always re-play. The premise is: *survive as long as possible.*

## The W-Questions

I chose to build this project because I strive to not just refresh and improve my development skills, but to get comfortable wandering outside of my comfort zone, to learn to use anything (especially docs!) at my disposal and rely on myself. Additionally, being a fan of (retro) games and literature, I had the classic story of hero vs the dark world in mind, so it served as an inspiration that ultimately culminated in choosing said idea, a ncurses-based Python game.

The challenges that awaited me at the beginning of making the project was that I haven't learnt necessary basics of ncurses, the POSIX library providing an API for text-based user interface, yet. So I firstly devoted myself to understanding the basics of manipulating the console and commanding it in a way that you can do cool things with it, such as colors, placing text in different positions, as well as intentionally breaking things to see what would happen. With ncurses, simply worded, you create programs that rely on TUI. It's surprisingly simpler after reading, understanding and playing around; in easiest terms, you initialize the window, flip switches, do anything within the framework and when you're done, revert switches to original position and end the window, returning the terminal to its original state. A well-known example of a program using ncurses is GNU Midnight Commander or htop.

Another challenge was that I froze coding for months to focus on important life matters, so it took a while to quickly re-learn and understand, it was however trivial. I wanted to structure my code better, so later on I learnt classes quickly and applied them, writing in OOP manner for the rest of the project.

What I learnt when making this project, besides the library and specific things, was how important it is to have a trained mind that can store vital ideas and constantly think, be it solutions, ways or to ponder. And when things get too complex or large for my mind, I learnt to rely on note-taking, especially notebooks, to simplify and dumb down things. As well, having an attitude of self-critique and persistence in spite of difficulties helps.

The program itself does only the basics and minimal things needed. Refreshing the values after terminal resize, handling mouse input, and other relevant things are thus not considered.

After all, it's a simple game. See and enjoy!

## Before you run:

The following requirements:
- Python 3
- curses library (currently used version is 2.2)
- A contemporary terminal

## I got an error and now my terminal is broken

Type `reset` and done. It restores the terminal to defaults.
