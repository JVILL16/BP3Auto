import win32com.client
from zone import *
from zone import getterGreet

def email_bp3(cc_email,file_name, PROD, final_txt):
    ##########################################
    # Opening outlook email to fill in the inputs
    # for the BP3 Template
    ##########################################
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.Display()
    mail.To = 'unknownuser@lgbs.com'
    mail.CC = cc_email
    mail.Subject = file_name
    mail.Body = getterGreet()+'\nPlease post the attached BP3 to '+PROD+'.\n\nThank you,'
    mail.Attachments.Add(final_txt) 