import pygame, sys
import csv
from button import Button
from main import Game
pygame.mixer.init()

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def read_leaderboard():
    leaderboard = []
    try:
        with open('leaderboard.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                leaderboard.append(row)
        leaderboard.sort(key=lambda x: int(x['Score']), reverse=True)
    except FileNotFoundError:
        print("Leaderboard file not found.")
    return leaderboard

def display_leaderboard():
    leaderboard = read_leaderboard()
    SCREEN.fill("white")
    
    # Load fonts for title and items
    title_font = get_font(60)
    item_font = get_font(45)

    # Display title
    title_text = title_font.render("Leaderboard", True, "Black")
    title_rect = title_text.get_rect(center=(640, 100))
    SCREEN.blit(title_text, title_rect)

    # Display top 5 scores
    y_offset = 200
    for i, entry in enumerate(leaderboard[:5]):
        name_text = item_font.render(f"{i+1}. {entry['Name']}", True, "Black")
        score_text = item_font.render(f"{entry['Score']}", True, "Black")
        
        SCREEN.blit(name_text, (400, y_offset))
        SCREEN.blit(score_text, (800, y_offset))
        y_offset += 60  # Adjust spacing between rows

    # Initialize and display the back button
    back_button = Button(image=None, pos=(640, 600),
                         text_input="BACK", font=get_font(50), base_color="Black", hovering_color="Green")
    back_button.update(SCREEN)
    pygame.display.update()

    # Event loop for leaderboard screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(pygame.mouse.get_pos()):
                    main_menu()  # Return to the main menu when "BACK" is clicked
                    return
        pygame.display.update()

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    pygame.mixer.music.stop()  # Stop the main menu music
    game = Game()  # Create an instance of your game
    game.run()  # Run the game, which should have its own music and sounds

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    # Check if music is already playing to prevent restarting it
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load('C:/Users/USER/Downloads/Super Pirate World Anaswar VS Code Fix Version Excluive 2024 for Anugrah VS CODE/Super Pirate World Anaswar Fix Version Excluive 2024 (For Anugrah)/audio/mainmenumusic.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # Loop the music indefinitely
    
    while True:
        SCREEN.blit(BG, (0, 0))  # Background image

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        
        leaderboard_image = pygame.image.load("assets/Options Rect.png")
        leaderboard_image = pygame.transform.scale(leaderboard_image, (900, leaderboard_image.get_height()))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 380), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEADERBOARD_BUTTON = Button(image=leaderboard_image, pos=(640, 510), 
                            text_input="LEADERBOARD", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 640), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        # Update all buttons
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, LEADERBOARD_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if LEADERBOARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    display_leaderboard()

        pygame.display.update()



# Start the main menu
main_menu()
