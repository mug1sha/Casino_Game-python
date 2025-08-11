import random  # Used for generating random bets and winning cells

# Global lists for storing game elements
players = []  # List of Player objects (Human + Computers)
table = []    # List of Cell objects representing the betting table
cells = []    # List of cell names ('R', 'B', '1'...'8') for betting

# -------------------------
# Base Player class
# -------------------------
class Player:
    def __init__(self, name, coin):
        self.name = name      # Player's name
        self.coin = coin      # Player's current coins
        self.bets = {}        # Dictionary to store bets for each cell
        self.reset_table()    # Initialize all bets to 0

    # Deduct bet from player's coins and store it in bets dictionary
    def set_bet_coin(self, bet_coin, bet_cell):
        self.coin -= bet_coin
        self.bets[bet_cell] = bet_coin
        print(self.name + ' bet ' + str(bet_coin) +
              ' coin(s) to ' + bet_cell + '.')

    # Reset all bets to 0 for a new round
    def reset_table(self):
        for cell in table:
            self.bets.update({cell.name: 0})

# -------------------------
# Human player class (inherits from Player)
# -------------------------
class Human(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin)

    # Handles the human's betting process
    def bet(self):
        # Limit maximum bet to 99 or player's current coins (whichever is smaller)
        if self.coin >= 99:
            max_bet_coin = 99
        else:
            max_bet_coin = self.coin

        # Ask for coin amount to bet
        bet_message = 'How many coins do you bet?:(1-' + str(max_bet_coin) + ')'
        bet_coin = input(bet_message)
        while not self.enable_bet_coin(bet_coin, max_bet_coin):
            bet_coin = input(bet_message)

        # Ask for cell to bet on (R, B, or number 1-8)
        bet_message = 'On what do you bet?: (R, B, 1-8)'
        bet_cell = input(bet_message)
        while not self.enable_bet_cell(bet_cell):
            bet_cell = input(bet_message)

        # Place bet using Player class method
        super().set_bet_coin(int(bet_coin), bet_cell)

    # Validate bet coin amount
    def enable_bet_coin(self, string, max_bet_coin):
        if string.isdigit():
            number = int(string)
            return 1 <= number <= max_bet_coin
        return False

    # Validate bet cell choice
    def enable_bet_cell(self, string):
        if string.isdigit():
            number = int(string)
            return 1 <= number <= 8
        else:
            return string in ('R', 'B')

# -------------------------
# Computer player class (inherits from Player)
# -------------------------
class Computer(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin)

    # Automatically places a random bet
    def bet(self):
        if self.coin >= 99:
            max_bet_coin = 99
        else:
            max_bet_coin = self.coin
        bet_coin = random.randint(1, max_bet_coin)  # Random bet amount

        # Pick a random cell from cells list
        bet_cell_number = random.randint(0, len(cells) - 1)
        bet_cell = cells[bet_cell_number]
        super().set_bet_coin(bet_coin, bet_cell)

# -------------------------
# Cell class (represents a betting option)
# -------------------------
class Cell:
    def __init__(self, name, rate, color):
        self.name = name    # Cell name (R, B, 1-8)
        self.rate = rate    # Payout multiplier
        self.color = color  # Cell color (red or black)

# -------------------------
# Color codes for text formatting
# -------------------------
class ColorBase:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    END = '\033[0m'

# -------------------------
# Setup helper functions
# -------------------------

# Store cell names in global cells list
def set_cells():
    global cells
    cells = []
    for cell in table:
        cells.append(cell.__dict__['name'])

# Create all players (1 human + 3 computers)
def create_players():
    global players
    human = Human('MY', 500)
    computer1 = Computer('C1', 500)
    computer2 = Computer('C2', 500)
    computer3 = Computer('C3', 500)
    players = [human, computer1, computer2, computer3]

# All players place bets
def bet_players():
    for player in players:
        player.bet()

# -------------------------
# Game logic functions
# -------------------------

# Pick winning cell and check who won
def check_hit():
    hit_cell_number = random.randint(0, len(cells) - 1)
    hit_cell = cells[hit_cell_number]
    print('Winning number is ' + hit_cell + '.')
    for player in players:
        if player.bets[hit_cell] >= 1:
            win_player(player, hit_cell_number)

# Give winnings to the winning player
def win_player(player, hit_cell_number):
    hit_cell = cells[hit_cell_number]
    win_coin = player.bets[hit_cell] * table[hit_cell_number].rate
    player.coin += win_coin
    print(player.name + ' won. Gained ' + str(win_coin) + ' coins.')

# Show each player's current coins
def show_coin():
    message = '[Players\' coin] '
    for player in players:
        message += player.name + ': ' + str(player.coin) + ' / '
    print(message)

# Create the betting table (red/black + numbers with payouts)
def create_table():
    global table
    table.append(Cell('R', 2, 'red'))
    table.append(Cell('B', 2, 'black'))
    table.append(Cell('1', 8, 'red'))
    table.append(Cell('2', 8, 'black'))
    table.append(Cell('3', 8, 'red'))
    table.append(Cell('4', 8, 'black'))
    table.append(Cell('5', 8, 'red'))
    table.append(Cell('6', 8, 'black'))
    table.append(Cell('7', 8, 'red'))
    table.append(Cell('8', 8, 'black'))

# Show table with current bets
def show_table():
    # Header row
    row = green_bar() + '_____' + green_bar()
    for player in players:
        row += player.name + green_bar()
    print(row)

    # Rows for each cell and bets
    for cell in table:
        row = green_bar() + color(cell.color, cell.name +
                                  '(x' + str(cell.rate) + ')') + green_bar()
        for player in players:
            row += str(player.bets[cell.name]).zfill(2) + green_bar()
        print(row)

# Reset all players' bets for new round
def reset_table():
    for player in players:
        player.reset_table()

# Color text based on given color name
def color(color_name, string):
    if color_name == 'red':
        return ColorBase.RED + string + ColorBase.END
    elif color_name == 'green':
        return ColorBase.GREEN + string + ColorBase.END
    else:
        return string

# Return a green-colored bar symbol
def green_bar():
    return color('green', '｜')

# -------------------------
# Game flow functions
# -------------------------

# Initialize game: table, players, cell names
def initialize():
    create_table()
    create_players()
    set_cells()

# Play one round
def play_once():
    reset_table()
    bet_players()
    show_table()
    check_hit()
    show_coin()

# Check if any player has 0 coins (end condition)
def is_game_end():
    for player in players:
        if player.coin <= 0:
            return True
    return False

# Announce game over and who lost
def game_end():
    for player in players:
        if player.coin <= 0:
            print('Game ends as ' + player.name + ' has no coin.')

# -------------------------
# Main game loop
# -------------------------
def play():
    initialize()
    show_coin()
    while not is_game_end():  # Keep playing until someone has no coins
        play_once()
    else:
        game_end()

# Start the game
play()
