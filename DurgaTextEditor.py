from tkinter import *
from PIL import ImageTk, Image
import webbrowser
from tkinter import messagebox
from tkinter import filedialog
import os

######################
# Creating Functions #
######################


# Creating new file
def newFile():
    global file
    root.title("Untitled - Durga Text Editor")
    file = None
    TextArea.delete(1.0, END)


# Opening old file
def openFile():
    global file
    file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Document", "*.txt"), ("Python Files", "*.py")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+" - Durga Text Editor")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


# Saving current file
def saveFile():
    global  file
    if file == None:
        file = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Document", "*.txt"), ("Python Files", "*.py")])

        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+" - Durga Text Editor")
            print("File Saved")

    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


# Exiting from text editor
def exitEditor():
    root.quit()


# Creating cut, copy, paste functions
def cut_text():
    TextArea.event_generate(("<<Cut>>"))


def copy_text():
    TextArea.event_generate(("<<Copy>>"))


def paste_text():
    TextArea.event_generate(("<<Paste>>"))


# Creating callback() function
def callback(url):
    webbrowser.open_new(url)


# Creating about function
def about_dev():
    # root.iconify()
    about = Toplevel()
    about.title("About")
    about.geometry("500x450")
    about.iconphoto(True, PhotoImage(file="/home/soumyo/PycharmProjects/Durga Text Editor/files/icons/about.png"))

    # Creating About Frame
    about_frame = Frame(about, width=400, height=400)
    about_frame.pack(fill="both", expand=1)

    # Adding Developer Image
    dev_img = Image.open("/home/soumyo/PycharmProjects/Durga Text Editor/files/images/about_profile_pic.jpg")
    dev_img = dev_img.resize((150, 151), Image.ANTIALIAS)
    DEV_IMG = ImageTk.PhotoImage(dev_img)
    dev_img_label = Label(about_frame, image=DEV_IMG)
    dev_img_label.grid(row=0, column=0, pady=30, padx=10, rowspan=2)

    # Creating About Label
    about_label1 = Label(about_frame, text="Soumyo Roy", font=("Noto Sans Medium", 20))
    about_label1.grid(row=0, column=1, padx=10, sticky=W)

    about_label2 = Label(about_frame, text="Student\nLoves to develop software and game.\nKrishnanagar, India.",
                         font=("Noto Sans Medium", 12), justify=LEFT)
    about_label2.grid(row=1, column=1, padx=10, columnspan=2, sticky=W)

    about_label3 = Label(about_frame, text="Profiles :-", font=("Noto Sans Medium", 20))
    about_label3.grid(row=2, column=0, sticky=W)

    # Adding profile icons
    fb_icon = Image.open("/home/soumyo/PycharmProjects/Durga Text Editor/files/icons/fb.png")
    fb_icon = fb_icon.resize((40, 40), Image.ANTIALIAS)
    FB_ICON = ImageTk.PhotoImage(fb_icon)
    fb_icon_label = Label(about_frame, image=FB_ICON, justify=LEFT, cursor="hand2")
    fb_icon_label.grid(row=3, column=0, sticky=W, padx=40, pady=30)
    fb_icon_label.bind("<Button-1>", lambda e: callback("https://www.facebook.com/soumyo.roy.31"))  # Creating Hyperlink

    twitter_icon = Image.open("/home/soumyo/PycharmProjects/Durga Text Editor/files/icons/twitter.png")
    twitter_icon = twitter_icon.resize((60, 60), Image.ANTIALIAS)
    TWITTER_ICON = ImageTk.PhotoImage(twitter_icon)
    twitter_icon_label = Label(about_frame, image=TWITTER_ICON, justify=LEFT, cursor="hand2")
    twitter_icon_label.grid(row=3, column=1, sticky=W, padx=10)
    twitter_icon_label.bind("<Button-1>", lambda e: callback("https://twitter.com/RoySoumyo"))  # Creating Hyperlink

    github_icon = Image.open("/home/soumyo/PycharmProjects/Durga Text Editor/files/icons/github3.png")
    github_icon = github_icon.resize((64, 58), Image.ANTIALIAS)
    GITHUB_ICON = ImageTk.PhotoImage(github_icon)
    github_icon_label = Label(about_frame, image=GITHUB_ICON, justify=LEFT, cursor="hand2")
    github_icon_label.grid(row=3, column=2, sticky=W)
    github_icon_label.bind("<Button-1>", lambda e: callback("https://github.com/Soumyo78"))  # Creating Hyperlink

    # Creating Close About Window Function
    def close_about():
        # root.deiconify()
        about.destroy()

    # Adding Close Button
    close_btn = Button(about_frame, text="Close", font=("Arial", 10), command=close_about)
    close_btn.grid(row=4, column=0, columnspan=3, pady=40)

    about.mainloop()


def about_durga_text_editor():
    messagebox.showinfo("About Durga Text Editor", "Thanks for using Durga,\na simple text editor,\nbuilt in python.")


if __name__ == '__main__':

    #######################
    # tKinter Basic Codes #
    #######################
    root = Tk()
    root.title("Untitled - Durga Text Editor")
    root.iconphoto(True, PhotoImage(file="/home/soumyo/PycharmProjects/Durga Text Editor/files/icons/icon.png"))
    root.geometry("644x788")
    root.attributes("-zoomed", True)

    ######################################
    # Adding Text Widget for Typing Text #
    ######################################
    TextArea = Text(root, font=("Noto Mono", 13))
    # Defining current file
    file = None  # Initially defining as 'None'
    # Packing text area
    TextArea.pack(expand=True, fill=BOTH)

    #######################
    # Creating a menu-bar #
    #######################
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Creating sub menus

    # Create File Sub-menu
    file_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=newFile)  # To create new file
    file_menu.add_command(label="Open", command=openFile)  # To open old file
    file_menu.add_command(label="Save", command=saveFile)  # To save current file
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exitEditor)  # To exit from the text editor

    # Create Edit Sub-menu
    edit_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut", command=cut_text)
    edit_menu.add_command(label="Copy", command=copy_text)
    edit_menu.add_separator()
    edit_menu.add_command(label="Paste", command=paste_text)

    # Create Help Sub-menu
    help_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="Developer Info", command=about_dev)
    help_menu.add_command(label="About", command=about_durga_text_editor)

    #####################
    # Adding Scrollbars #
    #####################

    # Creating a vertical ScrollBar
    y_scrollbar = Scrollbar(TextArea)
    y_scrollbar.pack(side=RIGHT, fill=Y)
    y_scrollbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=y_scrollbar.set)

    # Creating a horizontal ScrollBar
    x_scrollbar = Scrollbar(TextArea, orient=HORIZONTAL)
    x_scrollbar.pack(side=BOTTOM, fill=X)
    x_scrollbar.config(command=TextArea.xview)
    TextArea.config(wrap="none", xscrollcommand=x_scrollbar.set)

    ####################################
    # Adding Line Numbers on Left Side #
    ####################################
root.mainloop()