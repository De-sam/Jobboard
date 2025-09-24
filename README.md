# Job Board Backend – ProDev BE

A backend system for a modern **Job Board Platform**, designed as part of the **ProDev Backend (BE) Case Study**.
This project demonstrates building **robust APIs**, **role-based access control**, and **optimized data retrieval** for large-scale applications.

---

## 🚀 Overview

This backend powers a job board with support for:

* **Job postings management** (create, update, delete, search jobs)
* **Role-based access** (admins, recruiters, job seekers)
* **Applications and categories**
* **Optimized search queries** with indexing
* **Comprehensive API documentation** using Swagger

---

## 🎯 Project Goals

1. **API Development**

   * Endpoints for job postings, categories, and applications
2. **Access Control**

   * Secure role-based authentication with JWT
   * Admins manage jobs & categories
   * Users apply for jobs
3. **Database Efficiency**

   * Indexing for faster job search and filtering
   * Optimized queries for location & category

---

## 🛠️ Technologies Used

| Technology     | Purpose                                        |
| -------------- | ---------------------------------------------- |
| **Django**     | High-level Python web framework                |
| **PostgreSQL** | Relational database for storing job board data |
| **JWT**        | Secure role-based authentication (SimpleJWT)   |
| **Swagger**    | API documentation hosted at `/api/docs`        |

---

## ✨ Key Features

* **Job Posting Management**

  * APIs to create, update, delete, and fetch jobs
  * Categorization by industry, location, and job type

* **Role-Based Authentication**

  * Admins: full management access
  * Users: apply for jobs, manage applications

* **Optimized Job Search**

  * Indexed queries for speed
  * Location-based and category-based filtering

* **API Documentation**

  * Swagger/OpenAPI documentation at `/api/docs`

---

## 🏗️ Implementation Process

### Git Commit Workflow

* **Initial Setup**

  ```
  feat: set up Django project with PostgreSQL
  ```
* **Feature Development**

  ```
  feat: implement job posting and filtering APIs
  feat: add role-based authentication for admins and users
  ```
* **Optimization**

  ```
  perf: optimize job search queries with indexing
  ```
* **Documentation**

  ```
  feat: integrate Swagger for API documentation
  docs: update README with usage details
  ```

---

## 📦 Installation & Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/jobboard-backend.git
   cd jobboard-backend
   ```

2. **Create virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create `.env`:

   ```
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgres://user:password@localhost:5432/jobboard
   DEBUG=True
   ```

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Start server**

   ```bash
   python manage.py runserver
   ```

---

## 🔑 API Endpoints

### Auth

* `POST /api/auth/signup/` – Register user
* `POST /api/auth/token/` – Obtain JWT
* `POST /api/auth/token/refresh/` – Refresh JWT

### Jobs

* `GET /api/jobs/` – List jobs
* `POST /api/jobs/` – Create job (admin)
* `PUT /api/jobs/{id}/` – Update job (admin)
* `DELETE /api/jobs/{id}/` – Delete job (admin)

### Applications

* `POST /api/jobs/{id}/apply/` – Apply to job (user)

### Docs

* `GET /api/docs/` – Swagger API docs

---

## 🚀 Deployment

* Deploy Django app to **Render**, **Heroku**, or **AWS EC2**
* Use **PostgreSQL** hosted on AWS RDS/Render
* Serve Swagger docs at `/api/docs`

---

## ✅ Evaluation Criteria

* **Functionality**: job & category CRUD + role-based auth works
* **Code Quality**: modular, clean Django patterns
* **Performance**: indexed queries ensure fast search
* **Documentation**: detailed Swagger + this README

---

## 📌 Submission Details

* **Deliverables**: hosted API + Swagger docs + source repo
* **Deadline**: as per ProDev BE milestone schedule
