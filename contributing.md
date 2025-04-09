# 🤝 Team Collaboration Plan – Capstone MVP

Welcome, Capstone Team! Below are our role assignments and Git workflow for this project. 
Please follow this guide to keep our branches clean, organized, and productive.

---

## 🔧 Setup Instructions

1. Clone the school repo:
```bash
git clone https://github.com/YOUR-SCHOOL-ORG/YOUR-CAPSTONE-REPO.git
cd YOUR-CAPSTONE-REPO
```

2. Checkout your personal branch from Rena's MVP:
```bash
git checkout -b your-branch-name origin/baseline-mvp
```

3. Do your work on your own branch. Commit often.

4. Push your branch:
```bash
git push origin your-branch-name
```

5. Open a Pull Request (PR) **into the `staging` branch, not `main`.

## 👥 Roles & Branches

| Name | Branch Name | Role |
|------|-------------|------|
| **Rena Glare** | `baseline-mvp`, `staging`, `main` | Lead, DevOps, Backend |
| **Howard Mahaffey** | `prompt-tuning` | Prompt + RAG context improvements |
| **Khalisah Khan** | `frontend-ui` | UI/UX design and chat styling |
| **Ryan Pham** | `frontend-integration` | Connect frontend to backend |
| **Anthony Rodriguez** | `docs-and-readme` | API Docs, README, and guidance |

## 🛠 Merge Process

* Rena will review PRs into `staging`
* Once all parts work well together, Rena will merge `staging` into `main`
* No one should push directly to `main`

## 📌 Notes

* Always pull latest from `baseline-mvp` if starting fresh
* Use clear commit messages (e.g., `add input box styling`, `connect POST route`)
* Test your code before pushing
* Ask questions in Slack or GitHub issues!

Let's build something awesome 💪