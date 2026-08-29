# Web Applications Course — Yachay Tech University

Welcome to the official repository for the **Web Applications** course (8th Semester, August 2026) at **Yachay Tech University** (Ecuador), developed by **Kevin Sanchez (KevJoss)**.

This repository serves as a centralized hub for all practical workshops, architectural implementations, and progressive web projects developed throughout the semester, covering fundamental to advanced web technologies (HTML5, Vanilla CSS3, Web Servers, Responsive Design, and modern tooling).

---

## 📚 Workshops Overview & Project Index

| Workshop | Directory & Documentation | Core Topics & Description | Key Technologies |
| :--- | :--- | :--- | :--- |
| **Workshop 1** | [📂 `workshop-1-website-HTML`](workshop-1-website-HTML/)<br>[📖 `README.md`](workshop-1-website-HTML/README.md) \| [📝 `notes_about_W1.md`](workshop-1-website-HTML/notes_about_W1.md) | **Semantic HTML5 & Apache2 Server Deployment:**<br>Construction of a multi-page personal portfolio using strict semantic HTML5 elements. Deployment on a local Apache2 HTTP server under Linux (WSL2) with custom local domain resolution (`http://workshop1.webapp`). | `HTML5`, `Apache2`, `WSL2`, `VirtualHosts`, `Linux Networking` |
| **Workshop 2** | [📂 `workshop-2-website-HTML-with-CSS`](workshop-2-website-HTML-with-CSS/)<br>[📖 `README.md`](workshop-2-website-HTML-with-CSS/README.md) | **Modern Styling & Responsive Design (Vanilla CSS3):**<br>Complete visual transformation of the portfolio into a premium, accessible, and fully responsive website. Implements custom CSS design tokens, CSS Grid timetables, interactive forms, and multi-device media queries (Mobile, iPad, Desktop). | `HTML5`, `Vanilla CSS3`, `CSS Grid`, `Flexbox`, `Responsive Media Queries` |

---

## 🛠️ Summary of Workshop Contents

### 1. [Workshop 1 — Semantic HTML & Local Web Server](workshop-1-website-HTML/)
- **Semantic HTML5 Markup:** Explores structural elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<table>`, `<form>`) without relying on CSS frameworks.
- **Server Deployment & Networking:** Detailed guide on setting up an Apache2 web server on Ubuntu via WSL2 with mirrored networking mode (`.wslconfig`), configuring custom Virtual Hosts (`workshop1.webapp.conf`), managing file permission policies (`Require all granted`), and mapping local hostnames in the OS `hosts` file.
- **Technical Logs:** Comprehensive troubleshooting and step-by-step commands documented in [`workshop-1-website-HTML/notes_about_W1.md`](workshop-1-website-HTML/notes_about_W1.md).

### 2. [Workshop 2 — Advanced Styling & Responsive Architecture](workshop-2-website-HTML-with-CSS/)
- **Design System & Aesthetics:** Implementation of a cohesive design system using CSS Variables (`:root`), Google Fonts (*Montserrat*, *Oswald*), and modern color palettes.
- **Interactive Pages:** 6 fully developed pages covering Home, About Me, Professional & Research Experience (SDAS group, ML research study, industry internships), Extracurricular Leadership (IEEE CS, Computer Science Club, CompuFest 2026), Semester Courses, and Contact Form.
- **Advanced Layouts:** Interactive academic timetable engineered with CSS Grid (eliminating cell collisions and rendering issues across all hours).
- **Responsive Adaptability:** Specialized media queries tailored for Mobile devices (`< 768px`), Tablets / iPads (`768px – 1024px`), and Laptops/Desktops (`> 1024px`), featuring mobile horizontal navigation strips and stacked tactile CTAs.

---

## 📂 Repository Directory Tree

```text
Web-applications-course-Yachay-Tech/
│
├── README.md                                  # Repository overview and guide (This file)
│
├── workshop-1-website-HTML/                   # Workshop 1: Semantic HTML & Apache2
│   ├── index.html                             # Main landing page
│   ├── notes_about_W1.md                      # Apache server setup technical log
│   ├── README.md                              # Workshop 1 detailed documentation
│   ├── pages/                                 # Subpages (Professional, Courses, etc.)
│   └── images/                                # Project image assets
│
└── workshop-2-website-HTML-with-CSS/          # Workshop 2: Full CSS3 & Responsive Design
    ├── index.html                             # Main landing page (Home)
    ├── README.md                              # Workshop 2 detailed documentation
    ├── css/                                   # Modular CSS stylesheets (Grid, Flexbox, Tokens)
    ├── pages/                                 # Multi-page website subpages
    └── images/                                # High-res logos and portraits
```

---

## 🚀 Getting Started & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/KevJoss/Web-applications-course-Yachay-Tech.git
cd Web-applications-course-Yachay-Tech
```

### 2. Running Any Workshop
Navigate into the desired workshop directory and open with your preferred method:

- **Workshop 1 (Static or Apache):**
  - Read [`workshop-1-website-HTML/README.md`](workshop-1-website-HTML/README.md) for Apache VirtualHost instructions or open `workshop-1-website-HTML/index.html` directly in the browser.
- **Workshop 2 (Responsive Website):**
  - Read [`workshop-2-website-HTML-with-CSS/README.md`](workshop-2-website-HTML-with-CSS/README.md) and serve locally using Live Server, Python HTTP server (`python -m http.server 8000`), or open `workshop-2-website-HTML-with-CSS/index.html`.

---

## 👤 Author

**Kevin Sanchez (KevJoss)**
- **Role:** AI Engineer & Computer Science Student (8th Semester)
- **Institution:** Yachay Tech University, Imbabura, Ecuador
- **LinkedIn:** [/in/kevin-sanchez-josue](https://www.linkedin.com/in/kevin-sanchez-josue/)
- **GitHub:** [@KevJoss](https://github.com/KevJoss)
- **Course:** Web Applications (Academic Period: August 2026)

---

## 📄 License

This repository is maintained for academic and educational purposes within the Computer Science curriculum at Yachay Tech University. All rights reserved &copy; 2026.
