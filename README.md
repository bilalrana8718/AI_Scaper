# AI Web Scraper Project

This project is an AI-powered web scraping tool with a user-friendly interface built using Streamlit. The tool extracts data from various websites, allowing users to analyze and visualize the scraped information in real-time.

## Features
- **Easy-to-use interface**: A Streamlit-based web app for simple navigation.
- **Automated scraping**: Uses AI-based methods for efficient and intelligent web scraping.
- **Real-time data processing**: View and analyze scraped data instantly.

---

## Prerequisites

1. **Python**: Make sure Python 3.6 or higher is installed on your machine.
2. **Google Chrome**: Required to run the ChromeDriver.
3. **ChromeDriver**: Ensure you have the latest version of ChromeDriver installed and that it's compatible with your Chrome browser version. 
   - [Download ChromeDriver here](https://googlechromelabs.github.io/chrome-for-testing/#stable).

---

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/bilalrana8718/AI_Scaper.git
    cd ai-web-scraper
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Download and set up ChromeDriver**:
   - Place ChromeDriver in your project directory or add it to your system path.

6. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

---

## Usage

1. **Start the app**:
   After running the above command, Streamlit will provide a local URL (e.g., http://localhost:8501). Open this link in your browser.

2. **Interact with the Web Scraper**:
   Use the provided input fields to specify the target website and any relevant parameters for the AI-powered scraper.

---

