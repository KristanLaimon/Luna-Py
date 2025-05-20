import  flet as ft

def main(page: ft.Page):
  page.title = "Ejemplo flet"
  text = ft.Text(value="Hola, Mundo!", size=32, color="blue")
  page.add(text)
  page.update()

ft.app(main)