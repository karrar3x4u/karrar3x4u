
[app]
# اسم التطبيق الظاهر للمستخدم
title = Sam3x

# اسم الحزمة (يجب أن يكون فريدًا)
package.name = sam3x

# نطاق الحزمة (عادةً ما يكون معكوسًا من اسم النطاق أو اسم المستخدم)
package.domain = com.karrar3x4u

# مجلد المصدر (عادةً ما يكون المجلد الحالي)
source.dir = .

# رقم الإصدار
version = 0.1

# المتطلبات اللازمة لتشغيل التطبيق
requirements = python3,kivy

# الحد الأدنى لإصدار أندرويد المدعوم
android.minapi = 21

# (اختياري) تحديد أيقونة التطبيق
# icon.filename = %(source.dir)s/icon.png


# المجال العكسي (يفضل أن يكون خاصًا بك، مثلاً نطاقك أو حسابك على GitHub)
package.domain = https://github.com/karrar3x4u

# مسار المجلد الذي يحتوي على main.py (هنا هو نفس المجلد)
source.dir = https://github.com/karrar3x4u/karrar3x4u .

# اسم الملف الرئيسي
source.main = main.py

# رقم الإصدار
version = 1.0

# المتطلبات الأساسية
requirements = python3, flask

# إذن استخدام الإنترنت وقراءة ملفات الجهاز
android.permissions = INTERNET,READ_EXTERNAL_STORAGE

# اتجاه الشاشة
orientation = portrait

# وضع التشغيل
fullscreen = 0
