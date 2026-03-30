import flet as ft

def main(page: ft.Page):
    page.title = "Tayeb Link App"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("Tayeb Link v2.0 🚀", size=30, weight="bold", color="blue"),
                ft.Text("التطبيق شغال بنجاح!", size=20),
                ft.ElevatedButton("ابدأ الدردشة", on_click=lambda _: print("Started"))
            ], alignment=ft.MainAxisAlignment.CENTER),
            alignment=ft.alignment.center
        )
    )

ft.app(target=main
      )
