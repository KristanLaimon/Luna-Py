import flet as ft

def main(page:ft.Page):
  page.padding=30
    
  def slider_changed(e):
    mensaje.value = f"Valor del Slider: {slider.value}"
    page.update()
      
  texto = ft.Text("Selecciona un valor", size = 20)
  mensaje = ft.Text(size = 18, color = "blue")
  mensaje = ft.Text(size = 18, color = "blue")
  slider = ft.Slider(min =0, max = 10, divisions = 3, width = 400, label = "(value)", on_change = slider_changed)
  page.add(texto,slider,mensaje)

ft.app(main)
