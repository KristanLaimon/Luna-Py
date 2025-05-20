import flet as ft

def Suma(a:int, b:int) -> int:
  return a + b

def main(page: ft.Page):
  page.title = "A simple counter app"
  page.vertical_alignment = ft.MainAxisAlignment.CENTER
  
  txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
  
  def minus_click(e):
    txt_number.value = str(int(txt_number.value) - 1)
    page.update()
    
  def plus_click(e):
    txt_number.value = str(int(txt_number.value) + 1)
    page.update()
    
  page.add(
    ft.Row(
      [
        ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
        txt_number,
        ft.IconButton(ft.Icons.ADD, on_click=plus_click)
      ],
      alignment=ft.MainAxisAlignment.CENTER
    )
  )
  
ft.app(main)
