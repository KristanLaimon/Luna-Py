import flet as ft
import serial
import threading
import time

# Global flag to control the thread
send_data = False
current_freq = 440


def send_loop(arduino):
    global send_data, current_freq
    while True:
        if send_data:
            try:
                arduino.write(str(1).encode())
            except Exception as e:
                print("Error sending in thread:", e)
        else:
            try:
                arduino.write(f"{current_freq}:0\n".encode())
            except:
                pass
        time.sleep(0.05)

def main(page: ft.Page):
    global send_data, current_freq

    page.title = "Arduino Tone Controller"
    page.padding = 20

    # Connect to Arduino (adjust COM port!)
    arduino = serial.Serial("COM3", 9600, timeout=0.1)
    time.sleep(2)

    # Start background thread
    thread = threading.Thread(target=send_loop, args=(arduino))
    thread.daemon = True
    thread.start()

    def update_slider(e):
        global current_freq
        current_freq = int(slider.value)
        freq_text.value = f"Frecuencia: {current_freq} Hz"
        page.update()

    def toggle_sound(e):
        global send_data
        send_data = switch.value
        update_slider(e)  # Ensure frequency label is updated too

    # UI
    title = ft.Text("Control de frecuencia de tono", size=22)
    slider = ft.Slider(min=50, max=2000, divisions=100, label="{value}", on_change=update_slider, width=400)
    freq_text = ft.Text("Frecuencia: 440 Hz", size=18, color="blue")
    switch = ft.Switch(label="Activar sonido", value=False, on_change=toggle_sound)

    current_freq = 440  # Set initial frequency

    page.add(title, slider, freq_text, switch)

ft.app(target=main)
