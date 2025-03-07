# Test Data Ingestion Process

## Overview
This project is a Python FastAPI backend with a Vue.js frontend, designed to ingest and display structured data from an external API. It pulls data, processes and stores it in a MySQL database, and provides an interface to view and sync records. Your task is to diagnose an issue preventing data ingestion, analyze the system for potential improvements, and propose fixes where needed.

## Your Assignment
Your primary task is to identify and resolve an issue that has recently caused the system to break. Specifically:

1. Diagnose the Data Ingestion Failure
   - The system pulls data from an external API, but something has changed upstream, preventing the system from working.
   - Your goal is to identify the issue and restore functionality.

2. Analyze the System for Improvements
   - While working on the bug, take note of any other potential issues.
   - If you identify areas that need improvement, document them and propose solutions.

3. Refactor Where Necessary
   - Improve data flow, error handling and API response processing.
 
4. Ensure the Frontend Works Properly
   - The Vue.js frontend should correctly display the records from the database.
   - A button should allow users to sync data from the external API.
   - If there are UI issues or API failures, troubleshoot and fix them.

## How to Approach This
Instead of telling you exactly what’s wrong, we encourage you to think like an engineer and investigate. Here’s how you should proceed:

- Start by running the project to observe its behavior.
- Check API responses, logs, and errors to locate the data ingestion issue.
- Consider edge cases—what happens if the external API changes unexpectedly?
- Analyze the system beyond the immediate bug—can you identify security flaws, architectural problems?
- Propose and if time permits implement solutions where needed.

## Setup Instructions

### 1. Prerequisites
- Docker & Docker Compose installed
- Node.js installed

### 2. Clone the Repository
git clone https://github.com/dartmouth-itc/tu-online-services-test-data-ingestion-process.git  
cd test-data-ingestion-process  

### 3. Start the Application
docker-compose up --build -d  

### 4. Access the Services
Backend (FastAPI API docs): http://localhost:8072/docs  
Frontend (Vue.js app): http://localhost:8073  
Nginx Proxy (Frontend + API): http://localhost:8074  
Adminer (Database UI): http://localhost:8075  

### 5. Test the System
- Open http://localhost:8073 and click Sync Data.  
- If errors occur, investigate backend logs:  
  docker-compose logs backend  
- Review API responses in FastAPI docs: http://localhost:8072/docs  

## Submission Guidelines
- Provide a summary of your debugging process—what was broken and how you fixed it.
- Document any additional improvements you made and why.

## Evaluation Criteria
We are evaluating your ability to:
- Diagnose and fix the API failure.
- Analyze the project and implement or suggest improvements that follow best practices.


We are not looking for perfection, but rather how you approach problem-solving and software design. Good luck!
