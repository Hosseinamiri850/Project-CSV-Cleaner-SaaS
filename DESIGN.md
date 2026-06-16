# DESIGN.md

مستندات طراحی UI/UX پروژه CSV Cleaner SaaS.

---

## Design System

### Framework
- **DaisyUI v4** — component library روی Tailwind CSS
- **Tailwind CSS v4** — utility-first CSS
- **Theme**: `light` (DaisyUI default light theme)

### Typography
- فارسی: Tahoma (system fallback)
- انگلیسی: system-ui

### رنگ‌ها (DaisyUI tokens)

| Token | کاربرد |
|-------|--------|
| `text-primary` | آمار "ردیف قبل" — آبی |
| `text-success` | آمار "ردیف بعد" — سبز |
| `text-warning` | تکراری حذف‌شده — زرد |
| `text-error` | مقادیر خالی — قرمز |
| `bg-base-200` | پس‌زمینه صفحه |
| `bg-base-100` | کارت‌ها و navbar |

---

## Layout

```
┌─────────────────────────────────┐
│ Navbar: CSV Cleaner             │
├─────────────────────────────────┤
│                                 │
│   h1: فایل CSV کثیف؟           │
│   subtitle                      │
│                                 │
│ ┌─────────────────────────────┐ │
│ │  Card                       │ │
│ │  ┌─────────────────────────┐│ │
│ │  │  Drop Zone              ││ │
│ │  │  📂 drag & drop         ││ │
│ │  └─────────────────────────┘│ │
│ └─────────────────────────────┘ │
│                                 │
│ ┌────┬────┬────┬────┐           │
│ │ قبل│ بعد│ dup│null│  Stats   │
│ └────┴────┴────┴────┘           │
│                                 │
│ ┌─────────────────────────────┐ │
│ │  Preview Table (zebra)      │ │
│ └─────────────────────────────┘ │
│                                 │
│ [ ⬇️ دانلود CSV تمیز ]          │
└─────────────────────────────────┘
```

---

## UX Decisions

### چرا drag & drop؟
ساده‌ترین و سریع‌ترین روش آپلود. کاربر نیازی به دکمه browse نداره.

### چرا stats cards؟
کاربر باید سریع بفهمه چی تغییر کرد — عدد بزرگ = اطلاعات سریع.

### چرا preview table؟
اعتماد‌سازی — کاربر قبل از دانلود می‌بینه داده درسته.

### چرا RTL؟
مخاطب اولیه فارسی‌زبان — `dir="rtl"` روی `<html>`.

---

## Animations

```css
.fade-in {
  animation: fadeIn .3s ease;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

Result section با fade-in ظاهر می‌شه — کمتر abrupt.

---

## States

| State | UI |
|-------|----|
| Initial | فقط drop zone |
| Uploading | loading spinner، drop zone مخفی |
| Success | stats + preview + download button |
| Error | alert قرمز با پیام خطا |

---

## آینده (Planned)

- [ ] Dark mode toggle
- [ ] فونت Vazirmatn (نیاز به self-hosting)
- [ ] Progress bar برای فایل‌های بزرگ
- [ ] Column-by-column null visualization
- [ ] Before/After comparison slider
