from Tkinter import *
import luis, time

def lu(e):
    l = luis.Luis(url='https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/a5d46e19-7631-4f66-85ba-bfdf31aeb163?subscription-key=3966428ee6594e6dbd7fd3240f1f2ff0&verbose=true&timezoneOffset=0&q=')
    ln = len(e)
    r = l.analyze(e)
    if r.best_intent().intent == "Greeting":
      mylist.insert(END,"BOT: Hi! Please Tell Us Your problem")
      txt.delete(0,ln)
    
    
    elif r.best_intent().intent == "Actual problem":
      mylist.insert(END,"BOT: We are Sending Help") 
      txt.delete(0,ln)
      
    
    elif r.best_intent().intent == "Jokes":
       mylist.insert(END,"BOT: We can't help you")
       txt.delete(0,ln)
       
    
    else:
      mylist.insert(END,"My BOT: knowledge is limited")
      txt.delete(0,ln)
      
      

def send():
    e = txt.get()
    mylist.insert(END,"You: "+e)
    mylist.grid(row=4,column=1,rowspan=1,sticky=E+W)
    lu(e)
    



window = Tk()
window.title("Bhim Bot")
l= Label(window,text="typing..")
lbl = Label(window, text="Enter Message")
scrollbar = Scrollbar(window)
scrollbar.grid(row=4,column=2, rowspan=1, sticky=N+S)
mylist=Listbox(window,selectmode = "multiple", height=5, width=40, yscrollcommand=scrollbar.set)
Button(window, text="Send", command=send).grid(column=1, row=6)
scrollbar.config( command = mylist.yview )
lbl.grid(column=0, row=0)
txt = Entry(window,width=50)
txt.grid(column=1, row=0)
window.mainloop()
