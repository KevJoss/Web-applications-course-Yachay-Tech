# Workshop 1: Semantic HTML Website & Apache2 Local Server Deployment

A semantic multi-page website built with standard **HTML5** and deployed locally on an **Apache2 HTTP Server** running on Ubuntu (WSL2) with custom local domain resolution (`http://workshop1.webapp`).

Developed by **Kevin Sanchez (KevJoss)** — Computer Science student at **Yachay Tech University** — as part of the **Web Applications** course (8th Semester, August 2026).

---

## 📌 Project Overview

This workshop introduces the fundamentals of web application architecture, covering two core objectives:
1. **Semantic HTML5 Construction:** Structuring a complete personal and academic multi-page website without CSS frameworks, utilizing proper semantic elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<table>`, `<form>`).
2. **Local Web Server Deployment & DNS Simulation:** Configuring an Apache HTTP daemon in Linux (WSL2), enabling virtual hosts, managing directory permissions, and mapping a custom local domain via the OS `hosts` file.

> [!NOTE]
> Detailed command logs, technical notes, and troubleshooting steps for the Apache server setup are documented in [`notes_about_W1.md`](notes_about_W1.md).

---

## 🖥️ Apache2 Web Server Configuration Summary

The local server environment was configured to serve the website under `http://workshop1.webapp`. Below is a high-level summary of the setup process (detailed guide in [`notes_about_W1.md`](notes_about_W1.md)):

### 1. Local Domain Name Resolution
- Mapped `workshop1.webapp` to `127.0.0.1` (localhost) in both the Windows host `hosts` file (`C:\Windows\System32\drivers\etc\hosts`) and Linux WSL `/etc/hosts`.
- Verified hostname resolution using `ping -c 3 workshop1.webapp`.

### 2. WSL2 Mirrored Networking
- Configured `.wslconfig` on Windows with `networkingMode=mirrored` to ensure seamless bidirectional port forwarding and IPv4/IPv6 compatibility between Windows and the WSL2 Linux virtual environment.

### 3. Apache2 Daemon Setup & Virtual Host
- Verified port availability on port `80` and installed `apache2`.
- Created an Apache Virtual Host configuration at `/etc/apache2/sites-available/workshop1.webapp.conf`:
  ```apache
  <VirtualHost *:80>
      ServerName workshop1.webapp
      DocumentRoot /mnt/c/Users/Usuario/Documents/YachayTech/Eigth_semester/web_applications/Web-applications-course-Yachay-Tech/workshop-1-website-HTML

      <Directory /mnt/c/Users/Usuario/Documents/YachayTech/Eigth_semester/web_applications/Web-applications-course-Yachay-Tech/workshop-1-website-HTML>
          Options Indexes FollowSymLinks
          AllowOverride All
          Require all granted
      </Directory>
  </VirtualHost>
  ```
- **Permission Troubleshooting:** Added the `<Directory>` block with `Require all granted` to resolve the `AH01630: client denied by server configuration` authorization error when serving files across the Windows/WSL mount point.

### 4. Activation & Verification
- Enabled the virtual site with `sudo a2ensite workshop1.webapp.conf`.
- Checked configuration syntax with `sudo apache2ctl configtest` (Syntax OK).
- Restarted the service (`sudo systemctl restart apache2`) and verified the response via `curl -I http://localhost` (HTTP/1.1 200 OK).

---

## 📄 Website Pages & Semantic HTML Structure

| Page                | File                                                       | Description                                                             | Semantic Elements Used                                                           |
| :------------------ | :--------------------------------------------------------- | :---------------------------------------------------------------------- | :------------------------------------------------------------------------------- |
| **Home**            | [`index.html`](index.html)                                 | Landing page, personal summary, social links, and navigation.           | `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`                           |
| **Professional**    | [`pages/professional.html`](pages/professional.html)       | Academic research work and industry software engineering experience.    | `<article>`, `<section>`, `<ul>`, `<ol>`, `<p>`, `<b>`                           |
| **Extracurricular** | [`pages/extracurricular.html`](pages/extracurricular.html) | Leadership roles (IEEE Computer Society, CS Club) and student events.   | `<article>`, `<h3>`, `<ul>`, `<a>`, `<span>`                                     |
| **Courses**         | [`pages/courses.html`](pages/courses.html)                 | 8th-semester academic courses, instructors, topics, and syllabus links. | `<article>`, `<h2>`, `<h3>`, `<ul>`, `<ol>`, `<a>`                               |
| **Schedule**        | [`pages/schedule.html`](pages/schedule.html)               | Weekly academic timetable for courses and lab sessions.                 | `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>`, `rowspan`, `colspan`    |
| **Contact**         | [`pages/contact.html`](pages/contact.html)                 | Interactive contact form for messages, feedback, and student queries.   | `<form>`, `<label>`, `<input>`, `<select>`, `<option>`, `<textarea>`, `<button>` |

---

## 📂 Project Directory Structure

```text
workshop-1-website-HTML/
│
├── index.html               # Main landing page (Home)
├── notes_about_W1.md        # Technical documentation of the Apache server deployment
├── README.md                # Workshop documentation (This file)
│
├── pages/
│   ├── professional.html    # Research & professional experience
│   ├── extracurricular.html # Leadership & extracurricular activities
│   ├── courses.html         # Current semester courses
│   ├── schedule.html        # Academic weekly schedule table
│   └── contact.html         # Interactive contact form
│
└── images/
    ├── kevin_photo.png      # Profile picture
    ├── SDAS_logo.png        # Research group logo
    └── yachay_tech_logo.png # University logo
```

---

## 🚀 How to Run Locally

You can test and explore this workshop using any of the following approaches:

### Option A: Direct Web Browser Access
Simply double-click [`index.html`](index.html) or open it with your favorite web browser (Chrome, Firefox, Edge, Safari).

### Option B: Local Development Server (VS Code / Python)
```bash
# Python 3
cd workshop-1-website-HTML
python -m http.server 8080
```
Then navigate to `http://localhost:8080` in your browser.

### Option C: Apache2 Virtual Host (As deployed in Workshop 1)
Follow the step-by-step instructions in [`notes_about_W1.md`](notes_about_W1.md) to set up the Apache VirtualHost and navigate to:
```text
http://workshop1.webapp
```

---

## 👤 Author

**Kevin Sanchez (KevJoss)**
- **Role:** Computer Science Student (8th Semester) & AI Engineer
- **Institution:** Yachay Tech University, Ecuador
- **LinkedIn:** [/in/kevin-sanchez-josue](https://www.linkedin.com/in/kevin-sanchez-josue/)
- **GitHub:** [@KevJoss](https://github.com/KevJoss)
- **Academic Course:** Web Applications (August 2026)

---

## 📄 License

This repository is maintained for educational purposes as part of the Web Applications coursework at Yachay Tech University. All rights reserved &copy; 2026.
