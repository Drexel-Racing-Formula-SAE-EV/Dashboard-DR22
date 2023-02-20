import tkinter as tk
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

#GUI Setup
root = tk.Tk() #Capitalized methods are constructors
#root.geometry("540x270")
root.attributes('-fullscreen', True)

frame = tk.Frame(root, bg = "#000000")

#to close the window

pressed_f4 = False

def do_exit():
    global pressed_f4
    if pressed_f4:  # Deny if Alt-F4 is pressed
        pressed_f4 = False  # Reset variable
    else:
        close()     # Exit application

def alt_f4(event):  # Alt-F4 is pressed
    global pressed_f4
    pressed_f4 = True

def close(*event):  # Exit application
    root.destroy()

root.bind('<Alt-F4>', alt_f4)
root.bind('<Escape>', close)
root.protocol("WM_DELETE_WINDOW",do_exit)

#READY TO DRIVE
labRTD = tk.Label(frame, text = "READY TO DRIVE:", font = ('calibri', 25, 'bold'), fg = "#FFFFFF", bg = "#000000")
labTractionSys = tk.Label(frame, text = "Traction", font = ('calibri', 25), fg = "#FFFFFF",)
labBreakPedal = tk.Label(frame, text = "Break Pedal", font = ('calibri', 25), fg = "#FFFFFF",)
labAction = tk.Label(frame, text = "Action", font = ('calibri', 25), fg = "#FFFFFF",)

#Labels
labTemp = tk.Label(frame, text = "Temperature:", font = ('calibri', 37), bg = "#000000", fg = "#FFFFFF",)
labVoltage = tk.Label(frame, text = "Voltage:", font = ('calibri', 37), bg = "#000000", fg = "#FFFFFF",)
labSpeed = tk.Label(frame, text = "Speed:", font = ('calibri', 37), bg = "#000000", fg = "#FFFFFF",)

#CAN data
labTemperatureData = tk.Label(frame, font = ('calibri', 55, 'bold'), bg = "#000000", fg = "#FFFFFF",)
labVoltageData = tk.Label(frame, font = ('calibri', 55, 'bold'), bg = "#000000", fg = "#FFFFFF",)
labSpeedData = tk.Label(frame, font = ('calibri', 55, 'bold'), bg = "#000000", fg = "#FFFFFF",)

#Units of Measure
labTempUnit = tk.Label(frame, text = " C ", font = ('calibri', 30), bg = "#000000", fg = "#FFFFFF")
labVoltUnit = tk.Label(frame, text = " V ", font = ('calibri', 30), bg = "#000000", fg = "#FFFFFF")
labSpeedUnit = tk.Label(frame, text = " mph ", font = ('calibri', 30), bg = "#000000", fg = "#FFFFFF")

#placeholder
labPlaceholder1 = tk.Label(frame, font = ('calibri', 20, 'bold'), bg = "#000000", fg = "#000000")
labPlaceholder2 = tk.Label(frame, font = ('calibri', 12, 'bold'), bg = "#000000", fg = "#000000")
labPlaceholder3 = tk.Label(frame, font = ('calibri', 12, 'bold'), bg = "#000000", fg = "#000000")
labPlaceholder4 = tk.Label(frame, font = ('calibri', 20, 'bold'), bg = "#000000", fg = "#000000")

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
    speed = '50'
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
labTemp.grid(row = 3, column = 0, stick = "NESW")
labVoltage.grid(row = 5, column = 0)
labSpeed.grid(row = 7, column = 0)

labRTD.grid(row = 0, column = 1)
labTractionSys.grid(row = 1, column = 0)
labBreakPedal.grid(row = 1, column = 1)
labAction.grid(row = 1, column = 2)

labTemperatureData.grid(row = 3, column = 1)
labVoltageData.grid(row = 5, column = 1)
labSpeedData.grid(row = 7, column = 1)

labTempUnit.grid(row = 3, column = 2)
labVoltUnit.grid(row = 5, column = 2)
labSpeedUnit.grid(row = 7, column = 2)

#Placeholder
labPlaceholder1.grid(row = 2, column = 0, columnspan = 3)
labPlaceholder2.grid(row = 4, column = 0)
labPlaceholder3.grid(row = 6, column = 0)
labPlaceholder4.grid(row = 8, column = 0)

fetch()

frame.pack()

root.mainloop()
