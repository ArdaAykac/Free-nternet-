import os
import subprocess
import urllib.request
import zipfile
import shutil
import tkinter as tk
import time
import requests
import keyboard
import psutil
import ctypes

# Git kontrol ve kurulum
def is_git_installed():
    try:
        subprocess.check_output(["git", "--version"])
        return True
    except:
        return False

def download_and_extract_git(destination="git"):
    print("Git bulunamadı. İndiriliyor...")

    url = "https://github.com/git-for-windows/git/releases/download/v2.43.0.windows.1/PortableGit-2.43.0-64-bit.zip"
    zip_path = "git.zip"

    urllib.request.urlretrieve(url, zip_path)
    print("İndirme tamamlandı. Açılıyor...")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(destination)

    os.remove(zip_path)
    print("Git başarıyla indirildi ve çıkarıldı.")
    return os.path.abspath(destination)

def setup_git_environment(git_path):
    git_cmd_path = os.path.join(git_path, "cmd")
    os.environ["PATH"] = git_cmd_path + ";" + os.environ["PATH"]

#path
userprofile_path = os.environ.get('USERPROFILE')
repo_adresse = "https://github.com/cagritaskn/GoodbyeDPI-Turkey.git"
program_files = os.environ.get("APPDATA") 
freeinternet_path = os.path.join(program_files,"Free İnternet")
addictions_path = os.path.join(freeinternet_path,"Addictions")
forterminal_path = os.path.join(freeinternet_path, "Termınal","dist","FR Terminal")
turkey_dnsredir_cmd_path = os.path.join(addictions_path,"turkey_dnsredir.cmd")
service_remove_cmd_path = os.path.join(addictions_path,"service_remove.cmd")
service_install_dnsredir_turkeycmd = os.path.join(addictions_path,"service_install_dnsredir_turkey.cmd")
readme = os.path.join(addictions_path,"README-BENİ OKU.txt")

def function():
    for root, dirs, files in os.walk(forterminal_path):
        if "FR Terminal.exe" in files:
            print("FR Terminal.exe bulundu.")
            if not check_if_running("FR Terminal.exe"):
                print("FR Terminal.exe çalışmıyor. Başlatılıyor...")
                start_program(root)
            else:
                print("FR Terminal.exe zaten çalışıyor.")
            break
    else:
        print("FR Terminal.exe bulunamadı.")

def check_if_running(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            return True
    return False

def start_program(path):
    try:
        program_path = os.path.join(path, "FR Terminal.exe")
        subprocess.Popen(program_path)
        print(f"{program_path} başlatıldı.")
    except Exception as e:
        print(f"Program başlatılırken hata oluştu: {e}")

def starter_void():
    try:
        print(f" Hedef klasör yolu: {freeinternet_path}")
        if not os.path.exists(freeinternet_path):
            os.makedirs(freeinternet_path)
            os.makedirs(addictions_path)
            os.makedirs(forterminal_path)
            print("Klasör oluşturuldu.")
            time.sleep(3)
        else:
            print("Klasör zaten var.")
            time.sleep(2)
        
        # Git kontrolü
        if not is_git_installed():
            git_path = download_and_extract_git()
            setup_git_environment(git_path)
        else:
            print("Git zaten yüklü.")

        main()
    except PermissionError:
        print(" İzin hatası! Yönetici izni yok.")
        time.sleep(3)
    except Exception as e:
        print(f" Beklenmeyen hata oluştu: {e}")
        time.sleep(3)

def main():
    main_win = tk.Tk()
    main_win.title("Free Internet 🌐")
    main_win.geometry("900x200")

    def turkey_dnsredir_cmd():
        ctypes.windll.shell32.ShellExecuteW(
        None, "runas", turkey_dnsredir_cmd_path, None, None, 1
    )
    def service_removes():
        ctypes.windll.shell32.ShellExecuteW(
        None, "runas", service_remove_cmd_path, None, None, 1
    )
    keyboard.add_hotkey('alt+f5+t', function)
    def install_service():
         ctypes.windll.shell32.ShellExecuteW(
        None, "runas", service_install_dnsredir_turkeycmd, None, None, 1
    )
    def get_help():
        if os.path.exists(readme):
            try:
                with open(readme, 'r', encoding='utf-8') as dosya:
                    print(f"Dosya açıldı: {readme}")
            except Exception as e:
                print(f"Dosya açılırken hata oluştu: {e}")
        else:
            print(f"Dosya bulunamadı: {readme}")
    
    # Butonlar
    turkey_dnsredir_cmd_button = tk.Button(main_win,text="turkey_dnsredir_cmd",command=turkey_dnsredir_cmd,background="Green",fg="Blue")
    turkey_dnsredir_cmd_button.pack()
    service_install_dnsredir_turkey_button = tk.Button(main_win,text="service_install_dnsredir_turkey",command=install_service,background="Blue",fg="Green")
    service_install_dnsredir_turkey_button.pack()
    service_remove_cmd_button = tk.Button(main_win,text="service_remove_cmd_path",command=service_removes,background="Red",fg="Black")
    service_remove_cmd_button.pack()
    helps_button =tk.Button(main_win,text="Helps",command=get_help,background="Yellow",fg="Blue")
    helps_button.pack()

    note_label = tk.Label(main_win,text="Lütfen Appdata daki Free İnternet klasörünün içindeki Addictions klasörünün içindeki Readme.txt belgesini okuyun aksi takdirde sorumluluk kabul etmiyoruz",fg="Red")
    note_label.pack(side="left",anchor="s")

    main_win.mainloop()

starter_void()
