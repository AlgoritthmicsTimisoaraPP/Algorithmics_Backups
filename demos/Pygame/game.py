from pygame import *
from Character import CharacterSprite
from Enemy import EnemySprite


window = display.set_mode((700, 500))
display.set_caption("Catch")

background = transform.scale(image.load("c:/Users/BB/Pictures/images_bb.jfif"), (700, 500))
background1 = transform.scale(image.load("C:\\Users\BB\\Pictures\\wallpaper\\yyu.jpg"), (700, 500))
print("\t__\n__")
window.blit(background, (0,0))
# window.blit(background1, (250,250))

c1 = CharacterSprite('C:\\Users\\BB\\Documents\\GitHub\\PyQt\\demos\\Pygame\\Cave_Vines.webp', 100, 100, 2)
c2 = EnemySprite('C:\\Users\\BB\\Documents\\GitHub\\PyQt\\demos\\Pygame\\spider.webp', 100, 50, 1)

game = True 
while game:
    
    window.blit(background,(0, 0))
    # window.blit(background1,(0, 300))
    for e in event.get():
        if e.type == QUIT:
           game = False
    c1.update(window)
    c2.update(window)
    c2.move_horizontal()
    if c1.collide(c2):
        print("Colision detected")
    c1.handle_events()
    
    display.update()
