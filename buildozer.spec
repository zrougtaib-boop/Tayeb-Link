[app]
title = Tayeb Link
package.name = tayeblink
package.domain = org.tayeb
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# نقصنا المكتبات الزايدة باش يمر البناء بسلام
requirements = python3,flet,pillow

orientation = portrait
fullscreen = 0

# اسم ملف اللوغو اللي عندك في المستودع
icon.filename = icon.png

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.0
android.accept_sdk_license = True
android.archs = arm64-v8a

# هادي تضمن توافق المكتبات مع أندرويد
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
