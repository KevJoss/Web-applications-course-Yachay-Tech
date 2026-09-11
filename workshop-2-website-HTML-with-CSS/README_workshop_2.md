# Workshop 2: Personal Portfolio & Academic Website (HTML5 & CSS3)

A modern, semantic, accessible, and fully responsive multi-page personal portfolio and academic showcase built from scratch using pure **HTML5** and **Vanilla CSS3** (no third-party CSS frameworks).

Developed by **Kevin Sanchez (KevJoss)** — AI Engineer & Computer Science student at **Yachay Tech University** — as part of the **Web Applications** course (8th Semester, August 2026).

---

## 🚀 Live Demo & Project Overview

The website acts as a comprehensive personal and academic portfolio, structured across 6 dedicated pages:

| Page                | File                                                       | Description                                                                                                                     |
| :------------------ | :--------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| **Home**            | [`index.html`](index.html)                                 | Landing hero section, title tagline, call-to-action buttons, profile imagery, and direct social links.                          |
| **About**           | [`pages/about.html`](pages/about.html)                     | Background narrative, profile metadata card, and technical focus badges.                                                        |
| **Professional**    | [`pages/professional.html`](pages/professional.html)       | SDAS Research Group affiliation, research study breakdown, and industry work experience timeline (StrategIA, Webdit).           |
| **Extracurricular** | [`pages/extracurricular.html`](pages/extracurricular.html) | Leadership roles (IEEE Computer Society, Computer Science Club, Student Rep) and community events (CompuFest 2026, Hackathons). |
| **Courses**         | [`pages/courses.html`](pages/courses.html)                 | 8th-semester academic courses, core contents, topics of interest, syllabus access, and university accreditation.                |
| **Schedule**        | [`pages/schedule.html`](pages/schedule.html)               | Interactive weekly timetable built using pure CSS Grid, visual legends, and contact hour statistics.                            |
| **Contact**         | [`pages/contact.html`](pages/contact.html)                 | Direct channels (LinkedIn, timezone, availability) and a styled interactive contact form.                                       |

---

## 🛠️ Technology Stack & Architecture

- **Markup:** Semantic **HTML5** (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`, `<form>`).
- **Styling:** **Vanilla CSS3** (Custom Properties / Design Tokens, Flexbox, CSS Grid).
- **Typography:** [Google Fonts](https://fonts.google.com/) — *Montserrat* (Body & Headings) and *Oswald* (Labels, Numbers & Badges).
- **CSS Architecture:**
  - `main_styles.css`: Root design tokens (palette, reset, typography, footer, global CTAs).
  - `header_syles.css`: Navigation bar layout, active states, and mobile horizontal strip.
  - Page-specific stylesheets (`home_styles.css`, `about_styles.css`, `professional_styles.css`, `extracurricular_styles.css`, `courses_styles.css`, `schedule_styles.css`, `contact_styles.css`).
  - `normalize.css`: Cross-browser rendering consistency.

---

## 📱 Responsive Design & Breakpoints

The website is engineered to adapt seamlessly across multiple devices and viewport resolutions:

1. **Desktop / Laptop (`> 1024px`):**
   - Multi-column layouts, expanded timetables, large typography (`5rem` headings), and side-by-side content grids.
2. **iPad / Tablets (`768px – 1024px`):**
   - Balanced fluid single-to-two column layouts, scaled image sizes, and proportional font scaling.
   - Company logos placed side-by-side with timeline dates in the Professional section.
3. **Mobile Devices (`< 768px` and `< 480px`):**
   - Dedicated horizontal navigation bar with smooth touch scroll and overflow control.
   - Stacked full-width CTA buttons at the bottom of each page without detached arrows.
   - Full-width event cards with vertical status badges for optimal readability.

---

## 📂 Project Directory Structure

```text
workshop-2-website-HTML-with-CSS/
│
├── index.html                     # Main landing page (Home)
├── README.md                      # Project documentation (This file)
│
├── css/
│   ├── normalize.css              # Baseline CSS reset
│   ├── main_styles.css            # Global variables, typography & layout tokens
│   ├── header_syles.css           # Navigation bar & header styling
│   ├── home_styles.css            # Home / Hero section styles
│   ├── about_styles.css           # About Me page styles
│   ├── professional_styles.css    # Research & Industry experience styles
│   ├── extracurricular_styles.css # Extracurricular & Events styles
│   ├── courses_styles.css         # Academic courses styles
│   ├── schedule_styles.css        # Weekly schedule timetable grid styles
│   └── contact_styles.css         # Contact form & information styles
│
├── pages/
│   ├── about.html                 # About Me page
│   ├── professional.html          # Research and work experience
│   ├── extracurricular.html       # Extracurricular & leadership activities
│   ├── courses.html               # Semester courses details
│   ├── schedule.html              # Weekly academic calendar
│   └── contact.html               # Contact form and channels
│
└── images/
    ├── kevin_photo.png            # Profile portrait
    ├── Logo-YT.png                # Yachay Tech University logo
    ├── SDAS_logo.png              # SDAS Research Group logo
    ├── strategia_agile_solutions_logo.jpg # StrategIA company logo
    ├── webdit_logo.jpg            # Webdit company logo
    ├── IEEE_CS_logo.jpg           # IEEE Computer Society logo
    ├── ccc_logo.jpg               # Computer Science Club logo
    └── COMPUFEST_logo.svg         # CompuFest 2026 logo
```

---

## 💻 Getting Started / Running Locally

To view or work on this project locally, follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/KevJoss/Web-applications-course-Yachay-Tech.git
cd Web-applications-course-Yachay-Tech/workshop-2-website-HTML-with-CSS
```

### 2. Open the project
You can open `index.html` directly in any modern web browser, or serve it using a local server for the best development experience:

- **VS Code Live Server:** Right-click on `index.html` and select **"Open with Live Server"**.
- **Python HTTP Server:**
  ```bash
  # Python 3
  python -m http.server 8000
  ```
  Then navigate to `http://localhost:8000` in your browser.


---

## 👤 Author

**Kevin Sanchez (KevJoss)**
- **Role:** AI Engineer & Computer Science Student (8th Semester)
- **Institution:** Yachay Tech University, Ecuador
- **LinkedIn:** [/in/kevin-sanchez-josue](https://www.linkedin.com/in/kevin-sanchez-josue/)
- **GitHub:** [@KevJoss](https://github.com/KevJoss)
- **Academic Course:** Web Applications (August 2026)

---

## 📄 License & Attribution

This project is created for educational and professional demonstration purposes under the Web Applications course curriculum at Yachay Tech University. All rights reserved &copy; 2026.
