from graphics import *

# FUNCTIONS


def myCircle(win,centre,radius,colour):
    c = Circle(centre,radius)
    c.setFill(colour)
    c.draw(win)


def myRect(win, tlPoint, brPoint, colour):
    r = Rectangle(tlPoint,brPoint)
    r.setFill(colour)
    r.draw(win)


def print10():
    print("-" * 10)


def menu():
    print10()
    print("-- MENU --")
    print10()
    print("Select an option")
    print("1 - circle")
    print("2 - rect")
    print("3 -")
    print10()
    return int(input("please select an option: "))


# ENTRY POINT
def main():
    selection = menu()
    if selection == 1:
        pass
    elif selection == 2:
        pass
    else:
        pass

# EXEC (ENTRY POINT)
main()