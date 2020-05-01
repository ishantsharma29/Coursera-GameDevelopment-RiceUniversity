import simplegui, codeskulptor
import math
import time

speed_enemy=1
speed_duck=1
speed_player=5
speed_jump=2.5

PLAYER_SIZE = [30,30]
PLAYER_CENTER = [(64,64),(192,64)]
LEVEL_Y=[380,260,350]
ENEMY_SIZE = [55,55]
FLYINGDUCK_SIZE = [50,58]
Back_obj=[]
JUMP_MAX=90
CANVAS_WIDTH=800
FIXED_Y=[380,350,350]

LEVEL_PLATFORM=380
PLATFORM_IDX=-1
JUMP_SLOPE=0
ENEMY_IMAGE_FLAG=0
halt_flag=0
time1=0
time2=1

time1_duck=0
time2_duck=1

platform_idx=0
coin_idx=0
level=1
previous_level_x=0
previous_x=0
fire_idx=0

aImages = []
back_1=simplegui.load_image("https://dl.dropbox.com/s/kbsgisdfwuy7tye/SuperMarioWorldMap17BG.png?dl=1")
back_2=simplegui.load_image("https://dl.dropbox.com/s/rd0j99y8rza3f4p/level2.png?dl=1")
back_3=simplegui.load_image("https://dl.dropbox.com/s/k20plrpuiz56qw4/SuperMarioWorldMap17.png?dl=1")
coin1_img=simplegui.load_image("https://dl.dropbox.com/s/m4zp2fq05xmmlvg/screenshot_1353671388.png?dl=1")
pimg=simplegui.load_image("https://dl.dropbox.com/s/z4wx0dv9btejshw/mario3.png?dl=1")                               
pimg_ulta=simplegui.load_image("https://dl.dropbox.com/s/4lci512ctzsbdlg/mario2.png?dl=1")  
enemy=simplegui.load_image("https://dl.dropbox.com/s/ygkmb5o3695l4bs/smb_enemies_sheet.png?dl=1") 
back_over = simplegui.load_image("https://dl.dropbox.com/s/lpaigp63smkkcrx/back2.jpg?dl=1")
enemies = simplegui.load_image("https://dl.dropbox.com/s/1d99wyxy2xkt7tj/enemies.png?dl=1")
invert_enemies = simplegui.load_image("https://dl.dropbox.com/s/l6sd511ggy8yz3r/invert_enemy.png?dl=1")
fire = simplegui.load_image("https://dl.dropbox.com/s/8cyv6kie9e9ur12/firenew.png?dl=1")
question_marks = simplegui.load_image("https://dl.dropbox.com/s/xud555thcx0h50f/question.png?dl=1")
mushroom =simplegui.load_image("https://dl.dropbox.com/s/cdcbv1rfsqsgo4j/mushrum.png?dl=1")
gun_flower=simplegui.load_image("https://dl.dropbox.com/s/qi1dg625d11js9t/images_p.png?dl=1")
flyingduck=simplegui.load_image("https://dl.dropbox.com/s/2e3dyxi1yxyqbnd/duck.png?dl=1")
enemy_down=simplegui.load_image("https://dl.dropbox.com/s/ijd67inftyt6hpm/ulta_enemy.png?dl=1")
fruit=simplegui.load_image("https://dl.dropbox.com/s/e2g2h0cbf9fotzs/fruit.png?dl=1")
start_screen = simplegui.load_image("https://dl.dropbox.com/s/zzab2elctr24mos/1376340353_stretch.png?dl=1")
instructions = simplegui.load_image("https://dl.dropbox.com/s/1ywjmrnbkpuy62g/j5lDo8R.png?dl=1")

aImages.append(back_1)
aImages.append(back_2)
aImages.append(back_3)
aImages.append(coin1_img)
aImages.append(pimg)
aImages.append(pimg_ulta)
aImages.append(enemy)
aImages.append(back_over)
aImages.append(enemies)
aImages.append(invert_enemies)
aImages.append(fire)
aImages.append(question_marks)
aImages.append(mushroom)
aImages.append(gun_flower)
aImages.append(flyingduck)
aImages.append(enemy_down)
aImages.append(fruit)
aImages.append(start_screen)
aImages.append(instructions)
sounds= []
stage1_back_sound=simplegui.load_sound("https://dl.dropbox.com/s/qktaicguik6so7f/214_world_1_map.ogg?dl=1")
coin_sound=simplegui.load_sound("https://dl.dropbox.com/s/bhg0gpj1m099pkk/smb_coin.ogg?dl=1")
enemy_die =simplegui.load_sound("https://dl.dropbox.com/s/rdby2nacejxysq7/enemydie.ogg?dl=1")
player_die =  simplegui.load_sound("https://dl.dropbox.com/s/i4c79c9w61hr047/7d49d1_Super_Mario_Bros_Die_Sound_Effect.ogg?dl=1")
game_over = simplegui.load_sound("https://dl.dropbox.com/s/i4c79c9w61hr047/7d49d1_Super_Mario_Bros_Die_Sound_Effect.ogg?dl=1")

mushroom_sound = simplegui.load_sound("https://dl.dropbox.com/s/p99b2vc9q4wmpy4/Converted_file_306f01fe.ogg?dl=1")
duck_sound = simplegui.load_sound("https://dl.dropbox.com/s/abiukoyaj7qg2yp/duck.ogg?dl=1")
levelchange_sound = simplegui.load_sound("https://dl.dropbox.com/s/k70ak36304577jm/2cdd5c_New_Super_Mario_Bros_Pipe_Sound_Effect_conv.mp3?dl=1")
jump_sound = simplegui.load_sound("https://dl.dropbox.com/s/548nvdrrp583k0h/jump.ogg?dl=1")

sounds.append(stage1_back_sound)
sounds.append(coin_sound)
sounds.append(enemy_die)
sounds.append(player_die)
sounds.append(game_over)
sounds.append(mushroom_sound)
sounds.append(duck_sound)
sounds.append(levelchange_sound)
sounds.append(jump_sound)

coin_sound.set_volume(.3)
stage1_back_sound.set_volume(.4)
enemy_die.set_volume(.4)
player_die.set_volume(.5)
game_over.set_volume(.4)

mushroom_sound.set_volume(.5)
duck_sound.set_volume(.5)
levelchange_sound.set_volume(.7)
jump_sound.set_volume(.5)

pimg_coordinate=[[29,46],[87,46],[144,46],[201,46],[258,46],[315,46],[372,46],[429,46],[486,46],[543,46],[600,46],[657,46]]
level1_platforms = [[[1233,1305,320,1],[2246,2318,336,1],[4687,4760,329,1],[240,260,310,1],[1660,1680,315,1],[336,367,321,0],[434,510,272,0],[641,671,336,0],[785,814,336,0],[896,926,336,0],[977,1007,353,0],[1041,1071,336,0],[1346,1437,257,0],[1712,1775,321,1],[1840,1872,336,0],[2112,2127,288,0],[2127,2143,336,0],[2352,2382,289,0],[2706,2750,354,0],[2750,2850,410,0],[2850,2877,337,0],[2877,2979,410,0],[2979,3006,337,0],[3106,3215,336,0]],
                    [[33,85,277,0],[365,417,306,0],[476,528,277,0],[586,610,306,0],[670,721,304,0],[806,860,277,0],[917,941,165,0],[1027,1081,222,0],[1168,1219,333,0],[1664,1716,278,0]],
                     [] ]
level1_khai= [[[390,410],[719,735],[846,864],[943,976],[1742,1794],[2670,2703],[3373,3440],[4654,4800]],
              [[418,475],[529,585],[611,669],[722,805],[861,916],[942,1026],[1082,1167],[1220,1358]],
                [] ]
level1_slope = [[1440,1505,.5,272,303,-448],[1472,1565,-.5,350,304,1086],[2000,2080,-1,337,254,2334],[2080,2112,1,256,286,-1824],[2112,2127,0,288,288,288],[1565,1632,0,304,304,304],[3442,3520,0,304,304,304],[3520,3567,1,304,353,-3216],[3567,3647,0,353,353,353],[3647,3678,-1,353,320,4000],[3678,3744,0,320,320,320],[3744,3792,1,320,369,-3424],[3792,3855,0,369,369,369],[3855,3919,-1,369,305,4224],[3919,3968,0,305,305,305],[3968,4016,1,305,353,-3663],[4016,4079,0,353,353,353],[4079,4111,-1,353,321,4432],[4111,4175,0,321,321,321],[4175,4240,(1),321,380,-3854]]
coin_pos_list=[(440,260),(470,260),(500,260),(760,370),(830,370),(1150,325),(1170,325),(1190,325),(1210,325),(1230,325),(1250,325),(908,303),(991,332),(1025,364),(1487,338),(1514,338),(1538,338),(1639,314),(1669,314),(1699,314),(1719,244),(2087,258),(2137,258),(2234,324),(2251,324),(2268,324),(2463,331),(2493,331),(2523,331),(2553,331),(2583,331),(2613,331),(2807,324),(2898,310),(2930,310),(2960,310),(2990,310),(3240,310),(3270,310),(3300,310),(3558,263),(3588,263),(3618,263),(3770,263),(3800,263),(3830,263),(4000,263),(4030,263),(4060,263),(4300,263),(4350,263),(4400,263)]

power_position=[[250,325,0],[1670,330,0]]
fruit_position1 = [[114,310],[2457,341],[3160,278],[3480,268],[3604,317],[3950,270],[2502,343]]
fruit_position2 = [[216,255],[383,230],[500,192],[1123,284],[1434,262],[1464,262],[1494,262]]
fruit_position3 = [[189,268],[365,263],[762,263]]

fruit_level1 = []
fruit_level2 = []
fruit_level3 = []
Shots=[]
coin_img_list=[]
coin_captured=[]
score=0

moving_enemy = [[530,641,380],[1082,1180,380],[1180,1341,380],[1452,1631,380],[2386,2655,380],[2406,2665,380],[2426,2675,380],[2759,2847,400],[2895,2974,400],[3010,3103,380],[3567,3645,352],[3793,3855,369],[4016,4075,351],[4242,4608,380],[4269,4618,380],[4368,4648,380]]

moving_duck = [[10,336,375,1],[525,639,375,0],[738,784,375,1],[2142,2351,375,0],[3217,3372,380,0],[4299,4628,380,0],[4329,4638,380,0]]
flying_duck= [[610,665,200,350,0],[770,770,200,350,0],[1000,1000,75,240,0],[1280,1280,270,370,0]]
flying_duck_level2 = [[100,500,250,350,1],[100,500,200,300,1],[350,550,200,300,1],[350,550,150,250,1],[590,590,200,300,0],[640,640,200,300,0],[690,690,200,300,0]]
coin_pos_list_2 =[]
enemy_2_level2 = []

class Player:
    
    def __init__(self,player_type,level,name):
        global LEVEL_Y
        if level==1:
            self.pos=[40,LEVEL_Y[level-1]]
        elif level==2:
            self.pos[0,0]
        elif level==3:
            sel.pos=[0,0]
        self.name=name
        self.level_x=self.pos[0]
        self.ptype=player_type
        self.plife=3
        self.image_idx=1
        self.jump=0
        self.pvelocity = 0
        self.onplatform=0
        self.mushroom=0
        self.moveby=10
        LEVEL_Y[level-1]=380
        self.restart=0
        self.slope=0
        self.zinda=1
        self.gun=0
    
    def Capture_Coins(self):
        j=0
        global coin_sound,score,level
        for i in coin_pos_list:
            if coin_captured[j] == 0:
                if self.pos[0]+PLAYER_SIZE[0]/2>=i[0] and self.pos[0]-PLAYER_SIZE[0]/2<=i[0] and i[1]>=self.pos[1]-PLAYER_SIZE[1]/2 and i[1]<=self.pos[1]+PLAYER_SIZE[1]/2:
                    coin_captured[j]=1
                    score+=10
                    coin_sound.rewind()
                    coin_sound.play()
            j+=1
    def Capture_fruits(self):
        global score,level,coin_sound
        
        j=0
        if level==1:    
            for i in range(len(fruit_level1)):
                if fruit_level1[j].taken=="False":
                    if self.pos[0]+PLAYER_SIZE[0]/2>=fruit_level1[j].x and self.pos[0]-PLAYER_SIZE[0]/2<=fruit_level1[j].x and fruit_level1[j].y>=self.pos[1]-PLAYER_SIZE[1]/2 and fruit_level1[j].y<=self.pos[1]+PLAYER_SIZE[1]/2:
                        fruit_level1[j].taken="True"
                        coin_sound.rewind()
                        coin_sound.play()
                        score+=20
                j+=1
        j=0        
        if level==2:    
            for i in range(len(fruit_level2)):
                if fruit_level2[j].taken=="False":
                    if self.pos[0]+PLAYER_SIZE[0]/2>=fruit_level2[j].x and self.pos[0]-PLAYER_SIZE[0]/2<=fruit_level2[j].x and fruit_level2[j].y>=self.pos[1]-PLAYER_SIZE[1]/2 and fruit_level2[j].y<=self.pos[1]+PLAYER_SIZE[1]/2:
                        fruit_level2[j].taken="True"
                        coin_sound.rewind()
                        coin_sound.play()
                        score+=20
                j+=1
                
        if level==3:    
            for i in fruit_level3:
                if i.taken=="False":
                    if self.pos[0]+PLAYER_SIZE[0]/2>=i.x and self.pos[0]-PLAYER_SIZE[0]/2<=i.x and i.y>=self.pos[1]-PLAYER_SIZE[1]/2 and i.y<=self.pos[1]+PLAYER_SIZE[1]/2:
                        i.taken="True"
                        coin_sound.rewind()
                        coin_sound.play()
                        score+=20
        
        
        
    def Detect_questionmark(self):
        """ detect collision with question mark blocks on upside motin of player. if a block arrives player hit it and turn back
        and power or any flower,mushrum etc comes out,i[2] indicates that block is explored and its image changes
        """
        for i in power_position:
            if self.pos[0] >= i[0]-12.5 and self.pos[0] <=i[0]+12.5 and self.pos[1]-PLAYER_SIZE[1]/2==i[1]+15:
               self.jump=2
               i[2]=1
                
    def move_h(self,direction):                    
        if direction == "LEFT":
            self.pvelocity=-1
        else: 
            self.pvelocity=1
        
    def Jump(self):                                
        global LEVEL_Y,FIXED_Y,PLAYER_SIZE,LEVEL_PLATFORM,PLATFORM_IDX,level,speed_jump
        if self.jump==1:                           
            self.Detect_questionmark()             
            self.check_collision_duck(0)
            self.check_collision(1)	
            self.pos[1]-=speed_jump                          
            if self.pos[1] <= LEVEL_Y[level-1]-JUMP_MAX:
                self.jump=2                        
                LEVEL_Y[level-1]=FIXED_Y[level-1]   
                if self.mushroom==0 and level==2:
                    FIXED_Y[level-1]=345
                    LEVEL_Y[level-1]=FIXED_Y[level-1]
        x=0
        if level==2:
            x+=10
        
        if self.jump==2:
            self.pos[1]+=speed_jump						
            self.check_collision(1)				
            self.check_collision_duck(1)			
            self.check_collision_duck(0)
            if self.restart==0:						
                k=0
                for i in level1_platforms[level-1]:
                    k+=1
                    if self.pos[0]+PLAYER_SIZE[0]/4>=i[0] and self.pos[0]-(PLAYER_SIZE[0]/4)<=i[1] and self.pos[1]+PLAYER_SIZE[0]/4 <= i[2] : 
                        if self.pos[1] >= i[2]-PLAYER_SIZE[1]/2:
                            self.jump=0
                            self.onplatform=1		
                            self.plat_x1=i[0]		
                            self.plat_x2=i[1]		
                            self.pos[1]=i[2]-10		
                            LEVEL_Y[level-1]=i[2]-PLAYER_SIZE[1]/3-x
                            LEVEL_PLATFORM=i[2]-PLAYER_SIZE[1]/3-x
                            PLATFORM_IDX=k			
                            
                if self.pos[0]>=2706 and self.pos[0] <= 2979:
                    if self.mushroom==1:
                        LEVEL_Y[level-1]=390
                        print "hey"
                    elif self.mushroom==0:
                        LEVEL_Y[level-1]=400
                        print "hey 1"
                if self.slope==0:					
                    if self.pos[1]>= LEVEL_Y[level-1]:
                        self.jump=0
                        self.pos[1]=LEVEL_Y[level-1]
                if self.slope==1:					 
                    if self.pos[1]>=level1_slope[self.slope_idx][2]*self.pos[0] + level1_slope[self.slope_idx][5]:
                        self.jump=0
                        self.pos[1]=level1_slope[self.slope_idx][2]*self.pos[0] + level1_slope[self.slope_idx][5]
                        
            else:										
                if self.pos[1]>=460:					
                    
                    print 'dying' + " " + str(level)
                    self.die() 
                    player_die.rewind()
                    player_die.play()
                    
    
    def Move(self):
        
        global CANVAS_WIDTH,Back_obj,PLAYER_SIZE,level,speed_player
        
        if self.jump==1 or self.jump==2:				
            if level==1:
                self.moveby=speed_player/2
            elif level==2:
                self.moveby=(speed_player/4)
            elif level==3:
                self.moveby=(speed_player/4)
            self.Jump()
        else:
            
            if level==1:
                self.moveby=speed_player
            elif level==2:
                self.moveby=(speed_player/2)
            elif level==3:
                self.moveby=(speed_player/2)
            self.check_collision(0)  					
            self.check_collision_duck(0)				
        
        if self.pvelocity==1:							
            flag=self.Stop()							
            if self.pos[0] < 3510 or self.pos[0] >4250:
                if flag==1:								
                    return
            self.pos[0]+=self.moveby					
            
            if self.onplatform==1:						
                if self.pos[0]-(PLAYER_SIZE[0]/4)>self.plat_x2 :
                      if self.jump==0:					
                        self.jump=2
                        LEVEL_Y[level-1]=FIXED_Y[level-1] 
                        if self.mushroom==0 and level==2:
                            FIXED_Y[level-1]=345
                            LEVEL_Y[level-1]=FIXED_Y[level-1]
                      self.onplatform=0
                                   
            if level==1:								
                if self.level_x>=CANVAS_WIDTH/2 and self.pos[0]+ (CANVAS_WIDTH*.80) <=Back_obj[0].getWidth():
                    Back_obj[level-1].move()						
                else:
                    if self.pos[0] <= Back_obj[level-1].getWidth()-21:
                        self.level_x+=self.moveby		
            if level==2:
                if self.level_x>=CANVAS_WIDTH/2 and self.pos[0]+ CANVAS_WIDTH/2 <=Back_obj[level-1].getWidth():
                    Back_obj[level-1].move()					
                else:
                    if self.pos[0] <= Back_obj[level-1].getWidth()-21:
                        self.level_x+=self.moveby		
            if level==3:
                if self.pos[0] <= Back_obj[level-1].getWidth()-5:
                    self.level_x+=self.moveby			
                    
        elif self.pvelocity==-1:						
            flag=self.Stop()
            if flag==1:
                return
            if self.level_x>15:
                self.pos[0]-=self.moveby
                self.level_x-=self.moveby
          
            if self.onplatform==1:
                if self.pos[0]+(PLAYER_SIZE[0]/4)<self.plat_x1:
                     if self.jump==0:
                        self.jump=2
                        LEVEL_Y[level-1]=FIXED_Y[level-1]
                        if self.mushroom==0 and level==2:
                            FIXED_Y[level-1]=345
                            LEVEL_Y[level-1]=FIXED_Y[level-1]
                     self.onplatform=0
                                
    def move_slope(self):	

        global PLAYER_SIZE,JUMP_SLOPE,level,speed_player
        if self.jump==1 or self.jump==2:				
            self.moveby=speed_player/2   
            self.jump_slope()
        else:
            self.moveby=speed_player/1.5
            self.check_collision(0) 
            self.check_collision_duck(0)
            
            
        if self.pvelocity==1:
            
            self.pos[0]+=self.moveby 
  
            if self.level_x>=CANVAS_WIDTH/2 and self.pos[0]+ CANVAS_WIDTH/2 <=Back_obj[level-1].getWidth():
                Back_obj[level-1].move()
            else:
                if self.pos[0] <= Back_obj[level-1].getWidth()-21:
                    self.level_x+=self.moveby
                    
            if JUMP_SLOPE==0:        	
                self.pos[1]=level1_slope[self.slope_idx][2]*self.pos[0] + level1_slope[self.slope_idx][5]-10
                LEVEL_Y[level-1]=self.pos[1]
           
            if self.pos[0] < level1_slope[self.slope_idx][0] or self.pos[0] > level1_slope[self.slope_idx][1]:
                self.slope=0
                if self.mushroom==1:
                    LEVEL_Y[level-1]=370
                elif self.mushroom==0:
                    LEVEL_Y[level-1]=380
                if self.jump==0:
                    self.jump=2
        elif self.pvelocity==-1:
            self.pos[0]-=self.moveby
            self.level_x-=self.moveby          
            if JUMP_SLOPE==0:        
                self.pos[1]=level1_slope[self.slope_idx][2]*self.pos[0] + level1_slope[self.slope_idx][5]-10
                LEVEL_Y[level-1]=self.pos[1]
            
            if self.pos[0] < level1_slope[self.slope_idx][0] or self.pos[0] > level1_slope[self.slope_idx][1]:
                self.slope=0
                if self.mushroom==1:
                    LEVEL_Y[level-1]=370
                elif self.mushroom==0:
                    LEVEL_Y[level-1]=380
                if self.jump==0:
                    self.jump=2
                    
    def jump_slope(self):
        global PLAYER_SIZE,LEVEL_PLATFORM,PLATFORM_IDX,JUMP_SLOPE,level,speed_jump   
        if self.jump==1:
            self.pos[1]-=speed_jump
          
            if self.pos[1] <= LEVEL_Y[level-1]-JUMP_MAX:
                print LEVEL_Y[level-1]-JUMP_MAX
                print "on slope  = " + str(self.slope)
                self.jump=2
                
        if self.jump==2:
            self.pos[1]+=speed_jump
            self.check_collision(1)				
            self.check_collision_duck(1)			
            self.check_collision_duck(0)

            if self.restart==0:
                if self.pos[1]>=level1_slope[self.slope_idx][2]*self.pos[0] + level1_slope[self.slope_idx][5]-10:
                    print self.slope_idx
                    self.jump=0
                    JUMP_SLOPE=0
                    
                    self.pos[1]=level1_slope[self.slope_idx][2]*self.pos[0] + level1_slope[self.slope_idx][5]-10
            else:										
                if self.pos[1]>=460:					
                    
                    print 'dying' + " " + str(level)
                    self.die() 
                    player_die.rewind()
                    player_die.play()
          
            
    def platform_check(self):
        """checks if player is on any platform"""
        global PLATFORM_IDX,level
        k=0
        for i in level1_platforms[level-1]:				
              k+=1
              if self.pos[0]+PLAYER_SIZE[0]/4>=i[0] and self.pos[0]-(PLAYER_SIZE[0]/4)<=i[1] and self.pos[1]+PLAYER_SIZE[0]/4<=i[2]:
                PLATFORM_IDX=k 
                self.plat_x1=i[0]						
                self.plat_x2=i[1]						
                return 1
        PLATFORM_IDX=-1
        return 0
    
    def Stop(self):										
        global level
        if level==3:
            return 0
        x=0
        if level==2:
            x+=.4
        for i in level1_platforms[level-1]:				
            if self.pvelocity==1 and self.pos[0] <i[1] and self.pos[1]+PLAYER_SIZE[0]/4 > i[2] and i[3]==0 :
                if self.pos[0]+PLAYER_SIZE[0]*(.35+x) >i[0]:
                    return 1
                                                           
            elif self.pvelocity ==-1 and self.pos[0]>i[0] and self.pos[1]+PLAYER_SIZE[0]/4 > i[2] and i[3]==0:
                if self.pos[0]-PLAYER_SIZE[0]*(.35+x) <i[1]:
                    return 1							
        if level==1:
            if self.pos[0]+PLAYER_SIZE[0]/2>=240 and self.pos[0]-PLAYER_SIZE[0]/2<=260 and self.pos[1]-PLAYER_SIZE[1]/2 <=325 and self.pos[1]+PLAYER_SIZE[1]/8>=305:
                return 1
            if self.pos[0]+PLAYER_SIZE[0]/2>=1660 and self.pos[0]-PLAYER_SIZE[0]/2<=1680 and self.pos[1]-PLAYER_SIZE[1]/2 <=330 and self.pos[1]+PLAYER_SIZE[1]/8>=310:
                return 1
                
    def draw(self,canvas):								
        global JUMP_SLOPE,LEVEL_Y,level,JUMP_MAX
        self.slope= self.Slope()						
        
        if level==1:
            JUMP_MAX=90
        elif level==2:
            JUMP_MAX=140
        elif level==3:
            JUMP_MAX=140
        if self.slope==1:
            self.move_slope()							
        elif self.slope==0:
            self.Move()
            self.drop() 								
        
        self.Capture_Coins()							
        self.Capture_fruits()
        if self.pvelocity == 1 :						
            self.img_idx+=1
            if(self.img_idx==6):
                self.img_idx=0
            canvas.draw_image(pimg,pimg_coordinate[self.img_idx],(53,93),(self.level_x,self.pos[1]),(PLAYER_SIZE[0],PLAYER_SIZE[1]))       
        
        elif self.pvelocity == 0:						
            self.img_idx=1
            canvas.draw_image(pimg,pimg_coordinate[self.img_idx],(53,93),(self.level_x,self.pos[1]),(PLAYER_SIZE[0],PLAYER_SIZE[1]))       
        elif self.pvelocity == -1:						
            self.img_idx-=1
            if(self.img_idx==-1):
               self.img_idx=5
            canvas.draw_image(pimg_ulta,pimg_coordinate[self.img_idx],(53,93),(self.level_x,self.pos[1]),(PLAYER_SIZE[0],PLAYER_SIZE[1]))       
        elif self.pvelocity==-2:						
            self.img_idx=4
            canvas.draw_image(pimg_ulta,pimg_coordinate[self.img_idx],(53,93),(self.level_x,self.pos[1]),(PLAYER_SIZE[0],PLAYER_SIZE[1]))       
       
      
        
    def drop(self):
        """
        function for drop
        """
        global Back_obj,PLAYER_SIZE
        for i in level1_khai[level-1]:
            if self.pos[0]+PLAYER_SIZE[0]/4>=i[0] and self.pos[0]-(PLAYER_SIZE[0]/4)<=i[1] and self.pos[1]>=FIXED_Y[level-1]:
                self.jump=2
                self.restart=1
         
    def check_collision(self,type):
        global enemy_1,score,enemy_die,player_die,powers,level,halt_flag,halt1,halt2,mushroom_sound
          
        if halt_flag==0:
            if level==1: 							
                for i in range(len(moving_enemy)):		
                    if type==1 and self.restart==0:		
                        if self.pos[0]+PLAYER_SIZE[0]/2 >= enemy_1[i].x and self.pos[0] - PLAYER_SIZE[0]/2 <= enemy_1[i].x:
                            if self.pos[1]+PLAYER_SIZE[1]/2 >=enemy_1[i].y-ENEMY_SIZE[1]/4:
                                
                                score+=15
                                enemy_1[i].die()
                                enemy_die.rewind()
                                enemy_die.play()
                                
                    elif type==0 and self.restart==0 and enemy_1[i].life==1:
                        if self.pos[0]+PLAYER_SIZE[0]/2>= enemy_1[i].x and self.pos[0]-PLAYER_SIZE[0]/2<=enemy_1[i].x:
                            if self.pos[1]+PLAYER_SIZE[1]/2 >=enemy_1[i].y-ENEMY_SIZE[1]/4:
                                if self.mushroom==1:
                                    halt_flag=1
                                    halt1=time.time()
                                    
                                    self.mushroom=0
                                    self.jump=1
                                    LEVEL_Y[0]=380
                                    FIXED_Y[0]=380
                                    PLAYER_SIZE[0]=30
                                    PLAYER_SIZE[1]=30
                                    continue
                                self.jump=2				
                                self.restart=1	
                                score-=15
                                if self.plife==1:
                                    player_die.rewind()
                                    player_die.play()
                 
                if flower_flag <3 and self.pos[0]>641 and self.pos[0]<671 and self .pos[1]> 300:
                    self.jump=2
                    self.restart=1	
                    score-=15
                    if self.plife==1:
                        player_die.rewind()
                        player_die.play()
                        
                for i in powers:
                    if i.flower==1 and i.power_taken==0:
                        if self.pos[0]>=i.x1-15 and self.pos[0]<=i.x1+15:
                            if self.pos[1]>=i.y1-45 and i.y1+15>=self.pos[1]:
                                i.power_taken=1
                                if i.x1==250:
                                    self.mushroom=1
                                    mushroom_sound.rewind()
                                    mushroom_sound.play()
                                    halt_flag=1
                                    halt1=time.time()
                                    PLAYER_SIZE[0]=30
                                    PLAYER_SIZE[1]=50
                                    LEVEL_Y[0]=370
                                    FIXED_Y[0]=370
                                elif i.x1==1670:
                                    self.plife+=1
                                    mushroom_sound.rewind()
                                    mushroom_sound.play()
                            
                if self.pos[0]>1871 and self.pos[0]<1900 and self.pos[1]>=325:   
                    self.jump=2
                    self.restart=1	
                    score-=15
                    if self.plife==1:
                        player_die.rewind()
                        player_die.play()
            
            
                    
    def check_collision_duck(self,type):
        global enemy_2,score,enemy_die,player_die,enemy_3,level,halt1,halt_flag,duck_sound
        if halt_flag==1:
            return
        if level==1: 
            for i in range(len(moving_duck)):
                if type==1 and self.restart==0:
                    if self.pos[0]+PLAYER_SIZE[0]/2 >= enemy_2[i].x and self.pos[0] - PLAYER_SIZE[0]/2 <= enemy_2[i].x:
                        if self.pos[1]+PLAYER_SIZE[0]/2 >=enemy_2[i].y-ENEMY_SIZE[1]/4:
                            enemy_idx=3
                            score+=15
                            duck_sound.rewind()
                            duck_sound.play()
                            enemy_2[i].die()
                            self.jump=1        
                elif type==0 and self.restart==0 and enemy_2[i].life==1:
                    if self.pos[0]+PLAYER_SIZE[0]/2>= enemy_2[i].x and self.pos[0]-PLAYER_SIZE[0]/2<=enemy_2[i].x:
                        if self.pos[1]+PLAYER_SIZE[0]/2 >=enemy_2[i].y-ENEMY_SIZE[1]/4:
                            if self.mushroom==1:
                                self.mushroom=0
                                self.jump=1
                                halt_flag=1
                                halt1=time.time()
                                LEVEL_Y[0]=380
                                FIXED_Y[0]=380
                                PLAYER_SIZE[0]=30
                                PLAYER_SIZE[1]=30
                                continue
                            self.jump=2
                            self.restart=1	
                            score-=15
                            if self.plife==1:
                                player_die.rewind()
                                player_die.play()                                    
        if level==2:
            for i in range(len(flying_duck)):
                if self.pos[0] > enemy_3[i].x -FLYINGDUCK_SIZE[0]/2 and self.pos[0]< enemy_3[i].x + FLYINGDUCK_SIZE[0]/2 :
                    if self.pos[1]>enemy_3[i].y -FLYINGDUCK_SIZE[1]/2 and self.pos[1] <enemy_3[i].y+FLYINGDUCK_SIZE[0]/2 and self.jump==1:
                        if self.mushroom==1:
                            self.mushroom=0
                            halt_flag=1
                            LEVEL_Y[1]=350
                            FIXED_Y[1]=350
                            PLAYER_SIZE[0]=30
                            PLAYER_SIZE[1]=30
                            halt1=time.time()
                            Restart_level2()
                        else:
                            self.zinda=0
                            self.jump=2				
                            self.restart=1	
                            score-=15
                            if self.plife==1:
                                player_die.rewind()
                                player_die.play()
                    elif self.pos[1] +PLAYER_SIZE[1]/2 > enemy_3[i].y - FLYINGDUCK_SIZE[1]/2 and self.jump==2 and self.zinda==1:
                        score+=15
                        self.jump=1
                        duck_sound.rewind()
                        duck_sound.play()
                        enemy_3[i].die()
                        enemy_die.rewind()
                        enemy_die.play()       
        if level==3:
            
            for i in range(len(enemy_3_level2)):
                if self.pos[0] > enemy_3_level2[i].x -FLYINGDUCK_SIZE[0]/2 and self.pos[0]< enemy_3_level2[i].x + FLYINGDUCK_SIZE[0]/2 :
                    if self.pos[1]>enemy_3_level2[i].y -FLYINGDUCK_SIZE[1]/2 and self.pos[1] <enemy_3_level2[i].y+FLYINGDUCK_SIZE[0]/2 and self.jump==1 and enemy_3_level2[i].life==1:
                        if self.mushroom==1:
                            self.mushroom=0 
                            halt_flag=1
                            halt1=time.time()
                           
                            Restart_level3()
                        else:
                            self.zinda=0
                            self.jump=2				
                            self.restart=1	
                            score-=15
                            if self.plife==1:
                                player_die.rewind()
                                player_die.play()
                    elif self.pos[1] +PLAYER_SIZE[1]/2 > enemy_3_level2[i].y - FLYINGDUCK_SIZE[1]/2 and self.jump==2 and self.zinda==1 and enemy_3_level2[i].life==1:
                        score+=15
                        self.jump=1
                        duck_sound.rewind()
                        duck_sound.play()
                        enemy_3_level2[i].die()
                        enemy_die.rewind()
                        enemy_die.play()  
                        
            for i in range(len(enemy_2_level2)):
                
                if type==1 and self.restart==0:
                    if self.pos[0]+PLAYER_SIZE[0]/2 >= enemy_2_level2[i].x and self.pos[0] - PLAYER_SIZE[0]/2 <= enemy_2_level2[i].x:
                        if self.pos[1]+PLAYER_SIZE[0]/2 >=enemy_2_level2[i].y-ENEMY_SIZE[1]/4:
                            duck_sound.rewind()
                            duck_sound.play()
                            score+=15
                            enemy_2_level2[i].die()
                            self.jump=1
                
                elif type==0 and self.restart==0 and enemy_2_level2[i].life==1:
                    if self.pos[0]+PLAYER_SIZE[0]/2>= enemy_2_level2[i].x and self.pos[0]-PLAYER_SIZE[0]/2<=enemy_2_level2[i].x:
                        if self.pos[1]+PLAYER_SIZE[0]/2 >=enemy_2_level2[i].y-ENEMY_SIZE[1]/4:
                            if self.mushroom==1:
                                self.mushroom=0
                                halt_flag=1
                                halt1=time.time()
                                
                                self.jump=1
                                Restart_level3()
                                continue
                            self.jump=2
                            self.restart=1	
                            score-=15
                            if self.plife==1:
                                player_die.rewind()
                                player_die.play()               
          
    def Slope(self):								
        global Back_obj,PLAYER_SIZE,level
        j=-1
        if level==1:
            for i in level1_slope:
                j+=1
                if self.pos[0]>= i[0] and self.pos[0]<=i[1] and (self.pos[1] < i[3] or self.pos[1] < i[4]):
                    self.slope=1
                    self.slope_idx=j				
                    return 1
        return 0

    def die(self):
       
        global level,Back_obj
        level=1
        self.pos=[40,FIXED_Y[level-1]]
        self.plife-=1   
        Back_obj[0].shift=0
        Back_obj[1].shift=0
        Back_obj[2].shift=0
        self.image_idx=1
        self.jump=0
        self.pvelocity = 0
        self.onplatform=0
        self.mushroom=0
        self.moveby=10
        self.restart=0
        self.level_x=self.pos[0]
        self.pvelocity=0    
   
class Fruit:							
    def __init__(self,x,y):
       
        self.x=x
        self.y=y
        self.taken = "False"
      
    def capture(self):
        self.taken = "True"
  
    def draw(self,canvas):
        if self.taken=="False":
            canvas.draw_image(fruit,(30,29.5),(60,59),(self.x-Back_obj[level-1].shift,self.y),(20,20))

class Enemy:
    def __init__(self,x1,x2,y1):
        
        global ENEMY_SIZE,speed_enemy
        
        self.x_1=x1
        self.x_2=x2 -ENEMY_SIZE[0]/4
        self.y=y1
        self.visible="True"
        self.moveby=speed_enemy
        self.x=self.x_1
        self.life=1
    
    def draw(self,canvas):
        """ draws image of enemy,when in motion"""
        global Back_obj,ENEMY_IMAGE_FLAG,time1,time2,level
        
        time2= time.time()								
        if self.life==0:								
            if self.y <=600:
                self.y+=2
            
        if self.life==1 and level==1:
            self.move()									
            if time2-time1 < .3 :						
                if self.moveby<0:
                    canvas.draw_image(enemies,(20,340),(40,40),(self.x-Back_obj[level-1].shift,self.y+10),(55,55))
                elif self.moveby>0:
                    canvas.draw_image(invert_enemies,(380,340),(40,40),(self.x-Back_obj[level-1].shift,self.y+10),(55,55))
            else:
                if self.moveby<0:
                    canvas.draw_image(enemies,(60,340),(40,40),(self.x-Back_obj[level-1].shift,self.y+10),(55,55))
                elif self.moveby>0:
                    canvas.draw_image(invert_enemies,(420,340),(40,40),(self.x-Back_obj[level-1].shift,self.y+10),(55,55))
                
            if time2-time1 >.6:
                time1=time.time()
                
        elif self.life==0:
            canvas.draw_image(enemy_down,(60,1008),(40,40),(self.x-Back_obj[level-1].shift,self.y+10),(55,55))
            
    def move(self):
        global speed_enemy
        self.x+=self.moveby
        if(self.x>self.x_2):
           self.moveby=-speed_enemy
        if self.x<=self.x_1:
           self.moveby=speed_enemy
            
    def die(self):
        self.life=0
        
        
class Enemy_Duck:
    def __init__(self,x1,x2,y1,typ):
        global ENEMY_SIZE,speed_duck
        self.x_1=x1													
        self.x_2=x2-ENEMY_SIZE[0]/4 								
        self.y=y1													
        self.visible="True"
        self.moveby=speed_duck												
        self.x=(self.x_2+self.x_1)/2												
        self.life=1
        self.typ=typ
        self.jump=0
        
    def draw(self,canvas):
        global Back_obj,ENEMY_IMAGE_FLAG,time1_duck,time2_duck,level,player_1,level
        
        time2_duck= time.time()
        if self.life==-1:                    
            canvas.draw_image(enemy_down,(180,1328),(40,40),(self.x-Back_obj[level-1].shift,self.y+10),(55,55))
            if self.jump==1:
                if self.y>=LEVEL_Y[level-1]-15:
                    self.y-=2
                else:
                    self.jump=2
                    
            elif self.jump==2:
                if self.y <=600:
                    self.y+=3
                else:
                    self.jump=0
            
        if self.life==1:
            self.move()
            if time2_duck-time1_duck < .3 :
                if self.moveby<0:
                    canvas.draw_image(enemies,(260,20),(40,40),(self.x-Back_obj[level-1].shift,self.y+10),(55,55))
                elif self.moveby>0:
                    canvas.draw_image(invert_enemies,(140,20),(40,40),(self.x-Back_obj[level-1].shift,self.y+10),(55,55))
            else:
                if self.moveby<0:
                    canvas.draw_image(enemies,(300,20),(40,40),(self.x-Back_obj[level-1].shift,self.y+10),(55,55))
                elif self.moveby>0:
                    canvas.draw_image(invert_enemies,(180,20),(40,40),(self.x-Back_obj[level-1].shift,self.y+10),(55,55))
            if time2_duck-time1_duck >.6:
                time1_duck=time.time()
                
        elif self.life==0:						
            self.move()										
            self.collision_with_duck()						
            if self.moveby <0:								
                self.moveby=-10
            elif self.moveby >0:
                self.moveby=10
            if self.typ==1:									
                if self.x<=self.x_1:
                    self.life=-1         
            canvas.draw_image(enemies,(180,20),(40,40),(self.x-Back_obj[level-1].shift,self.y+15),(55,55))

    def move(self):
        global speed_duck
        self.x+=self.moveby
        if(self.x>self.x_2):
            if self.life==1:
               self.moveby=-speed_duck
            else:
               self.moveby=-(1.5*speed_duck)                        
        if self.x<=self.x_1:
            if self.life==1:
               self.moveby=speed_duck
            else:
               self.moveby=(1.5*speed_duck)
        
    def die(self):
        
        self.life-=1
        self.jump=1
        
    def collision_with_duck(self):
            global enemy_1,score,enemy_die,player_die,player_1,level,halt_flag,halt1
            if level==1: 
                for i in range(len(moving_enemy)):
                    if player_1.restart==0 and enemy_1[i].life==1:
                        if enemy_1[i].x+ENEMY_SIZE[0]/2 >= self.x and enemy_1[i].x- ENEMY_SIZE[0]/2 <=  self.x :
                           
                            if enemy_1[i].y+ENEMY_SIZE[1]/2 >=self.y:
                                enemy_idx=3
                                score+=15
                                enemy_1[i].die()
                                enemy_die.rewind()
                                enemy_die.play()
                                
            if player_1.restart==0:
                if player_1.pos[0]+PLAYER_SIZE[0]/2>= self.x and player_1.pos[0]-PLAYER_SIZE[0]/2<=self.x:
                                    
                    if player_1.pos[1]+PLAYER_SIZE[0]/2 >=self.y and player_1.jump==0:
                        if player_1.mushroom==1:
                            player_1.mushroom=0
                            halt_flag=1
                            halt1=time.time()
                                
                            self.jump=1
                            return
                        player_1.jump=2
                        player_1.restart=1	
                        score-=15
                        if player_1.plife==1:
                            player_die.rewind()
                            player_die.play()
             
class Flying_Duck:
    """ this is class of enemy of flying duck type"""
    def __init__(self,x1,x2,y1,y2,typ):
        
        global ENEMY_SIZE,speed_duck
        self.x_1=x1															
        self.x_2=x2-ENEMY_SIZE[0]/4 										
        self.y_1=y1															
        self.y_2=y2
        self.visible="True"
        self.moveby=speed_duck														
        self.x=(self.x_2+ self.x_1)/2
        self.y=self.y_1
        self.life=1															
        self.typ=typ														
        self.idx=0									
      
    def draw(self,canvas):
        global Back_obj,ENEMY_IMAGE_FLAG,time1_duck,time2_duck,level,player_1,enemy_2_level2,level
        
        if self.life==1:
            self.move_vertical()
            if self.idx<5:
                canvas.draw_image(flyingduck,(self.idx*39.6+19.8,186.5),(40,53),(self.x-Back_obj[level-1].shift,self.y),(50,63))
                self.idx+=1
            elif self.idx<10:
                canvas.draw_image(flyingduck,((self.idx-5)*39.6+19.8,234.5),(40,43),(self.x-Back_obj[level-1].shift,self.y),(50,53))
                self.idx+=1
            else:
                canvas.draw_image(flyingduck,((self.idx-5)*39.6+19.8,234.5),(40,43),(self.x-Back_obj[level-1].shift,self.y),(50,53))
                self.idx=0        
        elif self.life==0:			
            if self.typ==0:			
                canvas.draw_image(flyingduck,(55,275),(40,40),(self.x-Back_obj[level-1].shift,self.y+15),(55,55))
                if self.y<=600:
                    self.y+=2
                else:
                    self.life=-1
            elif self.typ==1:		
                if self.y<=LEVEL_Y[level-1]:
                    self.y+=2
                    canvas.draw_image(enemies,(300,20),(40,40),(self.x-Back_obj[level-1].shift,self.y+10),(55,55))
                else:
                    enemy_2_level2.append(Enemy_Duck(self.x_1,self.x_2,LEVEL_Y[level-1],1))
                    self.life=-1
                    canvas.draw_image(enemies,(300,20),(40,40),(self.x-Back_obj[level-1].shift,self.y+10),(55,55))
    
    def move_vertical(self):
        global speed_duck
        self.y+=self.moveby
        if(self.y>self.y_2):
            self.moveby=-speed_duck
        if self.y<=self.y_1:
            self.moveby=speed_duck

    def die(self):
        self.life=0          
      
class Power:
    def __init__(self,x1,y1,typ):
        self.typ=typ                                          
        self.flower=0										  
        self.idx=0											   				
        self.x1=x1		
        self.y1=y1
        self.power_taken=0										
                                
    def draw(self,canvas):
            global  Back_obj,level
            if level==1:
                for i in power_position:
                    if i[2]==0:   
                        canvas.draw_image(question_marks,(27.5,27.5),(55,55),(i[0]-Back_obj[level-1].shift,i[1]),(20,20))       
                    elif i[2]==1:
                        canvas.draw_image(question_marks,(81,27.5),(55,55),(i[0]-Back_obj[level-1].shift,i[1]),(20,20))
                    
                    if self.x1==i[0] and self.y1==i[1] and i[2]==1:
                        self.flower=1
                    if self.x1==250:
                        if self.flower==1 and self.power_taken==0:  		
                            if self.idx<98:
                                self.idx+=8
                            else:
                                self.idx=98
                            canvas.draw_image(mushroom,(98,self.idx),(196,2*self.idx),(i[0]-Back_obj[level-1].shift,i[1]-10-self.idx/7.5),(30,2*(self.idx/7.5)))             
                    elif self.x1==1670:
                        if self.flower==1 and self.power_taken==0:  		
                            if self.idx<107.5:
                                self.idx+=8
                            else:
                                self.idx=107.5
                            canvas.draw_image(gun_flower,(110.5,self.idx),(221,2*self.idx),(i[0]-Back_obj[level-1].shift,i[1]-10-self.idx/7.5),(30,2*(self.idx/7.5)))          
                    
            
class Background:
    def __init__(self,level):
        self.level=level
        self.shift=0
        self.slope=5/6
        
    def draw(self,canvas):
        if self.level==1:
            canvas.draw_image(back_1,(800/2 + self.shift,430/2),(800,430),(400,220),(800,440))
        elif self.level==2:
            canvas.draw_image(back_2,(800/2+ self.shift,440/2),(800,440),(400,220),(800,440))
        elif self.level==3:
            canvas.draw_image(back_3,(800/2+ self.shift ,440/2),(800,440),(400,220),(800,440))
            
    def move(self):
        global player_1
        self.shift+=player_1.moveby

    def getWidth(self):
        if self.level==1:
            return 5300
        elif self.level==2:
            return 1750
        elif self.level==3:
            return 1000


def Place_Coins(canvas):
    global coin_idx,coin_pos_list,coin_pos_list_2,level
    coin_idx+=1
    if coin_idx==64:
        coin_idx=0
    j=0    
    for i in coin_pos_list:
        if coin_captured[j]==0:
            canvas.draw_image(coin1_img,coin_img_list[coin_idx],(64,64),(i[0]-Back_obj[level-1].shift,i[1]),(20,20))
        j+=1

def Setup_Coins():
                
    global level    					
    for i in range(0,8):
        for j in range(0,8):
            coin_img_list.append([32+i*64,32+j*64])
            
    length = len(coin_pos_list[0])

def go_to_2nd_level():
    """func to go to 2nd lvel frm first level,we save the position of player in 1st level 
    so as to restore it when the player returns
    """
    global level,player_1,PLATFORM_IDX,previous_level_x,previous_x
    previous_x=player_1.pos[0]
    player_1.pos[0]=40
    player_1.pos[1]=260
    if player_1.mushroom==1:
        player_1.pos[0]=40
        player_1.pos[1]=250	
        LEVEL_Y[1]=250
        FIXED_Y[1]=330
        
    previous_level_x=player_1.level_x
    player_1.level_x=40
    level=2  
    player_1.image_idx=1#initial image 
    player_1.jump=0
    player_1.moveby=5
    player_1.pvelocity = 0
    player_1.onplatform=1
    player_1.slope=0
    PLATFORM_IDX=-1
    player_1.plat_x1=33#start of platform
    player_1.plat_x2=85#end of platform

def go_backto_1st_level():
    """func to go back to 1st level frm second and third  level,we have the position of player in 1st level 
    therfore we restore it when the player returns and moves backgrnd as well
    """
    global level,player_1,PLATFORM_IDX,previous_level_x,Back_obj,previous_x
    
    if player_1.mushroom==0:
        LEVEL_Y[0]=380
        FIXED_Y[0]=380
    else:
        LEVEL_Y[0]=370
        FIXED_Y[0]=370
    
    if level==2:
        player_1.pos[0]=990
        player_1.pos[1]=345
        if player_1.mushroom==1:
            player_1.pos[1]=340
        
    if level==3:
        player_1.pos[0]=2100
        player_1.pos[1]=260
        if player_1.mushroom==1:
            player_1.pos[1]=255
    
    player_1.level_x=previous_level_x
    player_1.moveby=10
    player_1.image_idx=1#initial image 
    player_1.jump=0
    player_1.pvelocity = 0
    player_1.onplatform=1
    player_1.slope=0
    PLATFORM_IDX=-1
    if level==2:
        player_1.plat_x1=977#start of platform
        player_1.plat_x2=1007#end of platform
        Back_obj[0].shift+=990-previous_x
    if level==3:
        
        Back_obj[0].shift+=2100-previous_x
    level=1 
    
    
def go_to_3rd_level():
    """transition frm 1st to 3rd level"""
    global level,player_1,PLATFORM_IDX,previous_level_x,previous_x
    previous_x=player_1.pos[0]
    player_1.pos[0]=40
    player_1.pos[1]=260
    player_1.moveby=5
    if player_1.mushroom==1:
        player_1.pos[0]=40
        player_1.pos[1]=250	
        LEVEL_Y[2]=340
        FIXED_Y[2]=340
    previous_level_x=player_1.level_x
    player_1.level_x=40
    level=3
    player_1.image_idx=1#initial image 
    player_1.jump=2
    player_1.pvelocity = 0
    player_1.onplatform=0
    player_1.slope=0
    PLATFORM_IDX=-1
    
    
def Play_sound():
    stage1_back_sound.rewind()
    stage1_back_sound.play()


flag_level2_done=0
flag_level3_done=0
    
def keydown_handler(key):
    
    global player_1,JUMP_SLOPE,level,jump_sound,levelchange_sound,flag_level2_done,flag_level3_done
    if key==simplegui.KEY_MAP["right"]:
        
        if player_1.pos[0]>770 and level==3:
            if player_1.pos[1]>=320:
                levelchange_sound.rewind()
                levelchange_sound.play()
                go_backto_1st_level()
        player_1.move_h("RIGHT")        
    if key==simplegui.KEY_MAP["left"]:
        player_1.move_h("LEFT")
    elif key==simplegui.KEY_MAP["up"]:
        if player_1.slope==1:
            JUMP_SLOPE=1
            player_1.jump=1 
        elif player_1.jump==0:
            player_1.jump=1 
            jump_sound.rewind()
            jump_sound.play()
    elif key==simplegui.KEY_MAP["down"]:
        """to go through the pipe in some other level"""
        if player_1.pos[0]>785 and player_1.pos[0]<814 and level==1:
            if player_1.pos[1]>=320 and flag_level2_done==0:                
                levelchange_sound.rewind()
                levelchange_sound.play()
                flag_level2_done=1
                go_to_2nd_level()
        elif player_1.pos[0]>1664 and player_1.pos[0]<1716 and level==2:
            if player_1.pos[1]>=245:
                levelchange_sound.rewind()
                levelchange_sound.play()
                go_backto_1st_level()
        elif player_1.pos[0]>1840 and player_1.pos[0]<1872 and level==1:
            if player_1.pos[1]>=320 and flag_level3_done==0:
                levelchange_sound.rewind()
                levelchange_sound.play()
                flag_level3_done=1
                go_to_3rd_level()
                
        
                
def keyup_handler(key):
    
    global player_1
    if key==simplegui.KEY_MAP["right"]:
        player_1.pvelocity=0 
    if key==simplegui.KEY_MAP["left"]:
        player_1.pvelocity=-2 
    
    if key==simplegui.KEY_MAP["space"]:
        
        Shots.append(Gun_shots(player_1.pos[0],player_1.pos[1],level))
       
def draw_fire(canvas):
    
        
        global fire_idx,Back_obj,level
        canvas.draw_image(fire,(30.75,21),(61.5,42),(1944-Back_obj[level-1].shift,361),(148,65))
        if fire_idx <= 3:
            canvas.draw_image(fire,(30.75+ 61.5*(fire_idx),21),(61.5,42),(1944-Back_obj[level-1].shift,361),(148,65))
        elif fire_idx<=7:
            canvas.draw_image(fire,(30.75+ 61.5*(fire_idx-4),66),(61.5,44),(1944-Back_obj[level-1].shift,361),(148,65))
        elif fire_idx<=11:
            canvas.draw_image(fire,(30.75+ 61.5*(fire_idx-8),119),(61.5,44),(1944-Back_obj[level-1].shift,361),(148,65))
        elif fire_idx<=13:
            canvas.draw_image(fire,(30.75+ 61.5*(fire_idx-8),168),(61.5,44),(1944-Back_obj[level-1].shift,361),(148,65))
        else:
            fire_idx=-1
        
        fire_idx+=1
        
        
flower_flag=0    #global variables for draw_flower     
flower_idx=0
time_flower1=0
time_flower2=0

def draw_flower(canvas):
    
        global time_flower1,time_flower2,flower_idx,flower_flag,Back_obj,level,player_1
        
        temp=0
        
        if player_1.level_x>=CANVAS_WIDTH/2 and player_1.pos[0]+ CANVAS_WIDTH/2 <=Back_obj[level-1].getWidth():
            temp=player_1.moveby
        
        if player_1.pvelocity==1:
            temp=temp*1
        elif player_1.pvelocity==-1:
            temp=temp*-1
        elif player_1.pvelocity==0:
            temp=0
        time_flower2=time.time()
        
        if flower_flag==0:					#flower is coming out of pipe slowly with increasing flower_idx,for that we shift 
            flower_idx +=.5					#the center of image we are displaying with time
            if flower_idx ==11 :
                flower_flag =1
            canvas.draw_image(invert_enemies,(20,520+flower_idx),(40,2*flower_idx),(655-Back_obj[level-1].shift+temp,345-flower_idx),(75,2*flower_idx))
            canvas.draw_image(invert_enemies,(20,520+flower_idx),(40,2*flower_idx),(1055-Back_obj[level-1].shift+temp,345-flower_idx),(75,2*flower_idx))
        elif flower_flag==1:				#flower is completel out ,and remains same for 10 seconds
            canvas.draw_image(invert_enemies,(20,580),(40,40),(655-Back_obj[level-1].shift+temp,340),(75,40))
            canvas.draw_image(invert_enemies,(20,580),(40,40),(1055-Back_obj[level-1].shift+temp,340),(75,40))
            if time_flower2-time_flower1 > 10:
               flower_flag=2
        elif flower_flag==2:                #flower is going down with decreaing flower_idx
            flower_idx -=.5
            if flower_idx ==1:
                flower_flag=3
            canvas.draw_image(invert_enemies,(20,520+flower_idx),(40,2*flower_idx),(655-Back_obj[level-1].shift+temp,345-flower_idx),(75,2*flower_idx))
            canvas.draw_image(invert_enemies,(20,520+flower_idx),(40,2*flower_idx),(1055-Back_obj[level-1].shift+temp,345-flower_idx),(75,2*flower_idx))
        else:								#flower is inside the pipe
            if time_flower2-time_flower1 > 20:
               time_flower1=time.time()
               flower_flag=0

                                

def draw(canvas):
        
        global player_1,score,moving_enemy,game_over,stage1_back_sound,Back_obj,level
        global enemy_2,powers,enemy_3,enemy_3_level2,halt1,halt2,halt_flag
        if halt_flag==1:
            halt()
        if player_1.pos[0]>5000:
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
            game_over.rewind()
            game_over.play()
            
        else:												#draw level
            if level==1:
                Back_obj[level-1].draw(canvas)
            elif level==2:
                Back_obj[level-1].draw(canvas)
            elif level==3:
                Back_obj[level-1].draw(canvas)
            player_1.draw(canvas)  
            
            if level==1:
                Place_Coins(canvas)  

                for i in range(len(moving_enemy)):                #draw enemy
                    enemy_1[i].draw(canvas)
                    
                    
                for i in range(len(moving_duck)):					#draw duck
                    enemy_2[i].draw(canvas)
                
                
                for i in range(len(power_position)):				#draw question marks
                    powers[i].draw(canvas)
                
                for i in range(len(fruit_position1)):
                    fruit_level1[i].draw(canvas)
                
                draw_fire(canvas)
                draw_flower(canvas)
                
                for i in range(len(Shots)):
                    Shots[i].draw(canvas)
                
            if level==2:
                for i in range(len(flying_duck)):					#draw flying duck
                    enemy_3[i].draw(canvas)
                
                for i in range(len(fruit_position2)):
                    fruit_level2[i].draw(canvas)
            if level==3:
                for i in range(len(flying_duck_level2)):					#draw flying duck
                    enemy_3_level2[i].draw(canvas)
                for i in range(len(enemy_2_level2)):    
                    enemy_2_level2[i].draw(canvas)
                
                for i in range(len(fruit_position3)):
                    fruit_level3[i].draw(canvas)
            
                
            
            canvas.draw_text("Score - "+str(score), (600, 30), 20, 'Red')
            canvas.draw_text("Life - "+str(player_1.plife), (600, 60), 20, 'Red')
            
            

# initialization frame
frame = simplegui.create_frame("SAVIOUR MARIO", 800, 440,150)
frame.set_canvas_background("Green")
timer = simplegui.create_timer(35000, Play_sound)
#

index=0

def Restart():
    
    global score,player_1,Back_obj,enemy_1,coin_captured,coin_pos_list,coin_idx,level
    global enemy_2,powers,enemy_3,enemy_3_level2,startgame,index
    
    stage1_back_sound.rewind()
    stage1_back_sound.play()
    
    startgame=1
    level=1
    coin_idx=0
    coin_captured=[]
    enemy_1=[]
    index+=1
    score=0
    player_1 = Player(1,1,"Priyu " + str(index))
    
    PLAYER_SIZE[0]=30
    PLAYER_SIZE[1]=30
    LEVEL_Y=[380,260,350]
    FIXED_Y=[380,350,350]
    
    for i in range(3):
        Back_obj.append(Background(i+1))
        Back_obj[i].shift=0
    
    for i in range(len(coin_pos_list)):
         coin_captured.append(0)
    Setup_Coins()
    
    
    player_1.zinda=1
    
    #Play_sound()
    #background of the game
    enemy_1 = []
    for i in moving_enemy:								#small moving enemy list of objects
        enemy_1.append(Enemy(i[0],i[1],i[2]))
   
    enemy_2 = []
    for i in moving_duck:
        enemy_2.append(Enemy_Duck(i[0],i[1],i[2],i[3]))   #moving duck object list    
    powers = []    
    print powers
    
    for i in power_position:							#powers object list
        powers.append(Power(i[0],i[1],i[2]))
        
    for i in power_position:	
        i[2]=0
    
    enemy_3 = []										#moving duck object list
    for i in flying_duck:
        enemy_3.append(Flying_Duck(i[0],i[1],i[2],i[3],i[4]))
    
    enemy_3_level2 = []										#moving duck object list
    for i in flying_duck_level2:
        enemy_3_level2.append(Flying_Duck(i[0],i[1],i[2],i[3],i[4]))
    
    #fruits at different level    
  
    for i in fruit_position1:
        fruit_level1.append(Fruit(i[0],i[1]))
        
    for i in fruit_position2:
        fruit_level2.append(Fruit(i[0],i[1]))
        
    for i in fruit_position3:
        fruit_level3.append(Fruit(i[0],i[1]))
 
    timer.start()
    
def Restart_level2():
    global level,player_1,PLATFORM_IDX,previous_level_x,previous_x
    player_1.pos[0]=40
    player_1.pos[1]=260
    player_1.level_x=40
    level=2  
    Back_obj[level-1].shift=0
    player_1.image_idx=1#initial image 
    player_1.jump=0
    player_1.pvelocity = 0
    player_1.onplatform=1
    player_1.slope=0
    PLATFORM_IDX=-1
    player_1.plat_x1=33#start of platform
    player_1.plat_x2=85#end of platform
    
def Restart_level3():
    global level,player_1,PLATFORM_IDX,previous_level_x,previous_x
    player_1.pos[0]=40
    player_1.pos[1]=260
    player_1.level_x=40
    level=3 
    Back_obj[level-1].shift=0
    player_1.image_idx=1#initial image 
    player_1.jump=2
    player_1.pvelocity = 0
    player_1.onplatform=0
    player_1.slope=0
    PLATFORM_IDX=-1
    
time1=time.time()
time1_duck=time.time()
startgame=0
    
def Start_game(canvas):
    
    global startgame
    
    if startgame==0:
        canvas.draw_image(start_screen,(315,354/2),(630,354),(400,220),(800,440)) 
    elif startgame==1:
        draw(canvas)
    elif startgame==2:
        canvas.draw_image(instructions,(300,424),(600,848),(400,220),(800,440)) 
        
        
halt1=0
halt2=0
halt_flag=0

def halt():
    global halt1,halt2,halt_flag
    halt2=time.time()
    if halt2-halt1>=2:
        halt_flag=0
        halt1=0

def Reset():
    global startgame
    startgame=0
    stage1_back_sound.rewind()
    stage1_back_sound.pause()

def Show_Instructions():   
    global startgame
    startgame=2 
    

def Load_Game(canvas):
    
    img_count = 19
    loaded_img_count = 0

    for aImg in aImages:
        if aImg.get_width() != 0:
            loaded_img_count += 1
    
    tot_sound=9
    loaded_sounds = 0
    for snd in sounds:
        if snd is not None:
            loaded_sounds += 1
    
    if loaded_img_count < img_count or loaded_sounds < tot_sound:
        canvas.draw_text("Please Wait !!! :) ", (200, 100), 50, 'Red')
        canvas.draw_text("Images loaded  " + str(loaded_img_count) + "/20", (200, 200), 50, 'Red')
        canvas.draw_text("Sounds loaded  " + str(loaded_sounds) + "/9", (200, 300), 50, 'Red')        
    else: 
        Start_game(canvas)
            
frame.add_button("Play", Restart, 100)
frame.add_button("Reset", Reset, 100)
frame.add_button("Instructions", Show_Instructions, 100)
frame.set_draw_handler(Load_Game)
frame.set_canvas_background('Black')
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
frame.start()

