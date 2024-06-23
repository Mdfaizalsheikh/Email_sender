import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox

def send_email():
    
    sender_email = sender_entry.get()
    sender_password = password_entry.get()
    recipient_email = recipient_entry.get()
    subject = subject_entry.get()
    message = message_entry.get("1.0", tk.END)

    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")


root = tk.Tk()
root.title("Email Sender")


tk.Label(root, text="Sender Email:").grid(row=0, column=0, padx=10, pady=5)
sender_entry = tk.Entry(root, width=50)
sender_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*", width=50)
password_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Recipient Email:").grid(row=2, column=0, padx=10, pady=5)
recipient_entry = tk.Entry(root, width=50)
recipient_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Subject:").grid(row=3, column=0, padx=10, pady=5)
subject_entry = tk.Entry(root, width=50)
subject_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Message:").grid(row=4, column=0, padx=10, pady=5)
message_entry = tk.Text(root, height=10, width=50)
message_entry.grid(row=4, column=1, padx=10, pady=5)


send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.grid(row=5, column=1, pady=10)


root.mainloop()

