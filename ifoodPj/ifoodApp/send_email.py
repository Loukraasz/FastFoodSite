import random
import win32com.client as win32
import pythoncom

def createCode():
    cont = 0
    while (cont==0):
        recCode = random.randint(0, 999999)
        recCode = str(recCode)
        if len(recCode) == 6:
            cont+=1
        return recCode
    return None
recCode = createCode()

def send_emails(emailToSend):
    pythoncom.CoInitialize()
    outlook=win32.Dispatch('outlook.application')
    try:
        mail=outlook.CreateItem(0)
        mail.to = emailToSend 
        mail.subject ="Recuperacao de Senha"
        mail.body = f"Seu codigo de verificacao: {recCode}"
        mail.Send()
    except Exception as e:
        print(f"An error occurred: {e}")
    print(recCode)

final = recCode
