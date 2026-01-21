# This code will insert a default username for me to use

from moodle_db import get_db_connection

def seed_user():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Check your create_tables.py for the exact column names, 
    # but usually it looks like this:
    try:
        cur.execute("""
            INSERT INTO users (email, password, first_name, last_name, role) 
            VALUES (%s, %s, %s, %s, %s)
        """, ("bbraniff@oakland.edu", "password123", "Ben", "Braniff", "1"))
        
        conn.commit()
        print("User created! You can now log in with: bbraniff@oakland.edu / password123")
    except Exception as e:
        print(f"Error seeding user: {e}")
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    seed_user()