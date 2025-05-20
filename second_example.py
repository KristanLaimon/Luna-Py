import  flet as ft

def main(page: ft.Page):
  page.title = "Ejemplo flet"
  page.theme_mode = ft.ThemeMode.LIGHT
  page.window.width = 300
  page.window.height = 300
  page.window.center()
  page.padding = 20
  mensaje = ft.Text(value="", size=24)
  nombre = ft.TextField(value="", width=200)
  
  def boton_clicked(e):
    mensaje.value = "Hola " + nombre.value
    page.update()
    
  boton = ft.ElevatedButton("Aceptar", width=100, on_click=boton_clicked)
  columna = ft.Column(
    controls=[nombre,boton,mensaje],
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
  )
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.add(columna)
  page.update()
  
ft.app(main)