[app]

# معلومات التطبيق
title = StreamSanctum
package.name = streamsanctum
package.domain = org.saden
source.dir = .
source.include_exts = py,html
version = 0.1

# المتطلبات (مكتبات بايثون)
requirements = python3,

# إعدادات العرض
orientation = portrait
fullscreen = 0

# صلاحيات أندرويد
android.permissions = INTERNET, READ_EXTERNAL_STORAGE

# إصدارات SDK/NDK
android.api = 33
android.minapi = 21
android.ndk = 25b

# استخدام تخزين خاص (اختياري)
android.private_storage = False

# الموافقة على رخصة SDK تلقائيًا (مهم جدًا لمنع الأخطاء)
android.accept_sdk_license = True

# تجنّب التثبيت التفاعلي في Actions
android.accept_ndk_license = True

# تشغيل سجل البناء التفصيلي (مفيد للتصحيح)
log_level = 2
