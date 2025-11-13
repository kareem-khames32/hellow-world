# 🔬 الآلة الحاسبة العلمية الشاملة
# Scientific Calculator - Advanced

آلة حاسبة علمية كبيرة وشاملة مكتوبة بلغة Python تحتوي على جميع الوظائف الرياضية المتقدمة.

## ✨ المميزات

### 1. العمليات الأساسية
- ✅ الجمع والطرح والضرب والقسمة
- ✅ الأس والجذور (التربيعية والنونية)
- ✅ القيمة المطلقة
- ✅ المضروب (Factorial)
- ✅ باقي القسمة (Modulo)

### 2. الدوال المثلثية
- ✅ sin, cos, tan
- ✅ asin, acos, atan (المعكوسات)
- ✅ sinh, cosh, tanh (الزائدية)
- ✅ دعم الراديان والدرجات

### 3. اللوغاريتمات
- ✅ اللوغاريتم الطبيعي (ln)
- ✅ اللوغاريتم العشري (log10)
- ✅ اللوغاريتم الثنائي (log2)
- ✅ اللوغاريتم بأي أساس
- ✅ الدالة الأسية (exp)

### 4. الدوال الإحصائية
- ✅ المتوسط الحسابي (Mean)
- ✅ الوسيط (Median)
- ✅ المنوال (Mode)
- ✅ الانحراف المعياري (Standard Deviation)
- ✅ التباين (Variance)

### 5. دوال رياضية إضافية
- ✅ التقريب (ceil, floor, round)
- ✅ القاسم المشترك الأكبر (GCD)
- ✅ المضاعف المشترك الأصغر (LCM)
- ✅ التباديل والتوافيق (Permutations & Combinations)
- ✅ التحقق من الأعداد الأولية
- ✅ تحويل الزوايا (درجات ↔ راديان)

### 6. الثوابت الرياضية
- π (pi)
- e (عدد أويلر)
- φ (phi) - النسبة الذهبية
- τ (tau) = 2π

### 7. الذاكرة
- 💾 حفظ القيم في الذاكرة (MS)
- 💾 استرجاع من الذاكرة (MR)
- 💾 مسح الذاكرة (MC)
- 💾 إضافة/طرح من الذاكرة (M+/M-)

### 8. السجل
- 📝 حفظ سجل جميع العمليات
- 📝 عرض السجل
- 📝 مسح السجل

### 9. تقييم التعبيرات الرياضية
- يمكنك كتابة تعبيرات رياضية معقدة مباشرة
- مثال: `2 + 3 * sin(pi/2) + sqrt(16)`

## 🚀 طريقة الاستخدام

### 1. الوضع التفاعلي
```bash
python3 scientific_calculator.py
```

ثم يمكنك إدخال العمليات الحسابية مباشرة:
```
➤ أدخل العملية: 2 + 3 * 4
✅ النتيجة: 14

➤ أدخل العملية: sin(pi/2)
✅ النتيجة: 1.0

➤ أدخل العملية: sqrt(16) + log10(100)
✅ النتيجة: 6.0

➤ أدخل العملية: factorial(5)
✅ النتيجة: 120
```

### 2. الأمثلة التوضيحية
```bash
python3 scientific_calculator.py --examples
```

### 3. تقييم تعبير من سطر الأوامر
```bash
python3 scientific_calculator.py "2 + 3 * 4"
python3 scientific_calculator.py "sin(pi/4) * sqrt(2)"
```

### 4. عرض المساعدة
```bash
python3 scientific_calculator.py --help
```

## 📖 أمثلة متقدمة

### العمليات الأساسية
```python
from scientific_calculator import ScientificCalculator

calc = ScientificCalculator()

# الجمع والضرب
result = calc.add(5, 3)  # 8
result = calc.multiply(4, 7)  # 28

# الأس والجذور
result = calc.power(2, 10)  # 1024
result = calc.sqrt(144)  # 12
result = calc.nth_root(27, 3)  # 3 (الجذر التكعيبي)

# المضروب
result = calc.factorial(6)  # 720
```

### الدوال المثلثية
```python
# الوضع الافتراضي: راديان
calc.sin(math.pi/2)  # 1.0
calc.cos(0)  # 1.0

# التبديل للدرجات
calc.set_angle_mode('deg')
calc.sin(90)  # 1.0
calc.cos(180)  # -1.0
```

### اللوغاريتمات
```python
calc.log10(1000)  # 3.0
calc.ln(math.e)  # 1.0
calc.log2(256)  # 8.0
calc.exp(2)  # 7.389...
```

### الدوال الإحصائية
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

calc.mean(numbers)  # 5.5
calc.median(numbers)  # 5.5
calc.stdev(numbers)  # 3.02...
calc.variance(numbers)  # 9.16...
```

### التباديل والتوافيق
```python
calc.permutation(5, 3)  # 60 (P(5,3))
calc.combination(5, 3)  # 10 (C(5,3))
```

### الأعداد الأولية
```python
calc.is_prime(17)  # True
calc.is_prime(18)  # False
```

### استخدام الذاكرة
```python
calc.memory_store(42)  # حفظ 42 في الذاكرة
calc.memory_add(8)  # الذاكرة الآن = 50
value = calc.memory_recall()  # استرجاع 50
calc.memory_clear()  # مسح الذاكرة
```

### تقييم التعبيرات المعقدة
```python
# يمكنك كتابة تعبيرات رياضية معقدة
calc.evaluate("2 + 3 * 4")  # 14
calc.evaluate("sin(pi/2) + cos(0)")  # 2.0
calc.evaluate("sqrt(16) + log10(100)")  # 6.0
calc.evaluate("factorial(5) / factorial(3)")  # 20
calc.evaluate("exp(ln(5))")  # 5.0
```

## 🎮 الأوامر في الوضع التفاعلي

| الأمر | الوصف |
|------|-------|
| `help` | عرض القائمة الرئيسية |
| `eval <expression>` | تقييم تعبير رياضي |
| `mode rad` | تغيير للراديان |
| `mode deg` | تغيير للدرجات |
| `ms` | حفظ في الذاكرة |
| `mr` | استرجاع من الذاكرة |
| `mc` | مسح الذاكرة |
| `m+` | إضافة للذاكرة |
| `m-` | طرح من الذاكرة |
| `history` | عرض السجل |
| `clear_history` | مسح السجل |
| `exit` / `quit` | الخروج |

## 🔧 المتطلبات

- Python 3.6+
- المكتبات المضمنة في Python (math, statistics)

لا يتطلب تثبيت أي مكتبات خارجية!

## 📝 ملاحظات

- جميع العمليات المثلثية تدعم الراديان والدرجات
- التعبيرات الرياضية تُقيّم بشكل آمن
- يتم حفظ سجل جميع العمليات تلقائياً
- الحاسبة تتعامل مع الأخطاء بشكل آمن وتعرض رسائل واضحة

## 🎯 أمثلة الاستخدام المباشر

```bash
# مثال 1: حساب مساحة دائرة نصف قطرها 5
python3 scientific_calculator.py "pi * pow(5, 2)"

# مثال 2: حساب جيب 45 درجة
python3 scientific_calculator.py "sin(pi/4)"

# مثال 3: حساب معادلة تربيعية
python3 scientific_calculator.py "(-5 + sqrt(25 - 4*1*6)) / (2*1)"

# مثال 4: النمو الأسي
python3 scientific_calculator.py "1000 * exp(0.05 * 10)"
```

## 🌟 مميزات إضافية

- ✅ واجهة عربية وإنجليزية
- ✅ أكثر من 40 دالة رياضية
- ✅ كود نظيف ومنظم وموثق
- ✅ معالجة شاملة للأخطاء
- ✅ سهل الاستخدام والتوسيع

## 📄 الترخيص

هذا المشروع مفتوح المصدر ومتاح للاستخدام الحر.

---

صُنع بـ ❤️ باستخدام Python 🐍
