'''
Anthony Karnati
akarnat1@binghamton.edu
Lab 12
Chelsea Montgomery
Section A55
4/26/14
'''


#imports

from tkinter import *


from queryWorldDBOO import *

#set up class
class WorldDBGUI:
      def __init__(self):
            #make window
            self.__win=Tk()
            #set up frames
            self.__top=Frame(self.__win)
            self.__mid=Frame(self.__win)
            self.__bottom=Frame(self.__win)
            #access queryWorldDBOO file
            self.__worldDB=QueryWorldDB('worldDB')
            #makes program description Label
            self.__descriptionLabel=Label(self.__top,text="Enter City to Find Population")
            #packs the label
            self.__descriptionLabel.pack(side='left')
            #puts content in middle section
            self.__promptLabel=Label(self.__mid, text="City") 
            self.__myEntry=Entry(self.__mid, width=14)
            self.__myEntry.bind('<Return>',self.set)
            #packs middle section
            self.__myEntry.pack(side='left')
            self.__promptLabel.pack(side='left')
            #creates bottom section
            self.__populationLabel=Label(self.__bottom, text='Population')
            #iVal accesses the population number
            self.__iVal=IntVar()
            #creates dynamic label
            self.__value=Label(self.__bottom,textvariable=self.__iVal)
            #packs content in bottom frame
            self.__populationLabel.pack(side='left')
            self.__value.pack(side='left')
            #packs all the frames
            self.__top.pack()
            self.__mid.pack()
            self.__bottom.pack()

            
            
            #listener
            mainloop()
      #creates event handler
      def set(self,event):
            print('Make sure to add an underscore(_) between cities with two names e.g. New_York')
            city=self.__myEntry.get()
            self.__worldDB.setCity(city.strip())
            self.__worldDB.popQuery()
            self.__worldDB.setAnswer()
            self.__iVal.set(self.__worldDB)
            
      
#calls and runs the class
WorldDBGUI()

      
            
      
      
