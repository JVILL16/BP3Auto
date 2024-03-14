from tkinter import messagebox, simpledialog

def popupmsg(msg):
    messagebox.showerror("ERROR!", msg)

def warnpopupmsg(msg):
    messagebox.showwarning("WARNING!", msg)
    
def signpopupmsg(sign): 
    while sign == None or sign == '000' or sign == '':
        sign = simpledialog.askstring('Signature', 'Type in your signature: ')
        sign = str(sign).upper()
        if sign.isalpha()==False or sign == None or len(sign) != 3 or sign == '' or sign == '000':
            popupmsg("Please try again...")
            sign = '000'
    return sign
    
            