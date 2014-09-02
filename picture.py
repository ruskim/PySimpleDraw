PX = 0
PY = 0

def m_set(x, y):
    global PX
    global PY
    PX = x
    PY = y

def m(dx, dy, draw=1):
    global PX
    global PY
    if draw == 1:
        l(PX, PY, PX+dx, PY+dy)
    PX = PX+dx
    PY = PY+dy


def k(x,y,d):
    l(x,y,x+d,y)
    l(x+d,y,x+d,y+d)
    l(x,y+d,x,y)
    l(x+d,y+d,x,y+d)

def t(x,y,d):
    l(x,y+d,x+d,y)
    l(x,y+d,x,y)
    l(x,y,x+d,y)
    pass

def r(x,y,d):
    l(x,y+d,x+d,y)
    l(x,y-d,x+d,y)
    l(x,y-d,x-d,y)
    l(x-d,y,x,y+d)
    pass

def dom (x,y,d):
    l(x-d,y,x,y+d)
    l(x,y+d,x+d,y)
    k(x-d,y-(d+d),d+d)
    pass

#k(100,100,300)
#k(200,200,100)
#k(230,230,40)
#k(50,90,200)


#t(0,0,100)

#for d in range(5,100, 5):
#    k(200,200,d)

#c(0,104,139,)

#dom(60,70,80)

#c(255,0,0)

#for x in range(-200,200,50):
#    for y in range(-200,200,120):
#        dom(x,y,20)

def t(x, y):
    l(x,y+22,0,0)
    l(x,y,0,0)
    l(x,y,x,y+22)



def r(x, y):
    l(x, y, x+10, y+10)
    l(x+10,y+10,x+15, y)
    l(x+10,y+10, x+10, y+20)
    k(x+5, y+20, 10)
    l(x, y+15, x+20, y+15)
    l(x, y+15, x, y+18)
    l(x, y+18, x-3, y+18)

#c(148,0,211)

def p(x, y, w, h):
    m_set(x, y)
    m(w,0)
    m(0,h)
    m(-w, 0)
    m(0, -h)

def pristavka(x, y, w, h):
    p(x, y, w, h)
    p(x+40, y+5, 40, 30)
    p(x+100,y+5,10,10)
    p(x+110,y+20,10,10)
    p(x,y+10,10,10)
    p(x+20,y+10,10,10)
    p(x+10,y+20,10,10)
    p(x+10,y,10,10)
    l(x+130,y+40,x+130,y+100)
    r(x+50,y+5)
   # c(142,229,238)
    l(x,y+40,x,y+100)
    l(x,y+100,x+130,y+100)
    r(x+100,y+50)
    l(x-10,y-10,x+100,y-1)
    r(x+60,y+50)
    r(x+30,y+50)

#pristavka(0,0,130,40)

#for x in range(-200,200,150):
#    for y in range(-200,200,120):
#        pristavka(x,y, 130,40)
#        c(28,28,28)


x=0
def tick():
    global x
    pristavka(x, 0, 130, 40)
    x = x + 1
