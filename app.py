# app.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
import sqlite3
import os

app = FastAPI()

# Setup static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Database setup
DATABASE_URL = "sqlite:///./iot_home_automation.db"

# Data Models
class User(BaseModel):
    id: int
    name: str
    email: str
    role: str

class Device(BaseModel):
    id: int
    name: str
    status: str
    type: str

class AutomationRule(BaseModel):
    id: int
    name: str
    conditions: str
    actions: str

# Initialize the database
def init_db():
    conn = sqlite3.connect('iot_home_automation.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        role TEXT NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS devices (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        status TEXT NOT NULL,
                        type TEXT NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS automation_rules (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        conditions TEXT NOT NULL,
                        actions TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

# Seed the database with initial data
def seed_db():
    conn = sqlite3.connect('iot_home_automation.db')
    cursor = conn.cursor()
    # Seed Users
    cursor.execute('''INSERT INTO users (name, email, role) VALUES
                      ('John Doe', 'john@example.com', 'admin'),
                      ('Jane Smith', 'jane@example.com', 'user')
                      ON CONFLICT(email) DO NOTHING''')
    # Seed Devices
    cursor.execute('''INSERT INTO devices (name, status, type) VALUES
                      ('Living Room Light', 'on', 'light'),
                      ('Thermostat', 'off', 'thermostat')
                      ON CONFLICT(name) DO NOTHING''')
    # Seed Automation Rules
    cursor.execute('''INSERT INTO automation_rules (name, conditions, actions) VALUES
                      ('Turn off lights at midnight', 'time == 00:00', 'turn_off_lights'),
                      ('Turn on heating at 6 AM', 'time == 06:00', 'turn_on_heating')
                      ON CONFLICT(name) DO NOTHING''')
    conn.commit()
    conn.close()

# Initialize and seed the database
init_db()
seed_db()

# Routes
@app.get("/", response_class=HTMLResponse)
async def get_dashboard(request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/devices", response_class=HTMLResponse)
async def get_devices_page(request):
    return templates.TemplateResponse("devices.html", {"request": request})

@app.get("/automation", response_class=HTMLResponse)
async def get_automation_page(request):
    return templates.TemplateResponse("automation.html", {"request": request})

@app.get("/users", response_class=HTMLResponse)
async def get_users_page(request):
    return templates.TemplateResponse("users.html", {"request": request})

@app.get("/settings", response_class=HTMLResponse)
async def get_settings_page(request):
    return templates.TemplateResponse("settings.html", {"request": request})

@app.get("/api/devices", response_model=List[Device])
async def get_devices():
    conn = sqlite3.connect('iot_home_automation.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM devices")
    devices = cursor.fetchall()
    conn.close()
    return [Device(id=row[0], name=row[1], status=row[2], type=row[3]) for row in devices]

@app.post("/api/devices", response_model=Device)
async def add_device(device: Device):
    conn = sqlite3.connect('iot_home_automation.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO devices (name, status, type) VALUES (?, ?, ?)",
                   (device.name, device.status, device.type))
    conn.commit()
    device_id = cursor.lastrowid
    conn.close()
    return {"id": device_id, **device.dict()}

@app.get("/api/rules", response_model=List[AutomationRule])
async def get_rules():
    conn = sqlite3.connect('iot_home_automation.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM automation_rules")
    rules = cursor.fetchall()
    conn.close()
    return [AutomationRule(id=row[0], name=row[1], conditions=row[2], actions=row[3]) for row in rules]

@app.post("/api/rules", response_model=AutomationRule)
async def add_rule(rule: AutomationRule):
    conn = sqlite3.connect('iot_home_automation.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO automation_rules (name, conditions, actions) VALUES (?, ?, ?)",
                   (rule.name, rule.conditions, rule.actions))
    conn.commit()
    rule_id = cursor.lastrowid
    conn.close()
    return {"id": rule_id, **rule.dict()}

@app.get("/api/users", response_model=List[User])
async def get_users():
    conn = sqlite3.connect('iot_home_automation.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return [User(id=row[0], name=row[1], email=row[2], role=row[3]) for row in users]
