from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
from datetime import datetime
import uuid

app = FastAPI()

# In-memory data storage (for simplicity)
triggers = {}
event_logs = []

# Scheduler
scheduler = BackgroundScheduler()
scheduler.start()

# Models
class Trigger(BaseModel):
    id: str = None
    type: str  # "scheduled" or "api"
    time: datetime = None  # For scheduled triggers
    description: str

@app.post("/triggers/")
def create_trigger(trigger: Trigger):
    trigger.id = str(uuid.uuid4())
    triggers[trigger.id] = trigger.dict()

    # Add to scheduler if it's a scheduled trigger
    if trigger.type == "scheduled" and trigger.time:
        scheduler.add_job(
            lambda: log_event(trigger.id),
            trigger=DateTrigger(run_date=trigger.time)
        )
    return {"message": "Trigger created", "trigger": trigger}

@app.get("/triggers/")
def list_triggers():
    return {"triggers": list(triggers.values())}

@app.delete("/triggers/{trigger_id}")
def delete_trigger(trigger_id: str):
    if trigger_id in triggers:
        del triggers[trigger_id]
        return {"message": "Trigger deleted"}
    raise HTTPException(status_code=404, detail="Trigger not found")

@app.post("/fire-trigger/{trigger_id}")
def fire_trigger(trigger_id: str):
    if trigger_id in triggers:
        log_event(trigger_id)
        return {"message": "Trigger fired manually"}
    raise HTTPException(status_code=404, detail="Trigger not found")

@app.get("/logs/")
def get_logs():
    return {"logs": event_logs}

def log_event(trigger_id: str):
    if trigger_id in triggers:
        event_logs.append({
            "id": str(uuid.uuid4()),
            "trigger_id": trigger_id,
            "timestamp": datetime.now(),
            "description": triggers[trigger_id]["description"]
        })
