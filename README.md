# RfTelegramBot
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Database](https://img.shields.io/badge/MongoDB-Enabled-green?logo=mongodb)
![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)

This guide focuses on the installation, configuration, and execution of the RfTelegramBot.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

1.  **Python 3.11+**
2.  **MongoDB Server** (Must be installed and running locally or accessible remotely)
3.  **Git**

## 🛠 Installation

### 1. Clone the repository
```bash
git clone https://github.com/qloops/RfTelegramBot.git
cd RfTelegramBot
```

### 2. Set up a Virtual Environment
It is recommended to use a virtual environment to isolate dependencies.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
This project uses `pyproject.toml`. Choose the installation mode that fits your needs:

**Option A: Development Mode (Recommended)**
Installs the project in "editable" mode along with development tools (like Black).

```bash
pip install -e ".[dev]"
```
**Option B: Production Mode**
Installs only the core dependencies required to run the bot.
```bash
pip install .
```

## ⚙️ Configuration

1.  **Create the environment file**
    Copy the example file to a new `.env` file:

    ```bash
    # Windows (CMD)
    copy .env.example .env
    ```
    ```bash
    # Linux/macOS
    cp .env.example .env
    ```

2.  **Edit `.env`**
    Open the `.env` file and fill in the required variables:

    ```ini
    # Telegram App Configuration (https://my.telegram.org)
    API_ID=YOUR_API_ID
    API_HASH=YOUR_API_HASH

    # Bot Configuration (from @BotFather)
    BOT_TOKEN=YOUR_BOT_TOKEN
    BOT_USERNAME=@YOUR_BOT_USERNAME

    # Game Settings
    BOT_GAME_ID=0123456789

    # Database Configuration
    DB_NAME=rf_bot_db
    DB_HOST=localhost
    DB_PORT=27017

    # Logging
    CONSOLE_LOG_LEVEL=INFO
    FILE_LOG_LEVEL=INFO
    ```

## 🚀 Running the Bot

1.  Ensure your **MongoDB** service is up and running.
2.  Start the application:

```bash
python main.py
```

## 🎨 Code Formatting

This project enforces code style using **Black**.
Before committing changes, please run the formatter:

```bash
black .
```