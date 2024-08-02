import sqlite3
import serial

# Establish serial connection to Arduino
ser = serial.Serial('COM3', 9600)  # Adjust COM port as needed

def authenticate_fingerprint():
    print("Waiting for fingerprint...")
    while True:
        if ser.in_waiting > 0:
            fingerprint_id = ser.readline().decode().strip()
            return int(fingerprint_id)

def get_user_by_fingerprint(fingerprint_id):
    conn = sqlite3.connect('atm_system.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE id=?', (fingerprint_id,))
    user = c.fetchone()
    conn.close()
    return user

def main():
    fingerprint_id = authenticate_fingerprint()
    user = get_user_by_fingerprint(fingerprint_id)
    
    if user:
        print(f"Welcome, {user[1]}")
        print(f"Your balance is: ${user[3]}")
        # Add further operations like withdrawal or deposit here
    else:
        print("User not found!")

if __name__ == "__main__":
    main()
