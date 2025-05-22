import flet as ft
import threading
import serial,time
def func_hilo(arduino,page,sw):
  while True:
    try:
      dato=int(arduino.readline())
      if dato ==1:sw.value=True
      else:sw.value = False
      page.update()
    except:None
    time.sleep(0.1)
    
def main(page:ft.Page):
  arduino = serial.Serial('COM3', 9600, timeout=0.01)
  sw=ft.Switch(label="Estado", value=False)
  page.add(sw)
  hilo=threading.Thread(target=func_hilo,args=(arduino,page,sw))
  hilo.daemon = True
  hilo.start()

ft.app(target=main) 