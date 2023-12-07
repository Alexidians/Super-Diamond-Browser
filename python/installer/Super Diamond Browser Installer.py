print("loading...")
import requests
import zipfile
import shutil
import os
import io
print("started up")

def install():
  print("starting instalation.")

  print("getting newest version")
  newVerRequest = requests.get("https://alexidians.github.io/Super-Diamond-Browser/python/installer/Super-Diamond-Browser-Python.zip", stream=True)
  if(newVerRequest.status_code == 200):
    print("Installing Super Diamond Browser...")
    z = zipfile.ZipFile(io.BytesIO(newVerRequest.content))
    z.extractall(path)
    os.mkdir(path + "/files/data")
    datarequest = requests.get("https://alexidians.github.io/Super-Diamond-Browser/python/installer/data.zip", stream=True)
    z = zipfile.ZipFile(io.BytesIO(datarequest.content))
    z.extractall(path + "/files/data")
    browserShortcutFile = open(shortcutPath + "/Super Diamond Browser/Open.py", 'w')
    browserShortcutFile.write("import os\nos.startfile('" + path + "/Super Diamond Browser.py')")
    browserShortcutFile.close()
    updateShortcutFile = open(shortcutPath + "/Super Diamond Browser/Update.py", 'w')
    updateShortcutFile.write("import os\nos.startfile('" + path + "/update.py')")
    updateShortcutFile.close()
    updateShortcutFile = open(shortcutPath + "/Super Diamond Browser/requirements.txt", 'w')
    updateShortcutFile.write("Python Packages:\nrequests\nPyQt5\nPyQtWebEngine\nCryptogtraphy")
    updateShortcutFile.close()
    print("Sucess")
    os.startfile(path + "/Super Diamond Browser.py")
  else:
   choice = input("Status code while getting version is not 200 (OK) its ", newVerRequest.status_code, " would you still like to update with the status code or retry? (Y (update with status_code)/N (retry)):")
   if choice == "Y":
    print("Installing Super Diamond Browser...")
    z = zipfile.ZipFile(io.BytesIO(newVerRequest.content))
    z.extractall(path)
    os.mkdir(path + "/files/data")
    datarequest = requests.get("https://alexidians.github.io/Super-Diamond-Browser/python/installer/data.zip", stream=True)
    z = zipfile.ZipFile(io.BytesIO(datarequest.content))
    z.extractall(path + "/files/data")
    browserShortcutFile = open(shortcutPath + "/Super Diamond Browser/Open.py", 'w')
    browserShortcutFile.write(b"import os\nos.startfile('" + path + "/Super Diamond Browser.py')")
    browserShortcutFile.close()
    updateShortcutFile = open(shortcutPath + "/Super Diamond Browser/Update.py", 'w')
    updateShortcutFile.write(b"import os\nos.startfile('" + path + "/update.py')")
    updateShortcutFile.close()
    updateShortcutFile = open(shortcutPath + "/Super Diamond Browser/requirements.txt", 'w')
    updateShortcutFile.write(b"Python Packages:\nrequests\nPyQt5\nPyQtWebEngine\nCryptogtraphy")
    updateShortcutFile.close()
    print("Sucess")
    os.startfile(path + "/Super Diamond Browser.py")
   else:
    install()

path = input("Enter Path Where to install Super Diamond Browser:")
if input("Should a SuperDiamondBrowser folder be created? (Y/N):"):
  os.mkdir(path + "/SuperDiamondBrowser")
  path = path + "/SuperDiamondBrowser"
shortcutPath = input("Enter Path Where to Put Super Diamond Browser Shortcut (Shortcut In Development):")
os.mkdir(shortcutPath + "/Super Diamond Browser")
install()
