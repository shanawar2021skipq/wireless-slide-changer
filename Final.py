import socket,json,math 
import time,pyautogui as p
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller
import time,autopy
from selenium import webdriver
mouse = Controller()

#keyboard = Controller()
s = socket.socket()         
x1 = 0
x2 = 0
x3 = 0
x4 = 0
y1 = 0
y2 = 0
y3 = 0
y4 = 0
count = 0
p.FAILSAFE = False # set failsafe for manual exit

screenWidth, screenHeight = p.size()
s.bind(('0.0.0.0', 13784))
s.listen(0)                 

while True:
 
    client, addr = s.accept()
 
    while True:
        content = client.recv(1024)
        
        if len(content) ==0:
           break
        else:
          # print(content)
            
           c=json.loads(content)
           Ax=float(c['Ax'])
           Ay=float(c['Ay'])
           Az=float(c['Az'])
           accTilt1 = math.atan2(Ax, Az)*180/math.pi
           accTilt2 = math.atan2(Ay, Az)*180/math.pi
           x4 = x3;
           x3 = x2;
           x2 = x1;
           x1 = accTilt1;
           x = (x4+x3+x2+x1)/4
           y4 = y3;
           y3 = y2;
           y2 = y1;
           y1 = accTilt2;
           y = (y4+y3+y2+y1)/4
           
           xn = x*10+screenWidth/2
           yn = 1*y*9+screenHeight/2  
          
          # p.moveTo(xn,yn)
          # mouse.position=(xn,yn)
           T=float(c['T'])
           st=str(content)
           fs=int(st[-4])
           back=int(st[-12])
           next=int(st[-20])
           lms=int(st[-28])
           off=int(st[-36])  # D3
           print('fs,back,next,lms,off,T,Ax,Ay,Az : ',fs,back,next,lms,off,T,Ax,Ay,Az)
           
           if(next==1):
               p.press('down')
           if(off==0):
               p.press('f5') 
               #keyboard.press(Key.down)
           if(back==1):
               #keyboard.press(Key.up)
               p.press('up')
               
           if(next==1&back==1):
                p.press('f5')
           if(fs==1):
               if(count == 0):
                   p.hotkey('win','=')
                   count = 1
               else:
                    try:
                      autopy.mouse.move(xn,yn)
                    except:
                      print('Mouse out of screen') 
           else:
                if(count == 1):
                   p.hotkey('win','esc')
                   autopy.mouse.click()
                   count = 0
                else:
                    pass
         
    #print("Closing connection")
    client.close()
