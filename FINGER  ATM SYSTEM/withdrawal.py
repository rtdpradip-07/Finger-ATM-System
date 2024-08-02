def withdraw_amount(user, amount):
    if user[3] >= amount:
        new_balance = user[3] - amount
        conn = sqlite3.connect('atm_system.db')
        c = conn.cursor()
        c.execute('UPDATE users SET balance=? WHERE id=?', (new_balance, user[0]))
        conn.commit()
        conn.close()
        print(f"Withdrawal successful! New balance: ${new_balance}")
    else:
        print("Insufficient funds!")

# In the main function
amount = float(input("Enter amount to withdraw: "))
withdraw_amount(user, amount)
