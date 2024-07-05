#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
PyAppDevKit Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
PyAppDevKit All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/PyAppDevKit
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/PyAppDevKit"""

import os, time, platform
from PyAppDevKit.InfoLib.pyappdevkit_info import *

def error_msg(error_dialog):
    print(error_dialog)

def exit_program_dialog_time(exit_dialog_msg,userTime):
    print(exit_dialog_msg)
    userTime = int(userTime)
    time.sleep(userTime)
    if platform.system() == "Windows":
        os.system("exit")
    else:
        exit()

def exit_program_time(userTime):
    userTime = int(userTime)
    time.sleep(userTime)
    if platform.system() == "Windows":
        os.system("exit")
    else:
        exit()

def exit_program_dialog(exit_dialog_msg):
    print(exit_dialog_msg)
    if platform.system() == "Windows":
        os.system("exit")
    else:
        exit()

""" Example Dialog (ExitSelectDialog): "Select the method to exit the program (0: Dialogue and Time entry, 1: Time entry only, 2: Dialogue entry only, 3: Normal exit (old style)): "
 Example Dialog (userTimeDialog): "After how many seconds should the program be closed?: "
 Example Dialog (exitDialog): "Exit program..."
 Example Dialog (errormsgDialog): "Invalid Command!" """

def all_exit(ExitSelectDialog,userTimeDialog,exitDialog,errormsgDialog):
    exit_select = int(input(ExitSelectDialog))
    exit_select = int(exit_select)
    if exit_select == 0:
        userTime = input(userTimeDialog)
        exit_program_dialog_time(exitDialog, userTime)
    elif exit_select == 1:
        userTime = input(userTimeDialog)
        exit_program_time(userTime)
    elif exit_select == 2:
        exit_program_dialog(exitDialog)
    elif exit_select == 3:
        exit()
    else:
        print(errormsgDialog)

def program_welcome_msg(welcome_msg,cfg):
    print(welcome_msg)
    if cfg == 1:
        LibAbout()
    elif cfg == 0:
        pass

def program_info(programnamedialog,program_name,programversiondialog,program_version,programsupportosdialog,program_support_os,programlicencedialog,program_licence,programimplementedcontractsdialog,program_imp_contracts,programimplementedcontractswebsitedialog,program_imp_contracts_web_site,programauthordialog,program_author,programauthorwebsitedialog,program_author_web_site,programreleasedatedialog,program_rs_date,programlastupdatedatedialog,program_last_update_date):
    print("{0} {1}". format(programnamedialog,program_name))
    print("{0} {1}". format(programversiondialog,program_version))
    print("{0} {1}". format(programsupportosdialog,program_support_os))
    print("{0} {1}". format(programlicencedialog,program_licence))
    print("{0} {1}". format(programimplementedcontractsdialog,program_imp_contracts))
    print("{0} {1}". format(programimplementedcontractswebsitedialog,program_imp_contracts_web_site))
    print("{0} {1}". format(programauthordialog,program_author))
    print("{0} {1}". format(programauthorwebsitedialog,program_author_web_site))
    print("{0} {1}". format(programreleasedatedialog,program_rs_date))
    print("{0} {1}". format(programlastupdatedatedialog,program_last_update_date))