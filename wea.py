import flet as ft
import threading
import serial, time

def main(page:ft.Page):
  
  def update_slider(e):
    global current_freq
    current_freq = int(slider.value)
    freq_text.value = f"Frecuencia: {current_freq} Hz"
    page.update()

  def toggle_sound(e):
    global send_data
    send_data = switch.value
    arduino.write(str(send_data).encode())
    update_slider(e)  
  
  arduino = serial.Serial("COM3", 9600)
  title = ft.Text("Control de frecuencia de tono", size=22)
  slider = ft.Slider(min=50, max=2000, divisions=100, label="{value}", on_change=update_slider, width=400)
  freq_text = ft.Text("Frecuencia: 440 Hz", size=18, color="blue")
  switch = ft.Switch(label="Activar sonido", value=False, on_change=toggle_sound)

  current_freq = 440  # Set initial frequency

  page.add(title, slider, freq_text, switch)

def func_hilo(arduino, page, sw):
    while True:
        try:
            dato = int(arduino.readline())
            if dato == 1:
                sw.value = True
            else:
                sw.value = False
            page.update()
        except:
            None
        time.sleep(0.1)
    

ft.app(main)