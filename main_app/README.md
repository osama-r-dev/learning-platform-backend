Description

This repository contains the frontend of an internal learning platform designed for organizations or teams that want to foster continuous learning and knowledge sharing among employees.
Unlike public platforms such as Coursera or Udemy, this system is intended for internal use, where employees can create and share short, skill-based learning materials — such as courses or tutorial videos — with their colleagues. The frontend is built using React and communicates with a Django REST API on the backend. It handles user interaction, course management, profile editing, and data fetching using authenticated API requests.

Teck stack
Backend: Python, Django, PostgreSQL, Postman
Frontend: CSS, React, HTML
Dev Tools: Git, Github

Frontend Repo link:
https://github.com/osama-r-dev/learning-platform-frontend

Installtion steps:

1. clone repo:

Frontend:
git clone git@github.com:osama-r-dev/learning-platform-frontend.git

Backend:
git clone git@github.com:osama-r-dev/learning-platform-backend.git

2. install

pipenv install

3. Start the backend server:
   python manage.py runserver

4. cd into:
   learning-platform-frontend

5. start React development server
   npm run dev

ERD Diagram:

![ERD](assets/images/learn_share_ERD.drawio.svg)

Routing Table:

![alt text](image.png)

Features I plan to add in the feature

- Achievements and badges for completing courses.

- Leaderboards or skill levels.

- In-app chat between employees.

- Analytics dashboard for course performance.

- Improved UI/UX
