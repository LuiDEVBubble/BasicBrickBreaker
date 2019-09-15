def setup():
    global x, speedX, y, speedY, b1, b2, b3, b4, b5
    speedX = random(3,5)
    speedY = random(3,5)
    size(500, 500)
    x = random(10,200)
    y = random(10,200)
    b1 = True
    b2 = True
    b3 = True
    b4 = True
    b5 = True
    

def draw():
    global x, speedX, y, speedY, b1, b2, b3, b4, b5
    background(255) 
    ellipse(x, y, 20,20)
    rect(mouseX-50, 450, 100, 10)
    
    x = x + speedX
    y = y + speedY
    
    #ball and walls
    if x > 500:
        speedX = -speedX
    elif x < 10:
        speedX = -speedX
    if y > 500:
        speedY = 0
        speedX = 0
    elif y < 10:
        speedY = -speedY
        
    #ball and paddle
    if x > mouseX and x < mouseX+50:
        if y > 440:
            speedX = -speedX
            speedY = -speedY
     
     #bricks   
    if b1 == True:
        rect(0,0, 100, 20)
    if b2 == True:
        rect(100,0, 100, 20)
    if b3 == True:
        rect(200,0, 100, 20)
    if b4 == True:
        rect(300,0, 100, 20)
    if b5 == True:
        rect(400,0, 100, 20)
        
    if x > 0 and x < 100:
        if y < 20:
            b1 = False
    if x > 100 and x < 200:
        if y < 20:
            b2 = False
    if x > 200 and x < 300:
        if y < 20:
            b3 = False
    if x > 300 and x < 400:
        if y < 20:
            b4 = False
    if x > 400 and x < 500:
        if y < 20:
            b5 = False
            
    if b1 == False and b2 == False and b3 == False and b4 == False and b5 == False:
        speedX = 0
        speedY = 0
    