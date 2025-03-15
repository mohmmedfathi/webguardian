# WebGuardian
[![LinkedIn][linkedin-shield]][linkedin-url]
[![MIT License][license-shield]][license-url]

<br />
<div>

<h3 align="center">WebGuardian</h3>

  <p align="center">
    Enhancing online safety
  </p>
</div>

[![Watch the video](https://github.com/user-attachments/assets/69911f1c-f7de-4f23-8802-dbbc69d38ad9)](https://drive.google.com/file/d/1fV151JJKRNyRfwEf4Bk28pT4ua3vu6Fl/view?usp=sharing)


## About The Project
WebGuardian is a powerful web application dedicated to enhancing online safety. By leveraging the VirusTotal API, it provides real-time security evaluations of web addresses, empowering users to navigate the internet securely and confidently.

## Features
- **URL Safety Check: Evaluates URLs for potential security risks using the VirusTotal API.**

- **Detailed Threat Analysis: Displays malicious, harmless, and suspicious source counts.**

- **User-Friendly Interface: Intuitive design for seamless URL validation.**


## Built With

* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
* ![VirusTotal API](https://img.shields.io/badge/VirusTotal-API-green?style=for-the-badge)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python <= 3.10.6
* Pip <= 22.0.2
* Python virtual environment

1. Clone the repo
   ```sh
   git clone https://github.com/mohmmedfathi/WebGuardian.git
   cd WebGuardian
   ```
2. Create virtual environment
   ```sh
   python3 -m venv venv
   ```
3. Activate virtual environment
   ```sh
   source venv/bin/activate
   ```
4. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
5. Configure Environment Settings:
   - Update your configuration (add your VirusTotal API key) in your Django settings or environment variables.
6. Apply Migrations:
   ```sh
   python manage.py migrate
   ```
7. Run server:
   ```sh
   python manage.py runserver
   ```

## Usage

### Via the Web Interface:
1. Open your browser and navigate to `http://127.0.0.1:8000/`.
2. Enter a URL in the input field.

3. View the safety analysis:

    - Safe: Green alert with harmless source count.

    - Dangerous: Red alert with malicious/suspicious counts.
      

### Example Scenario:
Enter *https://www.google.com* to see:

Safety status (Safe/Dangerous)

Breakdown of harmless, malicious, and suspicious sources

<!-- CONTACT -->
## Contact

Mohammed Fathi - mohmmedfathi.123@gmail.com

Project Link: [https://github.com/mohmmedfathi/WebGuardian](https://github.com/mohmmedfathi/WebGuardian)

<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mohammed-fathi-4a08071a7/
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://docs.djangoproject.com/en/3.2/
[Python]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://docs.python.org/3/
