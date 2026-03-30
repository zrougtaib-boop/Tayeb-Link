[app]
# (str) Title of your application
title = Tayeb Link

# (str) Package name
package.name = tayeblink

# (str) Package domain (needed for android packaging)
package.domain = org.tayeb

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# راني زدتلك pillow باش اللوغو يخدم بلا مشاكل
requirements = python3,flet,uvloop,certifi,pillow

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Icon of the application
# هادي هي اللي تجيب اللوغو الهكر اللي درناه
icon.filename = icon.png

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android build-tools version
android.build_tools_version = 34.0.0

# (bool) Accept SDK license
# هادي أهم وحدة باش ما يخرجلكش اللون الأحمر
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)

warn_on_root = 1
