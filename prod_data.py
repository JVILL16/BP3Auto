import sys,re
from errors import *
from errors import popupmsg

###############################
# Opening file paths and txt files
#############################
hou_f_path = 'PRODS/01_HOUPROD.txt'
sa_f_path = 'PRODS/02_SAPROD.txt'
toll_f_path = 'PRODS/03_TOLL.txt'
self_f_path = 'PRODS/04_SELFPAY.txt'
calif_f_path = 'PRODS/05_CALIF.txt'
chicago_f_path = 'PRODS/06_CHICAGO.txt'

hou_f = open(hou_f_path, 'r')
sa_f = open(sa_f_path, 'r')
toll_f = open(toll_f_path, 'r')
self_f = open(self_f_path, 'r')
calif_f = open(calif_f_path, 'r')
chicago_f = open(chicago_f_path, 'r')

def prod(txt_file_clientcode):

    ################################
    # Determining the email in which PROD it is in 
    # and inputting the CM for the cc
    ################################
    if txt_file_clientcode in hou_f.read():
        with open(hou_f_path,'r') as file:
            for line in file:
                if txt_file_clientcode in line:
                    email = re.search(r'\w+.\w+@\w+.com', line)
                    cc_email = email.group(0)     
        PROD = 'HOUPROD'
        hou_f.seek(0)
    elif txt_file_clientcode in sa_f.read():
        with open(sa_f_path,'r') as file:
            for line in file:
                if txt_file_clientcode in line:
                    email = re.search(r'\w+.\w+@\w+.com', line)
                    cc_email = email.group(0)        
        PROD = 'SAPROD'
        sa_f.seek(0)
    elif txt_file_clientcode in toll_f.read():
        with open(toll_f_path,'r') as file:
            for line in file:
                if txt_file_clientcode in line:
                    email = re.search(r'\w+.\w+@\w+.com', line)
                    cc_email = email.group(0)          
        PROD = 'TOLL'
        toll_f.seek(0)
    elif txt_file_clientcode in self_f.read():
        with open(self_f_path,'r') as file:
            for line in file:
                if txt_file_clientcode in line:
                    email = re.search(r'\w+.\w+@\w+.com', line)
                    cc_email = email.group(0)
        PROD = 'SELFPAY'
        self_f.seek(0)
    elif txt_file_clientcode in calif_f.read():
        with open(calif_f_path,'r') as file:
            for line in file:
                if txt_file_clientcode in line:
                    email = re.search(r'\w+.\w+@\w+.com', line)
                    cc_email = email.group(0)
        PROD = 'CALIF'
        calif_f.seek(0)
    elif txt_file_clientcode in chicago_f.read():
        with open(chicago_f_path,'r') as file:
            for line in file:
                if txt_file_clientcode in line:
                    email = re.search(r'\w+.\w+@\w+.com', line)
                    cc_email = email.group(0)
        PROD = 'CHICAGO'
        chicago_f.seek(0)
    else:
        popupmsg('Value doesn\'t exists. Please check the file to see if the client number is correct')
        PROD = ''
        cc_email = ''
    return PROD,cc_email