
[app]
title = Sam3X
package.name = sam3x
package.domain = org.karrar.sam
source.dir = .
source.include_exts = py,yaml
version = 0.1
entrypoint = main.py
requirements = python3,kivy,pyyaml

orientation = portrait
fullscreen = 0

android.java_src = 
android.api = 33
android.minapi = 21
android.ndk = 25.1.8937393
android.build_tools = 34.0.0
android.allow_backup = 1
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
android.sdk_path = $HOME/android-sdk
android.accept_sdk_license = true
