import pygame, sys
import random

from sqlalchemy import true

def ballanimation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <=0 or ball.bottom >= screen_h:
        ball_speed_y = -(ball_speed_y)
        pygame.mixer.Sound.play(boing_sound)
    if ball.left <= 0 or ball.right >= screen_w:
        ballreset()
    if ball.colliderect(opp) or ball.colliderect(player):
        ball_speed_x = -(ball_speed_x)
        pygame.mixer.Sound.play(boing_sound)

def playermovement():
    if ball_speed_x > 0:
        if player.bottom > ball.y:
            player.bottom -= player_speed
        if player.top < ball.y:
            player.top += player_speed
        if player.top <= 0:
            player.top = 0
        if player.bottom >= screen_h:
            player.bottom = screen_h

def oppmovement():
    if ball_speed_x < 0:
        if opp.bottom > ball.y:
            opp.bottom -= opp_speed
        if opp.top < ball.y:
            opp.top += opp_speed
        if opp.top <= 0:
            opp.top = 0
        if opp.bottom >= screen_h:
            opp.bottom = screen_h
def ballreset():
    global ball_speed_x, ball_speed_y, opp_score, player_score
    if ball.left <= 0:
        ball.center = (screen_w/2, screen_h/2)
        ball_speed_x *= random.choice((1,-1))
        ball_speed_y *= random.choice((1,-1))
        player_score += 1
    if ball.right >= screen_w:
        ball.center = (screen_w/2, screen_h/2)
        ball_speed_x *= random.choice((1,-1))
        ball_speed_y *= random.choice((1,-1))
        opp_score += 1

    
pygame.init()

boing_sound = pygame.mixer.Sound("boing.wav")
clock = pygame.time.Clock()

screen_w = 1280
screen_h = 960
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Pong')

ball = pygame.Rect((screen_w/2) - 15, (screen_h/2) - 15, 30, 30)
player = pygame.Rect(screen_w - 30, (screen_h/2) - 70, 15, 140)
opp = pygame.Rect(20, (screen_h/2) - 70, 15, 140)

bg_color = pygame.Color('grey12')
light_grey = (102,205,170)
white = (255,255,255)
gray = (193,205,205)
p_name = "Tweedledum"
o_name = "Tweedledee"

ball_speed_x = 9
ball_speed_y = 9
player_speed = 25
opp_speed = 25

player_score = 0
opp_score = 0
score_font = pygame.font.Font("freesansbold.ttf", 32)
bot_font = pygame.font.Font("freesansbold.ttf", 32)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#        if event.type == pygame.KEYDOWN:
 #           if event.key == pygame.K_DOWN:
 #               player_speed += 12
 #           if event.key == pygame.K_UP:
  #              player_speed -= 12
  #      if event.type == pygame.KEYUP:
  #          if event.key == pygame.K_DOWN:
   #             player_speed -= 12
   #         if event.key == pygame.K_UP:
   #             player_speed += 12

        
    oppmovement()
    ballanimation()
    playermovement()

    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey, player)
    pygame.draw.rect(screen,light_grey,opp)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (screen_w/2, 0), (screen_w/2,screen_h))

    player_text = score_font.render(f"{player_score}",True,white)
    screen.blit(player_text,(660,465))
    opp_text = score_font.render(f"{opp_score}",True,white)
    screen.blit(opp_text,(600,465))
    player_name = bot_font.render(f"{p_name}",True,white)
    screen.blit(player_name,((screen_w*.7), 50))
    opp_name = bot_font.render(f"{o_name}",True,white)
    screen.blit(opp_name,((screen_w*.15), 50))

    pygame.display.flip()
    clock.tick(165)
 
 
