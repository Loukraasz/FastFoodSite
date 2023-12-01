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
    outlook = win32.Dispatch("outlook.application", pythoncom.CoInitialize())
    
    email = outlook.CreateItem(0)
    
    email.To = emailToSend
    email.Subject = "IFood 2 Support"
    email.HTMLBody=f"aqui esta seu codigo para a verificacao de senha {recCode}"
    email.Send()
    print(recCode)

final = recCode
