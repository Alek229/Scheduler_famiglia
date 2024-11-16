import sqlite3
import schedule
import time
from datetime import datetime

DB_FILE = 'birthdays.db'

def send_birthday_reminders():
    """Check today's birthdays and send reminders."""
    today = datetime.utcnow().strftime("%m-%d")  # Get today's date in MM-DD format
    print(f"DEBUG (Scheduler): Checking birthdays for today: {today}")

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM birthdays WHERE strftime('%m-%d', birthday) = ?", (today,))
        today_birthdays = [row[0] for row in cursor.fetchall()]

        # Simulate sending reminders
        if today_birthdays:
            print(f"🎉 Today's Birthdays: {', '.join(today_birthdays)}! 🎂 Don't forget to celebrate!")
        else:
            print("DEBUG (Scheduler): No birthdays to notify at this moment.")

def schedule_reminders():
    """Schedule the reminder function to run every 3 minutes."""
    print("DEBUG (Scheduler): Scheduler started to send reminders every 3 minutes.")
    schedule.every(3).minutes.do(send_birthday_reminders)

    while True:
        schedule.run_pending()
        print("DEBUG (Scheduler): Running scheduled jobs...")
        time.sleep(1)



@app.route("/add_sample", methods=["GET"])
def add_sample():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO birthdays (name, birthday) VALUES (?, ?)", ("John", "2024-11-16"))
        conn.commit()
    return "Sample birthday added for testing!"


if __name__ == "__main__":
    # Start the scheduler
    print("DEBUG (Scheduler): Starting scheduler script...")
    schedule_reminders()
