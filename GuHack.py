import winreg
import eel
import keyboard
import requests
from bs4 import BeautifulSoup
import multiprocessing as mp
import webview

# Set web files folder
eel.init('data')

@eel.expose 
def setCradential(userID,userPass):
    hkey = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER,"SOFTWARE\\GalgotiasLMSToolkit")
    Envkey = winreg.OpenKey(hkey,"SOFTWARE\\GalgotiasLMSToolkit", 0, winreg.KEY_ALL_ACCESS )
    winreg.SetValueEx(Envkey,"GUHACK_USERID", 0, winreg.REG_SZ,userID)
    winreg.SetValueEx(Envkey,"GUHACK_PASSWORD", 0, winreg.REG_SZ,userPass)
    eel.credSaved()             
                
@eel.expose
def fetchFormSource(pram):
    soup = BeautifulSoup(pram,'html.parser')
    i = 0
    qNo = soup.find_all(class_="qno")
    ques = soup.find_all(class_="qtext")
    anss = soup.find_all(class_="answer")
    while(True):
        try:
            eel.fetchHTML(ques[i].text,anss[i].text,qNo[i].text)
            i=i+1
        except Exception as err:
                return 0

@eel.expose
def fetchFromReq(pram):
    print(pram)
    try:
        Envkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER,"SOFTWARE\\GalgotiasLMSToolkit", 0, winreg.KEY_ALL_ACCESS)
        getUserID = winreg.EnumValue(Envkey, 0)
        getPassword = winreg.EnumValue(Envkey, 1)
    except Exception as err:
        eel.credentialsNotFound(err)
        return 0

    print(getUserID[1])
    print(getPassword[1])
    try:
        req = requests.get(pram)
    except Exception as err:
        eel.connectionNotMade(err)
        return 1
    soap = BeautifulSoup(req.text, 'html.parser')
    token = soap.find('input', {'name': 'logintoken'})['value']

    headers = {
        'cookie': req.history[0].headers['set-cookie'].split(';')[0],
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    payload = {
        'anchor': '',
        'logintoken': token,
        'username': getUserID[1],
        'password': getPassword[1],
    }
    req2 = requests.post("https://lms.galgotiasuniversity.edu.in/login/index.php", data=payload,headers=headers)
    print(req2.text)
    print(req2.url)
    if(req2.url == "https://lms.galgotiasuniversity.edu.in/login/index.php"):
        eel.sessionNotCreated()
        return 1
    soup = BeautifulSoup(req2.text, 'html.parser')
    i = 0
    qNo = soup.find_all(class_="qno")
    ques = soup.find_all(class_="qtext")
    anss = soup.find_all(class_="answer")
    while(True):
        try:
            eel.fetchHTML(ques[i].text,anss[i].text,qNo[i].text)
            i=i+1
        except Exception as err:
            return 0


@eel.expose
def pasteText(objss):
    
    def writeText(objss):
        keyboard.write(objss)
        keyboard.unhook_all()
        eel.resetCopyBtn()
        keyboard.unhook_all_hotkeys()
    keyboard.add_hotkey('ctrl+q',writeText, args=[objss])
@eel.expose
def unhook():
    keyboard.unhook_all()

def display(links):
    print ('Hi !! I am Python',links)
    webview.create_window('Hello world',url=links, html=None, js_api=None, width=800, height=600, x=48, y=None,
                  resizable=True, fullscreen=False, min_size=(200, 100), hidden=False,
                  frameless=False, easy_drag=True,
                  minimized=False, on_top=False, confirm_close=False, background_color='#FFFFFF',
                  transparent=False, text_select=True, localization=None)
    webview.start()

def eelss():
    eel.start('index.htm',mode=None,size=(800, 550))  

if __name__ == '__main__':
    mp.freeze_support()
    mp.set_start_method('spawn')
    p1 = mp.Process(target=eelss)
    p2 = mp.Process(target=display,args=["http://localhost:8000/index.htm"])
    p1.start()
    p2.start()
    p2.join()
    p1.terminate()

    
    
