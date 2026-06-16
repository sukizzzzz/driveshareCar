# DriveShare: Peer-to-Peer Car Rental Platform

DriveShare is a desktop-based car rental application built with Python and Tkinter, inspired by Turo. It allows vehicle owners to list their cars and manage availability, while renters can search, book, and pay for rentals. This project was developed for CIS 476 at the University of Michigan–Dearborn.

## Features

- Role-based user system (Owner, Renter, or Both)
- Vehicle listing with availability scheduling
- Search, booking, and payment functionality
- In-app messaging between renters and car owners
- Password recovery using security questions
- Booking conflict prevention
- Review system and rental history tracking

## Design Patterns Used

Singleton, Observer, Mediator, Builder, Proxy, Chain of Responsibility

## Setup Instructions

```bash
# Clone the repository
git clone https://github.com/sukizzzzz/driveshareCar.git

# Navigate into the project directory
cd driveshareCar

# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Git Bash)
source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
'''

## Stack
Python 3.11 · Tkinter · SQLite · bcrypt · tkcalendar

## Team
Ayat Mohamed
Tamani Almaweri
Zaynab Abdallah
