 ##!/usr/bin/python3
 ## pyinstaller --onefile --icon=./16.ico activar.pyw



import tkinter
from tkinter import messagebox,StringVar,Tk,font,ttk
import os
from os import remove,path
import subprocess
import urllib.request

root=tkinter.Tk()
root.geometry("245x402+600+200")
root.resizable(width=False,height=False)
root.title("MT Activation WO")
root.config(cursor="trek",background="sky blue")
root.attributes('-topmost', True)
#root.iconbitmap(default='16.ico')
################################ VARIABLES #####################################################################
Varversion=StringVar()
VarCodigo=StringVar()
VarServer1=StringVar()
VarRearm=StringVar()
VarEstado=StringVar()
lis1=[]
UserName=os.getlogin()
print(UserName)

ComboServer =ttk.Combobox(root,textvariable=VarServer1,justify="right")
ComboVersion =ttk.Combobox(root,textvariable=Varversion,justify="right",state="readonly")
#####################################FUNCIONES###############################
def funcomboserver():
    try:        
        ComboServer.place( x=70, y = 33)
        ComboServer.config(width=25, height=10)
        ComboServer["values"]=(urllib.request.urlopen("https://pastebin.com/raw/1JaHWpa9").read().decode())
        ComboServer.current(1)
    except:
        messagebox.showerror("Error","Por favor revisa tu conexión a internet luego presiona el boton Actualizar")
def funversion():
    try:
        ComboVersion.place( x=10, y = 10)
        ComboVersion.config(width=35, height=20)
        ComboVersion["values"]=(urllib.request.urlopen("https://pastebin.com/raw/vnFRargV").read().decode())
        ComboVersion.current(0)
    except:
        messagebox.showwarning("Error","Por favor revisa tu conexión a internet \n\n e intentalo de nuevo ")
def Actualizar():
    funversion()
    funcomboserver()
    if len(lis1) >= 2:    
        subprocess.call("cmd /c start https://drive.google.com/drive/folders/12m0ZxdvEWCsAS-XWDO-7fF2spL4uC81H?usp=sharing/")
        lis1.insert(0,len(lis1)+1)
        messagebox.showinfo("Mensaje","Se abrira una ventana en el navegador para descargar y actualizar el programa de activacion  \nLa contraseña del archivo es  : OFFICE ")
    else:
        lis1.insert(-1,len(lis1)+1)
Actualizar()
def activarwin():
    try:
        fileser=open(f'c:\\activar.bat','w')
        if Varversion.get()=="Windows 10 Home":                    
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")
        
        if Varversion.get()=="Windows 10 Home N":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk 3KHY7-WNT83-DGQKR-F7HPR-844BM\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")
        
        if Varversion.get()=="Windows 10 Home Single Language":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")
        
        if Varversion.get()=="Windows 10 Home Country Specific":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk PVMJN-6DFY6-9CCP6-7BKTT-D3WVR\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 10 Professional":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")
            
        if Varversion.get()=="Windows 10 Professional N":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk MH37W-N47XK-V7XM9-C7227-GCQG9\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")
        
        if Varversion.get()=="Windows 10 Education":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 10 Education N":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")
        
        if Varversion.get()=="Windows 10 Enterprise":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")
        
        if Varversion.get()=="Windows 10 Enterprise N":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")
        
        if Varversion.get()=="Windows 10 Enterprise 2015 LTSB":      
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk WNMTR-4C88C-JK8YV-HQ7T2-76DF9\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 10 Enterprise 2015 LTSB N":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk 2F77B-TNFGY-69QQF-B8YKP-D69TJ\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 8 Core":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk BN3D2-R7TKB-3YPBD-8DRP2-27GG4\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 8 Core Single Language":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk 2WN2H-YGCQR-KFX6K-CD6TF-84YXQ\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 8 Professional":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk NG4HW-VH26C-733KW-K6F98-J8CK4\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 8 Professional N":       
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk XCVCF-2NXM9-723PB-MHCB7-2RYQQ\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 8 Professional WMC":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk GNBB8-YVD74-QJHX6-27H4K-8QHDG\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 8 Enterprise":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk 32JNW-9KQ84-P47T8-D8GGY-CWCK7\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 8 Enterprise N":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk JMNMF-RHW7P-DMY6X-RF3DR-X2BQT\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")
        
        if Varversion.get()=="Windows 8.1 Core":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk M9Q9P-WNJJT-6PXPY-DWX8H-6XWKK\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 8.1 Core N":       
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk 7B9N3-D94CG-YTVHR-QBPX3-RJP64\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 8.1 Core Single Language":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk BB6NG-PQ82V-VRDPW-8XVD2-V8P66\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 8.1 Professional":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk GCRJD-8NW9H-F2CDX-CCM8D-9D6T9\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 8.1 Professional N":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk HMCNV-VVBFX-7HMBH-CTY9B-B4FXY\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 8.1 Professional WMC":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk 789NJ-TQK6T-6XTH8-J39CJ-J8D3P\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 8.1 Enterprise":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk MHF9N-XY6XB-WVXMC-BTDCT-MKKG7\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")

        if Varversion.get()=="Windows 8.1 Enterprise N":        
            fileser.write("@echo off\ncscript.exe c:\windows\system32\slmgr.vbs /ipk TT4HM-HN7YT-62K67-RGRQJ-JFFXW\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr")
##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Versiones de Windows Server>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if Varversion.get()=="Windows Server 2016 Essentials":        
            fileser.write("@echo off\ncolor 2\ncscript.exe c:\windows\system32\slmgr.vbs /ipk JCKRF-N37P4-C2D82-9YXRT-4M63B\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
         
        if Varversion.get()=="Windows Server 2016 Standard":        
            fileser.write("@echo off\ncolor\ncscript.exe c:\windows\system32\slmgr.vbs /ipk WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        
        if Varversion.get()=="Windows Server 2016 Datacenter":        
            fileser.write("@echo off\ncolor\ncscript.exe c:\windows\system32\slmgr.vbs /ipk CB7KF-BWN84-R7R2Y-793K2-8XDDG\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        
        if Varversion.get()=="Windows Server 2019 Standard":        
            fileser.write("@echo off\ncolor\ncscript.exe c:\windows\system32\slmgr.vbs /ipk N69G4-B89J2-4G8F4-WWYCC-J464C\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        
        if Varversion.get()=="Windows Server 2019 Datacenter":        
            fileser.write("@echo off\ncolor\ncscript.exe c:\windows\system32\slmgr.vbs /ipk WMDGN-G9PQG-XVVXX-R3X43-63DFG\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        
        if Varversion.get()=="Windows Server 2022 Standard":        
            fileser.write("@echo off\ncolor\ncscript.exe c:\windows\system32\slmgr.vbs /ipk VDYBN-27WPP-V4HQT-9VMD4-VMK7H\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        
        if Varversion.get()=="Windows Server 2022 Datacenter":        
            fileser.write("@echo off\ncolor\ncscript.exe c:\windows\system32\slmgr.vbs /ipk WX4NM-KYWYW-QJJR4-XV3QB-6VM33\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        
        if Varversion.get()=="Windows Server 2012 R2 Datacenter":        
            fileser.write("@echo off\ncolor\ncscript.exe c:\windows\system32\slmgr.vbs /ipk W3GGN-FT8W3-Y4M27-J84CP-Q3VJ9\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        
        if Varversion.get()=="Windows Server 2012 R2 Standard":        
            fileser.write("@echo off\ncolor\ncscript.exe c:\windows\system32\slmgr.vbs /ipk D2N9P-3P6X9-2R39C-7RTCD-MDVJX\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        
        if Varversion.get()=="Windows Server 2012 Datacenter":        
            fileser.write("@echo off\ncolor\ncscript.exe c:\windows\system32\slmgr.vbs /ipk 48HP8-DN98B-MYWDG-T2DCC-8W83P\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        
        if Varversion.get()=="Windows Server 2012 Standard":        
            fileser.write("@echo off\ncolor\ncscript.exe c:\windows\system32\slmgr.vbs /ipk XC9B7-NBPP2-83J2H-RHMBY-92BT4\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        
        if Varversion.get()=="Windows Server 2008 R2 Datacenter":        
            fileser.write("@echo off\ncolor\ncscript.exe c:\windows\system32\slmgr.vbs /ipk 74YFP-3QFB3-KQT8W-PMXWJ-7M648\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        
        if Varversion.get()=="Windows Server 2008 R2 Entreprise":        
            fileser.write("@echo off\ncolor\ncscript.exe c:\windows\system32\slmgr.vbs /ipk 489J6-VHDMP-X63PK-3K798-CPX3Y\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        
        if Varversion.get()=="Windows Server 2008 R2 Standard":        
            fileser.write("@echo off\ncolor\ncscript.exe c:\windows\system32\slmgr.vbs /ipk YC6KT-GKW9T-YTKYR-T4X34-R7VHC\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        
        if Varversion.get()=="Windows Server 2008 Datacenter":        
            fileser.write("@echo off\ncolor\ncscript.exe c:\windows\system32\slmgr.vbs /ipk 7M67G-PC374-GR742-YH8V4-TCBY3\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        
        if Varversion.get()=="Windows Server 2008 Entreprise":        
            fileser.write("@echo off\ncolor 2\ncscript.exe c:\windows\system32\slmgr.vbs /ipk YQGMW-MPWTJ-34KDK-48M3W-X4Q6V\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        
        if Varversion.get()=="Windows Server 2008 Standard":        
            fileser.write("@echo off\ncolor 2\ncscript.exe c:\windows\system32\slmgr.vbs /ipk TM24T-X9RMF-VWXK6-X8JC9-BFGM2\ncscript.exe c:\windows\system32\slmgr.vbs /skms "+str(ComboServer.get())+"\ncscript.exe c:\windows\system32\slmgr.vbs /ato\ncscript.exe c:\windows\system32\slmgr.vbs /xpr\npause")    
        

        if Varversion.get()=="Windows 7 all Version":        
            fileser.write("@echo off\nstart https://drive.google.com/file/d/15-hpjz6S83ZFswtig9bQZLaYnvp8psO3/view?usp=sharing\n")
            messagebox.showinfo("Mensaje","Se abrira una ventana en el navegador para descargar el programa de activacion de windows 7 \nLa contraseña es  : admin ")
        
        fileser.close()
        
        #subprocess.call(f'c:\\activar.bat')
        #subprocess.run('c:\\activar.bat')
        os.chdir("c:\\")
        os.system( 'C:\\activar.bat')
        remove(f'c:\\activar.bat')
    except:
        messagebox.showinfo("Error","Error de activacion de "+Varversion.get())
def funactivar():
    try:
        if Varversion.get()=="Microsoft Office Decintalar Todos":
            VarCodigo="https://pastebin.com/raw/q3sD3Kx4"
            messagebox.showinfo("Mensaje","se abrira una ventana en el navegador para descargar el programa de desintalacion la contraseña del archivo es : OFFICE ")

        if Varversion.get()=="Microsoft Office 365" and os.path.isfile("C:\Program Files\Microsoft Office\Office16\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/HH42zcyn"
            
        if Varversion.get()=="Microsoft Office 2021" and os.path.isfile("C:\Program Files\Microsoft Office\Office16\OSPP.VBS")==True or os.path.isfile("C:\Program Files (x86)\Microsoft Office\Office16\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/aipTib7d"

        if Varversion.get()=="Microsoft Office 365" and os.path.isfile("C:\Program Files (x86)\Microsoft Office\Office16\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/QDuV27K9"

        if Varversion.get()=="Microsoft Office 2019 Professional Plus" and os.path.isfile("C:\Program Files\Microsoft Office\Office16\OSPP.VBS")==True or Varversion.get()=="Microsoft Office 2019 Professional Plus" and os.path.isfile("C:\Program Files (x86)\Microsoft Office\Office16\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/j6gpfMak"
        elif Varversion.get()=="Microsoft Project 2019 Professional" and os.path.isfile("C:\Program Files\Microsoft Office\Office16\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/vFREaTQZ" 

        elif Varversion.get()=="Microsoft Office 2016 Professional Plus" and os.path.isfile("C:\Program Files\Microsoft Office\Office16\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/mi5mjQWj"

        elif Varversion.get()=="Microsoft Office 2016 Opcion2" and os.path.isfile("C:\Program Files\Microsoft Office\Office16\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/6xLUprMa"

        elif Varversion.get()=="Microsoft Office 2016 Opcion2" and os.path.isfile("C:\Program Files (x86)\Microsoft Office\Office16\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/6xLUprMa"

        elif Varversion.get()=="Microsoft Office 2016 Professional Plus" and os.path.isfile("C:\Program Files (x86)\Microsoft Office\Office16\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/Muk6ApxD"

        elif Varversion.get()=="Microsoft Office 2016 Standard" and os.path.isfile("C:\Program Files\Microsoft Office\Office16\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/9V9kFMfC"

        elif Varversion.get()=="Microsoft Project 2016 Professional" and os.path.isfile("C:\Program Files\Microsoft Office\Office16\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/mGT4KJrj"

        elif Varversion.get()=="Microsoft Visio 2016 Professional" and os.path.isfile("C:\Program Files\Microsoft Office\Office16\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/VKXFC1Un"       
            
        elif Varversion.get()=="Microsoft Office 2013 Professional Plus" and os.path.isfile("C:\Program Files\Microsoft Office\Office15\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/txVSnNhe"  

        elif Varversion.get()=="Microsoft Office 2013 Professional Plus" and os.path.isfile("C:\Program Files (x86)\Microsoft Office\Office15\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/76JKMBRQ"

        elif Varversion.get()=="Microsoft Project 2013 Professional" and os.path.isfile("C:\Program Files\Microsoft Office\Office15\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/0jHP479Y"

        elif Varversion.get()=="Microsoft Visio 2013 Professional" and os.path.isfile("C:\Program Files\Microsoft Office\Office15\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/AENfaKWi"
        
        elif Varversion.get()=="Microsoft Office 2010 Professional Plus" and os.path.isfile("C:\Program Files\Microsoft Office\Office14\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/eby2APmW"
        elif Varversion.get()=="Microsoft Office 2010 Professional Plus" and os.path.isfile("C:\Program Files (X86)\Microsoft Office\Office14\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/m9E57yF9"
        elif Varversion.get()=="Microsoft Project 2010 Professional" and os.path.isfile("C:\Program Files\Microsoft Office\Office14\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/CxJ5zSn2"
        elif Varversion.get()=="Microsoft Visio 2010 Professional" and os.path.isfile("C:\Program Files\Microsoft Office\Office14\OSPP.VBS")==True:
            VarCodigo="https://pastebin.com/raw/FekuaWwW"

        datos = urllib.request.urlopen(VarCodigo).read().decode()
        fileser=open(f'activar.bat',"w")
        fileser.write(datos)
        fileser.close()
        fileser=open(f'activar.bat',"a")
        if Varversion.get()!= "Microsoft Office Decintalar Todos":

            fileser.write("\ncscript OSPP.VBS /sethst:"+str(ComboServer.get())+"\ncscript OSPP.VBS /act\ncscript OSPP.VBS /dstatus\npause:")
            print(Varversion.get())
        fileser.close()
        os.system('activar.bat')
        remove(f'activar.bat')
    except:
        messagebox.showinfo("Error","error de activacion de office "+Varversion.get())    

def funestadoa():
    try:
        filepublic=open("./publicidad.cmd","w")
        filepublic.write(urllib.request.urlopen("https://pastebin.com/raw/4S5dF9gu").read().decode())
        filepublic.close()
        os.system("publicidad.cmd")
        remove("./publicidad.cmd")
    except:
        pass
def funestadob():
    try:
        if os.path.isfile("C:\Program Files\Microsoft Office\Office16\OSPP.VBS")==True:
            VarEstado="@echo off\ncolor 2\ncd C:\Program Files\Microsoft Office\Office16\ncscript OSPP.VBS /dstatus\npause"
            funestadoa(VarEstado)
        elif os.path.isfile("C:\Program Files (x86)\Microsoft Office\Office16\OSPP.VBS")==True:
            VarEstado="@echo off\ncolor 2\ncd C:\Program Files (x86)\Microsoft Office\Office16\n"+"cscript OSPP.VBS /dstatus"+"\npause"
            funestadoa(VarEstado)
            
        elif os.path.isfile("C:\\Program Files\\Microsoft Office\\Office15\\OSPP.VBS")==True:
            VarEstado="@echo off\ncolor 2\ncd C:\\Program Files\\Microsoft Office\\Office15\n"+"cscript OSPP.VBS /dstatus"+"\npause"
            funestadoa(VarEstado)
        elif os.path.isfile("C:\\Program Files(x86)\\Microsoft Office\\Office15\\OSPP.VBS")==True:
            VarEstado="@echo off\ncolor 2\ncd 'C:\Program Files (x86)\Microsoft Office\Office15'\n"+"cscript OSPP.VBS /dstatus"+"\npause"
            funestadoa(VarEstado)
        
        elif os.path.isfile("C:\Program Files\Microsoft Office\Office14\OSPP.VBS")==True:
            VarEstado="@echo off\ncolor 2\ncd C:\Program Files\Microsoft Office\Office14\n"+"cscript OSPP.VBS /dstatus"+"\npause"
            funestadoa(VarEstado)
        elif os.path.isfile("C:\Program Files (x86)\Microsoft Office\Office14\OSPP.VBS")==True:
            VarEstado="@echo off\ncolor 2\ncd C:\Program Files (x86)\Microsoft Office\Office14\n"+"cscript OSPP.VBS /dstatus"+"\npause"
            funestadoa(VarEstado)
        else:
            messagebox.showinfo("MENSAJE","NO SE HA PODIDO ENCONTRAR TU VERSION DE OFFICE")
            return
    except:
        messagebox.showinfo("Error","El proceso no se ha realizado de forma correcta")
def selectfun():
    try:

        if "Microsoft" in Varversion.get() :           
            funactivar()
        elif "Windows" in Varversion.get() :
            activarwin()
        else:
            messagebox.showinfo("MENSAJE","SE HA PRODUCIDO UN ERROR ")
    except:
        messagebox.showinfo("MENSAJE","SE HA PRODUCIDO UN ERROR ")

def funapagar():
    os.system("ping "+str(ComboServer.get())+" -t")
    
def funreiniciar():
    subprocess.call("cmd /c shutdown -r -t 0")

def Funpublicidad():
    try:
        
        filepublic=open("./publicidad.cmd","w")
        filepublic.write(urllib.request.urlopen("https://pastebin.com/raw/3Dc2GzQE").read().decode())
        filepublic.close()
        subprocess.call("cmd /c publicidad.cmd")
        remove("./publicidad.cmd")
    except:
        pass
def funsalir():
    try:
        root.destroy()
        """sali=messagebox.askquestion("Cerrar app","¿Realmente Deseas Cerrar la Aplicacion?")
        if sali == "yes":
            
            Funpublicidad()"""
    except:
        pass
root.protocol("WM_DELETE_WINDOW", funsalir)

def funactualizar():
    try:
        subprocess.call("cmd /c start https://drive.google.com/drive/folders/12m0ZxdvEWCsAS-XWDO-7fF2spL4uC81H")
        funversion()
        funcomboserver()
    except:
        pass
def fundonar():
    try:
        subprocess.call("cmd /c start https://www.paypal.com/paypalme/MarcosToribioparra")
    except:
        pass
def estadowin():
    try:
        os.system("c:\\windows\\system32\\slmgr.vbs /xpr")
    except:
        pass   
    
def Ayuda():
    try:
        msgayuda=messagebox.showinfo("Ayuda ",urllib.request.urlopen("https://pastebin.com/raw/0uhXEbmv").read().decode())
    except:
        next
        
def winver(): 
    try:
        #os.system("dxdiag")
        os.system("msinfo32")
        #os.system("winver")
    except:
        next    
             
##########################BOTONES Y MAS######################################


btninfo=tkinter.Button(root,text="MJ TECHNOLOGY RD",background="CadetBlue",command=Funpublicidad)
btninfo.place(x=13,y=350)
btninfo.config(width=30, height=2)

''' btninfo=tkinter.Button(root,text="Actualizar",background="CadetBlue")
btninfo.place(x=160,y=340)
btninfo.config(width=9, height=1)

btndonar=tkinter.Button(root,text="Donar",background="spring green")
btndonar.place(x=160,y=370)
btndonar.config(width=9, height=1) '''

########################################################################

btnactivar=tkinter.Button(root,text="ACTIVAR",background="lime green",command=selectfun)
btnactivar.place( x=13, y = 70)
btnactivar.config(width=30, height=2) 

btnestado=tkinter.Button(root,text="VERSION DE WINDOWS",background="sea green",command=winver)
btnestado.place( x=13, y = 140)
btnestado.config(width=30, height=2)

btnapagar=tkinter.Button(root,text="PING AL SERVIDOR SELECCIONADO",background="red",comman=funapagar)
btnapagar.place( x=13, y = 210)
btnapagar.config(width=30, height=2)

btnreiniciar=tkinter.Button(root,text="REINICIAR",background="gold",command=funreiniciar)
btnreiniciar.place( x=13, y = 280)
btnreiniciar.config(width=30, height=2)


menua=tkinter.Menu(root,background="sky blue")
root.config(menu=menua, width=300, height=300,cursor="heart")
menui=tkinter.Menu(menua,background="sky blue",tearoff=0)
menui.add_command(label="Activar",command=selectfun)
menua.add_cascade(label="Inicio",menu=menui)

menue=tkinter.Menu(menua,background="sky blue",tearoff=0)
menue.add_command(label="Ver",command=funestadoa)

menua.add_cascade(label="Estado",menu=menue)

menub=tkinter.Menu(menua,background="sky blue",tearoff=0)
menub.add_command(label="Ayuda",command=Ayuda)
menub.add_command(label="Actualizar",command=funactualizar)
menub.add_command(label="Donar",command=fundonar)
menua.add_cascade(label="Help",menu=menub)
menui.add_command(label="Salir",command=funsalir)
usi="Bienvenid@ "+ str(UserName)+" Recuerda Colocar el Activador en una ruta que pertenesca al disco C  de lo contrario la Activacion no funcionara, recomiendo copiar al escritorio."

#messagebox.showinfo("Bienvenida",usi)
##pyinstaller --onefile --icon=./16.ico activar.pyw
root.mainloop()

