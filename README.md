# FastAPI Event Trigger Platform

This is a FastAPI-based platform for managing event triggers. The platform supports **scheduled triggers** and **API triggers**, allowing users to create, test, log, and manage event triggers efficiently.

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
   git clone {{repository-url}}
   cd {{project-name}}
