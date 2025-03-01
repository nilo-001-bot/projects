import pygame  # Import the pygame library for creating games and multimedia applications
import sys  # Import the sys module for system-specific parameters and functions


class Game:
    def __init__(self):
        pygame.init()  # Initialize all imported pygame modules

        pygame.display.set_caption("ninja game")  # Set the window title
        self.screen = pygame.display.set_mode((640, 480))  # Create a window of size 640x480
        self.clock = pygame.time.Clock()  # Create a clock object to control the frame rate

        # Load an image and set its color key for transparency
        self.img = pygame.image.load('C:/Users/Hp/python/data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0))  # Set black as transparent color

        self.movement = [False, False]  # Track vertical movement (up and down)
        self.img_pos = [160, 260]  # Initial position of the image

        self.collision_area = pygame.Rect(50, 50, 300, 50)  # Define a rectangular collision area

    def run(self):
        while True:  # Main game loop
            self.screen.fill((14, 219, 248))  # Fill the screen with a color

            # Create a rectangle for the image based on its position
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1],
                                self.img.get_width(), self.img.get_height())
            if img_r.colliderect(self.collision_area):  # Check for collision with the area
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)  # Draw the collision area
            else:
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)  # Draw the collision area

            # Update the image's vertical position based on movement
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.screen.blit(self.img, self.img_pos)  # Draw the image at its new position

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Check for quit event
                    pygame.quit()  # Uninitialize all pygame modules
                    sys.exit()  # Exit the program

                if event.type == pygame.KEYDOWN:  # Check for key press
                    if event.key == pygame.K_UP:  # If the up arrow is pressed
                        self.movement[0] = True  # Start moving up

                    if event.key == pygame.K_DOWN:  # If the down arrow is pressed
                        self.movement[1] = True  # Start moving down

                if event.type == pygame.KEYUP:  # Check for key release
                    if event.key == pygame.K_UP:  # If the up arrow is released
                        self.movement[0] = False  # Stop moving up

                    if event.key == pygame.K_DOWN:  # If the down arrow is released
                        self.movement[1] = False  # Stop moving down

            pygame.display.update()  # Update the display
            self.clock.tick(60)  # Limit the frame rate to 60 FPS


# Create an instance of the Game class and run the game
Game().run()
