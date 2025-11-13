#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
آلة حاسبة علمية شاملة
Scientific Calculator - Advanced Version
"""

import math
import statistics
from typing import List, Union
import re


class ScientificCalculator:
    """
    آلة حاسبة علمية كبيرة مع وظائف متقدمة
    Large Scientific Calculator with advanced functions
    """

    def __init__(self):
        """تهيئة الحاسبة مع الثوابت الرياضية"""
        self.memory = 0
        self.history = []
        self.constants = {
            'pi': math.pi,
            'π': math.pi,
            'e': math.e,
            'phi': (1 + math.sqrt(5)) / 2,  # النسبة الذهبية
            'tau': 2 * math.pi,
        }
        self.angle_mode = 'rad'  # 'rad' or 'deg'

    # ==================== العمليات الأساسية ====================

    def add(self, a: float, b: float) -> float:
        """الجمع"""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """الطرح"""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """الضرب"""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """القسمة"""
        if b == 0:
            raise ValueError("لا يمكن القسمة على صفر / Cannot divide by zero")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """الأس"""
        return math.pow(base, exponent)

    def sqrt(self, x: float) -> float:
        """الجذر التربيعي"""
        if x < 0:
            raise ValueError("لا يمكن حساب الجذر التربيعي لعدد سالب")
        return math.sqrt(x)

    def nth_root(self, x: float, n: float) -> float:
        """الجذر النوني"""
        return math.pow(x, 1/n)

    def absolute(self, x: float) -> float:
        """القيمة المطلقة"""
        return abs(x)

    def modulo(self, a: float, b: float) -> float:
        """باقي القسمة"""
        return a % b

    def factorial(self, n: int) -> int:
        """المضروب"""
        if n < 0:
            raise ValueError("المضروب غير معرف للأعداد السالبة")
        return math.factorial(int(n))

    # ==================== الدوال المثلثية ====================

    def _convert_angle(self, angle: float) -> float:
        """تحويل الزاوية حسب الوضع المحدد"""
        if self.angle_mode == 'deg':
            return math.radians(angle)
        return angle

    def sin(self, x: float) -> float:
        """جيب الزاوية"""
        return math.sin(self._convert_angle(x))

    def cos(self, x: float) -> float:
        """جيب تمام الزاوية"""
        return math.cos(self._convert_angle(x))

    def tan(self, x: float) -> float:
        """ظل الزاوية"""
        return math.tan(self._convert_angle(x))

    def asin(self, x: float) -> float:
        """معكوس الجيب"""
        result = math.asin(x)
        return math.degrees(result) if self.angle_mode == 'deg' else result

    def acos(self, x: float) -> float:
        """معكوس جيب التمام"""
        result = math.acos(x)
        return math.degrees(result) if self.angle_mode == 'deg' else result

    def atan(self, x: float) -> float:
        """معكوس الظل"""
        result = math.atan(x)
        return math.degrees(result) if self.angle_mode == 'deg' else result

    def sinh(self, x: float) -> float:
        """الجيب الزائدي"""
        return math.sinh(x)

    def cosh(self, x: float) -> float:
        """جيب التمام الزائدي"""
        return math.cosh(x)

    def tanh(self, x: float) -> float:
        """الظل الزائدي"""
        return math.tanh(x)

    # ==================== اللوغاريتمات ====================

    def log(self, x: float, base: float = 10) -> float:
        """اللوغاريتم"""
        if x <= 0:
            raise ValueError("اللوغاريتم معرف فقط للأعداد الموجبة")
        return math.log(x, base)

    def ln(self, x: float) -> float:
        """اللوغاريتم الطبيعي"""
        if x <= 0:
            raise ValueError("اللوغاريتم معرف فقط للأعداد الموجبة")
        return math.log(x)

    def log10(self, x: float) -> float:
        """اللوغاريتم العشري"""
        if x <= 0:
            raise ValueError("اللوغاريتم معرف فقط للأعداد الموجبة")
        return math.log10(x)

    def log2(self, x: float) -> float:
        """اللوغاريتم الثنائي"""
        if x <= 0:
            raise ValueError("اللوغاريتم معرف فقط للأعداد الموجبة")
        return math.log2(x)

    def exp(self, x: float) -> float:
        """الأسي (e^x)"""
        return math.exp(x)

    # ==================== الدوال الإحصائية ====================

    def mean(self, numbers: List[float]) -> float:
        """المتوسط الحسابي"""
        if not numbers:
            raise ValueError("القائمة فارغة")
        return statistics.mean(numbers)

    def median(self, numbers: List[float]) -> float:
        """الوسيط"""
        if not numbers:
            raise ValueError("القائمة فارغة")
        return statistics.median(numbers)

    def mode(self, numbers: List[float]) -> float:
        """المنوال"""
        if not numbers:
            raise ValueError("القائمة فارغة")
        return statistics.mode(numbers)

    def stdev(self, numbers: List[float]) -> float:
        """الانحراف المعياري"""
        if len(numbers) < 2:
            raise ValueError("يجب أن تحتوي القائمة على عنصرين على الأقل")
        return statistics.stdev(numbers)

    def variance(self, numbers: List[float]) -> float:
        """التباين"""
        if len(numbers) < 2:
            raise ValueError("يجب أن تحتوي القائمة على عنصرين على الأقل")
        return statistics.variance(numbers)

    # ==================== دوال إضافية ====================

    def ceil(self, x: float) -> int:
        """التقريب للأعلى"""
        return math.ceil(x)

    def floor(self, x: float) -> int:
        """التقريب للأسفل"""
        return math.floor(x)

    def round_number(self, x: float, decimals: int = 0) -> float:
        """التقريب لعدد معين من الخانات العشرية"""
        return round(x, decimals)

    def gcd(self, a: int, b: int) -> int:
        """القاسم المشترك الأكبر"""
        return math.gcd(int(a), int(b))

    def lcm(self, a: int, b: int) -> int:
        """المضاعف المشترك الأصغر"""
        return abs(int(a) * int(b)) // math.gcd(int(a), int(b))

    def permutation(self, n: int, r: int) -> int:
        """التباديل"""
        return math.perm(int(n), int(r))

    def combination(self, n: int, r: int) -> int:
        """التوافيق"""
        return math.comb(int(n), int(r))

    def is_prime(self, n: int) -> bool:
        """التحقق من كون العدد أولي"""
        n = int(n)
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def degrees_to_radians(self, degrees: float) -> float:
        """تحويل من درجات إلى راديان"""
        return math.radians(degrees)

    def radians_to_degrees(self, radians: float) -> float:
        """تحويل من راديان إلى درجات"""
        return math.degrees(radians)

    # ==================== الذاكرة ====================

    def memory_store(self, value: float):
        """حفظ في الذاكرة"""
        self.memory = value
        print(f"تم الحفظ في الذاكرة: {value}")

    def memory_recall(self) -> float:
        """استرجاع من الذاكرة"""
        return self.memory

    def memory_clear(self):
        """مسح الذاكرة"""
        self.memory = 0
        print("تم مسح الذاكرة")

    def memory_add(self, value: float):
        """إضافة للذاكرة"""
        self.memory += value
        print(f"الذاكرة الآن: {self.memory}")

    def memory_subtract(self, value: float):
        """طرح من الذاكرة"""
        self.memory -= value
        print(f"الذاكرة الآن: {self.memory}")

    # ==================== السجل ====================

    def add_to_history(self, operation: str, result: float):
        """إضافة عملية للسجل"""
        self.history.append({'operation': operation, 'result': result})

    def show_history(self):
        """عرض السجل"""
        if not self.history:
            print("السجل فارغ")
            return
        print("\n===== سجل العمليات =====")
        for i, entry in enumerate(self.history, 1):
            print(f"{i}. {entry['operation']} = {entry['result']}")

    def clear_history(self):
        """مسح السجل"""
        self.history = []
        print("تم مسح السجل")

    # ==================== تقييم التعبيرات ====================

    def evaluate(self, expression: str) -> float:
        """
        تقييم تعبير رياضي
        مثال: "2 + 3 * 4", "sin(pi/2)", "sqrt(16) + log(100)"
        """
        # إنشاء قاموس بالدوال والثوابت المتاحة
        safe_dict = {
            'sin': self.sin,
            'cos': self.cos,
            'tan': self.tan,
            'asin': self.asin,
            'acos': self.acos,
            'atan': self.atan,
            'sinh': self.sinh,
            'cosh': self.cosh,
            'tanh': self.tanh,
            'sqrt': self.sqrt,
            'log': self.log10,
            'ln': self.ln,
            'log10': self.log10,
            'log2': self.log2,
            'exp': self.exp,
            'abs': self.absolute,
            'ceil': self.ceil,
            'floor': self.floor,
            'factorial': self.factorial,
            'pow': self.power,
            # إضافة الثوابت مباشرة
            'pi': self.constants['pi'],
            'π': self.constants['π'],
            'e': self.constants['e'],
            'phi': self.constants['phi'],
            'tau': self.constants['tau'],
        }

        try:
            # تقييم التعبير بشكل آمن
            result = eval(expression, {"__builtins__": {}}, safe_dict)
            self.add_to_history(expression, result)
            return result
        except Exception as e:
            raise ValueError(f"خطأ في التعبير: {str(e)}")

    # ==================== تغيير الإعدادات ====================

    def set_angle_mode(self, mode: str):
        """تغيير وضع الزاوية (rad/deg)"""
        if mode.lower() not in ['rad', 'deg']:
            raise ValueError("الوضع يجب أن يكون 'rad' أو 'deg'")
        self.angle_mode = mode.lower()
        print(f"تم تغيير وضع الزاوية إلى: {self.angle_mode}")


def print_menu():
    """طباعة القائمة الرئيسية"""
    print("\n" + "="*60)
    print("🔬 الآلة الحاسبة العلمية الشاملة 🔬")
    print("Scientific Calculator - Advanced")
    print("="*60)
    print("\n📌 العمليات المتاحة:")
    print("\n1. العمليات الأساسية:")
    print("   add, subtract, multiply, divide, power, sqrt, abs, factorial")
    print("\n2. الدوال المثلثية:")
    print("   sin, cos, tan, asin, acos, atan, sinh, cosh, tanh")
    print("\n3. اللوغاريتمات:")
    print("   log, ln, log10, log2, exp")
    print("\n4. الدوال الإحصائية:")
    print("   mean, median, mode, stdev, variance")
    print("\n5. دوال إضافية:")
    print("   ceil, floor, round, gcd, lcm, permutation, combination")
    print("   is_prime, degrees_to_radians, radians_to_degrees")
    print("\n6. الذاكرة:")
    print("   ms (حفظ), mr (استرجاع), mc (مسح), m+ (إضافة), m- (طرح)")
    print("\n7. السجل:")
    print("   history (عرض السجل), clear_history (مسح السجل)")
    print("\n8. تقييم التعبيرات:")
    print("   eval <expression>  مثال: eval 2 + 3 * sin(pi/2)")
    print("\n9. الإعدادات:")
    print("   mode <rad/deg> (تغيير وضع الزاوية)")
    print("\n⚡ الثوابت المتاحة: pi, e, phi, tau")
    print("\n❌ للخروج اكتب: exit أو quit")
    print("="*60)


def interactive_mode():
    """الوضع التفاعلي للحاسبة"""
    calc = ScientificCalculator()
    print_menu()

    while True:
        try:
            user_input = input("\n➤ أدخل العملية: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['exit', 'quit', 'خروج']:
                print("👋 شكراً لاستخدامك الآلة الحاسبة العلمية!")
                break

            if user_input.lower() == 'help' or user_input == 'مساعدة':
                print_menu()
                continue

            if user_input.lower() == 'history':
                calc.show_history()
                continue

            if user_input.lower() == 'clear_history':
                calc.clear_history()
                continue

            if user_input.lower() == 'mc':
                calc.memory_clear()
                continue

            if user_input.lower() == 'mr':
                print(f"الذاكرة: {calc.memory_recall()}")
                continue

            # تقييم التعبيرات
            if user_input.lower().startswith('eval '):
                expression = user_input[5:]
                result = calc.evaluate(expression)
                print(f"✅ النتيجة: {result}")
                continue

            # تغيير وضع الزاوية
            if user_input.lower().startswith('mode '):
                mode = user_input[5:].strip()
                calc.set_angle_mode(mode)
                continue

            # محاولة تقييم التعبير مباشرة
            try:
                result = calc.evaluate(user_input)
                print(f"✅ النتيجة: {result}")
            except:
                print("❌ تعبير غير صحيح. اكتب 'help' للمساعدة")

        except KeyboardInterrupt:
            print("\n\n👋 شكراً لاستخدامك الآلة الحاسبة العلمية!")
            break
        except Exception as e:
            print(f"❌ خطأ: {str(e)}")


def run_examples():
    """تشغيل أمثلة توضيحية"""
    calc = ScientificCalculator()

    print("\n" + "="*60)
    print("🎯 أمثلة على استخدام الحاسبة العلمية")
    print("="*60 + "\n")

    examples = [
        ("2 + 3 * 4", "عملية حسابية أساسية"),
        ("sqrt(16) + pow(2, 3)", "جذر تربيعي وأس"),
        ("sin(pi/2)", "جيب 90 درجة (راديان)"),
        ("log10(100)", "لوغاريتم 100 للأساس 10"),
        ("exp(1)", "e^1"),
        ("factorial(5)", "مضروب 5"),
        ("abs(-10)", "القيمة المطلقة"),
        ("sqrt(2) * sqrt(8)", "ضرب جذور"),
    ]

    for expr, description in examples:
        try:
            result = calc.evaluate(expr)
            print(f"📝 {description}")
            print(f"   {expr} = {result}\n")
        except Exception as e:
            print(f"❌ خطأ في {expr}: {str(e)}\n")

    print("="*60)


if __name__ == "__main__":
    import sys

    print("\n🌟 مرحباً بك في الآلة الحاسبة العلمية الشاملة 🌟\n")

    if len(sys.argv) > 1:
        if sys.argv[1] == '--examples':
            run_examples()
        elif sys.argv[1] == '--help':
            print_menu()
        else:
            # تقييم التعبير من سطر الأوامر
            calc = ScientificCalculator()
            expression = ' '.join(sys.argv[1:])
            try:
                result = calc.evaluate(expression)
                print(f"{expression} = {result}")
            except Exception as e:
                print(f"❌ خطأ: {str(e)}")
    else:
        # الوضع التفاعلي
        interactive_mode()
