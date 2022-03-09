from unidecode import unidecode
from random import choice
from tkinter import *
from tkinter.font import Font
from time import sleep

# set languange for game on line 51


class Wordle:
    def __init__(self, width, height):
        self.top_word = None
        self.top_box = None
        self.keyboard_dict = None
        self.keyboard_keys = None
        self.canvas = None
        self.root = None
        self.width, self.height = width, height
        self.box_height = self.height * 0.045
        self.box_width = self.box_height * 0.85
        self.gap = self.box_height * 0.1
        self.pos_x = (self.width - (self.box_width * 5) - (self.gap * 4)) / 2
        self.new_pos_x = self.pos_x
        self.pos_y = self.height * 0.08
        self.new_pos_y = self.pos_y
        self.block = self.box_width + self.gap
        self.color_right = '#62A87C' #Correct letter
        self.color_place = '#F9DB6D' #Wrong location
        self.color_wrong = '#312a2c' #Not in word
        self.color_wrongFG = '#504a4b'
        self.color_empty = '#615458' #Not typed
        self.color_kb = '#313B72' 
        self.color_end_box = '#35273B' #34, 19, choice of rand end msg
        self.color_bg = '#35273B' 
        self.font = "Tahoma"
        self.row_counter = 0
        self.column_counter = 0
        self.guess = ''
        self.kb_box_height = self.box_height * 0.8
        self.kb_box_width = self.box_width * 0.8
        self.kb_gap = self.gap * 0.8
        self.kb_pos_x = 0.5 * (self.width - (self.kb_box_width * 10) - (self.kb_gap * 9))
        self.kb_new_pos_x = self.kb_pos_x
        self.kb_pos_y = self.pos_y + ((self.box_height + self.gap) * 6) * 2.55
        self.kb_new_pos_y = self.kb_pos_y
        self.kb_block = self.kb_box_width + self.kb_gap
        self.pow_x = (self.width - self.kb_box_width) * 0.2
        self.pow_y = (self.height - (self.kb_box_height + (self.kb_gap * 4))) * 0.5
        self.kb_row_counter = 0
        self.kb_column_counter = 0
        self.game_language = 'en'
        self.max_rows = 14 #Number of times allowed to guess a word
        self.end_game_words = ["Good job.", "Well done!", "W.O.W."]
        with open('word_list.txt', 'r', encoding='utf-8') as a:
            self.words = [unidecode(x.upper()) for x in a.read().split(' ')]
        self.word = choice(self.words)
        print(self.word)
        '''
        #with open('accepted_words_' + self.game_language + '.txt', 'r', encoding='utf-8') as a:
            #self.accepted_answers = [unidecode(x.upper()) for x in a.read().split(' ')]
        #self.words.extend(self.accepted_answers)
        
        '''
        self.invalid_message = 'Not in word list'
        self.game_on = True
        self.delay = 0.05
    def power_up_menu(self):
        self.power_keys = ["1","2","3","4","5"]
        for i in self.power_keys:
            self.create_pow_key(i, "white")
    
    def create_pow_key(self, letter, color):
        self.canvas.create_rectangle(self.pow_x,
                                     self.pow_y + self.gap,
                                     self.pow_x + self.kb_block + self.kb_box_width,
                                     self.pow_y + self.kb_box_height + self.kb_gap - self.gap,
                                     outline="black",
                                     fill=color,
                                     tags=letter)
        # insert letter

    def generate_gui(self):
        self.root = Tk(className=" Baddle")
        self.canvas = Canvas(self.root, height=self.height, width=self.width, bg=self.color_bg)
        self.canvas.pack(expand=True)

        self.create_letter_boxes()
        self.special_keys()
        self.generate_keyboard()
        self.power_up_menu()

        # title
        self.canvas.create_text((self.width * 0.5,
                                 self.pos_y * 0.2),
                                text='BADDLE FOR SUPREMACY!',
                                font=(self.font, int(self.kb_box_height * 0.55)),
                                fill='white')

        # event listeners
        self.root.bind('<KeyPress>', self.kb_input)
        self.root.bind('<BackSpace>', self.kb_delete)
        self.root.bind('<Return>', self.kb_enter)
        self.root.bind('<1>')

        self.canvas.create_text((self.width / 2,
                                 self.height * 0.98),
                                text='github.com/Pillaged',
                                font=(self.font, int(self.kb_box_height * 0.2)),
                                fill='white')

        self.root.mainloop()

    def create_letter_boxes(self): # Number of rows to be tested for game length.
        for y in range(self.max_rows+2):
            for x in range(5):
                self.new_pos_x = self.pos_x + ((self.box_width + self.gap) * x)
                self.new_pos_y = self.new_pos_y
                self.create_box(self.new_pos_x, self.new_pos_y, self.box_width, self.box_height, self.color_empty)

            self.new_pos_y = self.pos_y + ((self.box_height + self.gap) * y)
            self.new_pos_x = self.pos_x

    def generate_keyboard(self):
        self.keyboard_keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
                              ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
                              ["Z", "X", "C", "V", "B", "N", "M"]]
        self.keyboard_dict = {}

        for r, key_row in enumerate(self.keyboard_keys):
            for i, key in enumerate(key_row):
                # create box
                self.keyboard_dict[key] = {'r': r, 'i': i}
                self.create_kb_key(key, self.color_kb)

    def kb_input(self, event=None, letter=None):
        if self.game_on:
            if letter is None:
                letter = unidecode(event.char.upper())
            if self.column_counter == 0:
                self.guess = ''
            if 0 <= self.column_counter < 5 and letter.isalpha(): #Change number of inputs here.
                self.guess = self.guess + letter
                #Here is where the typed letters get put in the boxes themselves
                self.write_letters((self.pos_x + (self.block * self.column_counter)) + self.box_width * 0.5,
                                   (self.pos_y + ((self.gap + self.box_height) * self.row_counter)) + self.box_height * 0.5,
                                   letter,
                                   self.box_height)
                self.column_counter += 1

    # delete letters
    def kb_delete(self, event):
        if self.game_on:
            if self.column_counter == 0:
                return
            self.column_counter -= 1
            self.guess = self.guess[:-1]
            del_pos_x = self.pos_x + ((self.box_width + self.gap) * self.column_counter)
            del_pos_y = self.pos_y + ((self.box_height + self.gap) * self.row_counter)
            self.create_box(del_pos_x, del_pos_y, self.box_width, self.box_height, self.color_empty)

    def kb_enter(self, event):
        if self.guess in self.words:
            if self.game_on:
                if self.column_counter == 5 and self.row_counter == self.max_rows:
                    self.check_guess()
                    #             print('game over')
                    if self.game_on:
                        self.top_text(self.word, self.color_end_box)
                    self.game_on = False
                elif self.column_counter == 5:
                    #             print(guess)
                    self.check_guess()
                    self.row_counter += 1
                    self.column_counter = 0
        else:
            self.top_text(self.invalid_message, 'black')
            #sleep(0.5)
            self.root.update()
            self.delete_top_text()
            sleep(1)
            self.root.update()

            return

    def check_guess(self):
        if self.guess == self.word:
            for i, v in enumerate(self.guess):
                if v == self.word[i]:  # letters in a correct position
                    new_pos_x = self.pos_x + ((self.box_width + self.gap) * i)
                    new_pos_y = self.pos_y + ((self.box_height + self.gap) * self.row_counter)
                    self.create_box(new_pos_x, new_pos_y, self.box_width, self.box_height, self.color_right)
                    self.write_letters((self.pos_x + (self.block * i)) + (self.box_width * 0.5),
                                       (self.pos_y + ((self.gap + self.box_height) * self.row_counter)) + (self.box_height * 0.5),
                                       v,
                                       self.box_height)
                    self.create_kb_key(v, self.color_right)
                    self.root.update()
                    sleep(self.delay)
            self.game_on = False
            self.top_text(choice(self.end_game_words), self.color_end_box) #Change to output value to be sent to server/other player.
            return
        else:
            for i, v in enumerate(self.guess):
                if v == self.word[i]:  # letters in a correct position
                    new_pos_x = self.pos_x + ((self.box_width + self.gap) * i)
                    new_pos_y = self.pos_y + ((self.box_height + self.gap) * self.row_counter)
                    self.create_box(new_pos_x, new_pos_y, self.box_width, self.box_height, self.color_right)
                    self.write_letters((self.pos_x + (self.block * i)) + (self.box_width * 0.5),
                                       (self.pos_y + ((self.gap + self.box_height) * self.row_counter)) + (self.box_height * 0.5),
                                       v,
                                       self.box_height)
                    self.create_kb_key(v, self.color_right)
                    self.root.update()
                    sleep(self.delay)

                elif v in self.word and self.word.count(v) >= self.guess.count(v):  # esta na palavra
                    new_pos_x = self.pos_x + ((self.box_width + self.gap) * i)
                    new_pos_y = self.pos_y + ((self.box_height + self.gap) * self.row_counter)
                    self.create_box(new_pos_x, new_pos_y, self.box_width, self.box_height, self.color_place)
                    self.write_letters((self.pos_x + (self.block * i)) + (self.box_width * 0.5),
                                       (self.pos_y + ((self.gap + self.box_height) * self.row_counter)) + (self.box_height * 0.5),
                                       v,
                                       self.box_height)
                    self.create_kb_key(v, self.color_place)
                    self.root.update()
                    sleep(self.delay)

                elif v in self.word and self.word.count(v) < self.guess.count(v) and i < self.guess.rfind(v):
                    new_pos_x = self.pos_x + ((self.box_width + self.gap) * i)
                    new_pos_y = self.pos_y + ((self.box_height + self.gap) * self.row_counter)
                    self.create_box(new_pos_x, new_pos_y, self.box_width, self.box_height, self.color_place)
                    self.write_letters((self.pos_x + (self.block * i)) + (self.box_width * 0.5),
                                       (self.pos_y + ((self.gap + self.box_height) * self.row_counter)) + (self.box_height * 0.5),
                                       v,
                                       self.box_height)
                    self.create_kb_key(v, self.color_place)
                    self.root.update()
                    sleep(self.delay)

                else:
                    new_pos_x = self.pos_x + ((self.box_width + self.gap) * i)
                    new_pos_y = self.pos_y + ((self.box_height + self.gap) * self.row_counter)
                    self.create_box(new_pos_x, new_pos_y, self.box_width, self.box_height, self.color_wrong)
                    self.write_letters((self.pos_x + (self.block * i)) + (self.box_width * 0.5),
                                       (self.pos_y + ((self.gap + self.box_height) * self.row_counter)) + (self.box_height * 0.5),
                                       v,
                                       self.box_height)
                    self.create_kb_key(v, self.color_wrong)
                    self.root.update()
                    sleep(self.delay)

    def create_box(self, x, y, box_w, box_h, color):
        self.canvas.create_rectangle(x,
                                     y,
                                     x + box_w,
                                     y + box_h,
                                     outline="",
                                     fill=color)

    def write_letters(self, x, y, letter, h):
        self.canvas.create_text(x,
                                y,
                                text=letter,
                                font=(self.font, int(h * 0.7)),
                                fill='white')

    def create_kb_key(self, letter, color):
        self.canvas.create_rectangle(self.kb_new_pos_x + (self.kb_block * self.keyboard_dict[letter]['i']) + (self.keyboard_dict[letter]['r'] * (self.kb_box_width * 0.3)),
                                     self.kb_new_pos_y + ((self.kb_box_height + self.kb_gap) * self.keyboard_dict[letter]['r']),
                                     (self.kb_new_pos_x + (self.kb_block * self.keyboard_dict[letter]['i'])) + self.kb_box_width + (self.keyboard_dict[letter]['r'] * (self.kb_box_width * 0.3)),
                                     self.kb_new_pos_y + ((self.kb_box_height + self.kb_gap) * self.keyboard_dict[letter]['r']) + self.kb_box_height,
                                     outline="black",
                                     fill=color,
                                     tags=letter)
        # insert letter
        self.canvas.create_text((self.kb_pos_x + (self.kb_block * self.keyboard_dict[letter]['i']) +
                                 (self.kb_box_width * 0.5) + (self.keyboard_dict[letter]['r'] * (self.kb_box_width * 0.3)),
                                 (self.kb_pos_y + ((self.kb_gap + self.kb_box_height) * self.keyboard_dict[letter]['r'])) +
                                 (self.kb_box_height * 0.5)),
                                text=letter,
                                font=(self.font, int(self.kb_box_height * 0.5)),
                                fill='white',
                                tags=letter)

        # Bind key presses to clicking. Need add bind to clicking a powerup.
        self.canvas.tag_bind(letter, "<Button-1>", lambda e, var=letter: self.kb_input(letter=var))

    def top_text(self, top_word, color):
        answer_box_width = Font(family=self.font, size=int(self.kb_box_height * 0.5)).measure(top_word)
        answer_pos_x_1 = (self.width * 0.5 - (answer_box_width / 2)) * 0.98
        answer_pos_x_2 = (answer_pos_x_1 + answer_box_width) * 1.025  # * 0.57
        answer_pos_y_1 = self.pos_y * 0.5  # (((pos_y) - (pos_y / 4)) * 0.95) - answer_pos_y_2
        answer_pos_y_2 = answer_pos_y_1 * 1.9

        self.top_box = self.canvas.create_rectangle(answer_pos_x_1,
                                                    answer_pos_y_1,
                                                    answer_pos_x_2,
                                                    answer_pos_y_2,
                                                    outline="",
                                                    fill=color)

        self.top_word = self.canvas.create_text((self.width / 2,
                                                 (self.pos_y - (self.pos_y / 4)) * 0.95),
                                                text=top_word,
                                                font=(self.font, int(self.kb_box_height * 0.5)),
                                                fill='white')

    def delete_top_text(self):
        self.canvas.delete(self.top_box)
        self.canvas.delete(self.top_word)

    def special_keys(self):
        # positions of enter and back keys
        ent_pos_x1 = self.kb_new_pos_x + (self.kb_block * 7) + (2 * (self.kb_box_width * 0.3))
        ent_pos_x2 = (self.kb_new_pos_x + (self.kb_block * 9)) + self.kb_box_width + (2 * (self.kb_box_width * 0.5))
        ent_pos_y1 = self.kb_new_pos_y + ((self.kb_box_height + self.kb_gap) * 2)
        ent_pos_y2 = self.kb_new_pos_y + ((self.kb_box_height + self.kb_gap) * 2) + self.kb_box_height

        del_pos_x1 = self.kb_new_pos_x + (self.kb_block * 9) + (1 * (self.kb_box_width * 0.3))
        del_pos_x2 = (self.kb_new_pos_x + (self.kb_block * 9)) + self.kb_box_width + (1 * (self.kb_box_width * 0.6))
        del_pos_y1 = self.kb_new_pos_y + ((self.kb_box_height + self.kb_gap) * 1)
        del_pos_y2 = self.kb_new_pos_y + ((self.kb_box_height + self.kb_gap) * 1) + self.kb_box_height

        #Power up rect positions
        pow_pos_x1 = self.pow_x
        pow_pos_y1 = self.pow_y
        pow_pos_x2 = self.pow_x + self.kb_box_width
        pow_pos_y2 = self.pow_x - self.kb_box_height

        self.canvas.create_rectangle(pow_pos_x1,
                                     pow_pos_y1,
                                     pow_pos_x2,
                                     pow_pos_y2,
                                     outline="black",
                                     fill=self.color_kb,
                                     tags='ENTER')
        

        # enter key
        self.canvas.create_rectangle(ent_pos_x1,
                                     ent_pos_y1,
                                     del_pos_x2,
                                     ent_pos_y2,
                                     outline="black",
                                     fill=self.color_kb,
                                     tags='ENTER')

        self.canvas.create_text(((ent_pos_x1 + del_pos_x2) / 2,
                                 ent_pos_y1 + (self.kb_box_height * 0.5)),
                                text='ENTER',
                                font=(self.font, int(self.kb_box_height * 0.5)),
                                fill='white',
                                tags='ENTER')
        # Backspace key
        self.canvas.create_rectangle(del_pos_x1,
                                     del_pos_y1,
                                     del_pos_x2,
                                     del_pos_y2,
                                     outline="black",
                                     fill=self.color_kb,
                                     tags='⌫')

        self.canvas.create_text(((del_pos_x1 + del_pos_x2) / 2,
                                 del_pos_y1 + (self.kb_box_height * 0.5)),
                                text='⌫',
                                font=(self.font, int(self.kb_box_height * 0.5)),
                                fill='white',
                                tags='⌫')

        # bind special keys to action
        self.canvas.tag_bind('ENTER', "<Button-1>", lambda e, var='ENTER': self.kb_enter(var))
        self.canvas.tag_bind('⌫', "<Button-1>", lambda e, var='⌫': self.kb_delete(var))


wordle = Wordle(600, 700)
wordle.generate_gui()