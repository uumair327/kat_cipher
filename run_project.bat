@echo off
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python main.py
pause
