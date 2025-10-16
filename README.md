# REA - One Stop Mentoring Solutions

**Tagline:** A fullstack mentoring platform with emotion detection, NLP-powered diary analysis, and real-time mentor interactions.

---

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [Contact](#contact)

---

## About the Project
REA is a Python Django fullstack application designed to provide comprehensive mentoring solutions.  
It allows mentees to:  
- Write diary entries analyzed by **Emotion detection** and **NLP** for sentiment understanding.  
- Chat and **video call** with mentors in real-time.  
- Receive **daily motivational quotes** from mentors they follow.  

Mentors can:  
- Track mentees’ emotional progress.  
- Send daily inspirational messages.  
- Engage directly through chat and video calls.

This platform aims to support both personal and professional growth through technology-driven mentoring.

---

## Features
- **Diary Emotion Analysis:** Sentiment detection using NLP on diary entries.  
- **Real-time Chat:** Connect with mentors seamlessly.  
- **Video Calls:** One-on-one video sessions with mentors.  
- **Daily Motivational Quotes:** Mentors can send inspiring messages to their mentees.  
- **User & Mentor Dashboard:** Track progress, interactions, and received insights.

---

## Tech Stack
- **Backend:** Python, Django  
- **Frontend:** HTML , CSS , Javascript
- **Database:**  SQLite  
- **NLP & Emotion Detection:** NLTK , OpenCV , 
- **Real-time Communication:** Agora RTC SDK for real-time video call and chat  

---

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/REA-One-Stop-Mentoring-Solutions.git
cd REA-One-Stop-Mentoring-Solutions
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3.Install dependencies:
```bash
pip install -r requirements.txt
```

4.Setup Environment variable in .env
```bash
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
```

5.Apply migrations
```bash
python manage.py migrate
```

6.Run the development server
```bash
python manage.py runserver
```

## Usage
- Diary Entry: Navigate to the diary section and write your entry; emotions and sentiment are automatically analyzed.
- Chat / Video Call: Access the mentor dashboard to start a conversation or video session.
- Daily Quotes: Mentees receive motivational quotes automatically from mentors they follow.

## Screenshots
<img width="1901" height="855" alt="Screenshot 2024-02-20 212746" src="https://github.com/user-attachments/assets/1c3545e8-1bfc-4fb9-9672-52f6741b8c5a" />
<img width="1903" height="871" alt="Screenshot 2024-02-20 213015" src="https://github.com/user-attachments/assets/afe970d6-307c-4b78-aee2-8e5b642a9c44" />
<img width="1898" height="861" alt="Screenshot 2024-02-20 213051" src="https://github.com/user-attachments/assets/0c283cbd-65b8-4f4a-a6b0-e7fa6c8a81f7" />
<img width="1900" height="862" alt="Screenshot 2024-02-28 155602" src="https://github.com/user-attachments/assets/03ccc51c-435d-4c96-87e8-31becced2550" />

## Contributing
Contributions are welcome! Please follow these steps:
1. **Fork the repository**
2. **Create a new branch (git checkout -b feature/YourFeature)**
3. **Commit your changes (git commit -m 'Add some feature')**
4. **Push to the branch (git push origin feature/YourFeature)**
5. **Open a Pull Request**

## Contact
- **Author:** Abhijith P V

- **Email:** abhijithsreejith04@gmail.com

- **GitHub:** https://github.com//Abhijith-04-ops




