import flet as ft

def main(page: ft.Page):
    page.title = "Tayeb-Link"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "auto"

    # دالة اختيار الصور
    def on_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            for f in e.files:
                chat_list.controls.append(ft.Text(f"تم اختيار صورة: {f.name}", color="green"))
            page.update()

    file_picker = ft.FilePicker(on_result=on_file_result)
    page.overlay.append(file_picker)

    chat_list = ft.ListView(expand=True, spacing=10)
    
    # خانة الرسائل مع زر (+)
    message_input = ft.TextField(hint_text="اكتب رسالتك هنا...", expand=True)
    
    def send_click(e):
        if message_input.value:
            chat_list.controls.append(ft.Text(f"أنا: {message_input.value}"))
            message_input.value = ""
            page.update()

    page.add(
        ft.Text("Tayeb-Link Messenger", size=30, weight="bold", color="blue"),
        chat_list,
        ft.Row([
            ft.IconButton(icon=ft.icons.ADD_A_PHOTO, on_click=lambda _: file_picker.pick_files()),
            message_input,
            ft.IconButton(icon=ft.icons.SEND, on_click=send_click)
        ])
    )

ft.app(target=main)
