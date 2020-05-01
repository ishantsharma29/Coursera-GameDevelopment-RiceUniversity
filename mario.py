#http://www.codeskulptor.org/#user38_po6AxqhKI1QNpHn.py

import simplegui

PLAYER_SIZE = [30,30]
PLAYER_CENTER = [(64,64),(192,64)]
LEVEL_Y=380
JUMP_MAX=130
CANVAS_WIDTH=800
FIXED_Y=380

platform_idx=0
coin_idx=0

back_1=simplegui.load_image("https://dl.dropbox.com/s/kbsgisdfwuy7tye/SuperMarioWorldMap17BG.png?dl=1")
back_2=simplegui.load_image("https://dl.dropbox.com/s/kbsgisdfwuy7tye/SuperMarioWorldMap17BG.png?dl=1")
back_3=simplegui.load_image("https://dl.dropbox.com/s/kbsgisdfwuy7tye/SuperMarioWorldMap17BG.png?dl=1")
coin_img=simplegui.load_image("https://dl.dropbox.com/s/j2ywfbshikekxd4/pickup_coin.png?dl=1")
coin1_img=simplegui.load_image("https://dl.dropbox.com/s/m4zp2fq05xmmlvg/screenshot_1353671388.png?dl=1")
pimg=simplegui.load_image("https://dl.dropbox.com/s/z4wx0dv9btejshw/mario3.png?dl=1")                               
pimg_ulta=simplegui.load_image("https://dl.dropbox.com/s/4lci512ctzsbdlg/mario2.png?dl=1")  
enemy=simplegui.load_image("https://dl.dropbox.com/s/ygkmb5o3695l4bs/smb_enemies_sheet.png?dl=1") 
back_over = simplegui.load_image("https://dl.dropbox.com/s/lpaigp63smkkcrx/back2.jpg?dl=1")

#sound files
stage1_back_sound=simplegui.load_sound("https://dl.dropbox.com/s/qktaicguik6so7f/214_world_1_map.ogg?dl=1")
coin_sound=simplegui.load_sound("https://dl.dropbox.com/s/bhg0gpj1m099pkk/smb_coin.ogg?dl=1")
enemy_die =simplegui.load_sound("https://dl.dropbox.com/s/rdby2nacejxysq7/enemydie.ogg?dl=1")
player_die =  simplegui.load_sound("https://dl.dropbox.com/s/i4c79c9w61hr047/7d49d1_Super_Mario_Bros_Die_Sound_Effect.ogg?dl=1")
game_over = simplegui.load_sound("https://www.dropbox.com/s/i4c79c9w61hr047/7d49d1_Super_Mario_Bros_Die_Sound_Effect.ogg?dl=1")



coin_sound.set_volume(.5)
stage1_back_sound.set_volume(.2)
enemy_die.set_volume(.5)
player_die.set_volume(.5)
game_over.set_volume(1)

pimg_coordinate=[[29,46],[87,46],[144,46],[201,46],[258,46],[315,46],[372,46],[429,46],[486,46],[543,46],[600,46],[657,46]]
level1_platforms = [[336,367,321],[434,510,272],[641,671,336],[785,814,336],[896,926,336],[977,1007,353],[1041,1071,336],[1346,1437,257],[1680,1775,321],[1840,1872,336],[2352,2382,289],[2706,2750,354],[2750,2850,410],[2850,2877,337],[2877,2979,410],[2979,3006,337],[3106,3215,336],[3442,3520,304],[3567,3647,353],[3678,3744,320],[3792,3855,369],[3919,3968,305],[4016,4079,353],[4111,4175,321]]
level1_khai= [[390,410],[719,735],[846,864],[943,976],[1742,1794],[2670,2703],[3373,3440],[4654,4800]]
level1_slope = [[3520,3567,(49/47),353,304],[3647,3678,-(33/31),320,353],[3744,3792,(49/48),369,320],[3855,3919,-(36/36),305,369],[3968,4016,(48/48),353,305],[4079,4111,-(32/32),321,353],[4175,4240,(1),380,321]]
coin_pos_list=[(440,260),(470,260),(500,260),(760,370),(830,370),(1150,325),(1170,325),(1190,325),(1210,325),(1230,325),(1250,325),(908,303),(991,332),(1025,364),(1487,338),(1514,338),(1538,338),(1639,314),(1669,314),(1699,314),(1719,244),(2087,258),(2137,258),(2234,324),(2251,324),(2268,324),(2463,331),(2493,331),(2523,331),(2553,331),(2583,331),(2613,331),(2807,324),(2898,310),(2930,310),(2960,310),(2990,310),(3240,310),(3270,310),(3300,310),(3558,263),(3588,263),(3618,263),(3770,263),(3800,263),(3830,263),(4000,263),(4030,263),(4060,263),(4300,263),(4350,263),(4400,263)]

#COINS LIST
coin_img_list=[]
coin_captured=[]
score=0

#enemies list
moving_enemy = [[530,641,380],[1082,1180,380],[1180,1341,380],[1452,1631,380],[1882,2334,380],[1892,2344,380],[1902,2354,380],[2759,2847,400],[2895,2974,400],[3567,3645,352],[3793,3855,369],[4016,4075,351],[4242,4608,380],[4269,4618,380],[4299,4628,380],[4329,4638,380],[4368,4648,380]]




class Player:
    
    def __init__(self,player_type,level):#constructor
        global LEVEL_Y
        if level==1:
            self.pos=[40,LEVEL_Y]
        elif level==2:
            self.pos[0,0]
        elif level==3:
            sel.pos=[0,0]
        self.level_x=self.pos[0]#level_x is pos of player on canvas
        self.ptype=player_type#there can be choice among the players
        self.plife=3#total life
        self.image_idx=1#initial image 
        self.jump=0
        self.pvelocity = 0
        self.onplatform=0
        self.mushroom=0
        self.moveby=10#the amount by which player moves in horizontal motion
        LEVEL_Y=380#initial level
        self.restart=0
        self.slope=0
    
    def Capture_Coins(self):
        j=0
        global coin_sound,score
        for i in coin_pos_list:
            if coin_captured[j] == 0:
                if self.pos[0]+PLAYER_SIZE[0]/2>=i[0] and self.pos[0]-PLAYER_SIZE[0]/2<=i[0] and i[1]>=self.pos[1]-PLAYER_SIZE[1]/2 and i[1]<=self.pos[1]+PLAYER_SIZE[1]/2:
                    coin_captured[j]=1
                    score+=10
                    coin_sound.rewind()
                    coin_sound.play()
            j+=1
    
    def move_h(self,direction):#action if right or left key is pressed
        if direction == "LEFT":
            self.pvelocity=-1
        else: 
            self.pvelocity=1
        
    def Jump(self):#action if a player jummps
        global LEVEL_Y,FIXED_Y,PLAYER_SIZE
        if self.jump==1:#player is going up
            self.pos[1]-=5
            if self.pos[1] <= LEVEL_Y-JUMP_MAX:#reaches max height
                self.jump=2
                #LEVEL_Y=FIXED_Y
    
        if self.jump==2:#player is coming down
            self.pos[1]+=5
            self.check_collision(1,1)#check if any enemy is cming
            if self.restart==0:#if the player is landing safely
                
                for i in level1_platforms:#check if it is on any platform
                    if self.pos[0]+PLAYER_SIZE[0]/4>=i[0] and self.pos[0]-(PLAYER_SIZE[0]/4)<=i[1]:
                        if self.pos[1] >= i[2]-15:
                            self.jump=0
                            self.onplatform=1#indicates it is on a platform
                            self.plat_x1=i[0]#start of platform
                            self.plat_x2=i[1]#end of platform
                            self.pos[1]=i[2]-10#players height=platform height
                            LEVEL_Y=i[2]-10
                if self.pos[1]>= LEVEL_Y:#when player reaches platform stop it
                    self.jump=0
                    self.pos[1]=LEVEL_Y
            else:#if the player is falling in a khai
                if self.pos[1]>=460:#reset everything
                    self.pos=[40,FIXED_Y]
                    self.plife-=1
                    self.die()
                    player_die.rewind()
                    player_die.play()
                    
    
    def Move(self):
        #to move 
        global CANVAS_WIDTH,Back_obj,LEVEL_Y,FIXED_Y,PLAYER_SIZE
        if self.jump==1 or self.jump==2:#if player is jumping than adjust its x motion
            self.moveby=3
            self.Jump()
        else:
            self.moveby=10
            self.check_collision(1,0) 
        
        if self.pvelocity==1:#motion in forward direction
            flag=self.Stop()#wheather it is blocked by obstacle
            if flag==1:#if yes,returns,no further motion
                return
            self.pos[0]+=self.moveby#move
            
            if self.onplatform==1:#if platform ends
                if self.pos[0]+(PLAYER_SIZE[0]/4)*3>self.plat_x2 :
                     #self.pos[1]=LEVEL_Y
                     flag1=self.platform_check()   
                     if flag1==1:
                        LEVEL_Y=400    
                        if self.jump==0:#if player is not jumping than fall
                          self.jump=2
                     else:
                          self.onplatform=0      
                          self.jump=2      
                          LEVEL_Y=FIXED_Y
                                    
            
            if self.level_x>=CANVAS_WIDTH/2 and self.pos[0]+ CANVAS_WIDTH/2 <=Back_obj.getWidth():
                Back_obj.move()#move background
            else:
                if self.pos[0] <= Back_obj.getWidth()-21:
                    self.level_x+=self.moveby#if background is not moving
                    
                
        elif self.pvelocity==-1:#moton in backward direction
            flag=self.Stop()
            if flag==1:
                return
            if self.level_x>15:
                self.pos[0]-=self.moveby
                self.level_x-=self.moveby
          
            if self.onplatform==1:
                if self.pos[0]-(PLAYER_SIZE[0]/4)*3<self.plat_x1:
                     #self.pos[1]=LEVEL_Y
                     flag1=self.platform_check()   
                     if flag1==1:
                        LEVEL_Y=400    
                        if self.jump==0:#if player is not jumping than fall
                          self.jump=2
                     else:
                          self.onplatform=0      
                          self.jump=2      
                          LEVEL_Y=FIXED_Y
                                
          
            
    def platform_check(self):
        
        for i in level1_platforms:#check if it is on any platform
              if self.pos[0]+PLAYER_SIZE[0]/4>=i[0] and self.pos[0]-(PLAYER_SIZE[0]/4)<=i[1]:
                     return 1
        return 0
    
    def Stop(self):#if any obstacle comes
       
        for i in level1_platforms:
            if i[0]== 1680 and i[1] == 1775 :
                if self.pos[0]+PLAYER_SIZE[0]/2 >i[0] and self.pos[0]+PLAYER_SIZE[0]/2 < i[1] :
                    return 0
            elif self.pvelocity==1 and self.pos[0] <i[1] and self.pos[1]>i[2] :
                if self.pos[0]+PLAYER_SIZE[0]/2 >i[0]:
                    return 1#in forward direction
            elif self.pvelocity ==-1 and self.pos[0]>i[0] and self.pos[1]>i[2]:
                if self.pos[0]-PLAYER_SIZE[0]/2 <i[1]:
                    return 1#in backward direction
      
    def draw(self,canvas):#draw the player object
        if self.slope==0:
            self.Slope()
        
        if self.slope==1:
            #print "moving_slope"
            self.move_slope()
        elif self.slope==0:
            #print "moving normal"
            self.Move()
            self.drop() 
        #check for drop
        
        self.Capture_Coins()# To check if a coin is captured
        
        if self.pvelocity == 1 :#moving in forward direction
            self.img_idx+=1
            if(self.img_idx==6):
                self.img_idx=0
            canvas.draw_image(pimg,pimg_coordinate[self.img_idx],(53,93),(self.level_x,self.pos[1]),(30,30))       
        
        elif self.pvelocity == 0:#standing in forward direction
            self.img_idx=1
            canvas.draw_image(pimg,pimg_coordinate[self.img_idx],(53,93),(self.level_x,self.pos[1]),(30,30))       
        elif self.pvelocity == -1:#moving in back direction
            self.img_idx-=1
            if(self.img_idx==-1):
               self.img_idx=5
            canvas.draw_image(pimg_ulta,pimg_coordinate[self.img_idx],(53,93),(self.level_x,self.pos[1]),(30,30))       
        elif self.pvelocity==-2:#standing in back direction
            self.img_idx=4
            canvas.draw_image(pimg_ulta,pimg_coordinate[self.img_idx],(53,93),(self.level_x,self.pos[1]),(30,30))       
       
      #  else:
       #   self.img_idx=4
        
    def drop(self):
        """
        function for drop
        """
        global Back_obj,FIXED_Y,PLAYER_SIZE
        for i in level1_khai:#if any khai comes
            if self.pos[0]+PLAYER_SIZE[0]/4>=i[0] and self.pos[0]-(PLAYER_SIZE[0]/4)<=i[1] and self.pos[1]>=FIXED_Y:
                self.jump=2#fallllll
                #LEVEL_Y=600
                
                self.restart=1#game is restrted
    

            
            
    def check_collision(self,level,type):
        
        global LEVEL_Y,enemy_1,score,enemy_die,player_die
        #if self.mushroom ==0 :
        #    self.pos[1]=380
        #    LEVEL_Y=380
        #else:
        #    self.pos[1]=370
        #    LEVEL_Y=370   
        
        if level==1: 
            for i in range(len(moving_enemy)):
                if type==1 and self.restart==0:
                    if self.pos[0]+PLAYER_SIZE[0]/2 >= enemy_1[i].x and self.pos[0] - PLAYER_SIZE[0]/2 <= enemy_1[i].x:
                        #print "xx"
                        if self.pos[1]+PLAYER_SIZE[0]/2 >=enemy_1[i].y:
                            enemy_idx=3
                            #print "yy"
                            score+=15
                            enemy_1[i].die()
                            enemy_die.rewind()
                            enemy_die.play()
                            
                elif type==0 and self.restart==0 and enemy_1[i].life==1:
                    if self.pos[0]+PLAYER_SIZE[0]/2>= enemy_1[i].x and self.pos[0]-PLAYER_SIZE[0]/2<=enemy_1[i].x:
                        #print "marja"
                        if self.pos[1]+PLAYER_SIZE[0]/2 >=enemy_1[i].y:
                            self.jump=2
                            self.restart=1	
                            score-=15
                            if self.plife==1:
                                player_die.rewind()
                                player_die.play()
        
    def Slope(self):#checks if player is on a slope
        global Back_obj,PLAYER_SIZE
        j=-1
        for i in level1_slope:
            j+=1
            if self.pos[0]-8>= i[0] and self.pos[0]+8<=i[1]:
                self.slope=1
                self.slope_idx=j
                return 
        
    
    def move_slope(self):#motion on slope
        global PLAYER_SIZE
        if self.pvelocity==1:
            self.pos[0]+=self.moveby 
            
            if self.level_x>=CANVAS_WIDTH/2 and self.pos[0]+ CANVAS_WIDTH/2 <=Back_obj.getWidth():
                Back_obj.move()#move background
            else:
                if self.pos[0] <= Back_obj.getWidth()-21:
                    self.level_x+=self.moveby
                    
            self.pos[1]+=self.moveby*level1_slope[self.slope_idx][2]
            #print "hey " + str(self.pos[0]) + " " + str(level1_slope[self.slope_idx][1])
            
            #print "hey " + str(self.pos[1]) + " " + str(level1_slope[self.slope_idx][3] ,level1_slope[self.slope_idx][2])
            
            if level1_slope[self.slope_idx][2] <0.0:  
                if self.pos[1]<=level1_slope[self.slope_idx][3]:
                    
                    print "in"
                    self.slope=0
                
            if level1_slope[self.slope_idx][2] >0.0:  
                if self.pos[1]>=level1_slope[self.slope_idx][3]:
                    
                    print "out"
                    self.slope=0
                    
        elif self.pvelocity==-1:
            self.pos[0]-=self.moveby
            self.level_x-=self.moveby          
  
            self.pos[1]-=self.moveby*level1_slope[self.slope_idx][2]
            
            #print "hey " + str(self.pos[0]) + " " + str(level1_slope[self.slope_idx][1])
            
            #print "hello " +str(self.pos[0])+" "+ str(self.pos[1]) + " " + str(level1_slope[self.slope_idx][4])
            
            if level1_slope[self.slope_idx][2] <0.0:  
                if self.pos[1]>=level1_slope[self.slope_idx][4]:
                    
                    #print "in negat"
                    #print self.pos[1]
                    self.slope=0
                
            if level1_slope[self.slope_idx][2] >0.0:  
                if self.pos[1]<=level1_slope[self.slope_idx][4]:
                    
                    #print "out pos"
                    #print self.pos[1]
                    self.slope=0
              
    
    def die(self):
       
        Back_obj.shift=0
        self.image_idx=1
        self.jump=0
        self.pvelocity = 0
        self.onplatform=0
        self.mushroom=0
        self.moveby=10
        self.restart=0
        self.level_x=self.pos[0]
        self.pvelocity=0    
        
        



class Capture_object:#objects that can be captured
    def __init__(self,pos,o_type):
        self.pos[0]=pos[0]
        self.pos[1]=pos[1]
        self.o_type=o_type
        self.visible = "True"
        
        
    def capture(self):
        self.visible = "False"
        
    def draw(self,canvas):
        if self.visible=="True":
            #canvas.draw_image(capture[self.o_type],self.pos,,,(10,10))
            a=1
         

class Enemy:
    def __init__(self,x1,x2,y1):
        self.x_1=x1#x from which enemy starts
        self.x_2=x2 # x at which enemy ends
        self.y=y1#height of enemy
        self.visible="True"
        self.moveby=5#initial velocity
        self.x=self.x_1#current position
        self.life=1
        
        
    def draw(self,canvas):
        global Back_obj
        if self.life==0:
            if self.y <=600:
                self.y+=2
            
        if self.life==1:
            self.move()
            canvas.draw_image(enemy,(15,15),(30,30),(self.x-Back_obj.shift,self.y+10),(30,30))
        elif self.life==0:
            canvas.draw_image(enemy,(75,15),(30,30),(self.x-Back_obj.shift,self.y+10),(30,30))
            
    def move(self):
        self.x+=self.moveby
        if(self.x>self.x_2):
           self.moveby=-1
        if self.x<=self.x_1:
            self.moveby=1
            
    def die(self):
        self.life=0
        
class Background:
    def __init__(self,level):
        self.level=level
        self.shift=0
        self.slope=5/6
        
    def draw(self,canvas):
        if self.level==1:
            canvas.draw_image(back_1,(800/2 + self.shift,430/2),(800,430),(400,220),(800,440))
        elif self.level==2:
            canvas.draw_image(back_2,(800/2+ self.shift,430/2),(800,430),(400,220),(800,440))
        elif self.level==3:
            canvas.draw_image(back_3,(800/2+ self.shift ,430/2),(800,430),(400,220),(800,440))
            
    def move(self):
        global player_1
        self.shift+=player_1.moveby

    def getWidth(self):
        if self.level==1:
            return 3500
        elif self.level==2:
            return 3000
        elif self.level==3:
            return 3000


def Place_Coins(canvas):
    global coin_idx,coin_pos_list
    coin_idx+=1
    if coin_idx==64:
        coin_idx=0
    j=0    
    for i in coin_pos_list:
        if coin_captured[j]==0:
            canvas.draw_image(coin1_img,coin_img_list[coin_idx],(64,64),(i[0]-Back_obj.shift,i[1]),(20,20))
        j+=1

def Setup_Coins():
    for i in range(0,8):
        for j in range(0,8):
            coin_img_list.append([32+i*64,32+j*64])
            
    length = len(coin_pos_list)
    
    #for i in range (0,length):
        #coin_captured.append(0)    
    
    
def Play_sound():
    stage1_back_sound.rewind()
    stage1_back_sound.play()

    
def keydown_handler(key):
    
    global player_1,FIXED_Y,LEVEL_Y
    if key==simplegui.KEY_MAP["right"]:
        player_1.move_h("RIGHT")
    if key==simplegui.KEY_MAP["left"]:
        player_1.move_h("LEFT")
    elif key==simplegui.KEY_MAP["up"]:
        if player_1.jump==0:
            player_1.jump=1      
            
def keyup_handler(key):
    
    global player_1
    if key==simplegui.KEY_MAP["right"]:
        player_1.pvelocity=0 
    if key==simplegui.KEY_MAP["left"]:
        player_1.pvelocity=-2 

       

def draw(canvas):
        
        global player_1,Back_obj,score,moving_enemy,game_over,stage1_back_sound
        if player_1.pos[0]>3300:
            game_over.rewind()
            game_over.play()
            canvas.draw_image(back_over,(200,200),(400,400),(400,220),(800,440))
            canvas.draw_text("Score - "+str(score), (270, 200), 70, 'Red')
            canvas.draw_text("YOU WON", (250, 100), 50, 'Red')
            canvas.draw_text("Press Restart for a New game", (150, 350), 40, 'Red')
        elif player_1.plife==0:
            canvas.draw_image(back_over,(200,200),(400,400),(400,220),(800,440))
            canvas.draw_text("Score - "+str(score), (270, 200), 70, 'Red')
            canvas.draw_text("GAME OVER", (250, 100), 50, 'Red')
            canvas.draw_text("Press Restart for a New Game", (150, 350), 40, 'Red')
            stage1_back_sound.pause()
            #player_die.stop()
            game_over.rewind()
            game_over.play()
            
        else:
            Back_obj.draw(canvas)
            player_1.draw(canvas)   
            Place_Coins(canvas)   
            for i in range(len(moving_enemy)):
                enemy_1[i].draw(canvas)
            canvas.draw_text("Score - "+str(score), (600, 30), 20, 'Red')
            canvas.draw_text("Life - "+str(player_1.plife), (600, 60), 20, 'Red')

# initialization frame
frame = simplegui.create_frame("SAVIOUR MARIO", 800, 440,150)
frame.set_canvas_background("Green")

timer = simplegui.create_timer(35000, Play_sound)
#

def Restart():
    global score,player_1,Back_obj,enemy_1,coin_captured,coin_pos_list,coin_idx
    coin_idx=0
    coin_captured=[]
    enemy_1=[]
    score=0
    player_1 = Player(1,1)
    Back_obj=Background(1)
   
    for i in range(len(coin_pos_list)):
         coin_captured.append(0)
    Setup_Coins()
    
    Play_sound()
    #background of the game
    enemy_1 = []
    for i in moving_enemy:
        enemy_1.append(Enemy(i[0],i[1],i[2]))
   
    timer.start()

Restart()
#create buttons and canvas callback
frame.add_button("Restart", Restart, 100)
#frame.add_button("Play", Play, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
frame.start()

