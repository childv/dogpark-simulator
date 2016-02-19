# Rachel Moore and Veronica Child
# CS 111, Andy Exley, 6/8/15
# dogpark.py : a dog park simulation

import sys, pygame, random
from pygame.locals import *

class Dog(pygame.sprite.Sprite):
	#file lsit of dog names - each dog has its own name
	fp = open('dog_names.txt', 'r')
	name_list = fp.read()
	name_list = name_list.split('\n')

	def __init__(self, screen, rectx, recty):
		super().__init__()
		#creates dog image
		self.screen = screen
		self.image = pygame.image.load("newdog.png")
		self.image = pygame.transform.scale(self.image, (75, 75))
		white = (250, 250, 250)
		self.image.set_colorkey(white)
		self.rect = self.image.get_rect()

		screen = pygame.display.get_surface()
		#area where the sprite is allowed to move
		self.area = screen.get_rect()
		self.size = self.screen.get_size()

		#starting location:	
		self.rect.x = rectx
		self.rect.y = recty

		#names dog
		self.name = Dog.name_list.pop()

		#dog's vitals
		self.energy = 10
		self.speed = [0.0, 0.0]
		self.state = 'moving'
		self.mood = 'happy!'


		#sets accumulators
		self.collided = False
		self.plays = False
		self.playcount = 0
		self.origspeed = [0, 0]

		self.adddog = False
		self.adddog_count = 0
		self.track_xpos = [rectx]
		self.track_ypos = [recty]
		self.collided_tree_count = 0
		self.collided_dog_count = 0

	#dog stops playing
	def stop_play(self):
		self.plays = False

	#counts number of times dog has collided with a tree
	#given a certain number, dog will move away
	def coll_count_dog(self):
		self.collided_dog_count += 1
		return self.collided_dog_count

	def coll_dog_zero(self):
		self.collided_dog_count = 0

	#species movement for tree one
	def collided_tree(self):
		self.collided_tree_count = 0
		self.move_tree()

	def collided_tree2(self):
		self.collided_tree_count = 0
		self.move_tree2()

	def collided_tree3(self):
		self.collided_tree_count = 0
		self.move_tree3()

	def coll_count_zero(self):
		self.collided_tree_count = 0

	#specifed movement for tree 1
	def move_tree(self):
		self.speed = [10, 3]
		newpos = self.rect.move(self.speed)
		self.rect = newpos
		self.track_xpos.append(self.rect.x)
		self.track_ypos.append(self.rect.y)
		self.collided_tree_count = 0
		self.update()

	def move_tree2(self):
		self.speed = [0, -10]
		newpos = self.rect.move(self.speed)
		self.rect = newpos
		self.track_xpos.append(self.rect.x)
		self.track_ypos.append(self.rect.y)
		self.collided_tree_count = 0
		self.update()

	def move_tree3(self):
		self.speed = [-8, 0]
		newpos = self.rect.move(self.speed)
		self.rect = newpos
		self.track_xpos.append(self.rect.x)
		self.track_ypos.append(self.rect.y)
		self.collided_tree_count = 0
		self.update()

	#specified movement for when a dog is added
	def start_move(self):
		self.adddog = True
		if self.adddog_count == 0:
			self.speed = [60, 0]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
		if self.adddog_count == 1:
			self.speed = [10, 0]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
		if self.adddog_count == 2:
			self.speed = [10, 0]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
		if self.adddog_count == 3:
			self.speed = [10, 0]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
		if self.adddog_count == 4:
			self.speed = [5, 0]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
		if self.adddog_count == 5:
			self.speed = [5, 0]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
		if self.adddog_count == 6:
			self.speed = [5, 0]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
		if self.adddog_count == 7:
			self.speed = [5, 0]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
		if self.adddog_count == 8:
			self.adddog = False
			self.adddog_count == 0
			self.update()
		if self.adddog_count < 8:
			self.adddog_count += 1

	#function that updates dog's position, takes
	#energy and mood into consideration
	def update(self):
		#sets mood based on energy
		if self.energy > 12:
			self.mood = "hyper!"
		if 8 < self.energy <= 12:
			self.mood = "happy!"
		if 5 < self.energy <= 8:
			self.mood = "okay"
		if self.energy <= 5:
			self.mood = "sleepy..."

		#gets ingame time
		milli = pygame.time.get_ticks()
		seconds = milli // 2

		#flips image, giving appearance of tail wagging
		if seconds % 2 == 0:
			self.image = pygame.transform.flip(self.image, 1, 0)
		if self.energy <= 2:
			self.__rest()
		else:
			self.__move()

	#changes dog's speed if not playing
	def changespeed(self, x, y):
		if self.plays != True:
			self.speed[0] = x
			self.speed[1] = y
		else:
			self.update()

	#general move function for dog
	def __move(self):
		if len(self.track_xpos) > 40:
			xpos_total = 0
			for x in self.track_xpos:
				xpos_total += x 
			xave = xpos_total / self.track_xpos[0]
			if -20 < (xave - self.track_xpos[0]) < 20:
				self.play = False
				if self.rect.x < 150:
					self.speed[0] = random.randint(8, 10)
				elif self.rect.x > 950:
					self.speed[0] = random.randint(-5, -3)
				else:
					self.speed[0] = random.randint(-2, 2)
				for x in self.track_xpos:
					self.track_xpos.remove(x)
			else:
				if self.plays == True:
					self.play()
				else:
					for x in self.track_xpos:
						self.track_xpos.remove(x)
					if self.rect.x < 150:
						self.speed[0] = random.randint(3, 5)
					elif self.rect.x > 950:
						self.speed[0] = random.randint(-8, -5)
					else:
						self.speed[0] = random.randint(-2, 2)
		else:
			#intiates play movement
			if self.plays == True:
				self.play()

			#initiates added dog movement
			elif self.adddog == True:
				self.start_move()

			else:
				oldx = self.speed[0] 
				oldy = self.speed[1]
				change_x = random.randint(-1, 1)
				change_y = random.randint(-1, 1)        
				self.speed[0] += 1 * change_x
				self.speed[1] += 1 * change_y
				if self.speed[0] > 10:
					num = random.randint(1, 5)
					self.speed[0] -= num
				if self.speed[1] > 10:
					num = random.randint(1, 5)
					self.speed[1] -= num

				newpos = self.rect.move(self.speed)
				if self.rect.left < 125 or self.rect.right > (self.size[0]):
					if self.plays != True:
						self.speed[0] = -self.speed[0]
						newpos = self.rect.move(self.speed)
					self.image = pygame.transform.flip(self.image, 1, 0)
				if self.rect.bottom > (self.size[1]) or self.rect.top < 0:
					if self.play != True:
						self.speed[1] = -self.speed[1]
						newpos = self.rect.move(self.speed)
				self.rect = newpos
				self.track_xpos.append(self.rect.x)
				self.track_ypos.append(self.rect.y)

	#specifies play movement when two dogs interact
	def play(self):
		#begins accumulator function
		if self.playcount == 0:
			#reduces energy
			self.energy -= 1
			self.speed[0] = -self.origspeed[0] * 3
			self.speed[1] = -self.origspeed[1] * 3
			newpos = self.rect.move(self.speed)

			#gets parameters to show "Ruff" text
			self.rect = newpos
			newx = self.rect.x 
			newy = self.rect.y - 30
			b = Bark(self.screen, newx, newy)

		elif self.playcount == 1:
			self.speed = [0, 0]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
			newx = self.rect.x + 100
			newy = self.rect.y - 100
			textpos = (newx, newy)
		elif self.playcount == 2:
			self.speed = [0, 2]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
			newx = self.rect.x + 100
			newy = self.rect.y - 100
			textpos = (newx, newy)
		elif self.playcount == 3:
			self.speed = [0, 0]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
			newx = self.rect.x + 100
			newy = self.rect.y - 100
			textpos = (newx, newy)
		elif self.playcount == 4:
			self.speed = [0, -2]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
			newx = self.rect.centerx + 100
			newy = self.rect.centery - 100
			textpos = (newx, newy)
		elif self.playcount == 5:
			self.speed = [0, 0]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
			newx = self.rect.x 
			newy = self.rect.y - 30
			b = Bark(self.screen, newx, newy)
		elif self.playcount == 6:
			self.speed = [0, 2]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
		elif self.playcount == 7:
			self.speed = [0, 0]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
		elif self.playcount == 8:
			self.speed = [0, -2]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
		elif self.playcount == 9:
			self.speed = [0, 0]
			newpos = self.rect.move(self.speed)
			self.rect = newpos
		elif self.playcount == 10:
			self.speed[0] = self.origspeed[0]    
			self.speed[1] = self.origspeed[1]   
			newpos = self.rect.move(self.speed)
			self.rect = newpos

		#after 11 runs, ends play 
		elif self.playcount == 11:
			self.playcount = 0
			self.plays = False
			self.update()
		if self.playcount < 11:
			self.playcount += 1

	#adds to tree colision accumulator
	def collide_tree(self):
		self.collided_tree_count += 1
		return self.collided_tree_count

	#dog stops moving
	def __rest(self):
		self.speed = self.speed
		self.rect.move(self.speed)
		self.state = 'resting'

	#initials play
	##change function name?
	def growl(self):
		self.origspeed = self.speed
		self.plays = True
		self.update()

	#reverses speed of dog
	def switchspeed(self):
		self.speed[0] = -self.speed[0] 
		self.speed[1] = -self.speed[1]        

	#after every minute on timer, reduces energy of dog 
	def make_tired(self):
		self.energy -= 1
		return self.energy

	#feeds dog, increases their energy
	def feed(self):
		self.energy += 1
		return self.energy

	#get variables:
	def get_name(self):
		return self.name

	def get_energy(self):
		return self.energy

	def get_xpos(self):
		return self.rect.x

	def get_ypos(self):
		return self.rect.y

	def get_image(self):
		return self.image

	def get_mood(self):
		return self.mood


class status_screen(pygame.sprite.Sprite):
	def __init__(self, screen, width, height, name, energy, mood, image):
		super().__init__()
		self.pause = True

		#sets color
		self.white = (255, 255, 255)
		self.black = (0, 0, 0)
		self.cyan = (51, 153, 204)
		self.orange = (255, 153, 51)

		#sets text
		self.title = "%s Status:" % name
		self.energy = "- %s energy" % str(energy)
		self.mood = "They are %s" % mood

		#initializes text
		self.font = pygame.font.Font(None, 40)
		self.font2 = pygame.font.Font(None, 25)	

		#creates text given text, font color, and background color
		self.titletext = self.font.render(self.title, True, self.orange, self.white)
		self.titlerect = self.titletext.get_rect()
		self.moodtext = self.font2.render(self.mood, True, self.cyan, self.white)
		self.moodrect = self.moodtext.get_rect()
		self.energytext = self.font2.render(self.energy, True, self.cyan, self.white)
		self.energyrect = self.energytext.get_rect()

		#places text screen in middle
		self.titlerect.center = 280, 270 
		self.moodrect.center = 270, 300    
		self.energyrect.center = 270, 320

		#draws background rectangle
		pygame.draw.rect(screen, self.white, (width / 6, \
				                              height / 3, 295, 150))    

		#adds text
		screen.blit(self.titletext, self.titlerect)
		screen.blit(self.energytext, self.energyrect)
		screen.blit(self.moodtext, self.moodrect)
		screen.blit(image, (370, 290))
		pygame.display.flip()

		#pauses game to show screen
		while self.pause == True:
			for event in pygame.event.get():
				#unpauses with mouse button
				if event.type == MOUSEBUTTONDOWN:
					self.pause = False  
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN:
					if event.key == K_q:
						pygame.quit()
						sys.exit()

#creates the bark text to appear
class Bark(pygame.sprite.Sprite):
	def __init__(self, screen, xpos, ypos):
		super().__init__()
		#sets text
		self.screen = screen
		self.font = pygame.font.Font(None, 15)
		self.barktext = self.font.render("RUFF", 1, (0, 0, 0))
		self.barkrect = self.barktext.get_rect()
		#gets x and y pos of dog
		self.barkrect.x = xpos
		self.barkrect.y = ypos
		self.screen.blit(self.barktext, self.barkrect)
		pygame.display.flip()

#creates bones
class Bone(pygame.sprite.Sprite):
	def __init__(self, xpos, ypos):
		super().__init__()
		#creates image
		self.image = pygame.image.load("bone.png")
		self.image = pygame.transform.scale(self.image, (50, 50))
		lime_green = (102, 204, 0)
		white = (250, 250, 250)
		self.image.set_colorkey(white)
		self.rect = self.image.get_rect()
		#gets inputted x and y pos
		self.rect.x = xpos
		self.rect.y = ypos

#Poop class, generated under dog
class Poop(pygame.sprite.Sprite):
	def __init__(self, xpos, ypos):
		super().__init__()
		#creates image
		self.image = pygame.image.load('poop.png')
		self.image = pygame.transform.scale(self.image, (20, 20))
		lime_green = (102, 204, 0)
		white = (250, 250, 250)
		self.image.set_colorkey(lime_green)
		self.rect = self.image.get_rect()
		#appears based on given x positions
		self.rect.x = xpos
		self.rect.y = ypos

#class for trees
class Tree(pygame.sprite.Sprite):
	def __init__(self, xpos, ypos):
		super().__init__()
		#generates image
		self.image = pygame.image.load("tree.png")
		self.image = pygame.transform.scale(self.image, (150, 150))
		lime_green = (102, 204, 0)
		white = (250, 250, 250)
		self.image.set_colorkey(white)
		self.rect = self.image.get_rect()
		self.rect.x = xpos
		self.rect.y = ypos


#creates screen for beginning of game
class StartingScreen(pygame.sprite.Sprite):
	def __init__(self, screen):
		self.screen = screen
		self.pause = True
	
		white = (250, 250, 250)
		black = (0, 0, 0)
		self.font = pygame.font.Font(None, 60)
		self.font2 = pygame.font.Font(None, 30)
		#draws background rectangle
		pygame.draw.rect(self.screen, white, (200, 175, 650, 400))
	
		self.string1 = "You are the owner of a dog park."
		self.string2 = "Keep the dogs happy by feeding them and cleaning"
		self.string3 = "up after them. Be careful! If the dogs have no"
		self.string4 = "energy left, they will leave and the park will close."
		self.string5 = "Good luck!"
	
		#initializes text
		self.titletext = self.font.render("Exley Park", 1, black)
		self.text1 = self.font2.render(self.string1, 1, black)
		self.text2 = self.font2.render(self.string2, 1, black)
		self.text3 = self.font2.render(self.string3, 1, black)
		self.text4 = self.font2.render(self.string4, 1, black)
		self.text5 = self.font2.render(self.string5, 1, black)
	
		#displays text
		self.screen.blit(self.titletext, (410, 250))
		self.screen.blit(self.text1, (250, 360))
		self.screen.blit(self.text2, (250, 380))
		self.screen.blit(self.text3, (250, 400))
		self.screen.blit(self.text4, (250, 420))
		self.screen.blit(self.text5, (250, 440))
	
		pygame.display.flip()
	
		while self.pause == True:
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONDOWN:
					self.pause = False
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
	
				if event.type == KEYDOWN:
					if event.key == K_q:
						pygame.quit()
						sys.exit()

#creates screen for end of game
class ClosingScreen(pygame.sprite.Sprite):
	def __init__(self, screen, endtext):
		self.screen = screen
		pause = True
		font = pygame.font.Font(None, 30)
		pygame.draw.rect(self.screen, (250, 250, 250), (350, 175, 400, 400))
		if endtext == None:
			self.endtext = 0
			self.text1 = font.render("The park is closed", 1, (0, 0, 0))
			self.text2 = font.render("Thanks for coming!", 1, (0, 0, 0))

			self.screen.blit(self.text1, (400, 200))
			self.screen.blit(self.text2, (400, 375))

		else:
			self.endtext = str(endtext)
			self.text1 = font.render("The park closed early today", 1, (0, 0, 0))
			self.text2 = font.render(self.endtext, 1, (0, 0, 0))

			self.screen.blit(self.text1, (400, 200))
			self.screen.blit(self.text2, (400, 375))

		pygame.display.flip()
		while pause == True:
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONDOWN:
					pygame.quit()
					sys.exit()

				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN:
					if event.key == K_q:
						pygame.quit()
						sys.exit()


#initializes simulation and holds event queue
#while keeping track of collisions
def main():
	pygame.init()

	#sets screen presets
	width, height = 1000, 750
	white = (250, 250, 250)
	lime_green = (102, 204, 0)
	size = (width, height)

	screen = pygame.display.set_mode(size)
	screen.fill(lime_green)

	#creates ADD DOG button
	font = pygame.font.Font(None, 30)
	text = font.render("ADD DOG", 1, (0, 0, 0))
	textpos = text.get_rect()
	screen.blit(text, (10, 10))
	button = pygame.draw.rect(screen, (255, 192, 203), (0, 0, 125, 40))
	
	#creates FEED DOGS button
	textfeed = font.render("FEED DOGS", 1, (0, 0, 0))
	feedbutton = pygame.draw.rect(screen, (200, 200, 0), (0, 40, 125, 40))
	screen.blit(textfeed, (5, 50))	

	#makes portal for dogs to enter
	textsign = font.render("DOG PARK", 1, (0, 0, 0))
	textsignpos = text.get_rect()
	pygame.draw.line(screen, (0, 200, 200), (120, 600), (120, 750), 5)
	pygame.draw.line(screen, (0, 200, 200), (0, 600), (0, 750), 5)
	screen.blit(textsign, (10, 600))

	#initializes clock
	clock = pygame.time.Clock()

	#generates groups
	bone_group = pygame.sprite.Group()
	tree_group = pygame.sprite.Group()
	poop_group = pygame.sprite.Group()
	dog_group = pygame.sprite.Group()
	
	#initializes starting screen
	s = StartingScreen(screen)

	#set positions of trees
	#adds to starting position lists
	tree1 = Tree(150, 0)
	tree_group.add(tree1)
	tree2 = Tree(850, 250)
	tree_group.add(tree2)
	tree3 = Tree(600, 600)
	tree_group.add(tree3)
	#draws trees
	tree_group.draw(screen)

	#spawn preset dogs  
	dog1 = Dog(screen, 300, 100)
	dog_group.add(dog1)
	dog2 = Dog(screen, 400, 300)
	dog_group.add(dog2)
	dog3 = Dog(screen, 700, 400)
	dog_group.add(dog3)
	dog4 = Dog(screen, 750, 150)
	dog_group.add(dog4)

	#sets event IDs and their timers
	TIRED_DOGS = 1
	TREE_COUNT = 2
	DOG_COLL = 3
	ADD_DOG = 4
	add_dog = True
	END_GAME = 31

	pygame.time.set_timer(TIRED_DOGS, 25000)
	pygame.time.set_timer(TREE_COUNT, 2000)
	pygame.time.set_timer(DOG_COLL, 5000)
	pygame.time.set_timer(ADD_DOG, 10000)
	pygame.time.set_timer(END_GAME, 240000)

	#begins even queue
	while 1:
		dogs_interact = []
		for event in pygame.event.get():
			#every 25 seconds, reduces energy of dogs
			#and creates poop
			if event.type == TIRED_DOGS:
				for dog in dog_group:
					dog.make_tired()
					xpos = dog.get_xpos()
					ypos = dog.get_ypos()
					poop = Poop(xpos, ypos)
					poop_group.add(poop)

			#gets number of time a dog has collided with a tree
			if event.type == TREE_COUNT:
				for dog in dog_group:
					if dog.collided_tree_count > 2:
						if 0 < dog.rect.x < 400:
							dog.collided_tree()
							dog.coll_count_zero()

						elif 450 < dog.rect.x < 750:
							dog.collided_tree2()
							dog.coll_count_zero()

						else:
							dog.collided_tree3()
							dog.coll_count_zero()

				for dog in dog_group:
					dog.coll_count_zero()

			if event.type == DOG_COLL:
				for dog in dog_group:
					if dog.coll_count_dog() > 2:
						dog.stop_play()
						dog.update()

			#allows user to add a dog every 30 seconds			
			if event.type == ADD_DOG:
				add_dog = True
			if event.type == END_GAME:
				endscreen = ClosingScreen(screen, None)

			#quits game
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			#if mousebutton clicked...
			if event.type == MOUSEBUTTONDOWN:
				mousept = pygame.mouse.get_pos()
				#opens window if dog is clicked showing status,
				#closes when player clicks again
				for dog in dog_group:
					if dog.rect.collidepoint(mousept):
						#gets info of dog
						name = dog.get_name()
						energy = dog.get_energy()
						image = dog.get_image()
						mood = dog.get_mood()

						#generates screen
						s = status_screen(screen, width, height, name, energy, mood, image)

				#if player clicks on poop, removes poop
				for poop in poop_group:
					if poop.rect.collidepoint(mousept):
						poop.kill()

				#if ADD DOG button is clicked...
				if mousept[0] < 130 and mousept[1] < 40:
					#adds a dog if able
					if add_dog == True:
						dog = Dog(screen, 20, 675)
						dog.start_move()
						dog_group.add(dog)
						add_dog = False
					#if not, blits a message
					else:
						textno = font.render("Not yet!", 1, (0, 0, 0))
						screen.blit(textno, (10, 640))

				#if FEED DOG button is clicked, generates 3 bones
				if mousept[0] < 130 and 40 < mousept[1] < 80:
					for i in range(3):
						xpos = random.randint(300, 800)
						ypos = random.randint(200, 600)
						bone = Bone(xpos, ypos)
						bone_group.add(bone)

			elif event.type == KEYDOWN:
				#quits game if "q" is pressed
				if event.key == K_q:
					pygame.quit()
					sys.exit()

		for dog in dog_group:
		#gets dogs that each dog has interacted with
			dogs_interact = pygame.sprite.spritecollide(dog, dog_group, False)
			if len(dogs_interact) > 1:
				#makes both dogs play and begins count collide
				#function to prevent dogs from getting stuck
				dog.growl()
				dog.coll_count_dog()
				for dog in dogs_interact:
					dog.growl()
					dog.coll_count_dog()

		#checks if dog has collided with bone. If true, then
		#feeds the dog and removes the bone
		for dog in dog_group:
			dog_bone_list = pygame.sprite.spritecollide(dog, bone_group, True)
			for bone in dog_bone_list:
				dog.feed()

		#checks if tress has collided with dog. If true, then
		#changes dog's movement
		for tree in tree_group:
			dog_tree_list = pygame.sprite.spritecollide(tree, dog_group, False)
			for dog in dog_tree_list:
				dog.collide_tree()
				dog.switchspeed()

		#if dog has less than zero energy, causes them to leave
		for dog in dog_group:
			if dog.get_energy() < 0:
				#gets dog's info
				name = dog.get_name()
				energy = "no"
				image = dog.get_image()
				mood = "leaving"
				#generates leaving screen
				l = status_screen(screen, width, height, name, energy, mood, image)
				#removes dog from active group
				dog.kill()

		#if too many dogs leave or if amount of poop is twice
		#the amount of dogs, the game ends
		if len(dog_group) < 2:
			endscreen = ClosingScreen(screen, "The dogs are too tired to play")
		if len(poop_group) > len(dog_group) * 2:
			endscreen = ClosingScreen(screen, "The park is too dirty")

		#updates positions of dogs
		dog_group.update()

		# redraw the screen and objects
		screen.fill(lime_green)

		#draws buttons
		button = pygame.draw.rect(screen, (255, 192, 203), (0, 0, 125, 40))
		screen.blit(text, (10, 10))
		button2 = pygame.draw.rect(screen, (0, 200, 200), (0, 585, 125, 40))
		screen.blit(textsign, (10, 600))

		pygame.draw.line(screen, (0, 200, 200), (120, 600), (120, 750), 5)
		pygame.draw.line(screen, (0, 200, 200), (0, 600), (0, 750), 5)
		feedbutton = pygame.draw.rect(screen, (200, 200, 0), (0, 40, 125, 40))
		screen.blit(textfeed, (5, 50))

		#draws objects
		poop_group.draw(screen)
		bone_group.draw(screen)
		tree_group.draw(screen)
		dog_group.draw(screen)

		#sets FPS rate and updates display
		clock.tick(8)
		pygame.display.flip()
		pygame.display.update
	

if __name__ == '__main__':
	main()
