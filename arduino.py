import flet as ft
import serial

def main(page:ft.Page):
  arduino = serial.Serial('COM3', 9600)
  
  def prender_clicked(e):
    arduino.write(str(1).encode())
    
  def apagar_clicked(e):
    arduino.write(str(0).encode())
    
  btnPrender = ft.ElevatedButton("Prender", on_click=prender_clicked)
  btnApagar = ft.ElevatedButton("Apagar", on_click=apagar_clicked)
  page.add(btnPrender,btnApagar)
  page.update()

ft.app(main)
