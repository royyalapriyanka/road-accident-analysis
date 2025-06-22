import mysql.connector
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",           # your MySQL username
    password="Priyanka@123",   # your MySQL password
    database="AccidentTables"     # your MySQL DB name
)
cursor = conn.cursor()

# Function to insert data
def insert_accident(date, time, location, cause, severity):
    query = "INSERT INTO accidents (accident_date, accident_time, location, cause, severity) VALUES (%s, %s, %s, %s, %s)"
    data = (date, time, location, cause, severity)
    cursor.execute(query, data)
    conn.commit()
    print("Accident added.")

# Function to view data
def view_accidents():
    cursor.execute("SELECT * FROM accidents")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Function to generate chart
def generate_chart():
    cursor.execute("SELECT cause, COUNT(*) FROM accidents GROUP BY cause")
    data = cursor.fetchall()
    causes = [row[0] for row in data]
    counts = [row[1] for row in data]

    plt.bar(causes, counts, color='skyblue')
    plt.title("Accidents by Cause")
    plt.xlabel("Cause")
    plt.ylabel("Number of Accidents")
    plt.savefig("accident_chart.png")
    plt.show()

# Function to generate report
def generate_html_report():
    cursor.execute("SELECT * FROM accidents")
    rows = cursor.fetchall()

    with open("report.html", "w") as f:
        f.write("<html><head><link rel='stylesheet' href='style.css'></head><body>")
        f.write("<h1>Accident Report</h1>")
        f.write("<img src='accident_chart.png' width='500'><br><br>")
        f.write("<table><tr><th>ID</th><th>Date</th><th>Time</th><th>Location</th><th>Cause</th><th>Severity</th></tr>")
        for row in rows:
            f.write(f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td></tr>")
        f.write("</table></body></html>")
    print("Report generated.")
# Insert some test data
insert_accident('2025-06-21', '10:30:00', 'Hyderabad', 'Pothole', 'Minor')
insert_accident('2025-06-21', '12:15:00', 'Secunderabad', 'Overspeeding', 'Major')
insert_accident('2025-06-22', '09:45:00', 'Vizag', 'Drunk driving', 'Fatal')
insert_accident('2025-06-23', '14:00:00', 'Vijayawada', 'Signal jump', 'Minor')

# View the data
view_accidents()

# Generate chart
generate_chart()

# Generate HTML report
generate_html_report()
