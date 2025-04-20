# 📅 Unified Task & Calendar Manager

A personal productivity app that brings your schedules and tasks from different platforms into one unified interface. Built as a local-first, privacy-focused tool for tracking calendars, to-dos, and reminders.

---

## 🧠 Why This Exists

This is a **personal project**, created both to meet my own daily (and ever growing) productivity needs and to **learn full-stack development** in a real, hands-on way.

I’ve always used a combination of tools—Google Calendar, Apple Reminders, sticky notes, and task apps—to manage my time. But they don’t talk to each other, and I kept losing track of things.

So this is my solution: one place to bring it all together.

---

## 🎯 Project Goals

This app is designed to be:

- ✅ **Personally useful**  
  It solves my actual problem: scattered to-dos and calendars across platforms.

- ✅ **A learning playground**  
  I’m using this to learn FastAPI, Vue.js, PostgreSQL, and how to plan, build, and track a real-world project.

- ✅ **Unifying**  
  View tasks, calendar events, and reminders from multiple platforms in one interface.

- ✅ **Local-first & private**  
  Data lives on my machine. External services are used only for syncing when I choose to.

- ✅ **Simple, clean, and extendable**  
  Start with the essentials, but build it so it can grow later (Google Calendar, Apple Reminders, Notion, etc.).

---

## 🛠️ Tech Stack

| Layer        | Tech                   |
|--------------|------------------------|
| Frontend     | [Vue.js](https://vuejs.org/) |
| Backend      | [FastAPI](https://fastapi.tiangolo.com/) |
| Database     | [PostgreSQL](https://www.postgresql.org/) |
| Sync Targets | Google Calendar API, Apple Reminders (TBD) |
| Hosting      | Local development environment |
| Versioning   | GitHub + Issues for tracking |

---

## 🚧 Current Status

> ✨ Actively being built — this is a work in progress!  
Right now, I’m setting up the project structure and core systems. You can check out the [Issues](https://github.com/your-username/your-repo-name/issues) tab for progress and planning.

---

```
calendar-tracker/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI entry point
│   │   ├── api/                 # Route definitions
│   │   ├── models/              # Pydantic models & DB models
│   │   ├── crud/                # CRUD utility functions
│   │   └── db/                  # DB config and init
│   ├── tests/                   # Backend tests
│   └── requirements.txt         # Optional if not using conda
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── views/
│   │   ├── App.vue
│   │   └── main.js
│   ├── .env
│   ├── vite.config.js
│   └── package.json
│
├── docs/
│   ├── architecture.md
│   ├── setup.md
│   └── ideas.md
│
├── .gitignore               
├── LICENSE
├── README.md
├── environment.yml            # Conda environment file
└── issue_templates/
    ├── feature_request.md
    └── bug_report.md
```
---

## 📝 Contributions & Feedback

This is a personal and learning-first project, but I’m always open to ideas, feedback, or encouragement.  
Feel free to:

- ⭐ Star the repo
- Open an issue with suggestions
- Watch the project grow

---
