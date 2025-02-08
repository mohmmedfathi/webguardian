# WebGuardian
[![LinkedIn][linkedin-shield]][linkedin-url]
[![MIT License][license-shield]][license-url]

<br />
<div>

<h3 align="center">WebGuardian</h3>

  <p align="center">
    Enhancing online safety and accessibility
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
WebGuardian is a powerful web application dedicated to enhancing online safety and accessibility. It empowers users—especially those who are blind or visually impaired—by transforming spoken content into actionable insights. Through advanced audio processing and immediate, audible feedback on web address safety, WebGuardian helps users navigate the internet securely and confidently.

## Features

- **Audio Processing:** Converts uploaded audio files into text using state-of-the-art speech-to-text technology. This hands-free approach is specifically designed to assist blind and visually impaired users in interacting with online content.
- **URL Safety Check:** Leverages the VirusTotal API to evaluate URLs for potential security risks, ensuring that users are informed about the trustworthiness of web addresses.
- **Text-to-Speech Feedback:** Provides clear, audible feedback on the URL’s safety status via gTTS, delivering an accessible user experience through sound.
- **User-Friendly Web Interface:** Offers an intuitive interface for both audio uploads and direct URL entry, ensuring effortless navigation and usage.

## Built With

* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
* ![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-blue?style=for-the-badge)
* ![pydub](https://img.shields.io/badge/pydub-yellow?style=for-the-badge)
* ![gTTS](https://img.shields.io/badge/gTTS-red?style=for-the-badge)
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
2. You have two main options:
    - **Upload an Audio File:**
        - Select an audio file and upload it. WebGuardian will:
            - Transcribe the spoken content into text.
            - Extract any URL mentioned in the audio.
            - Analyze the URL's safety using the VirusTotal API.
            - Provide clear, audible feedback (e.g., *"هذا الموقع امن"* or *"احترس الموقع ضار"*) via gTTS.
    - **Direct URL Entry:**
        - Enter a URL directly into the provided field.
        - WebGuardian will immediately check its safety and display the results on-screen along with audible feedback.

### Example Scenario:
Imagine you upload an audio clip in which someone says, *"Please check out https://www.google.com."* WebGuardian will:

1. Transcribe the audio into text.
2. Extract and clean the URL from the text.
3. Submit the URL to the VirusTotal API for safety analysis.
4. Return a detailed safety report and generate an audible message informing you whether the site is safe or if caution is advised.

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
