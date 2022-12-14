from tkinter import *
from tkinter import messagebox
import random
# class Application(Frame):
#     def __init__(self,master=None):
#         super().__init__(master)    #super代表的是父类的定义，不是父类对象
#         self.createWidget()
#         self.master=master
#         self.pack
#     def createWidget(self):
#         self.btn1=Button(root)
#         self.btn1["text"]="生成随机数"

#         self.btn1.pack()     #调用主界面管理器，将按钮合理放在界面上
#         self.btn1["command"]=
#         def self


root=Tk()
root.title("随机数生成器")
root.geometry("500x300")

btn1=Button(root)
btn1["text"]="生成随机数"

btn1.pack()     #调用主界面管理器，将按钮合理放在界面上

btnQuit=Button(root)
btnQuit["text"]="退出程序"
btnQuit.pack()


def suijichouzuohao(e):      #e是事件对象
    suijichouzuohao_i=random.randint(1,61)
    messagebox.showinfo("随机数生成器","随机数是\n{}".format(suijichouzuohao_i))
btn1.bind("<Button-1>",suijichouzuohao)
btnQuit.bind("<Button-1>",exit)
#app=Application(master=root)


root.mainloop()       #进入事件循环，放在程序末尾