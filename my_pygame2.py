import pygame  # Import the pygame library for creating games and multimedia applications

# Initialize the pygame library


pygame.init()  # Initialize all imported pygame modules


# Set up the display window with a width and height of 500 pixels
win = pygame.display.set_mode((500, 500))  # Create a window for the game


# Initialize the position and dimensions of the rectangle
x = 50  # X-coordinate of the rectangle
y = 50  # Y-coordinate of the rectangle
width = 40  # Width of the rectangle
height = 60  # Height of the rectangle
vel = 5  # Velocity of the rectangle movement (speed of movement)


run = True  # Variable to control the main loop
while run:  # Main loop that runs until 'run' is set to False
    pygame.time.delay(100)  # Delay to control the frame rate (100 milliseconds)

    pygame.time.delay(100)  # Delay to control the frame rate (100 milliseconds)

    
    for event in pygame.event.get():  # Check for events in the event queue
        # If the quit event is triggered, exit the main loop

        if event.type == pygame.QUIT:  # If the quit event is triggered

            run = False  # Exit the main loop

    
    keys = pygame.key.get_pressed()  # Get the state of all keyboard keys to check for input

    
    # Move the rectangle based on key presses

    if keys[pygame.K_LEFT]:  # If the left arrow key is pressed, move left

        x -= vel  # Move the rectangle left

        
    if keys[pygame.K_RIGHT]:  # If the right arrow key is pressed, move right

        x += vel  # Move the rectangle right

        
    if keys[pygame.K_UP]:  # If the up arrow key is pressed, move up

        y -= vel  # Move the rectangle up

        
    if keys[pygame.K_DOWN]:  # If the down arrow key is pressed, move down

        y += vel  # Move the rectangle down

    
    win.fill((0, 0, 0))  # Fill the window with black color to clear the previous frame

    
    # Draw the rectangle on the window with red color

    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))  # Draw the rectangle

    pygame.display.update()  # Update the display to show the new frame


pygame.quit()  # Uninitialize all pygame modules and close the window
