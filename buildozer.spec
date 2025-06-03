[app]

# معلومات التطبيق
title = StreamSanctum
package.name = streamsanctum
package.domain = org.saden
source.dir = .
source.include_exts = py,html
version = 0.1

# المتطلبات (مكتبات بايثون)
requirements = python3

# إعدادات العرض
orientation = portrait
fullscreen = 0

# صلاحيات أندرويد
android.permissions = INTERNET,READ_EXTERNAL_STORAGE

# إعدادات SDK/NDK
android.api = 33
android.minapi = 21
android.ndk = 25b

# تخزين خاص (اختياري)
android.private_storage = False

# قبول تلقائي للرخص
android.accept_sdk_license = True
android.accept_ndk_license = True

# سجل البناء التفصيلي
log_level = 2
