import json
import sqlite3
import os

def main(event, context):
    # Path to the database file
    db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'quiz.db')

    # Connect to the SQLite database
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Fetch all questions from the database
    cursor.execute('SELECT id, question, options, correct_option, points FROM questions')
    rows = cursor.fetchall()

    # Format the data as JSON
    questions = []
    for row in rows:
        question = {
            "id": row[0],
            "question": row[1],
            "options": json.loads(row[2]),  # Convert JSON string back to list
            "correctOption": row[3],
            "points": row[4]
        }
        questions.append(question)

    # Close the database connection
    connection.close()

    # Create the response
    response = {
        "statusCode": 200,
        "body": json.dumps({"questions": questions}),
        "headers": {
            "Content-Type": "application/json"
        }
    }

    return response
