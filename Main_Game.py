import pygame as pg

pg.init()

display_width = 800
display_height = 600

gameDisplay = pg.display.set_mode((display_width, display_height))
pg.display.set_caption("A bit Racey")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73

clock = pg.time.Clock()
crashed = False
carImg = pg.image.load("car.png")

startPosX = ( display_width * 0.35)
startPosY = (display_height * 0.5)

def car(x,y):
    gameDisplay.blit(carImg, (x,y) )

def game_loop():
    x = startPosX
    y = startPosY
    x_change = 0
    y_change = 0
    car_speed = 0

    gameExit = False

    while not gameExit:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameExit = True
        
        ### Movement

        # Check if a key has been clicked
        if event.type == pg.KEYDOWN:
            # Left or right (Cant go both at same time)
            if event.key == pg.K_LEFT:
                x_change = -5
            elif event.key == pg.K_RIGHT:
                x_change = 5

            # Up or down (Cant go both at same time)
            if event.key == pg.K_UP:
                y_change = -5
            elif event.key == pg.K_DOWN:
                y_change = 5

        # Check if user stopped clicking
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                x_change = 0
            if event.key == pg.K_UP or event.key == pg.K_DOWN:
                y_change = 0


        # Update car location
        x += x_change
        y += y_change

        # Make background white
        gameDisplay.fill(white)
        # Show car at new location
        car(x,y)

        # Car Boundary
        if x > display_width - car_width or x<0 or y > display_height or y<0:
            x = startPosX
            y = startPosY
        
        # Update display & tick clock 60 frames forward
        pg.display.update()
        clock.tick(60)


# Call the game loop
game_loop()
# Quit program once the gameloop has ended
pg.quit()
quit()
