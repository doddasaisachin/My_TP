from PIL import Image,ImageOps
from pytesseract import pytesseract

img = Image.open("C:\\Users\\dodda\\.jupyter\\med_exp.jpeg")
img.show()

path_to_tesseract=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.tesseract_cmd=path_to_tesseract
text = pytesseract.image_to_string(img)
print(text)

for i in text:
    abc=text.replace('/'," ")

def PrintMFD():
    print("MFG : ",end="")
    for key,value in enumerate(abc):
        if (key>=0) and (key<(len(abc)/2)):
            print(value,end="")

def PrintEXD():
    print("EXP : ",end="")
    for key,value in enumerate(abc):
        if (key>=(len(text)/2)) and (key<len(text)):
            print(value,end="")

PrintMFD()
PrintEXD()

def EXP_YEAR():
    i=int(abc[13])
    for i in range(0,1+1):
        exp_year=(2000+(10+int(abc[14])))
        return exp_year
Exp_Year=EXP_YEAR()

def EXP_MONTH():
    exp_month=0
    i=int(abc[10])
    if i:
        for i in range(0,1+1):
            exp_month+=(10+int(abc[11]))
            return exp_month
    if i==0:
        exp_month =(exp_month+abc[12])
        return exp_month
Exp_Month=EXP_MONTH()

def EXP_DATE():
    exp_date=0
    i=int(abc[8])
    if i:
        for i in range(0,1+1):
            exp_date+=(int(abc[8]))
            return exp_date
    if i==0:
        exp_date =(exp_date+abc[8])
        return exp_date
Exp_Date=EXP_DATE()

from datetime import date
today = date.today()
Today=today.day
Year=today.year
Month=today.month

if (Exp_Year >= Year):
    print("Food is Edible")
elif  (Exp_Year==Year and Exp_Month >= Month):
    print("Food is Edible")
elif (Exp_Year==Year and Exp_Month == Month and Exp_Date>Today):
    print("Food is Edible")
else:
    print("Food is Expired!.")
    