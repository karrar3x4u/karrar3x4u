[app]

# العنوان الظاهر للتطبيق
title = StreamScutum

# اسم الحزمة (بدون فراغات أو رموز خاصة)
package.name = streamscutum

# النطاق العكسي الخاص بك (يمكن تعديله لاحقًا)
package.domain = https://github.com/karrar3x4u/karrar3x4u

# إصدار التطبيق
version = 1.0

# الملف الرئيسي
source.main = main.py

# مسار المجلد الذي يحتوي على الكود (هنا نفس مجلد buildozer.spec)
source.dir = .

# مكتبات بايثون المطلوبة
requirements = python3,kivy

# اتجاه الشاشة
orientation = portrait

# إعدادات المنصة
android.api = 33
android.minapi = 21
android.archs = armeabi-v7a

# الصلاحيات المطلوبة (للوصول للإنترنت وتخزين الملفات)
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# خيارات متقدمة
copy_libs = 1
log_level = 2

# حفظ الـ APK في مجلد bin
android.allow_backup = 1

# الأيقونة (اختياري – فعّل عند إضافة ملف)
# icon.filename = icons/streamscutum_icon.png

# اسم مجلد البناء المؤقت
build_dir = .buildozer

# اللغة الافتراضية
android.manifest.placeholders = appName=StreamScutum

# تمكين خيارات متقدمة إذا لزم
# android.ndk = 25b
# android.accept_sdk_license = True

# لإزالة التطبيق السابق من الجهاز تلقائيًا أثناء التجريب
# (إن لم تفعل ذلك، قد تفشل عملية التثبيت)
# android.install_always = True

# دعم تسجيل السجلات أثناء التشغيل
# android.logcat_filters = *:S python:D

# إضافة شاشة بدء (splash) لاحقًا
# presplash.filename = images/splash.png

# إضافة خلفية أثناء التحميل
# android.presplash_color = #000000
