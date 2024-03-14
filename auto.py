from tkinter import *
import pandas as pd
import numpy as np
import re, sys, os, glob, time
from zipfile import ZipFile
from emails import email_bp3
from signatures import *
from zone import *
from prod_data import *
from errors import *

def automate_bp3():

    file_name,final_txt,txt_file_clientcode = convert_bp3()

    #######################################
    # Outlook BP3 email generater
    #######################################
    PROD, cc_email = prod(txt_file_clientcode)
    email_bp3(cc_email,file_name, PROD, final_txt)
    logging('BP3 Email with '+txt_file_clientcode)

def automate_bp3_file():
    ts = timestamp()
    file_name,final_txt,txt_file_clientcode = convert_bp3()
    logging('Text file with '+txt_file_clientcode)
    return [file_name,final_txt,txt_file_clientcode,ts]

def convert_bp3():

    ####################################
    # Read and store content of an excel file 
    ####################################
    read_file = pd.read_excel('assets/BP3_TEMPLATE_TEST.xlsx', converters={'CRN': lambda x: str(x)})
    read_file['TRANS DATE'] = pd.to_datetime(read_file['TRANS DATE']).dt.strftime('%m/%d/%Y')
    txt_file_clientcode = read_file.loc[0]['CLIENT #']
    read_file.fillna('', inplace=True)
    my_output_file = [read_file.columns.tolist()] + read_file.values.tolist()

    #############################################
    # Opens up the txt file and inputs the csv info into it
    #############################################
    while True:
        clientcode = re.sub(r'\d{0,2}$|\d[.XP]\d{0,2}$', '', txt_file_clientcode)
        rcl_fields = read_file[['BALANCE','TRANS AMOUNT','PRE-ACTION','PRE-STATUS']]
        adj_fields = read_file[['BALANCE','TRANS AMOUNT']]
        swc_fields = read_file['PRE-STATUS'] 
        sign = getterSig()
        month_date = getterMonth()
        try:         
            if rcl_fields.values.any() == '':
                bp3_rcl_txt = 'BP3_Test\RCL\BP3_'+clientcode+'n_RCL_'+sign+'_2022'+month_date+'.txt'
                np.savetxt(bp3_rcl_txt, my_output_file, fmt='%s', delimiter='\t')
                file_name = os.path.basename(bp3_rcl_txt)
                final_txt = os.path.realpath(bp3_rcl_txt)
                break
            elif adj_fields.values.any() != '':
                bp3_adj_txt = 'BP3_Test\ADJ\BP3_'+clientcode+'n_ADJ_'+sign+'_2022'+month_date+'.txt' 
                np.savetxt(bp3_adj_txt, my_output_file, fmt='%s', delimiter='\t')
                file_name = os.path.basename(bp3_adj_txt)
                final_txt = os.path.realpath(bp3_adj_txt)
                break
            elif swc_fields.values.any() == 'SWC':
                bp3_swc_txt = 'BP3_Test\SWC\BP3_'+clientcode+'n_SWC_'+sign+'_2022'+month_date+'.txt' 
                np.savetxt(bp3_swc_txt, my_output_file, fmt='%s', delimiter='\t')
                file_name = os.path.basename(bp3_swc_txt)
                final_txt = os.path.realpath(bp3_swc_txt)
                break
            else: 
                popupmsg('\n\nFields were off, please look into the file and try again.\n\n')
                continue
        except:
            popupmsg('\n\nTEXT FILE WAS NOT GENERATED\n\n')
            sys.exit()
    return file_name,final_txt,txt_file_clientcode

def dmv_erc_stop():
    dir_name,str_date_time,year = ERC_STOP_time()
    str_date_time = '06/02/2022'
    for file_name in glob.glob('/DMV/ERC_STOP'+year+'*'):
        file_path = os.path.join(dir_name, file_name)
        timestamp_str = time.strftime(  '%m/%d/%Y',
                                        time.gmtime(os.path.getmtime(file_path)))
        if timestamp_str == str_date_time:
            txt_name = os.path.basename(file_path)
            file_txt_name = 'U:/Zip/'+txt_name+'.txt'
            zipfile_name = 'U:/Zip/'+txt_name+'.zip'
            with open(file_path, 'r') as oldfile, open(file_txt_name, 'w') as newfile, ZipFile(zipfile_name, 'w') as myzip:
                for line in oldfile:
                    txt = re.sub(r"^.{0,11}\s+\d+\n","",line)
                    newfile.write(txt)
                newfile.close()
                oldfile.close()
                myzip.write(file_txt_name,arcname=txt_name+'.txt')
                myzip.close()
    