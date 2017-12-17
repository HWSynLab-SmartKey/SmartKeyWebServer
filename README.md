# Smart Key for Smart Home - Webserver

หน้าเว็บไซต์ของโปรเจค Smart Key สามารถลงทะเบียนและจัดการประตูบ้านได้
ตามที่มีสิทธิ์ โดยมี admin account จัดการ user ต่างๆ ได้ด้วย

## Installation

- ติดตั้ง Python 3
- Add Path Python `<path to python>\Scripts`
- `pip install virtualenv`
- ไปที่โฟลเดอร์ที่ clone project มา
- `virtualenv env`
- `.\env\Scripts\activate` ถ้ารันไม่ได้ให้เปิด Powershell ด้วย Admin
- `Get-Command pip` -> `<project folder>\Scripts\pip.exe`
- `pip install -r requirements.txt`
- `python app.py runserver`
- Go to http://localhost:5000
- ถ้าต้องลงอะไรเพิ่ม พอลงเสร็จแล้วให้เรียกคำสั่ง `pip freeze > requirements.txt` ด้วย

Reference: https://medium.com/@perwagnernielsen/getting-started-with-flask-login-can-be-a-bit-daunting-in-this-tutorial-i-will-use-d68791e9b5b5
