
# ===> colors <===
r = list ( "" )    #==> right face
l = list ( "" )    #==> left face
u = list ( "" )    #==> up face
d = list ( "" )    #==> down face
f = list ( "" )    #==> front face
b = list ( "" )    #==> back face

# ===> swaping <===
r1 = list ( 9 * ' ' )
l1 = list ( 9 * ' ' )
u1 = list ( 9 * ' ' )
d1 = list ( 9 * ' ' )
f1 = list ( 9 * ' ' )
b1 = list ( 9 * ' ' )

#=> out moves <=
moves = []

#===================
def turn_90_right():

    r1[0] = r[6]
    r1[1] = r[3]
    r1[2] = r[0]
    r1[3] = r[7]
    r1[5] = r[1]
    r1[6] = r[8]
    r1[7] = r[5]
    r1[8] = r[2]

    f1[2] = d[2]
    f1[5] = d[5]
    f1[8] = d[8]

    u1[2] = f[2]
    u1[5] = f[5]
    u1[8] = f[8]

    b1[0] = u[8]
    b1[3] = u[5]
    b1[6] = u[2]

    d1[2] = b[6]
    d1[5] = b[3]
    d1[8] = b[0]

    r[0] = r1[0]
    r[1] = r1[1]
    r[2] = r1[2]
    r[3] = r1[3]
    r[5] = r1[5]
    r[6] = r1[6]
    r[7] = r1[7]
    r[8] = r1[8]

    f[2] = f1[2]
    f[5] = f1[5]
    f[8] = f1[8]

    u[2] = u1[2]
    u[5] = u1[5]
    u[8] = u1[8]

    b[0] = b1[0]
    b[3] = b1[3]
    b[6] = b1[6]

    d[2] = d1[2]
    d[5] = d1[5]
    d[8] = d1[8]

#====================
def turn_270_right():

    r1[0] = r[2]
    r1[1] = r[5]
    r1[2] = r[8]
    r1[3] = r[1]
    r1[5] = r[7]
    r1[6] = r[0]
    r1[7] = r[3]
    r1[8] = r[6]

    f1[2] = u[2]
    f1[5] = u[5]
    f1[8] = u[8]

    u1[2] = b[6]
    u1[5] = b[3]
    u1[8] = b[0]

    b1[0] = d[8]
    b1[3] = d[5]
    b1[6] = d[2]

    d1[2] = f[2]
    d1[5] = f[5]
    d1[8] = f[8]

    r[0] = r1[0]
    r[1] = r1[1]
    r[2] = r1[2]
    r[3] = r1[3]
    r[5] = r1[5]
    r[6] = r1[6]
    r[7] = r1[7]
    r[8] = r1[8]

    f[2] = f1[2]
    f[5] = f1[5]
    f[8] = f1[8]

    u[2] = u1[2]
    u[5] = u1[5]
    u[8] = u1[8]

    b[0] = b1[0]
    b[3] = b1[3]
    b[6] = b1[6]

    d[2] = d1[2]
    d[5] = d1[5]
    d[8] = d1[8]

#====================
def turn_180_right():

    r1[0] = r[8]
    r1[1] = r[7]
    r1[2] = r[6]
    r1[3] = r[5]
    r1[5] = r[3]
    r1[6] = r[2]
    r1[7] = r[1]
    r1[8] = r[0]

    f1[2] = b[6]
    f1[5] = b[3]
    f1[8] = b[0]

    u1[2] = d[2]
    u1[5] = d[5]
    u1[8] = d[8]

    b1[0] = f[8]
    b1[3] = f[5]
    b1[6] = f[2]

    d1[2] = u[2]
    d1[5] = u[5]
    d1[8] = u[8]

    r[0] = r1[0]
    r[1] = r1[1]
    r[2] = r1[2]
    r[3] = r1[3]
    r[5] = r1[5]
    r[6] = r1[6]
    r[7] = r1[7]
    r[8] = r1[8]

    f[2] = f1[2]
    f[5] = f1[5]
    f[8] = f1[8]

    u[2] = u1[2]
    u[5] = u1[5]
    u[8] = u1[8]

    b[0] = b1[0]
    b[3] = b1[3]
    b[6] = b1[6]

    d[2] = d1[2]
    d[5] = d1[5]
    d[8] = d1[8]

#===================
def turn_90_left():

    l1[0] = l[6]
    l1[1] = l[3]
    l1[2] = l[0]
    l1[3] = l[7]
    l1[5] = l[1]
    l1[6] = l[8]
    l1[7] = l[5]
    l1[8] = l[2]

    f1[0] = u[0]
    f1[3] = u[3]
    f1[6] = u[6]

    u1[0] = b[8]
    u1[3] = b[5]
    u1[6] = b[2]

    b1[2] = d[6]
    b1[5] = d[3]
    b1[8] = d[0]

    d1[0] = f[0]
    d1[3] = f[3]
    d1[6] = f[6]

    l[0] = l1[0]
    l[1] = l1[1]
    l[2] = l1[2]
    l[3] = l1[3]
    l[5] = l1[5]
    l[6] = l1[6]
    l[7] = l1[7]
    l[8] = l1[8]

    f[0] = f1[0]
    f[3] = f1[3]
    f[6] = f1[6]

    u[0] = u1[0]
    u[3] = u1[3]
    u[6] = u1[6]

    b[2] = b1[2]
    b[5] = b1[5]
    b[8] = b1[8]

    d[0] = d1[0]
    d[3] = d1[3]
    d[6] = d1[6]

#===================
def turn_270_left():

    l1[0] = l[2]
    l1[1] = l[5]
    l1[2] = l[8]
    l1[3] = l[1]
    l1[5] = l[7]
    l1[6] = l[0]
    l1[7] = l[3]
    l1[8] = l[6]

    f1[0] = d[0]
    f1[3] = d[3]
    f1[6] = d[6]

    u1[0] = f[0]
    u1[3] = f[3]
    u1[6] = f[6]

    b1[2] = u[6]
    b1[5] = u[3]
    b1[8] = u[0]

    d1[0] = b[8]
    d1[3] = b[5]
    d1[6] = b[2]

    l[0] = l1[0]
    l[1] = l1[1]
    l[2] = l1[2]
    l[3] = l1[3]
    l[5] = l1[5]
    l[6] = l1[6]
    l[7] = l1[7]
    l[8] = l1[8]

    f[0] = f1[0]
    f[3] = f1[3]
    f[6] = f1[6]

    u[0] = u1[0]
    u[3] = u1[3]
    u[6] = u1[6]

    b[2] = b1[2]
    b[5] = b1[5]
    b[8] = b1[8]

    d[0] = d1[0]
    d[3] = d1[3]
    d[6] = d1[6]

#===================
def turn_180_left():

    l1[0] = l[8]
    l1[1] = l[7]
    l1[2] = l[6]
    l1[3] = l[5]
    l1[5] = l[3]
    l1[6] = l[2]
    l1[7] = l[1]
    l1[8] = l[0]

    f1[0] = b[8]
    f1[3] = b[5]
    f1[6] = b[2]

    u1[0] = d[0]
    u1[3] = d[3]
    u1[6] = d[6]

    b1[2] = f[6]
    b1[5] = f[3]
    b1[8] = f[0]

    d1[0] = u[0]
    d1[3] = u[3]
    d1[6] = u[6]

    l[0] = l1[0]
    l[1] = l1[1]
    l[2] = l1[2]
    l[3] = l1[3]
    l[5] = l1[5]
    l[6] = l1[6]
    l[7] = l1[7]
    l[8] = l1[8]

    f[0] = f1[0]
    f[3] = f1[3]
    f[6] = f1[6]

    u[0] = u1[0]
    u[3] = u1[3]
    u[6] = u1[6]

    b[2] = b1[2]
    b[5] = b1[5]
    b[8] = b1[8]

    d[0] = d1[0]
    d[3] = d1[3]
    d[6] = d1[6]

#================
def turn_90_up():

    u1[0] = u[6]
    u1[1] = u[3]
    u1[2] = u[0]
    u1[3] = u[7]
    u1[5] = u[1]
    u1[6] = u[8]
    u1[7] = u[5]
    u1[8] = u[2]

    f1[0] = r[0]
    f1[1] = r[1]
    f1[2] = r[2]

    r1[0] = b[0]
    r1[1] = b[1]
    r1[2] = b[2]

    l1[0] = f[0]
    l1[1] = f[1]
    l1[2] = f[2]

    b1[0] = l[0]
    b1[1] = l[1]
    b1[2] = l[2]

    u[0] = u1[0]
    u[1] = u1[1]
    u[2] = u1[2]
    u[3] = u1[3]
    u[5] = u1[5]
    u[6] = u1[6]
    u[7] = u1[7]
    u[8] = u1[8]

    f[0] = f1[0]
    f[1] = f1[1]
    f[2] = f1[2]

    r[0] = r1[0]
    r[1] = r1[1]
    r[2] = r1[2]

    l[0] = l1[0]
    l[1] = l1[1]
    l[2] = l1[2]

    b[0] = b1[0]
    b[1] = b1[1]
    b[2] = b1[2]

#=================
def turn_270_up():

    u1[0] = u[2]
    u1[1] = u[5]
    u1[2] = u[8]
    u1[3] = u[1]
    u1[5] = u[7]
    u1[6] = u[0]
    u1[7] = u[3]
    u1[8] = u[6]

    f1[0] = l[0]
    f1[1] = l[1]
    f1[2] = l[2]

    r1[0] = f[0]
    r1[1] = f[1]
    r1[2] = f[2]

    l1[0] = b[0]
    l1[1] = b[1]
    l1[2] = b[2]

    b1[0] = r[0]
    b1[1] = r[1]
    b1[2] = r[2]

    u[0] = u1[0]
    u[1] = u1[1]
    u[2] = u1[2]
    u[3] = u1[3]
    u[5] = u1[5]
    u[6] = u1[6]
    u[7] = u1[7]
    u[8] = u1[8]

    f[0] = f1[0]
    f[1] = f1[1]
    f[2] = f1[2]

    r[0] = r1[0]
    r[1] = r1[1]
    r[2] = r1[2]

    l[0] = l1[0]
    l[1] = l1[1]
    l[2] = l1[2]

    b[0] = b1[0]
    b[1] = b1[1]
    b[2] = b1[2]

#=================
def turn_180_up():

    u1[0] = u[8]
    u1[1] = u[7]
    u1[2] = u[6]
    u1[3] = u[5]
    u1[5] = u[3]
    u1[6] = u[2]
    u1[7] = u[1]
    u1[8] = u[0]

    f1[0] = b[0]
    f1[1] = b[1]
    f1[2] = b[2]

    r1[0] = l[0]
    r1[1] = l[1]
    r1[2] = l[2]

    b1[0] = f[0]
    b1[1] = f[1]
    b1[2] = f[2]

    l1[0] = r[0]
    l1[1] = r[1]
    l1[2] = r[2]

    u[0] = u1[0]
    u[1] = u1[1]
    u[2] = u1[2]
    u[3] = u1[3]
    u[5] = u1[5]
    u[6] = u1[6]
    u[7] = u1[7]
    u[8] = u1[8]

    f[0] = f1[0]
    f[1] = f1[1]
    f[2] = f1[2]

    r[0] = r1[0]
    r[1] = r1[1]
    r[2] = r1[2]

    b[0] = b1[0]
    b[1] = b1[1]
    b[2] = b1[2]

    l[0] = l1[0]
    l[1] = l1[1]
    l[2] = l1[2]

#==================
def turn_90_down():

    d1[0] = d[6]
    d1[1] = d[3]
    d1[2] = d[0]
    d1[3] = d[7]
    d1[5] = d[1]
    d1[6] = d[8]
    d1[7] = d[5]
    d1[8] = d[2]

    f1[6] = l[6]
    f1[7] = l[7]
    f1[8] = l[8]

    r1[6] = f[6]
    r1[7] = f[7]
    r1[8] = f[8]

    l1[6] = b[6]
    l1[7] = b[7]
    l1[8] = b[8]

    b1[6] = r[6]
    b1[7] = r[7]
    b1[8] = r[8]
        
    d[0] = d1[0]
    d[1] = d1[1]
    d[2] = d1[2]
    d[3] = d1[3]
    d[5] = d1[5]
    d[6] = d1[6]
    d[7] = d1[7]
    d[8] = d1[8]

    f[6] = f1[6]
    f[7] = f1[7]
    f[8] = f1[8]

    r[6] = r1[6]
    r[7] = r1[7]
    r[8] = r1[8]

    l[6] = l1[6]
    l[7] = l1[7]
    l[8] = l1[8]

    b[6] = b1[6]
    b[7] = b1[7]
    b[8] = b1[8]

#===================
def turn_270_down():

    d1[0] = d[2]
    d1[1] = d[5]
    d1[2] = d[8]
    d1[3] = d[1]
    d1[5] = d[7]
    d1[6] = d[0]
    d1[7] = d[3]
    d1[8] = d[6]

    f1[6] = r[6]
    f1[7] = r[7]
    f1[8] = r[8]

    r1[6] = b[6]
    r1[7] = b[7]
    r1[8] = b[8]

    l1[6] = f[6]
    l1[7] = f[7]
    l1[8] = f[8]

    b1[6] = l[6]
    b1[7] = l[7]
    b1[8] = l[8]

    d[0] = d1[0]
    d[1] = d1[1]
    d[2] = d1[2]
    d[3] = d1[3]
    d[5] = d1[5]
    d[6] = d1[6]
    d[7] = d1[7]
    d[8] = d1[8]

    f[6] = f1[6]
    f[7] = f1[7]
    f[8] = f1[8]

    r[6] = r1[6]
    r[7] = r1[7]
    r[8] = r1[8]

    l[6] = l1[6]
    l[7] = l1[7]
    l[8] = l1[8]

    b[6] = b1[6]
    b[7] = b1[7]
    b[8] = b1[8]

#===================
def turn_180_down():

    d1[0] = d[8]
    d1[1] = d[7]
    d1[2] = d[6]
    d1[3] = d[5]
    d1[5] = d[3]
    d1[6] = d[2]
    d1[7] = d[1]
    d1[8] = d[0]

    f1[6] = b[6]
    f1[7] = b[7]
    f1[8] = b[8]

    r1[6] = l[6]
    r1[7] = l[7]
    r1[8] = l[8]

    b1[6] = f[6]
    b1[7] = f[7]
    b1[8] = f[8]

    l1[6] = r[6]
    l1[7] = r[7]
    l1[8] = r[8]

    d[0] = d1[0]
    d[1] = d1[1]
    d[2] = d1[2]
    d[3] = d1[3]
    d[5] = d1[5]
    d[6] = d1[6]
    d[7] = d1[7]
    d[8] = d1[8]

    f[6] = f1[6]
    f[7] = f1[7]
    f[8] = f1[8]

    r[6] = r1[6]
    r[7] = r1[7]
    r[8] = r1[8]

    b[6] = b1[6]
    b[7] = b1[7]
    b[8] = b1[8]

    l[6] = l1[6]
    l[7] = l1[7]
    l[8] = l1[8]

#===================
def turn_90_front():

    f1[0] = f[6]
    f1[1] = f[3]
    f1[2] = f[0]
    f1[3] = f[7]
    f1[5] = f[1]
    f1[6] = f[8]
    f1[7] = f[5]
    f1[8] = f[2]

    u1[6] = l[8]
    u1[7] = l[5]
    u1[8] = l[2]

    r1[0] = u[6]
    r1[3] = u[7]
    r1[6] = u[8]

    d1[0] = r[6]
    d1[1] = r[3]
    d1[2] = r[0]

    l1[2] = d[0]
    l1[5] = d[1]
    l1[8] = d[2]

    f[0] = f1[0]
    f[1] = f1[1]
    f[2] = f1[2]
    f[3] = f1[3]
    f[5] = f1[5]
    f[6] = f1[6]
    f[7] = f1[7]
    f[8] = f1[8]

    u[6] = u1[6]
    u[7] = u1[7]
    u[8] = u1[8]

    r[0] = r1[0]
    r[3] = r1[3]
    r[6] = r1[6]

    d[0] = d1[0]
    d[1] = d1[1]
    d[2] = d1[2]

    l[2] = l1[2]
    l[5] = l1[5]
    l[8] = l1[8]

#====================
def turn_270_front():

    f1[0] = f[2]
    f1[1] = f[5]
    f1[2] = f[8]
    f1[3] = f[1]
    f1[5] = f[7]
    f1[6] = f[0]
    f1[7] = f[3]
    f1[8] = f[6]

    u1[6] = r[0]
    u1[7] = r[3]
    u1[8] = r[6]

    r1[0] = d[2]
    r1[3] = d[1]
    r1[6] = d[0]

    d1[0] = l[2]
    d1[1] = l[5]
    d1[2] = l[8]

    l1[2] = u[8]
    l1[5] = u[7]
    l1[8] = u[6]

    f[0] = f1[0]
    f[1] = f1[1]
    f[2] = f1[2]
    f[3] = f1[3]
    f[5] = f1[5]
    f[6] = f1[6]
    f[7] = f1[7]
    f[8] = f1[8]

    u[6] = u1[6]
    u[7] = u1[7]
    u[8] = u1[8]

    r[0] = r1[0]
    r[3] = r1[3]
    r[6] = r1[6]

    d[0] = d1[0]
    d[1] = d1[1]
    d[2] = d1[2]

    l[2] = l1[2]
    l[5] = l1[5]
    l[8] = l1[8]

#====================
def turn_180_front():

    f1[0] = f[8]
    f1[1] = f[7]
    f1[2] = f[6]
    f1[3] = f[5]
    f1[5] = f[3]
    f1[6] = f[2]
    f1[7] = f[1]
    f1[8] = f[0]

    u1[6] = d[2]
    u1[7] = d[1]
    u1[8] = d[0]

    r1[0] = l[8]
    r1[3] = l[5]
    r1[6] = l[2]

    d1[0] = u[8]
    d1[1] = u[7]
    d1[2] = u[6]

    l1[2] = r[6]
    l1[5] = r[3]
    l1[8] = r[0]

    f[0] = f1[0]
    f[1] = f1[1]
    f[2] = f1[2]
    f[3] = f1[3]
    f[5] = f1[5]
    f[6] = f1[6]
    f[7] = f1[7]
    f[8] = f1[8]

    u[6] = u1[6]
    u[7] = u1[7]
    u[8] = u1[8]

    r[0] = r1[0]
    r[3] = r1[3]
    r[6] = r1[6]

    d[0] = d1[0]
    d[1] = d1[1]
    d[2] = d1[2]

    l[2] = l1[2]
    l[5] = l1[5]
    l[8] = l1[8]

#==================
def turn_90_back():

    b1[0] = b[6]
    b1[1] = b[3]
    b1[2] = b[0]
    b1[3] = b[7]
    b1[5] = b[1]
    b1[6] = b[8]
    b1[7] = b[5]
    b1[8] = b[2]

    u1[0] = r[2]
    u1[1] = r[5]
    u1[2] = r[8]

    r1[2] = d[8]
    r1[5] = d[7]
    r1[8] = d[6]

    l1[0] = u[0]
    l1[3] = u[1]
    l1[6] = u[2]

    d1[6] = l[0]
    d1[7] = l[3]
    d1[8] = l[6]

    b[0] = b1[0]
    b[1] = b1[1]
    b[2] = b1[2]
    b[3] = b1[3]
    b[5] = b1[5]
    b[6] = b1[6]
    b[7] = b1[7]
    b[8] = b1[8]

    u[0] = u1[0]
    u[1] = u1[1]
    u[2] = u1[2]

    r[2] = r1[2]
    r[5] = r1[5]
    r[8] = r1[8]

    l[0] = l1[0]
    l[3] = l1[3]
    l[6] = l1[6]

    d[6] = d1[6]
    d[7] = d1[7]
    d[8] = d1[8]

#===================
def turn_270_back():

    b1[0] = b[2]
    b1[1] = b[5]
    b1[2] = b[8]
    b1[3] = b[1]
    b1[5] = b[7]
    b1[6] = b[0]
    b1[7] = b[3]
    b1[8] = b[6]

    u1[0] = l[6]
    u1[1] = l[3]
    u1[2] = l[0]

    r1[2] = u[0]
    r1[5] = u[1]
    r1[8] = u[2]

    l1[0] = d[6]
    l1[3] = d[7]
    l1[6] = d[8]

    d1[6] = r[8]
    d1[7] = r[5]
    d1[8] = r[2]

    b[0] = b1[0]
    b[1] = b1[1]
    b[2] = b1[2]
    b[3] = b1[3]
    b[5] = b1[5]
    b[6] = b1[6]
    b[7] = b1[7]
    b[8] = b1[8]

    u[0] = u1[0]
    u[1] = u1[1]
    u[2] = u1[2]

    r[2] = r1[2]
    r[5] = r1[5]
    r[8] = r1[8]

    l[0] = l1[0]
    l[3] = l1[3]
    l[6] = l1[6]

    d[6] = d1[6]
    d[7] = d1[7]
    d[8] = d1[8]

#====================
def turn_180_back():

    b1[0] = b[8]
    b1[1] = b[7]
    b1[2] = b[6]
    b1[3] = b[5]
    b1[5] = b[3]
    b1[6] = b[2]
    b1[7] = b[1]
    b1[8] = b[0]

    u1[0] = d[8]
    u1[1] = d[7]
    u1[2] = d[6]

    r1[2] = l[6]
    r1[5] = l[3]
    r1[8] = l[0]

    l1[0] = r[8]
    l1[3] = r[5]
    l1[6] = r[2]

    d1[6] = u[2]
    d1[7] = u[1]
    d1[8] = u[0]

    b[0] = b1[0]
    b[1] = b1[1]
    b[2] = b1[2]
    b[3] = b1[3]
    b[5] = b1[5]
    b[6] = b1[6]
    b[7] = b1[7]
    b[8] = b1[8]

    u[0] = u1[0]
    u[1] = u1[1]
    u[2] = u1[2]

    r[2] = r1[2]
    r[5] = r1[5]
    r[8] = r1[8]

    l[0] = l1[0]
    l[3] = l1[3]
    l[6] = l1[6]

    d[6] = d1[6]
    d[7] = d1[7]
    d[8] = d1[8]

#==================
def create_cross():

    while ( d[1] != 'l' or d[3] != 'l' or d[5] != 'l' or d[7] !='l' ):

        if ( f[5] == 'l' ):

            if ( d[5] == 'l' ):
                moves.append('D')
                turn_90_down()

                if ( d[5] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[5] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('r')
            turn_270_right()

        elif ( f[3] == 'l' ):

            if ( d[3] == 'l' ):
                moves.append('D')
                turn_90_down()

                if ( d[3] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[3] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('L')
            turn_90_left()

        elif ( l[5] == 'l' ):

            if ( d[1] == 'l' ):
                moves.append('D')
                turn_90_down()

                if ( d[1] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[1] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('f')
            turn_270_front()

        elif ( l[3] == 'l' ):

            if ( d[7] == 'l' ):
                moves.append('D')
                turn_90_down()

                if ( d[7] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[7] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('B')
            turn_90_back()

        elif ( b[5] == 'l' ):

            if ( d[3] == 'l' ):
                moves.append('D')
                turn_90_down()

                if ( d[3] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[3] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('l')
            turn_270_left()

        elif ( b[3] == 'l' ):

            if ( d[5] == 'l' ):
                moves.append('D')
                turn_90_down()

                if ( d[5] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[5] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('R')
            turn_90_right()

        elif ( r[5] == 'l' ):

            if ( d[7] == 'l' ):
                moves.append('D')
                turn_90_down()

                if ( d[7] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[7] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('b')
            turn_270_back()

        elif ( r[3] == 'l' ):

            if ( d[1] == 'l' ):
                moves.append('D')
                turn_90_down()

                if ( d[1] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[1] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('F')
            turn_90_front()

        elif ( u[1] == 'l' ):

            if ( d[7] == 'l' ):
                moves.append('D')
                turn_90_down()

                if ( d[7] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[7] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('6')
            turn_180_back()

        elif ( u[3] == 'l' ):

            if ( d[3] == 'l'):
                moves.append('D')
                turn_90_down()

                if ( d[3] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[3] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('2')
            turn_180_left()

        elif ( u[5] == 'l' ):

            if ( d[5] == 'l' ):
                moves.append('D')
                turn_90_down()

                if ( d[5] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[5] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('1')
            turn_180_right()

        elif ( u[7] == 'l' ):

            if ( d[1] == 'l' ):
                moves.append('D')
                turn_90_down()

                if ( d[1] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[1] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('5')
            turn_180_front()

        elif ( f[1] == 'l' or f[7] == 'l' ):

            if ( d[1] == 'l' ):
                moves.append('D')
                turn_90_down()

                if ( d[1] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[1] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('F')
            turn_90_front()

        elif ( l[1] == 'l' or l[7] == 'l' ):

            if ( d[3] == 'l' ):
                moves.append('D')
                turn_90_down()

                if ( d[3] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[3] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('L')
            turn_90_left()

        elif ( b[1] == 'l' or b[7] == 'l' ):

            if ( d[7] == 'l' ):
                moves.append('D')
                turn_90_down()

                if ( d[7] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[7] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('B')
            turn_90_back()

        elif ( r[1] == 'l' or r[7] == 'l' ):

            if ( d[5] == 'l' ):
                moves.append('D')
                turn_90_down()

                if ( d[5] == 'l' ):
                    moves.append('D')
                    turn_90_down()

                    if ( d[5] == 'l' ):
                        moves.append('D')
                        turn_90_down()

            moves.append('R')
            turn_90_right()

#=================================
def reverse_cross():

    while ( u[1]!='l' or u[3]!='l' or u[5]!='l' or u[7]!='l' ):

        if( f[7] == f[4] and d[1] == 'l' ):
            moves.append('5')
            turn_180_front()

        elif ( r[7] == r[4] and d[5] == 'l' ):
            moves.append('1')
            turn_180_right()


        elif ( b[7] == b[4] and d[7] == 'l' ):
            moves.append('6')
            turn_180_back()

        elif ( l[7] == l[4] and d[3] == 'l' ):
            moves.append('2')
            turn_180_left()

        else :
            moves.append('D')
            turn_90_down()

#===================================
def finish_first_layer():

    while ( (''.join(u) != "lllllllll") and (''.join(f[0:3]) != "ggg") and (''.join(r[0:3]) != "rrr") and (''.join(b[0:3]) != "bbb") and (''.join(l[0:3]) != "ooo") ):

        if ( f[8] == 'l' ):

            if ( (r[6] == 'g' and d[2] == 'o') or (r[6] == 'o' and d[2] == 'g') ):
                moves.append('d')
                turn_270_down()
                moves.append('L')
                turn_90_left()
                moves.append('D')
                turn_90_down()
                moves.append('l')
                turn_270_left()

            elif ( (r[6] == 'o' and d[2] == 'b') or (r[6] == 'b' and d[2] == 'o') ):
                moves.append('4')
                turn_180_down()
                moves.append('B')
                turn_90_back()
                moves.append('D')
                turn_90_down()
                moves.append('b')
                turn_270_back()

            elif ( (r[6] == 'b' and d[2] == 'r') or (r[6] == 'r' and d[2] == 'b') ):
                moves.append('D')
                turn_90_down()
                moves.append('R')
                turn_90_right()
                moves.append('D')
                turn_90_down()
                moves.append('r')
                turn_270_right()

            else :
                moves.append('F')
                turn_90_front()
                moves.append('D')
                turn_90_down()
                moves.append('f')
                turn_270_front()

        elif ( f[6] == 'l' ):

            if ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):
                moves.append('D')
                turn_90_down()
                moves.append('r')
                turn_270_right()
                moves.append('d')
                turn_270_down()
                moves.append('R')
                turn_90_right()

            elif ( (b[0] == 'b' and l[8] == 'o') or (b[0] == 'o' and l[8] == 'b') ):
                moves.append('d')
                turn_270_down()
                moves.append('l')
                turn_270_left()
                moves.append('d')
                turn_270_down()
                moves.append('L')
                turn_90_left()


            elif ( (b[0] == 'b' and l[8] == 'r') or (b[0] == 'r' and l[8] == 'b') ):
                moves.append('4')
                turn_180_down()
                moves.append('b')
                turn_270_back()
                moves.append('d')
                turn_270_down()
                moves.append('B')
                turn_90_back()

            else :
                moves.append('f')
                turn_270_front()
                moves.append('d')
                turn_270_down()
                moves.append('F')
                turn_90_front()

        elif ( r[8] == 'l' ):

            if ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            elif ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            elif ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            else :

        elif ( r[6] == 'l' ):

            if ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            elif ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            elif ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            else :

        elif ( b[8] =='l' ):

            if ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            elif ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            elif ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            else :

        elif ( b[6] == 'l' ):

            if ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            elif ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            elif ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            else :

        elif ( l[8] == 'l' ):

            if ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            elif ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            elif ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            else :

        elif ( l[6] == 'l' ):

            if ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            elif ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            elif ( (b[0] == 'r' and l[8] == 'g') or (b[0] == 'g' and l[8] == 'r') ):

            else :

        elif ( f[0] == 'l' ):
            moves.append('f')
            turn_270_front()
            moves.append('d')
            turn_270_down()
            moves.append('F')
            turn_90_front()

        elif ( f[2] == 'l' ):
            moves.append('F')
            turn_90_front()
            moves.append('D')
            turn_90_down()
            moves.append('f')
            turn_270_front()

        elif ( r[0] == 'l' ):
            moves.append('r')
            turn_270_right()
            moves.append('d')
            turn_270_down()
            moves.append('R')
            turn_90_right()

        elif ( r[2] == 'l' ):
            moves.append('R')
            turn_90_right()
            moves.append('D')
            turn_90_down()
            moves.append('r')
            turn_270_right()

        elif ( b[0] == 'l' ):
            moves.append('b')
            turn_270_back()
            moves.append('d')
            turn_270_down()
            moves.append('B')
            turn_90_back()

        elif ( b[2] == 'l' ):
            moves.append('B')
            turn_90_back()
            moves.append('D')
            turn_90_down()
            moves.append('b')
            turn_270_back()

        elif ( l[0] == 'l' ):
            moves.append('l')
            turn_270_left()
            moves.append('d')
            turn_270_down()
            moves.append('L')
            turn_90_left()

        elif ( l[2] == 'l' ):
            moves.append('L')
            turn_90_left()
            moves.append('D')
            turn_90_Down()
            moves.append('l')
            turn_270_left()

        elif ( ( u[6] == 'l' ) and ( f[0] != 'g' or l[2] != 'o' ) ):
            moves.append('f')
            turn_270_front()
            moves.append('d')
            turn_270_down()
            moves.append('F')
            turn_90_front()

        elif ( ( u[8] == 'l' ) and ( f[2] != 'g' or r[0] != 'r' ) ):
            moves.append('F')
            turn_90_front()
            moves.append('D')
            turn_90_down()
            moves.append('f')
            turn_270_front()

        elif ( ( u[2] == 'l' ) and ( r[2] != 'r' or b[0] != 'b' ) ):
            moves.append('b')
            turn_270_back()
            moves.append('d')
            turn_270_down()
            moves.append('B')
            turn_90_back()

        elif ( ( u[0] == 'l' ) and ( b[2] != 'b' or l[0] != 'o' ) ):
            moves.append('B')
            turn_90_back()
            moves.append('D')
            turn_90_down()
            moves.append('b')
            turn_270_back()

        elif ( d[0] == 'l' ):
            if ():
            elif ():
            elif ():
            else :

        elif ( d[2] == 'l' ):
            if ():
            elif ():
            elif ():
            else :

        elif ( d[6] == 'l' ):
            if ():
            elif ():
            elif ():
            else :

        elif ( d[8] == 'l' ):
            if ():
            elif ():
            elif ():
            else :



#====================
def optmize_moves():
    print "h"
#====================

