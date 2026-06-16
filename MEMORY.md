# MEMORY.md

تاریخچه تصمیمات و context پروژه — برای مراجعه بعدی.

## تصمیمات معماری

### چرا FastAPI؟
- async native
- مستندات خودکار با `/docs`
- سریع‌تر از Django برای API-only

### چرا pandas؟
- استاندارد پردازش داده در Python
- built-in برای drop_duplicates، dropna، و normalization

### چرا DaisyUI + Tailwind v4؟
- component-based، نیاز به کمترین CSS سفارشی
- RTL support خوب
- build شده و serve شده بدون CDN

### چرا بدون Auth فعلاً؟
- MVP اول باید فروش رو ثابت کنه
- Auth بعد از اولین مشتری اضافه می‌شه
- مدل فعلی: stateless، هر request مستقل

### چرا AI غیرفعال؟
- API key نیاز به billing داره
- MVP بدون AI هم کار می‌کنه
- بعداً Gemini یا Anthropic وصل می‌شه

## مشکلات حل‌شده

### NaN در JSON
pandas مقادیر خالی رو به `NaN` تبدیل می‌کنه که JSON-compliant نیست.
**راه‌حل**: تبدیل `NaN` به `None` قبل از return.

```python
def clean_value(v):
    if isinstance(v, float) and math.isnan(v):
        return None
    return v
```

### PowerShell Execution Policy
ویندوز اجازه اجرای script نمیداد.
**راه‌حل**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### DaisyUI build
Tailwind v4 دیگه `tailwind.config.js` نمی‌خواد.
**راه‌حل**: استفاده از `@plugin` در `input.css`:
```css
@import "tailwindcss";
@plugin "daisyui" {
  themes: light;
}
```

## مراحل انجام‌شده

- [x] Backend با FastAPI
- [x] پاک‌سازی CSV با pandas
- [x] Frontend با DaisyUI
- [x] Serve کردن frontend از FastAPI
- [x] فایل‌های پروژه (README, .gitignore, requirements.txt)

## مراحل بعدی

- [ ] دیپلوی روی Railway
- [ ] Landing page برای فروش
- [ ] سیستم پرداخت با Paddle
- [ ] Auth و دیتابیس (Supabase)
- [ ] AI feature فعال
- [ ] Usage limits برای پلان رایگان
