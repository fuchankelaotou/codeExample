################################################################################################
#
# TODO: Replace these comments with your own...
# I'm sorry we turned in late work. The reason for this is that during this period of time
# I have been vaccinated, resulting in fever, headache and other symptoms,
# which makes me very uncomfortable. I reflected the situation to the professor,
# who understood me and accepted my request to hand in my overdue homework.
# The professor asked me to reflect the situation to TA
#


# Header comments (Author, Date, Description, Class, etc)
#
# Example PyGame program provided to students as the basis for
# Assignment A5 - An Avoider Game.
#
################################################################################################

import math, pygame, random, sys

################################################################################################
# Helper Functions

# pixel_collision()
#   - Test if two sprite masks overlap
#   - Do NOT modify.  This is written for you.
def pixel_collision( mask1, rect1, mask2, rect2 ):
    offset_x = rect2[0] - rect1[0]
    offset_y = rect2[1] - rect1[1]
    # See if the two masks at the offset are overlapping.
    overlap = mask1.overlap( mask2, (offset_x, offset_y) )
    return overlap

################################################################################################
# Sprite Class
#
#   A basic Sprite class that can draw itself, move, and test collisions
#
#   Do NOT modify.  This is written for you.
#
class Sprite:

    def __init__( self, image ):
        self.image = image
        self.rectangle = image.get_rect()
        self.mask = pygame.mask.from_surface( image )

    def set_position( self, new_position ):
        self.rectangle.center = new_position

    def draw( self, screen ):
        screen.blit( self.image, self.rectangle )

    def is_colliding( self, other_sprite ):
        return pixel_collision( self.mask, self.rectangle, other_sprite.mask, other_sprite.rectangle )

################################################################################################
# Enemy Class
#
#   TODO: 1) Implement the TODO items below.  
#         2) Fill in comments here for what this class does.
#
#            This class make the the image could overlap on the window and show up in a random place
#            and also is for enemy to make them move randomly and when
#            they touch the edge, make them bounce back in to the window.
#            with tuple.
class Enemy:

    def __init__( self, image, screen_width, screen_height ):
        self.image = image
        self.mask = pygame.mask.from_surface( image )
        self.rectangle = image.get_rect()
        self.rectangle.center = (random.randint(0, screen_width), random.randint(0, screen_height))
        self.speed=(random.randint(-5,5),random.randint(-5,5))

    def move( self ):
        self.rectangle.center=(self.rectangle.center[0]+self.speed[0],self.rectangle.center[1]+self.speed[1])

    def bounce( self, screen_width, screen_height ):
            if self.rectangle.top >= screen_height or self.rectangle.bottom <= 0:
                self.speed=(self.speed[0],-self.speed[1])
            if self.rectangle.left >= screen_width or self.rectangle.right <= 0:
                self.speed=(-self.speed[0],self.speed[1])

    def draw(self, screen):
        # Same draw as Sprite - Do not modify.
        screen.blit(self.image, self.rectangle)

class DropEnemy(Enemy):
    def __init__(self, image, screen_width, screen_height):
        super().__init__(image, screen_width, screen_height,)
        self.position=(random.randint(0, screen_width), random.randint(0, screen_height))
    #     Assign random positions to items

    def move(self):
        # self.position=(self.position[0]+self.speed[0],self.position[1]+self.speed[1]+.5)
        self.speed=(self.speed[0],self.speed[1]+.2)
        # Give gravity to objects
        return super().move()

# class DropEnemy(Enemy):
#

#     def __init__(self, image, screen_width, screen_height):
#         super().__init__(image, screen_width, screen_height)
#         self.position = self.rectangle.center
#         self.speed = [0, 0.5]
#
#     def move( self ):
#         x,y=self.position
#         vx,vy=self.speed
#         x += vx
#         y+= vy
#         self.position=[x,y]
#         self.rectangle.center = self.position





################################################################################################
# PowerUp Class
#
#   TODO: 1) Implement the TODO item below.  
#         2) Fill in comments here for what this class does.

#             this class make powerup image to overlap and shw up on a random place on the window with tuple.
#
class PowerUp:

    def __init__( self, image, screen_width, screen_height ):
        # TODO: Set the PowerUp position randomly like is done for the Enemy class.
        # There is no speed for this object as it does not move.
        self.image = image
        self.mask = pygame.mask.from_surface( image )
        self.rectangle = image.get_rect()
        self.rectangle.center = (random.randint(0, screen_width), random.randint(0, screen_height))

    def draw( self, screen ):
        # Same as Sprite - Do not modify.
        screen.blit( self.image, self.rectangle )

class PowerUpRotate(PowerUp):
    def __init__(self, image, screen_width, screen_height):
        super().__init__(image, screen_width, screen_height)
        self.angle = 0
        # Angle - initialize it to 0
        self.original_image = image

    def draw(self, screen):
        self.angle+=5
        # Apply rotation to the object and specify a uniform speed
        rotated_image = pygame.transform.rotate(self.original_image, self.angle)
        self.image = rotated_image
        position = self.rectangle.center
        # Redefine image
        self.rectangle = self.image.get_rect()
        self.rectangle.center = position
        self.mask = pygame.mask.from_surface(self.image)
        super().draw(screen)
        # Use super() to call the draw method in the powerup class

################################################################################################

def main():

    # Colors
    TEAL = ( 0, 0, 75 )

    # Setup pygame
    pygame.init()

    clock = pygame.time.Clock() # Used to control FPS
    FPS = 30 # max frames per second


    # Make the mouse invisible.
    pygame.mouse.set_visible( False )
    # pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

    # Get a font for printing the lives left on the screen.
    myfont = pygame.font.SysFont( 'monospace', 24 )

    # Define the screen
    s_width, s_height = 600, 400
    size = s_width, s_height
    screen = pygame.display.set_mode( size )



    # Load image assets
    # Choose your own image
    enemy_image = pygame.image.load( "jj1.png" ).convert_alpha()
    # Here is an example of scaling it to fit a 50x50 pixel size.
    enemy_image_1 = pygame.transform.smoothscale( enemy_image, (50, 50) )

    DropEnemy_image=pygame.image.load( "jj11.png" ).convert_alpha()
    DropEnemy_image_1 = pygame.transform.smoothscale( DropEnemy_image, (50, 50) )



    # TODO: Make some number of initial enemies that will bounce around the screen.
    enemy_sprites = []

    # This is the character you control. TODO: Choose your image.
    player_image = pygame.image.load( "jj2.png" ).convert_alpha()     #load the image and make it in exact pixels.
    player_image_1 = pygame.transform.smoothscale(player_image, (50, 50))       #make the image siza in 50*50.
    player_sprite = Sprite( player_image_1 )        #use the sprite class and make it work.
    health = 5

    # This is the powerup image. TODO: Choose your image.
    power = pygame.image.load( "jj3.png" ).convert_alpha()
    powerrotate=pygame.image.load( "jj10.png" ).convert_alpha()

    # Start with an empty list of powerups and add them (in the main game loop) as the game runs.
    powerups = []

    # Main Game Loop
    is_playing = True
    pause = True # Whether to pause after game ends...
    frame = 1

    while is_playing:
        # TODO: Modify the loop to stop when health is <= to 0.
        if health <=0:
            break
        # Check for events
        for event in pygame.event.get():
            # Stop loop if user clicks on window close button
            if event.type == pygame.QUIT:
                is_playing = False
                pause = False # User killed game, don't pause...
                continue
        # Make the player follow the mouse
        pos = pygame.mouse.get_pos()
        player_sprite.set_position( pos )
        # TODO: Make a new Enemy instance once each second and add it to enemy_sprites.
        #   - Use the frame number mod FPS to know when a second has passed.
        #   - You might choose to change how / when new enemies are created
        #     based on your Creative Element game addition.

        #     enemy_sprites.append(Enemy(enemy_image_1,s_width,s_height))
        # TODO:  Loop over the enemy sprites. If the player sprite is
        # colliding with an enemy, deduct from the health variable.
        # A player is likely to overlap an enemy for a few iterations
        # of the game loop - experiment to find a small value to deduct that
        # makes the game challenging but not frustrating.
        if frame % FPS == 0:
            # make the enemy_image move per sec.
            for enemy_sprite in enemy_sprites:
                if Sprite.is_colliding(player_sprite,enemy_sprite):     #when the player_image touches the enemy_image, reduce one blood.
                    health-=1
            # Trigger blood deduction when touching the enemy
            if random.random() < 0.5:
             # Make enemies appear in random alternation
                enemy_sprites.append(Enemy(enemy_image_1, s_width, s_height))
            else:
                enemy_sprites.append(DropEnemy(DropEnemy_image_1, s_width, s_height))
            frame = 0

        # TODO: Loop over the powerups. If the player sprite is colliding, add
        # 1 to health.
        for powerup in powerups:
            if player_sprite.is_colliding(powerup):     #make the player_image when touches the enemy_image, increase one blood.
                health += 1

        # TODO: Make a list comprehension that removes powerups that are colliding with
        # the player sprite.
        powerups=[x for x in powerups if not player_sprite.is_colliding(x)]     #use comprehension to create a list holds the powerups if the player image didnt
                                                                                #touch the powerups.



        # TODO: Loop over the enemy_sprites. Each enemy should call move and bounce.
        for enemy in enemy_sprites:
            enemy.move()
            enemy.bounce(s_width,s_height)

        # TODO: Choose a random number. Use the random number to decide to add a new
        # powerup to the powerups list. Experiment to make them appear not too
        # often, so the game is challenging.
        powerup = pygame.transform.smoothscale(power, (50, 50))
        poweruprotate = pygame.transform.smoothscale(powerrotate, (50, 50))
        if random.random() < 0.01:
            # Make powerup appear randomly and alternately
            if random.random() < 0.5:
                powerups.append(PowerUp(powerup, s_width, s_height))
            else:
                powerups.append(PowerUpRotate(poweruprotate, s_width, s_height))



        # Erase the screen with a background color
        screen.fill( TEAL ) # fill the window with a color

        # Draw the characters
        for enemy_sprite in enemy_sprites:
            enemy_sprite.draw( screen )

        # Draw the powerups
        for powerup_sprite in powerups:
            powerup_sprite.draw( screen )

        player_sprite.draw( screen )

        # Display the player's health on the screen.
        text = "Health: " + str( '%.1f' % health )
        label = myfont.render( text, True, (255, 255, 0) )
        screen.blit( label, (20, 20) )

        # Bring all the changes to the screen into view
        pygame.display.update()

        # Pause for a few milliseconds
        # pygame.time.wait( 20 )
        clock.tick( FPS )
        frame += 1

    # Once the game loop is done, pause, close the window and quit.
    # Pause for a few seconds
    if pause:
        pygame.time.wait( 2000 )

    pygame.quit()
    sys.exit()

################################################################################################

if __name__ == "__main__":
    main()
