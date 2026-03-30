import flet as ft

def main(page: ft.Page):
    page.title = "Tayeb-Link"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "auto"

    # رسالة ترحيب زرقاء عند التشغيل
    def show_welcome():
        page.snack_bar = ft.SnackBar(
            content=ft.Text("مرحباً بك في Tayeb-Link! حافظ على هذا الهاتف 🛡️", color="white"),
            bgcolor="blue",
        )
        page.snack_bar.open = True
        page.update()

    chat_list = ft.ListView(expand=True, spacing=10)
    message_input = ft.TextField(hint_text="اكتب رسالتك هنا...", expand=True, border_color="blue")
    
    def send_click(e):
        if message_input.value:
            chat_list.controls.append(
                ft.Container(
                    content=ft.Text(f"أنا: {message_input.value}", color="white"),
                    padding=10, bgcolor="blue", border_radius=10
                )
            )
            message_input.value = ""
            page.update()

    page.add(
        ft.Text("Tayeb-Link Messenger", size=25, weight="bold", color="blue"),
        chat_list,
        ft.Row([
            message_input,
            ft.IconButton(icon=ft.icons.SEND, icon_color="blue", on_click=send_click)
        ])
    )
    show_welcome()

ft.app(target=main)
