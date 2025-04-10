# 🤩 Capstone Agile Challenge

## 📚 Framework Selection: Kanban vs Scrum

For our Capstone chatbot project, **Kanban** is the more appropriate framework over Scrum. Since we are working on a short MVP sprint with limited time, and tasks can be picked up and completed independently, Kanban offers better flexibility without the overhead of structured sprints and roles like Scrum Master or Product Owner. If our team were engaging in a longer-term iterative process with bi-weekly deliveries, user feedback, and retrospectives, Scrum would be a better choice. For our single-turn chatbot MVP, Kanban helps us stay focused, visual, and adaptable.

---

## 📋 Backlog Creation (Product Backlog: 8–10 Items)

| Priority | User Story / Feature | Description |
|----------|----------------------|-------------|
| 🥇 1 | As a developer, I want a clear folder structure so I can organize the backend, frontend, and RAG logic properly. | Set up initial file structure as planned in the architecture. |
| 🥈 2 | As a user, I want a simple chatbot interface so I can ask housing-related questions. | Build the UI in Next.js with an input box and response display. |
| 🥉 3 | As a developer, I want a NestJS endpoint to handle chatbot requests. | Create a `/chatbot` POST route. |
| 4 | As a developer, I want to connect to an LLM service so I can generate responses. | Integrate with LM Studio or Python FastAPI service. |
| 5 | As a user, I want relevant responses from the chatbot so I can get helpful information. | Implement basic RAG by searching context files. |
| 6 | As a developer, I want an ethics disclaimer so users understand the chatbot's limits. | Add a markdown file and link in the UI. |
| 7 | As a team, we want to follow Bloom’s standards so our app can integrate later. | Align component structure, ethical guidelines, and code practices. |
| 8 | As a mentor, I want to see the progress easily so I can support the team. | Use GitHub Projects to track all issues and updates. |
| 9 | As a developer, I want to see success/error messages from the chatbot. | Add basic error handling in the UI and backend. |
| 🔟 10 | As a user, I want the app to be responsive on mobile devices. | Apply responsive styles using CSS Modules. |

---

## ✅ GitHub Project & Issues Setup

- [x] **Created a GitHub Project board** named `Capstone: Single-Turn Chatbot`
- [x] **Added columns**: Backlog, To Do, In Progress, Blocked, Done
- [x] **Created GitHub Issues** for all 10 backlog items and linked them to the board
- [x] **Added team members & mentors** as collaborators to both the repo and the project board

---

## 🔧 Tool Evaluation: GitHub Projects vs Trello

| Feature                 | GitHub Projects | Trello |
|-------------------------|------------------|--------|
| Native code integration | ✅ Yes            | ❌ No  |
| Link issues & PRs       | ✅ Yes            | ❌ No  |
| Agile features (labels, assignees, automation) | ✅ Yes | ✅ Basic |
| Timeline view           | ✅ Yes (v2 Projects) | ❌ No |
| Kanban-style UI         | ✅ Yes            | ✅ Yes |
| Custom fields           | ✅ Yes (limited)  | ✅ Yes (with Power-Ups) |
| Markdown support        | ✅ Yes            | ❌ No |

**Best for Capstone?**  
✅ **GitHub Projects** is the better fit for our Capstone because we are managing code and project planning in one place. It allows us to directly connect issues to commits and pull requests, reducing context-switching and keeping everything streamlined.

---

## 🧐 Reflection

The most valuable phase of today's session for me was **abstract conceptualization**. By outlining our full architecture and breaking down tasks into backlog items, I was able to mentally connect how each technical component ties into real Agile workflows. It helped me understand how planning and code organization directly impact collaboration and delivery. This process gave me clarity and confidence as we move forward with development.

