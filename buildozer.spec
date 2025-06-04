[app]
title = Sam3X
package.name = sam3x
package.domain = org.karrar.sam
source.dir = .
source.include_exts = py,yaml
version = 0.1
entrypoint = main.py
requirements = python3,kivy,pyyaml,cython==0.29.36,pyjnius
orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 21
android.build_tools = 34.0.0
android.permissions = INTERNET
android.allow_backup =
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b

[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = true
