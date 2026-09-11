# Workshop 3 — Interactive Website with JavaScript & jQuery

## 📋 Overview

This workshop adds **client-side interactivity** to the portfolio website built in Workshops 1 & 2. Using **Vanilla JavaScript** and **jQuery**, two independent features were implemented, each in its own script file to keep the code organized and easy to understand.

---

## ✨ JavaScript Features Implemented

### 1. 🎨 Hero Color Toggle — `js/main.js`

**What it does:** A button in the hero section randomly changes the hero's background color each time it is clicked.

**How it works:**
- A predefined `colorPalette` array stores a set of soft, curated colors.
- On each click, `Math.random()` picks a random index and jQuery's `.css()` applies the new background color to the `.hero` section.
- The ring around the profile photo remains visible on every background color thanks to a corrected `z-index` stacking (`::before` at `z-index: 1`, photo at `z-index: 2`).

**Key concepts used:** jQuery selectors, event listeners (`.on("click")`), arrays, `Math.random()`, CSS manipulation with jQuery.

```js
$boton.on("click", changeColor);
```

---

### 2. 🖼️ Image Gallery Modal — `js/main.js`

**What it does:** Clicking on the profile photo in the hero section opens a **popup modal** that displays the image enlarged, with a blurred dark overlay behind it.

**How it works:**
- The modal is an HTML `<div>` placed at the end of `<body>` with the `hidden` attribute so it starts invisible.
- `$(document).ready()` ensures the JS runs only **after** the full DOM (including the modal) is loaded.
- Clicking the photo removes `hidden` and adds the `.modal-visible` class, which triggers a CSS fade + scale-up animation.
- The modal can be closed three ways: the **× button**, clicking the **dark overlay**, or pressing **Escape**.
- A `transitionend` event listener waits for the CSS fade-out animation to finish before setting `hidden` back.

**Key concepts used:** `$(document).ready()`, `.removeAttr()` / `.attr()`, `.addClass()` / `.removeClass()`, `setTimeout()` for animation timing, event delegation, keyboard events.

```js
$trigger.on("click", openModal);
$closeBtn.on("click", closeModal);
$modal.on("click", function(e) { if ($(e.target).is($modal)) closeModal(); });
$(document).on("keydown", function(e) { if (e.key === "Escape") closeModal(); });
```

**Why `$(document).ready()`?**  
The `<script>` tags appear *before* the modal `<div>` in the HTML. Without `ready()`, jQuery would try to select `#image-modal` before it exists in the DOM and return an empty object, making the click listener do nothing.

---

### 3. ✅ Form Validation — `js/form_validation.js`

**What it does:** Intercepts the contact form submission, validates all fields, shows inline error messages, and displays `"Form submitted successfully!"` only when all data is valid.

**How it works:**
- `e.preventDefault()` stops the browser's default form submission so JS can validate first.
- Each field is checked individually with its own rule. If invalid, `showError()` adds a red border (`.input-error` class) and inserts a `<span class="error-msg">` with a descriptive message below the field.
- A live listener (`.on("input change")`) clears errors in real time as the user corrects them.
- If all fields pass (`isValid === true`), an `alert()` confirms success and the form resets.

**Fields validated and their rules:**

| Field | Rule |
| :--- | :--- |
| Full Name | Not empty + only letters and spaces (no numbers or special characters). Uses regex `/^[a-zA-ZÀ-ÿ\s]+$/` to support accented/Spanish letters. |
| Email | Not empty + valid email format. Uses regex `/^[^\s@]+@[^\s@]+\.[^\s@]+$/`. |
| Date of Birth | Not empty (a date must be selected). |
| Degree, Semester, Reason | Must have a selected value (not empty/null). |
| Message | Not empty. |
| Consent checkbox | Must be checked. |

**Key concepts used:** `e.preventDefault()`, regex (`RegExp.test()`), jQuery DOM manipulation (`.after()`, `.siblings()`, `.remove()`), CSS class toggling, form reset (`this.reset()`).

**CSS enhancements (`css/contact_styles.css`):**
- `.input-error` → red border + light red background + `shake` keyframe animation.
- `.error-msg` → small red text displayed below the invalid field.
- `@keyframes shake` → a quick left-right vibration (0 → -5px → +5px → -4px → 0) that runs in 0.3 seconds to visually signal the error.

---

## 📂 File Structure

```text
workshop-3-website-with-JS/
│
├── index.html                  # Home page (hero, modal trigger)
├── pages/
│   ├── contact.html            # Contact page with validated form
│   └── ...                     # Other pages (about, professional, etc.)
│
├── js/
│   ├── main.js                 # Color toggle + Image modal logic
│   └── form_validation.js      # Contact form validation logic
│
├── css/
│   ├── home_styles.css         # Hero styles + modal styles
│   ├── contact_styles.css      # Contact form styles + validation styles
│   └── ...                     # Other stylesheets
│
└── images/                     # Profile photo and other assets
```

---

## 🔑 Key JavaScript & jQuery Concepts

| Concept | Where used |
| :--- | :--- |
| `$(document).ready()` | Modal — ensures DOM is fully loaded before binding events |
| `.on("click")` / `.on("submit")` | All interactive elements |
| `e.preventDefault()` | Form — stops default browser submission |
| `Math.random()` | Color toggle — picks a random color |
| `RegExp.test()` | Form — validates name and email format |
| `.addClass()` / `.removeClass()` | Modal — triggers CSS animations |
| `.attr("hidden")` / `.removeAttr()` | Modal — shows/hides the overlay |
| `setTimeout()` | Modal — small delay for CSS transition to register |
| `transitionend` event | Modal — waits for fade-out before hiding element |
| `@keyframes` (CSS) | Form — shake animation on invalid fields |
| `z-index` stacking | Hero — keeps the ring visible over changing backgrounds |

---

## 👤 Author

**Kevin Sanchez (KevJoss)**
- **Institution:** Yachay Tech University, Ecuador
- **Course:** Web Applications — 8th Semester, August 2026
- **GitHub:** [@KevJoss](https://github.com/KevJoss)
