# 🇯🇵 Animanage

## Open Source Anime Management Web API

### ⚙️ Installation

**1.** Create a new PostgreSQL user and grant all permissions.

**2.** Create a new postgreSQL Database.

**2.** Create the virtual environment using ```python3 -m venv .venv```

**3.** Activate the virtual environment using ```source .venv/bin/activate``` (MacOS/Linux) or ```.venv/bin/activate``` (Windows)

**4.** Install dependencies using ```pip install -r requirements.txt```

**5.** Set up both `.env` and `.flaskenv` files with desired information.

**6.** Create and seed tables `flask db create` and `flask db seed`.

**6.** Run application using ```flask run```. To stop the application use ***Ctrl + C***.

### 🧪 Testing & Usage

Using an API client such as Postman or Insomnia (My personal choice), import ***endpoints.json** to import all endpoints.

### 🖥️ System/Hardware Requirements

- No specific hardware requirements.
- Operating System: Compatible with any OS that can run Python 3 (e.g., Windows, macOS, Linux).
