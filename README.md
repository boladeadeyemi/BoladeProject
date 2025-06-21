# 👨‍💻 Group 6 Tech Crush Capstone Project

This is a full-stack web application that allows users to search for group members of Group 6 using a React-based frontend and a Flask-based backend. It is fully containerized using Docker and can be deployed locally via Docker Compose.

---

## 🚀 Features

- 🔎 Search for a group member by name
- ⚡ Fast, responsive React frontend
- 🐍 Lightweight Flask API backend
- 🔗 Frontend communicates with backend via REST API
- 📦 Dockerized with multi-service setup
- 🔄 Ready for CI/CD with GitHub Actions (optional)

---

## 🖼️ Project Structure

```
my-project/
├── Backend/
│   ├── server.py
├── Frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
├── Dockerfile.backend
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🧪 Tech Stack

- **Frontend**: React, Axios, HTML/CSS
- **Backend**: Python, Flask, Flask-CORS
- **Containerization**: Docker, Docker Compose
- **DevOps**: GitHub, GitHub Actions (optional)

---

## 🐳 Run Locally with Docker Compose

### Prerequisites

- Docker & Docker Compose installed

### Commands

```bash
# Clone the repository
git clone https://github.com/your-username/group6-capstone.git
cd group6-capstone

# Build and start all services
docker-compose up --build
```

- Frontend: http://localhost:3000
- Backend API: http://localhost:5000/api/groupmembers

---

## 🛠️ API Endpoint

- `GET /api/groupmembers`  
  Returns a list of group member names.

```json
{
  "groupMembers": ["Bolade", "Felix", "Idowu", ...]
}
```

---

## 🔍 Example Use Case

Search for a name like “Peace” using the search bar. If the name exists in Group 6, you'll get a confirmation message.

---

## 🤝 Group Members

- **Felix**
- **Idowu**
- **James**
- **Agape**
- **Oyerinde**
- **John**
- **Folashade**
- **Ifeoluwa**
- **Paul**
- **Peter**
- **Peace**
- **Esther**
- **Covenant**
- **Hassan**
- **Ingrid**

---

## 📄 License

This project is for educational purposes only.

---

## 📬 Contact

For questions or suggestions, please send an email to boladeadeyemi@gmail.com
