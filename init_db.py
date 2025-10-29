import sqlite3, os

DB_PATH = "database/quiz.db"

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Users table
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Quizzes table
c.execute('''CREATE TABLE IF NOT EXISTS quizzes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    quiz_id INTEGER,
    topic TEXT,
    score INTEGER,
    total_questions INTEGER,
    taken_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
)''')


# Questions table
c.execute('''CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz_id INTEGER,
    question_text TEXT,
    option_a TEXT,
    option_b TEXT,
    option_c TEXT,
    option_d TEXT,
    correct_answer TEXT,
    user_answer TEXT,
    is_correct INTEGER,
    FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
)''')


conn.commit()
conn.close()
print("✅ Database initialized successfully!")
