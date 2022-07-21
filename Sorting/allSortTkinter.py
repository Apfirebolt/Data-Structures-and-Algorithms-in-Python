import tkinter as tk 
from tkinter import simpledialog
from tkinter.ttk import *
from time import strftime

class ApplicationWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.numbers = []
        self.title('All Sort Program in Tkinter')
        self.geometry('400x400')
        self.addMenu()

    def addMenu(self):
        self.menubar = tk.Menu(self)
        # Adding File Menu and commands
        self.file = tk.Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label ='Menu', menu = self.file)
        self.file.add_command(label ='Bubble Sort', command = self.bubbleSort)
        self.file.add_command(label ='Insertion', command = None)
        self.file.add_command(label ='Quick', command = None)
        self.file.add_command(label ='Merge', command = None)
        self.file.add_command(label ='Heap', command = None)
        self.file.add_command(label ='Selection', command = None)
        self.file.add_separator()
        self.file.add_command(label ='Exit', command = self.destroy)
        self.config(menu = self.menubar)
    

    def getInput(self):
        answer = simpledialog.askstring("Enter Numbers", "Please enter numbers with spaces to sort!",parent=self)
        try:
            self.numbers = [int(x) for x in answer.split(' ')]
        except Exception as err:
            pass

    def bubbleSort(self):
        self.getInput()
        arr = self.numbers
        n = len(self.numbers)
        for i in range(n-1):
            swapped = False
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        self.resultLabel = Label(self, text=' '.join([str(x) for x in self.numbers]), font=("Arial", 25), wraplength = 300).pack(pady=20)
        

    def insertionSort(self):
        pass

    def selectionSort(self):
        pass

    def mergeSort(self):
        pass

    def heapSort(self):
        pass

    def quickSort(self):
        pass



root = ApplicationWindow()
root.mainloop()