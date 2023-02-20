import tkinter as tk
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
#Data 

#Functions

def do_exit():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

#GUI Setup
root = tk.Tk() #Capitalized methods are constructors

root.protocol("WM_DELETE_WINDOW", do_exit)

frame = tk.Frame(root, padx = 20, pady = 20, bg = "#000000")

#Labels
labTemp = tk.Label(frame, text = "Battery Temperature:",bg = "#000000")
labVoltage = tk.Label(frame, text = "Battery Voltage:",bg = "#000000")
labSpeed = tk.Label(frame, text = "Car Speed:",bg = "#000000")

#Units of Measure
labTempUnit = tk.Label(frame, text = "C",bg = "#000000",)
labVoltUnit = tk.Label(frame, text = "V:",bg = "#000000")
labSpeedUnit = tk.Label(frame, text = "mph",bg = "#000000")

#READY TO DRIVE
labRTD = tk.Label(frame, text = "READY TO DRIVE:", font = ('calibri', 15, 'bold'), bg = "#000000")
labTractionSys = tk.Label(frame, text = "Traction")
labBreakPedal = tk.Label(frame, text = "Break Pedal")
labAction = tk.Label(frame, text = "Action")

#CAN data
labTemperatureData = tk.Label(frame, font = ('calibri', 25, 'bold'), bg = "#000000")
labVoltageData = tk.Label(frame, font = ('calibri', 25, 'bold'), bg = "#000000")
labSpeedData = tk.Label(frame, font = ('calibri', 25, 'bold'), bg = "#000000")

def fetch():
    fetchTemp()
    fetchVoltage()
    fetchSpeed()

    fetchTraction()
    fetchBreakPedal()
    fetchAction()

#fetch data
def fetchTemp():
    temp = '34'
    labTemperatureData.config(text = temp)
    labTemperatureData.after(1000, fetchTemp)

def fetchVoltage():
    voltage = '1.2'
    labVoltageData.config(text = voltage)
    labVoltageData.after(1000, fetchVoltage)

def fetchSpeed():
    speed = '50 mph'
    labSpeedData.config(text = speed)
    labSpeedData.after(1000, fetchSpeed)

#fetch ready to drive
def fetchTraction():
    bg = "#FF0000"
    labTractionSys.config(bg = bg)
    labTractionSys.after(1000, fetchTraction)

def fetchBreakPedal():
    bg = "#FF0000"
    labBreakPedal.config(bg = bg)
    labBreakPedal.after(1000, fetchBreakPedal)

def fetchAction():
    bg = "#FF0000"
    labAction.config(bg = bg)
    labAction.after(1000, fetchAction)

#Adding everything to the window
labTemp.grid(row = 1, column = 0, stick = "NESW")
labVoltage.grid(row = 2, column = 0)
labSpeed.grid(row = 3, column = 0)
labRTD.grid(row = 0, column = 0)
labTractionSys.grid(row = 0, column = 1)
labBreakPedal.grid(row = 0, column = 2)
labAction.grid(row = 0, column = 3)

labTemperatureData.grid(row = 1, column = 1, columnspan = 3)
labVoltageData.grid(row = 2, column = 1, columnspan = 3)
labSpeedData.grid(row = 3, column = 1, columnspan = 3)

labTempUnit.grid(row = 1, column = 4)
labVoltUnit.grid(row = 2, column = 4)
labSpeedUnit.grid(row = 3, column = 4)

fetch()

frame.pack()

root.mainloop()
