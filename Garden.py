import pygame, os, sys, time, socket, threading
from threading import Thread
from collections import deque

# Sockets --------------------------------------------------#
localIP     = "127.0.0.1"
localPort   = 6001
bufferSize  = 1024
msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
bytesToSend = str.encode(msgFromServer)
message = ""

#Open Theme from text file ---------------------------------#
theme = open('theme.txt')
themeContent = theme.read().splitlines()
themeBg = themeContent[2] #Background
themeFg = themeContent[4] #Foreground
themeLn = themeContent[6] #Lines
themeFnt = themeContent[8] #Font
themeTtlSize = themeContent[10] #Font1 size
themeTxtSize = themeContent[12] #Font2 size

themeTxtCycle = themeContent[14] #Text Cycle
txtCycle = []
for letter in themeTxtCycle:
    txtCycle.append(letter) #split line into an array of characters





# Initialize pygame ----------------------------------------#
pygame.init()

# Set the height and width of the screen -------------------#
size = [600, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Window caption & icon & font -----------------------------#
pygame.display.set_caption("Garden")
pygame_icon = pygame.image.load('images/ico.png') #import icon
pygame.display.set_icon(pygame_icon) # Set icon

themeTxtCycle = []

#Open PureData Path from text file -------------------------#
filePath = open('pdpath.txt')
pathContent = filePath.read().splitlines()
pdFilePath = pathContent[0]



# Import font ----------------------------------------------#
font1 = pygame.font.Font(themeFnt, int(themeTxtSize))
font2 = pygame.font.Font(themeFnt, int(themeTtlSize))

# Get screen info for sizing -------------------------------#
infoObject = pygame.display.Info() 

# Other Junk------------------------------------------------#
clock = pygame.time.Clock() # clock usage for fps
input_box = pygame.Rect(50, infoObject.current_h-100, (infoObject.current_w/2), 50) # beginning box size
color_inactive = pygame.Color(themeFg) 
color_active = pygame.Color(themeLn)
color = color_inactive # box colour
active = False # is the box in use?
text = '' # default text
asciiIndex = 0

# Binary arrays---------------------------------------------#
array1 = [0,0,0,0,0,0,0,0]
array1Add = [0,0,0,0,0,0,0,0]

array2 = [0,0,0,0,0,0,0,0]
array2Add = [0,0,0,0,0,0,0,0]

binArray = [128,64,32,16,8,4,2,1]

textDist = 50
textY = 150
textY2 = 350


# Command arrays--------------------------------------------#
lastCommands = (["","","","","","","",""])
lastCommands = deque(lastCommands)
lstCmdIndex = 0
upCmdIndex = 0
lstComColor = themeLn
notLstComColor = themeFg

done = False



# send message to PD
def send2pd(message = ''):
    os.system("echo " + message +"|" + pdFilePath + "pdsend 6000 127.0.0.1 udp")
    
#Set user input to be sent to PD
def sendCommand():
    send2pd(userInput)


# Array1 text----------------------------------------#
def array1Text():
    global textDist, textY
    global array1_128,array1_64,array1_32,array1_16,array1_8,array1_4,array1_2,array1_1
    
    array1_128 = font2.render(str(array1[0]), True, themeFg)
    screen.blit(array1_128,((infoObject.current_w/2 + textDist),textY))
    array1_64 = font2.render(str(array1[1]), True, themeFg)
    screen.blit(array1_64,((infoObject.current_w/2 + textDist* 2),textY))
    array1_32 = font2.render(str(array1[2]), True, themeFg)
    screen.blit(array1_32,((infoObject.current_w/2 + textDist * 3),textY))
    array1_16 = font2.render(str(array1[3]), True, themeFg)
    screen.blit(array1_16,((infoObject.current_w/2 + textDist * 4),textY))
    array1_8 = font2.render(str(array1[4]), True, themeFg)
    screen.blit(array1_8,((infoObject.current_w/2 + textDist * 5),textY))
    array1_4 = font2.render(str(array1[5]), True, themeFg)
    screen.blit(array1_4,((infoObject.current_w/2 + textDist * 6),textY))
    array1_2 = font2.render(str(array1[6]), True, themeFg)
    screen.blit(array1_2,((infoObject.current_w/2 + textDist * 7),textY))
    array1_1 = font2.render(str(array1[7]), True, themeFg)
    screen.blit(array1_1,((infoObject.current_w/2 + textDist * 8),textY))
    
    

# Array2 text----------------------------------------#
def array2Text():
    global textDist, textY2
    global array2_128,array2_64,array2_32,array2_16,array2_8,array2_4,array2_2,array2_1
    array2_128 = font2.render(str(array2[0]), True, themeFg)
    screen.blit(array2_128,((infoObject.current_w/2 + textDist),textY2))
    array2_64 = font2.render(str(array2[1]), True, themeFg)
    screen.blit(array2_64,((infoObject.current_w/2 + textDist* 2),textY2))
    array2_32 = font2.render(str(array2[2]), True, themeFg)
    screen.blit(array2_32,((infoObject.current_w/2 + textDist * 3),textY2))
    array2_16 = font2.render(str(array2[3]), True, themeFg)
    screen.blit(array2_16,((infoObject.current_w/2 + textDist * 4),textY2))
    array2_8 = font2.render(str(array2[4]), True, themeFg)
    screen.blit(array2_8,((infoObject.current_w/2 + textDist * 5),textY2))
    array2_4 = font2.render(str(array2[5]), True, themeFg)
    screen.blit(array2_4,((infoObject.current_w/2 + textDist * 6),textY2))
    array2_2 = font2.render(str(array2[6]), True, themeFg)
    screen.blit(array2_2,((infoObject.current_w/2 + textDist * 7),textY2))
    array2_1 = font2.render(str(array2[7]), True, themeFg)
    screen.blit(array2_1,((infoObject.current_w/2 + textDist * 8),textY2))

# Array process---------------------------------------#
def array1Addition():
    global array1, array1Add, array2, array2Add, textY, textY2
    
    for x in range(8):
        if array1[x] == 1:
            array1Add[x] = binArray[x]
        else: array1Add[x] = 0
    
    for x in range(8):
        if array2[x] == 1:
            array2Add[x] = binArray[x]
        else: array2Add[x] = 0
    
    array1Text = font2.render(str(sum(array1Add)), True, themeLn)
    screen.blit(array1Text,(infoObject.current_w/2 + textDist * 10, textY))
    array2Text = font2.render(str(sum(array2Add)), True, themeLn)
    screen.blit(array2Text,(infoObject.current_w/2 + textDist * 10, textY2))

# Command History------------------------------------#
def commandHist():
    hist0 = font1.render(">_" + lastCommands[0], True, (themeFg))
    screen.blit(hist0,(50, infoObject.current_h-200))
    hist1 = font1.render(lastCommands[1], True, (themeLn))
    screen.blit(hist1,(50, infoObject.current_h-300))
    hist2 = font1.render(lastCommands[2], True, (themeLn))
    screen.blit(hist2,(50, infoObject.current_h-400))
    hist3 = font1.render(lastCommands[3], True, (themeLn))
    screen.blit(hist3,(50, infoObject.current_h-500))
    hist4 = font1.render(lastCommands[4], True, (themeLn))
    screen.blit(hist4,(50, infoObject.current_h-600))
    hist5 = font1.render(lastCommands[5], True, (themeLn))
    screen.blit(hist5,(50, infoObject.current_h-700))
    hist6 = font1.render(lastCommands[6], True, (themeLn))
    screen.blit(hist6,(50, infoObject.current_h-800))
    hist7 = font1.render(lastCommands[7], True, (themeLn))
    screen.blit(hist7,(50, infoObject.current_h-900))
    
def showUI():
    closeX = font1.render('X', True, (themeFg))
    screen.blit(closeX,(infoObject.current_w-50, 50))
    
    title = font2.render('GARDEN', True, (themeFg))
    screen.blit(title,(50,50))
    
    bin2DecTitle = font1.render('Bin2Dec', True, (themeFg))
    screen.blit(bin2DecTitle,((infoObject.current_w/2)+50 ,50))
    
    feedTitle = font1.render('Feedback', True, (themeFg))
    screen.blit(feedTitle,((infoObject.current_w/2)+50 ,infoObject.current_h/2+50))
    
    
    pygame.draw.line(screen, (themeLn), [infoObject.current_w/2 ,50 ], [infoObject.current_w/2,infoObject.current_h-105], 2)
    pygame.draw.line(screen, (themeLn), [(infoObject.current_w/2)+50 ,infoObject.current_h/2 ], [(infoObject.current_w)-50 ,infoObject.current_h/2 ], 2)
    
    txt_surface = font1.render(text, True, themeFg)
    # Resize the box if the text is too long.
    width = max(infoObject.current_w/2 - 100, txt_surface.get_width()+10)
    input_box.w = width
    # Blit the text.
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    # Blit the input_box rect.
    pygame.draw.rect(screen, color, input_box, 2)
    
    
def mouseProcess():
    
    global array1_128, array1_64,array1_32,array1_16,array1_8,array1_4,array1_2,array1_1
    global array2_128, array2_64,array2_32,array2_16,array2_8,array2_4,array2_2,array2_1
    global array1, array2, textDist, textY
    

    
    ar10Rect = array1_128.get_rect(topleft = (infoObject.current_w/2 + textDist, textY))
    ar11Rect = array1_64.get_rect(topleft = (infoObject.current_w/2 + textDist*2, textY))
    ar12Rect = array1_32.get_rect(topleft = (infoObject.current_w/2 + textDist*3, textY))
    ar13Rect = array1_16.get_rect(topleft = (infoObject.current_w/2 + textDist*4, textY))
    ar14Rect = array1_8.get_rect(topleft = (infoObject.current_w/2 + textDist*5, textY))
    ar15Rect = array1_4.get_rect(topleft = (infoObject.current_w/2 + textDist*6, textY))
    ar16Rect = array1_2.get_rect(topleft = (infoObject.current_w/2 + textDist*7, textY))
    ar17Rect = array1_1.get_rect(topleft = (infoObject.current_w/2 + textDist*8, textY))
    
    ar20Rect = array2_128.get_rect(topleft = (infoObject.current_w/2 + textDist, textY2))
    ar21Rect = array2_64.get_rect(topleft = (infoObject.current_w/2 + textDist*2, textY2))
    ar22Rect = array2_32.get_rect(topleft = (infoObject.current_w/2 + textDist*3, textY2))
    ar23Rect = array2_16.get_rect(topleft = (infoObject.current_w/2 + textDist*4, textY2))
    ar24Rect = array2_8.get_rect(topleft = (infoObject.current_w/2 + textDist*5, textY2))
    ar25Rect = array2_4.get_rect(topleft = (infoObject.current_w/2 + textDist*6, textY2))
    ar26Rect = array2_2.get_rect(topleft = (infoObject.current_w/2 + textDist*7, textY2))
    ar27Rect = array2_1.get_rect(topleft = (infoObject.current_w/2 + textDist*8, textY2))
    
    
    
    if ar10Rect.collidepoint(event.pos):
        array1[0] = (array1[0] + 1) % 2
    if ar11Rect.collidepoint(event.pos):
        array1[1] = (array1[1] + 1) % 2
    if ar12Rect.collidepoint(event.pos):
        array1[2] = (array1[2] + 1) % 2
    if ar13Rect.collidepoint(event.pos):
        array1[3] = (array1[3] + 1) % 2
    if ar14Rect.collidepoint(event.pos):
        array1[4] = (array1[4] + 1) % 2
    if ar15Rect.collidepoint(event.pos):
        array1[5] = (array1[5] + 1) % 2
    if ar16Rect.collidepoint(event.pos):
        array1[6] = (array1[6] + 1) % 2
    if ar17Rect.collidepoint(event.pos):
        array1[7] = (array1[7] + 1) % 2
        
    if ar20Rect.collidepoint(event.pos):
        array2[0] = (array2[0] + 1) % 2
    if ar21Rect.collidepoint(event.pos):
        array2[1] = (array2[1] + 1) % 2
    if ar22Rect.collidepoint(event.pos):
        array2[2] = (array2[2] + 1) % 2
    if ar23Rect.collidepoint(event.pos):
        array2[3] = (array2[3] + 1) % 2
    if ar24Rect.collidepoint(event.pos):
        array2[4] = (array2[4] + 1) % 2
    if ar25Rect.collidepoint(event.pos):
        array2[5] = (array2[5] + 1) % 2
    if ar26Rect.collidepoint(event.pos):
        array2[6] = (array2[6] + 1) % 2
    if ar27Rect.collidepoint(event.pos):
        array2[7] = (array2[7] + 1) % 2    
    
        
# UDP thread -----------------------------------------------#
def listenUp():
    global message
    while True:    
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0]

        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
        
        print(clientMsg)
        print(clientIP)

        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)
        
        

def udpIn():
        global message
        UDP_in = font1.render(message, True, (themeFg))
        screen.blit(UDP_in,((infoObject.current_w/2)+50 ,infoObject.current_h/2+150))


threadListen = threading.Thread(target = listenUp, daemon=True)
threadListen.daemon = True
threadListen.start()

while not done:
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    
    
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            UDPServerSocket.shotdown()
            UDPServerSocket.close()
            done = True  # Flag that we are done so we exit this loop
            
            
        if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                mouseProcess()
                
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
        
        
            
        
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                  
                    userInput = text # take the text from input and store it
                    
                    text = '' #delete text from textbox
                    
                    lastCommands.rotate(1) #rotate the array one to the right
                    
                    lastCommands[0] = userInput #set the first item in array to the text input
                    
                    lstCmdIndex = (lstCmdIndex + 1)%8 # up the index
                    
                    sendCommand()
                    
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    
    # Clear the screen and set the screen background
    screen.fill((themeBg))
    
    # Run the functions----------------------------------#
    showUI()
    commandHist()
    array1Text()
    array2Text()
    array1Addition()
    udpIn()
    pygame.display.flip() # permit section of screen to be refreshed, not all.
        
# Be IDLE friendly
pygame.quit()