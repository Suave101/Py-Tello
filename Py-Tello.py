import os
pw = "GOHSU2020"
# pw is the password to crash the drone
'''
This Program Was Developed By: Alexander P. Doyle
'''

def EnterSession():
    f = open("temp.js", "w+")
    f.write("var http = require('http');")
    f.write("http.createServer(function (req, res) {")
    f.write("  res.writeHead(200, {'Content-Type': 'text/plain'});")
    f.write("  res.end('Hello World\n');")
    f.write("}).listen(8889, '192.168.10.1');")
    f.close()


def takeoff():
    f = open("temp.js", "a+")
    f.write("console.log('takeoff');")
    f.close()


def land():
    f = open("temp.js", "a+")
    f.write("console.log('land')")
    f.close()


def move(d, a):
    f = open("", "a+")
    if d == "forward":
        f.write("console.log('forward' + " + a + ');')
    elif d == "back":
        f.write("console.log('back' + " + a + ');')
    elif d == "left":
        f.write("console.log('left' + " + a + ');')
    elif d == "right":
        f.write("console.log('right' + " + a + ');')
    elif d == "up":
        f.write("console.log('up' + " + a + ');')
    elif d == "down":
        f.write("console.log('down' + " + a + ');')
    else:
        print("-------------------------------------")
        print("ERROR-Invalid Direction, move command")
        print("-------------------------------------")
    f.close()


def rotate(d, a):
    f = open("", "a+")
    if d == "cw":
        f.write("console.log('cw' + " + a + ');')
    elif d == "ccw":
        f.write("console.log('ccw' + " + a + ');')
    else:
        print("-----------------------------------------")
        print("ERROR-Invalid Direction, rotation command")
        print("-----------------------------------------")


def flip(d):
    f = open("", "a+")
    if d == "left":
        f.write("console.log('flip' + l);")
    elif d == "right":
        f.write("console.log('flip' + r);")
    elif d == "forward":
        f.write("console.log('flip' + f);")
    elif d == "back":
        f.write("console.log('flip' + b);")
    f.close()


def run():
    os.system("")


def ExitSession():
    f = open("temp.js", "a+")
    f.write("var wshShell = new ActiveXObject('WScript.Shell');")
    f.write()
    f.close()


def estop(cc):
    if cc == pw:
        f = open("temp.js", "a+")
        f.write("console.log(emergency);")
        f.close()
    else:
        print("ERROR-Invalid Credentials")


def kill(n, cc, k):
    if cc == k or cc == pw:
        os.remove(n)
