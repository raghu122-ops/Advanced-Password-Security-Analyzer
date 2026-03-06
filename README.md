# Advanced Password Security Analyzer

### 🔐 Overview
This project is a professional web-based tool designed to evaluate password strength and detect if a password has been leaked in known data breaches. It helps users understand the mathematical security of their credentials.

### 🚀 Key Features
* **Strength Analysis:** Scores passwords based on length and character complexity.
* **Entropy Calculation:** Measures the unpredictability and randomness of the password.
* **Breach Detection:** Uses the HaveIBeenPwned API with SHA-1 hashing to check if the password is safe.
* **Crack Time Estimation:** Predicts how long it would take for a computer to guess the password.
* **Security Suggestions:** Provides real-time tips to improve password security.

### 🛠️ Tech Stack
* **Backend:** Python Flask
* **Frontend:** HTML5, CSS3, JavaScript
* **Security:** HIBP API (k-Anonymity model)

### 📂 Folder Structure
* `/static`: Contains CSS, JS, and background image.
* `/templates`: Contains the HTML interface.
* `app.py`: Main Flask application logic.
* `requirements.txt`: Project dependencies.

### 🔧 Installation & Usage
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Open `http://127.0.0.1:5000` in your browser.
5. Clone the repository:
   ```bash
   git clone [https://github.com/raghu122-ops/Advanced-Password-Security-Analyzer.git](https://github.com/raghu122-ops/Advanced-Password-Security-Analyzer.git)
