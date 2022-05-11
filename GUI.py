from GUI_code import *


def main():
    window = Tk()
    window.title('Final Project')
    window.geometry('500x200')
    widgets = GUI(window)
    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    main()