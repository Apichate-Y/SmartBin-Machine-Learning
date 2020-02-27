# SmartBin-Machine-Learning
- เป็นส่วนหนึ่งของรายวิชา 523496 โครงงานวิศวกรรมคอมพิวเตอร์ 2
- เป็น model ที่แบ่งแยกลักษณะ ขยะรีไซเคิลได้และรีไซเคิลไม่ได้ สร้างโดยใช้หลักการ Convolutional Neural Network (CNN) หรือ โครงข่ายประสาทแบบคอนโวลูชัน 
- มีข้อมูลทั้งหมด 422 ภาพ แบ่งเป็นภาพที่ใช้สำหรับ train 266 ภาพ และ test 156 ภาพ
- train ขยะรีไซเคิลได้ 126 ภาพ, ขยะรีไซเคิลไม่ได้ 140 ภาพ
- test ขยะรีไซเคิลได้ 72 ภาพ, ขยะรีไซเคิลไม่ได้ 84 ภาพ

# Create a new Conda virtual environment
```
conda create -n smartbin pip python=3.6
activate smartbin
```
# Install Modules
```
pip install -r requirements.txt
```

# Server RUN
```
- cd server
- python App-Server.py
```

# SmartBin RUN
```
- cd server
- python Request-Server.py
```
