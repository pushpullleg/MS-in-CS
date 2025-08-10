project document including:

Problem Statement

Introduction

SVD (System/Software Vision Document)

Hardware and Software Requirements

Use Cases

User Stories

📄 Project Title: PantryPal – AI-powered WhatsApp Assistant for Pantry Management
🔍 Problem Statement
In today's busy lifestyle, managing household pantry items efficiently is often overlooked. Most people either overstock or run out of essential items due to lack of tracking. Traditional pen-and-paper methods or manual spreadsheet updates are time-consuming and error-prone.

There is a need for a conversational AI-based solution that allows users to interact naturally, manage inventory in real time, and access or update their pantry information on the go, especially via familiar platforms like WhatsApp.

📘 Introduction
PantryPal is a smart AI assistant built on WhatsApp that helps households keep track of their pantry inventory through natural conversation. Integrated with a dynamic backend (an Excel or Google Sheet), PantryPal can:

Answer queries like "Do we have milk left?"

Record updates like "I just bought 2kg rice"

Manage stock levels collaboratively (supports multi-user input)

It brings the power of AI and automation to everyday household management and supports both text-based updates and query responses via WhatsApp, making it extremely user-friendly and widely accessible.

🧭 SVD – System Vision Document
📌 Problem:
Lack of an intuitive, always-available solution to manage pantry stock collaboratively in real-time using common communication tools.

🎯 Solution:
A WhatsApp-integrated conversational AI agent that:

Reads from and writes to a pantry spreadsheet

Understands natural language using GPT

Identifies and manages multiple users (you and your wife)

Runs 24/7 and keeps pantry records updated

🌟 Benefits:
Easy inventory tracking

No need to open apps or spreadsheets manually

Prevents overbuying and understocking

Accessible from anywhere via WhatsApp

🖥️ Hardware & Software Requirements
🔧 Hardware Requirements:
PC or Laptop for development (Windows/macOS/Linux)

Smartphone with WhatsApp installed (for testing)

Optional: Cloud hosting server (for deployment)

💻 Software Requirements:
Component	Description
Python 3.x	Programming Language
Flask / FastAPI	Web framework for handling requests
OpenAI API	Natural language understanding
Twilio API	WhatsApp messaging platform
pandas/openpyxl	Excel handling
Google Sheets API (optional)	Spreadsheet sync
Git & GitHub	Version control & collaboration
Replit / Render / Railway	Deployment options
📊 Use Case Scenarios
Use Case ID	Name	Description
UC-01	Query Stock	User asks: "Do we have eggs?" and the system replies
UC-02	Add Item	User says: "Bought 1kg sugar" and the system updates stock
UC-03	Remove Item	System deducts quantities as items are consumed
UC-04	Multi-user Support	Wife and husband both update and query independently
UC-05	Summary View	User asks: “What do we need to restock?” and receives a list
👥 User Stories
👤 As Mukesh (the user),
I want to ask via WhatsApp whether we have a certain item in the pantry

So that I don't need to check manually before shopping

👤 As Mukesh's wife,
I want to update the pantry stock via text after grocery shopping

So that we stay in sync and avoid duplicating items

👤 As a family member,
I want to receive a summary of low-stock items

So that I know what needs to be purchased next

👤 As a developer,
I want the AI to extract item names, quantities, and units from free-text messages

So that the system can update the stock automatically without manual input
