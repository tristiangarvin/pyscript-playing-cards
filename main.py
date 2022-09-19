import datetime as dt 
import random
import copy

card_deck = [['Ace of Spades &#9824;', 'King of Spades &#9824;', \
            'Queen of Spades &#9824;', 'Jack of Spades &#9824;', \
            '10 of Spades &#9824;', '9 of Spades &#9824;', \
            '8 of Spades &#9824;', '7 of Spades &#9824;', \
            '6 of Spades &#9824;', '5 of Spades &#9824;', \
            '4 of Spades &#9824;', '3 of Spades &#9824;', \
            '2 of Spades &#9824;'], \
            ['Ace of Diamonds <span style="color:red;">&#9830;</span>', 'King of Diamonds <span style="color:red;">&#9830;</span>', \
            'Queen of Diamonds <span style="color:red;">&#9830;</span>', 'Jack of Diamonds <span style="color:red;">&#9830;</span>', \
            '10 of Diamonds <span style="color:red;">&#9830;</span>', '9 of Diamonds <span style="color:red;">&#9830;</span>', \
            '8 of Diamonds <span style="color:red;">&#9830;</span>', '7 of Diamonds <span style="color:red;">&#9830;</span>', \
            '6 of Diamonds <span style="color:red;">&#9830;</span>', '5 of Diamonds <span style="color:red;">&#9830;</span>', \
            '4 of Diamonds <span style="color:red;">&#9830;</span>', '3 of Diamonds <span style="color:red;">&#9830;</span>', \
            '2 of Diamonds <span style="color:red;">&#9830;</span>'],\
            ['Ace of Clubs &#9827', 'King of Clubs &#9827', \
            'Queen of Clubs &#9827', 'Jack of Clubs &#9827', \
            '10 of Clubs &#9827', '9 of Clubs &#9827', \
            '8 of Clubs &#9827', '7 of Clubs &#9827', \
            '6 of Clubs &#9827', '5 of Clubs &#9827', \
            '4 of Clubs &#9827', '3 of Clubs &#9827', \
            '2 of Clubs &#9827'],\
            ['Ace of Hearts <span style="color:red;">&hearts;</span>', 'King of Hearts <span style="color:red;">&hearts;</span>', \
            'Queen of Hearts <span style="color:red;">&hearts;</span>', 'Jack of Hearts <span style="color:red;">&hearts;</span>', \
            '10 of Hearts <span style="color:red;">&hearts;</span>', '9 of Hearts <span style="color:red;">&hearts;</span>', \
            '8 of Hearts <span style="color:red;">&hearts;</span>', '7 of Hearts <span style="color:red;">&hearts;</span>', \
            '6 of Hearts <span style="color:red;">&hearts;</span>', '5 of Hearts <span style="color:red;">&hearts;</span>', \
            '4 of Hearts<span style="color:red;">&hearts;</span>', '3 of Hearts <span style="color:red;">&hearts;</span>', \
            '2 of Hearts <span style="color:red;">&hearts;</span>']]

game_deck = copy.deepcopy(card_deck)
output_el = Element('cards').element
shuffle_el = Element('shuffled').element
remaining_el = Element('remaining').element

def remaining():
    counter = 0
    for suite in game_deck:
        for card in suite:
            counter += 1
    if counter > 1:
        remaining_el.innerHTML = '<b>There are ' + str(counter) + ' cards remaining.</b>'
    else: 
        remaining_el.innerHTML = '<b>There are no more cards :(</b>'

def shuffle(*args):
    global game_deck
    game_deck = copy.deepcopy(card_deck)
    output_el.innerHTML = ''
    remaining_el.innerHTML = '<b>The Deck Has Been Shuffled</b>'
    remaining()

def card_draw(*args):
    while True:
        if len(game_deck) == 0:
           break
        random_suit = random.randint(0, len(game_deck) - 1)
        if len(game_deck[random_suit]) == 0:
            del game_deck[random_suit]
            continue
        random_card = random.randint(0, len(game_deck[random_suit]) -1)
        card_selection = game_deck[random_suit][random_card]
        output_el.innerHTML += '<li>' + card_selection + '</li>'
        del game_deck[random_suit][random_card]
        break

def game(*args):
    output_el.innerHTML = ''
    remaining_el.innerHTML = ''
    numCards = Element('num-cards').element.value
    try:
        int(numCards)
    except:
        remaining_el.innerHTML = '<b>Please enter an integer.</b>'
        numCards = Element('num-cards').element.value = ''
    for i in range(int(numCards)):
        if game_deck.__len__() > 0:
            card_draw()
    numCards = Element('num-cards').element.value = ''
    remaining()

remaining()

