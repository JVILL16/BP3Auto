from venv import create
from auto import *
import tkinter
from tkinter.ttk import *
from tkinter import *
import os

def launch():

    root = tkinter.Tk()
    root.title(string='BP3 TEST')
    p1 = PhotoImage(file = 'assets/linebarger_logo.png')  
    root.iconphoto(False, p1)         
    root.geometry('700x900+800+450') 
    root.minsize(700, 600)
    menubar = Menu(root, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')  
    file = Menu(menubar, background='#ffcc99', foreground='black')
    file.add_command(label="Log File", command=lambda: os.startfile('assets\logging.log'))  
    file.add_command(label="Exit", command=root.quit)  
    menubar.add_cascade(label="File", menu=file) 

    #########################################
    # Label on the top
    #########################################
    top_label = Label(root, text ='\nNew updates to come out soon! Please read the following when\n'+
                        'proceding these automations', font=("Arial", 15),justify= CENTER)

    #########################################
    # BP3 automation section 
    #########################################
    bp3_frame = Frame(root,bg='#07758B',bd=8)
    bp3_menu(bp3_frame)

    #########################################
    # BP3 File automation section 
    #########################################
    bp3_file_frame = Frame(root,bg='#999',bd=8)
    file_frame = Frame(root,bg='#07758B',bd=8)
    bp3_file_menu(bp3_file_frame,file_frame)

    erc_dmv_frame = Frame(root,bg='#999',bd=8)
    erc_dmv_menu(erc_dmv_frame)
    
    


    ########################################
    # Connecting and setting the objects up in order 
    ########################################
    root.config(menu=menubar)
    top_label.pack()
    bp3_frame.pack(padx = 5, pady = 20)
    bp3_file_frame.pack(padx = 5, pady = 20)
    file_frame.pack(padx = 5, pady = 20)
    erc_dmv_frame.pack(padx = 5, pady = 20)
    
    #os.startfile('assets\BP3_TEMPLATE_TEST.xlsx')
    return root

def bp3_menu(bp3_frame):
    
    l_automate = Label(bp3_frame, text = "SENDING WITH EMAIL - Click the automation button \nIF you QUICK SAVED BP3 Template\n"
                        +"and everything is correct: ",font=("Arial", 10))

    btn_automate = Button(bp3_frame, foreground = "red", background = "#42FF33", text = 'BP3 Automate!', command = automate_bp3)

    l_automate.grid(row=0, column=0, padx=20, pady=20)
    btn_automate.grid(row=0, column=1, padx=10, pady=10)

def bp3_file_menu(bp3_file_frame,file_frame):

    l_automate = Label(bp3_file_frame, text = "FOR THE FILE ONLY - Click the automation button \nIF you QUICK SAVED BP3 Template\n"
                        +"and everything is correct: ",font=("Arial", 10))

    btn_automate = Button(bp3_file_frame, foreground = "red", background = "#42FF33", text = 'BP3 File Automate!', command=lambda: file_show(file_frame))

    l_automate.grid(row=0, column=0, padx=20, pady=20)
    btn_automate.grid(row=0, column=1, padx=10, pady=10)

 
def file_show(file_frame):
    
    values = automate_bp3_file()
    file_name = values[0]
    final_txt = values[1]
    txt_file_clientcode = values[2]
    ts = values[3]

    btn_file_open = Button(file_frame, text="BP3 File", foreground = "red", background = "#42FF33",command=lambda: os.startfile(final_txt))
    l_file_automate = Label(file_frame, text = f"Client #: {txt_file_clientcode} \n\n"+
                            f"File Name: {file_name}",font=("Arial", 10),justify= LEFT)
    l_timestamp = Label(file_frame, background = "yellow", text = f"TimeStamp: {ts}",font=("Arial", 10),justify= CENTER)
    l_file_automate.grid(row=0, column=0, padx=20, pady=5)
    btn_file_open.grid(row=0, column=1, padx=10, pady=20)
    l_timestamp.grid(row=1, column=0, padx=20, pady=20)

def erc_dmv_menu(erc_dmv_frame):

    dir_name,str_date_time,year = ERC_STOP_time()
    for file_name in glob.glob('/DMV/ERC_STOP'+year+'*'):
        file_path = os.path.join(dir_name, file_name)
        print(file_path)
        timestamp_str = time.strftime(  '%m/%d/%Y',
                                        time.gmtime(os.path.getmtime(file_path)))
        if timestamp_str == str_date_time:
            print('true')
            img = PhotoImage(file='assets/GL.png')
        elif timestamp_str != str_date_time:
            print('false')
            img = PhotoImage(file='assets/RL.png')
    
    l_automate = Label(erc_dmv_frame, text = "ERC DMV Release Files Task",font=("Arial", 10))

    btn_automate = Button(erc_dmv_frame, foreground = "red", background = "#42FF33", text = 'ERC_STOP Automate!', command= dmv_erc_stop)

    #img_label = Label(erc_dmv_frame, image=img, background = "#999", borderwidth=0, highlightthickness=0)

    l_automate.grid(row=0, column=0, padx=20, pady=20)
    btn_automate.grid(row=0, column=1, padx=10, pady=10)
    #img_label.grid(row=0, column=2, padx=10, pady=10)
    #img_label.image_names = img
    
    
    


launch().mainloop()