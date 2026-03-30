import flet as ft
import os
import subprocess

# --- الجزء 1: الدوال اللي كتبتها أنت (المخ) ---
def decompile_apk(apk_path):
    return f"جاري تفكيك: {apk_path}"

def link_sniper(url):
    return f"جاري فحص الرابط: {url}"

# --- الجزء 2: الواجهة (الأزرار والربط) ---
def main(page: ft.Page):
    page.title = "TAYEB-LINK V2.1"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # صندوق النصوص (اللي تظهر فيه النتائج)
    log_text = ft.Text("أنا جاهز للتطوير يا شريكي.. هاني واش تحب تدير؟", color="green", text_align="center")

    # واش يصرى كي تضغط على الأزرار
    def on_sniper_click(e):
        log_text.value = link_sniper("الرابط المكتشف") # هنا نعيطو للدالة تاعك
        page.update()

    def on_decompile_click(e):
        log_text.value = decompile_apk("file.apk") # هنا نعيطو للدالة تاعك
        page.update()

    # تصميم الأزرار كيما الفوطو تاعك
    btn_security = ft.ElevatedButton("فحص الأمان", bgcolor="green", color="black", width=160)
    btn_decompile = ft.ElevatedButton("تفكيك APK", bgcolor="green", color="black", width=160, on_click=on_decompile_click)
    btn_sniper = ft.ElevatedButton("🎯 قناص الروابط (Link Sniper)", bgcolor="red", color="white", width=330, on_click=on_sniper_click)

    # إضافة العناصر للصفحة
    page.add(
        ft.Image(src="https://raw.githubusercontent.com/zrougtaib-boop/Tayeb-Link/main/logo.png", width=100), # إذا عندك لوقو
        ft.Text("TAYEB-LINK V2.1", size=25, color="green", weight="bold"),
        ft.Text("وضع القناص مفعل", size=12, color="grey"),
        ft.Row([btn_security, btn_decompile], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([btn_sniper], alignment=ft.MainAxisAlignment.CENTER),
        ft.Container(
            content=log_text,
            padding=20,
            border=ft.border.all(1, "green"),
            border_radius=10,
            width=350,
            margin=ft.margin.only(top=20)
        )
    )

ft.app(tar
       get=main)
