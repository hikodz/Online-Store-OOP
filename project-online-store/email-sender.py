import smtplib
from random import randint
sender = "medbloul2002@gmail.com"
resiver = "bloulmohamed2002@gmail.com"
password = "raqxaazztghlnxzf"
massege = f"""
Dear Client

Thank you for choosing to enhance your online security with us. As requested, here is your verification code: {randint(10000,50000)}.

Please enter this code in the designated field on our website to complete your verification process. This step ensures that only authorized users like you can access your account.

If you did not initiate this verification or need assistance, please contact our support team immediately at [Customer Support Email] or [Customer Support Phone Number].

Stay secure and thank you for being a valued member of our community.

Best regards,
Codezilla online store"""
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
print("accsses")
server.sendmail(sender, resiver, massege)
print("accsses")