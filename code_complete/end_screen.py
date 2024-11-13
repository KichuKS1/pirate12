import pygame
import sys
from button import Button  # Assuming you already have a Button class to handle buttons

pygame.init()

# Initialize screen
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("End Screen")

# Load background image (use your own background image here)
BG = pygame.image.load("assets/Background.png")

# Function to get font
def get_font(size):  
    return pygame.font.Font("assets/font.ttf", size)  # Replace with your font file path

# Function to display credits
def show_credits():
    SCREEN.fill("black")
    credits_text = get_font(50).render("Credits: Developed by Your Name", True, "white")
    credits_rect = credits_text.get_rect(center=(640, 360))
    SCREEN.blit(credits_text, credits_rect)
    pygame.display.update()

    # Pause to show credits for a moment
    pygame.time.delay(2000)  # Delay 2 seconds
    end_screen()  # Return to the end screen after showing credits

# End screen where the two buttons are displayed
def end_screen():
    while True:
        SCREEN.blit(BG, (0, 0))  # Set background image
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Title text
        TITLE_TEXT = get_font(100).render("GAME OVER", True, "#b68f40")
        TITLE_RECT = TITLE_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(TITLE_TEXT, TITLE_RECT)

        # Button designs
        MAIN_MENU_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                                  text_input="Go to Main Menu", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        CREDITS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 380), 
                                text_input="Credits", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        # Update the buttons
        for button in [MAIN_MENU_BUTTON, CREDITS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        # Event loop for button actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return  # Exit the end screen function to proceed to the main menu
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    show_credits()  # Show credits screen and then return to end screen

        pygame.display.update()

# Start the end screen when the game is over
end_screen()  # Display the end screen first
import pygame
import sys
from button import Button  # Assuming you already have a Button class to handle buttons
from main_menu import main_menu  # Your main menu function

pygame.init()

# Initialize screen
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("End Screen")

# Load background image (use your own background image here)
BG = pygame.image.load("assets/Background.png")

# Function to get font
def get_font(size):  
    return pygame.font.Font("assets/font.ttf", size)  # Replace with your font file path

# Function to display credits
def show_credits():
    SCREEN.fill("black")
    credits_text = get_font(50).render("Credits: Developed by Your Name", True, "white")
    credits_rect = credits_text.get_rect(center=(640, 360))
    SCREEN.blit(credits_text, credits_rect)
    pygame.display.update()

    # Pause to show credits for a moment
    pygame.time.delay(2000)  # Delay 2 seconds
    end_screen()  # Return to the end screen after showing credits

# End screen where the two buttons are displayed
def end_screen():
    while True:
        SCREEN.blit(BG, (0, 0))  # Set background image
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Title text
        TITLE_TEXT = get_font(100).render("GAME OVER", True, "#b68f40")
        TITLE_RECT = TITLE_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(TITLE_TEXT, TITLE_RECT)

        # Button designs
        MAIN_MENU_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                                  text_input="Go to Main Menu", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        CREDITS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 380), 
                                text_input="Credits", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        # Update the buttons
        for button in [MAIN_MENU_BUTTON, CREDITS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        # Event loop for button actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return  # Exit the end screen function to proceed to the main menu
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    show_credits()  # Show credits screen and then return to end screen

        pygame.display.update()

# Start the end screen when the game is over
end_screen()  # Display the end screen first
main_menu()  # Only call main_menu() after end_screen() finishes
  # Only call main_menu() after end_screen() finishes
