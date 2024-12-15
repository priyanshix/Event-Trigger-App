# FastAPI Event Trigger Platform

This is a FastAPI-based platform for managing event triggers. The platform supports **scheduled triggers** and **API triggers**, allowing users to efficiently create, test, log, and manage event triggers.

## Features

- **Scheduled Triggers**: Set one-time or recurring triggers at specific times.
- **API Triggers**: Trigger events via API calls.
- **Manual Testing**: Test triggers without saving them permanently.
- **Event Logging**: Logs events with details and archives them after 2 hours.
- **Trigger Management**: Create, view, edit, and delete triggers.
- **Automatic Cleanup**: Deletes events 48 hours after they are fired.

---

## Requirements

- Python 3.9 or higher
- FastAPI, Uvicorn, APScheduler

---

## Setup Instructions

### **Run Locally**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/priyanshix/Event-Trigger-App
   cd Event-Trigger-App
2. **Install Dependencies: Install the necessary dependencies for the project using pip:**
```bash
pip install -r requirements.txt
```

## Deployed Version: 
[Event Trigger Platform](https://segwise-px-39o2.onrender.com/docs)