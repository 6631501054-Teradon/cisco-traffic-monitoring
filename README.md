# Cisco R1 Real-time Traffic Monitoring Dashboard

โปรเจกต์ระบบมอนิเตอร์ Traffic บน Cisco Router (R1) แบบ Real-time โดยใช้ SNMP, Apache Kafka, Flask-SocketIO และ Chart.js

## 🛠️ Requirements & Prerequisites
- Docker & Docker Compose
- Python 3.10+
- Cisco Router (รัน SNMP Community `public`) หรือ GNS3 Environment

## 🚀 Quick Start (วิธีเริ่มใช้งาน)

### 1. Clone Repository
```bash
git clone <YOUR_GIT_REPOSITORY_URL>
cd cisco-kafka-automation
docker compose up -d
pip3 install -r requirements.txt --break-system-packages
python3 collector.py
python3 web_server.py
