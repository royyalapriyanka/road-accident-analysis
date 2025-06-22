# 🚗 Road Accident Analysis Report

An interactive full-stack project for visualizing and analyzing road accident data using HTML, CSS, JavaScript, MySQL, and Python.

## 📊 Features

- Bar chart of accident counts by city (Chart.js)
- Search accidents by location
- Filter data by accident severity (Minor, Major, Fatal)
- Python script to insert and retrieve accident records
- MySQL database for structured storage
- Auto-generated HTML report from Python
- Clean and responsive frontend design

---

## 🖥️ Technologies Used

- HTML, CSS, JavaScript
- Chart.js (for graphs)
- Python (for data handling & report generation)
- MySQL (for backend database)

---

## 📁 Project Structure

road-accident-analysis/
├── report.html # Main interactive web report
├── style.css # CSS for styling the table
├── accident_chart.png # Chart image used in HTML
├── README.md # Project documentation
├── AccidentTables.sql # SQL script to create the DB and table
├── accident_data.py # Python script for inserting data & generating report

---

## 🔧 Setup Instructions

### 💽 1. Set Up MySQL Database

Run this in your MySQL client:
```sql
SOURCE AccidentTables.sql;

2. Run the Python Script
Make sure MySQL is running and update credentials if needed in accident_data.py:

bash
Copy code
python accident_data.py

This will:

Insert sample data

Generate a chart

Create a new report.html

3. Open the Web Dashboard
Simply open report.html in your browser to see the interactive accident report.

## Author

**Royyala Priyanka**  
🔗 [GitHub](https://github.com/royyalapriyanka)  
🔗 [LinkedIn](https://linkedin.com/in/royyala-priyanka108)

