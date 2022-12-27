from email import message
import smtplib
email_list=["email1","email2"]
credentials={"email:Your email id here,password:Your password here"}
for email_id in email_list:
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(credentials["email"],credentials["password"])
    message="Message you nees to send"
    s.sendmail(credentials['email'],email_id,message)
    s.quit()