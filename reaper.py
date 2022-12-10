import math
import pygame

# Define some colors
BACKGROUND = pygame.colordict.THECOLORS["black"]
FOREGROUND = pygame.colordict.THECOLORS["white"]

pygame.init()

# Set the height and width of the screen
size = [700, 500]
#screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode((size), pygame.FULLSCREEN)

pygame.display.set_caption("The Repeaer")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.Font(None, 75)
big_font = pygame.font.Font(None, 400)

frame_count = 0
frame_rate = 60
start_time = 90

state = 1

running = True

# Provide background noise
background_sound = './party.ogg'
pygame.mixer.init()
pygame.mixer.music.load(background_sound)


def timer():
    print("tick")
    # --- Timer going up ---
    # Calculate total seconds
    total_seconds = frame_count // frame_rate

    # Divide by 60 to get total minutes
    minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

    # Use python string formatting to format in leading zeros
    output_string = "Time elapsed  {0:02}:{1:02}".format(minutes, seconds)

    # Blit to the screen
    text = font.render(output_string, True, FOREGROUND)
    screen.blit(text, [50, 220])

    survival_percentage = math.ceil(100 - (total_seconds / 6))
    if survival_percentage < 0:
        survival_percentage = 0;

    # Use python string formatting to format in leading zeros
    output_string = "Chance of survival {0:02}%".format(survival_percentage)

    # Blit to the screen
    text = font.render(output_string, True, FOREGROUND)

    screen.blit(text, [50, 300])

def countdown(seconds):
    output_string = "{0:2}".format(seconds)
    text = big_font.render(output_string, True, FOREGROUND)
    screen.blit(text, [200,150])


# Main Program Loop
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q: # Quit
                done = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE: # toggle pause
                running = not running
                if running:
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.pause()

    # Set the screen background
    screen.fill(BACKGROUND)

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    if state == 1: # Initial count down to begin
        seconds_until_start = 10 - (frame_count // frame_rate)

        countdown(seconds_until_start)
        if seconds_until_start <= 0:
            frame_count = 0
            state += 1
        seconds_until_start -= seconds_until_start

    elif state == 2: # Prep for main run
        pygame.mixer.music.play()
        state += 1

    elif state == 3: # Main run
        timer()

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    if running:
        frame_count += 1

    # Limit frames per second
    clock.tick(frame_rate)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
