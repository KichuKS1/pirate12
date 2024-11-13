import pygame
import sys
from settings import * 
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join
from support import * 
from data import Data
from debug import debug
from ui import UI
from overworld import Overworld
import os

print(os.getcwd())

class Button:
	def __init__(self, x, y, image, font, text_color, hovering_color, text=''):
		self.image = image
		self.rect = self.image.get_rect(center=(x, y))
		self.font = font
		self.text = text
		self.text_color = text_color
		self.hovering_color = hovering_color

	def draw(self, screen):
		text_surface = self.font.render(self.text, True, self.text_color)
		text_rect = text_surface.get_rect(center=self.rect.center)
		screen.blit(self.image, self.rect)
		screen.blit(text_surface, text_rect)

	def check_for_input(self, position):
		return self.rect.collidepoint(position)

	def update_text_color(self, position):
		if self.rect.collidepoint(position):
			self.text_color = self.hovering_color
		else:
			self.text_color = self.text_color

class Game:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption('Super Pirate World')
		self.clock = pygame.time.Clock()
  
		self.import_assets()

		self.ui = UI(self.font, self.ui_frames)
		self.data = Data(self.ui)
		self.tmx_maps = {
			0: load_pygame(join('data', 'levels', 'omni.tmx')),
			1: load_pygame(join('data', 'levels', '1.tmx')),
			2: load_pygame(join('data', 'levels', '2.tmx')),
			3: load_pygame(join('data', 'levels', '3.tmx')),
			4: load_pygame(join('data', 'levels', '4.tmx')),
			5: load_pygame(join('data', 'levels', '5.tmx')),
		}
		self.tmx_overworld = load_pygame(join('data', 'overworld', 'overworld.tmx'))
		self.current_stage = Level(self.tmx_maps[self.data.current_level], self.level_frames, self.audio_files, self.data, self.switch_stage)
		self.bg_music.play(-1)
		self.game_over = False

	def switch_stage(self, target, unlock=0):
		if target == 'level':
			self.current_stage = Level(self.tmx_maps[self.data.current_level], self.level_frames, self.audio_files, self.data, self.switch_stage)
		else:  # overworld
			if unlock > 0:
				self.data.unlocked_level = 6
			else:
				self.data.health -= 1
			self.current_stage = Overworld(self.tmx_overworld, self.data, self.overworld_frames, self.switch_stage)

	def import_assets(self):
		self.level_frames = {
			'flag': import_folder('graphics', 'level', 'flag'),
			'saw': import_folder('graphics', 'enemies', 'saw', 'animation'),
			'floor_spike': import_folder('graphics', 'enemies', 'floor_spikes'),
			'palms': import_sub_folders('graphics', 'level', 'palms'),
			'candle': import_folder('graphics', 'level', 'candle'),
			'window': import_folder('graphics', 'level', 'window'),
			'big_chain': import_folder('graphics', 'level', 'big_chains'),
			'small_chain': import_folder('graphics', 'level', 'small_chains'),
			'candle_light': import_folder('graphics', 'level', 'candle light'),
			'player': import_sub_folders('graphics', 'player'),
			'saw': import_folder('graphics', 'enemies', 'saw', 'animation'),
			'saw_chain': import_image('graphics', 'enemies', 'saw', 'saw_chain'),
			'helicopter': import_folder('graphics', 'level', 'helicopter'),
			'boat': import_folder('graphics', 'objects', 'boat'),
			'spike': import_image('graphics', 'enemies', 'spike_ball', 'Spiked Ball'),
			'spike_chain': import_image('graphics', 'enemies', 'spike_ball', 'spiked_chain'),
			'tooth': import_folder('graphics', 'enemies', 'tooth', 'run'),
			'shell': import_sub_folders('graphics', 'enemies', 'shell'),
			'pearl': import_image('graphics', 'enemies', 'bullets', 'pearl'),
			'items': import_sub_folders('graphics', 'items'),
			'particle': import_folder('graphics', 'effects', 'particle'),
			'water_top': import_folder('graphics', 'level', 'water', 'top'),
			'water_body': import_image('graphics', 'level', 'water', 'body'),
			'bg_tiles': import_folder_dict('graphics', 'level', 'bg', 'tiles'),
			'cloud_small': import_folder('graphics', 'level', 'clouds', 'small'),
			'cloud_large': import_image('graphics', 'level', 'clouds', 'large_cloud'),
		}
		self.font = pygame.font.Font(join('graphics', 'ui', 'runescape_uf.ttf'), 40)
		self.ui_frames = {
			'heart': import_folder('graphics', 'ui', 'heart'), 
			'coin': import_image('graphics', 'ui', 'coin')
		}
		self.overworld_frames = {
			'palms': import_folder('graphics', 'overworld', 'palm'),
			'water': import_folder('graphics', 'overworld', 'water'),
			'path': import_folder_dict('graphics', 'overworld', 'path'),
			'icon': import_sub_folders('graphics', 'overworld', 'icon'),
		}

		self.audio_files = {
			'coin': pygame.mixer.Sound(join('audio', 'coin.wav')),
			'attack': pygame.mixer.Sound(join('audio', 'attack.wav')),
			'jump': pygame.mixer.Sound(join('audio', 'jump.wav')), 
			'damage': pygame.mixer.Sound(join('audio', 'damage.wav')),
			'pearl': pygame.mixer.Sound(join('audio', 'pearl.wav')),
		}
		self.bg_music = pygame.mixer.Sound(join('audio', 'starlight_city.mp3'))
		self.bg_music.set_volume(0.5)

	def check_game_over(self):
		if self.data.health <= 0:
			self.show_game_over_screen()

	def show_game_over_screen(self):
		self.game_over = True
		while self.game_over:
			self.display_surface.fill((0, 0, 0))
			game_over_text = self.font.render("GAME OVER", True, (255, 0, 0))
			self.display_surface.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOW_HEIGHT // 2 - 100))

			# Button
			main_menu_button_image = pygame.Surface((300, 80))
			main_menu_button = Button(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100, main_menu_button_image, self.font, (255, 255, 255), (200, 200, 200), "Main Menu")
			main_menu_button.update_text_color(pygame.mouse.get_pos())
			main_menu_button.draw(self.display_surface)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if main_menu_button.check_for_input(pygame.mouse.get_pos()):
						self.data.health = 3  # Reset health for restarting
						self.game_over = False
						self.switch_stage("overworld")

			pygame.display.update()

	def run(self):
		while True:
			dt = self.clock.tick() / 1000
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.check_game_over()
			self.current_stage.run(dt)
			self.ui.update(dt)
			
			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()
