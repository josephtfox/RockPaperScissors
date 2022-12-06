# Name: Tanner Fox 
# Email: josephtfox@gmail.com

# define the inbetween to be able to have click able images for the user inputs 
def inbetween(pt1, pt2, pt3):
    return pt1.getX() <= pt2.getX() <= pt3.getX() and pt1.getY() <= pt2.getY() <= pt3.getY()

# define function to make the images clickable
def clickable_images(win):
    # x and y values of the top left and bottom right corners of each image respectively 
    click_rock_left = Point(16, 600)
    click_rock_right = Point(284, 901)
    click_paper_left = Point(330, 633)
    click_paper_right = Point(638, 868)
    click_scissor_left = Point(685, 622)
    click_scissor_right = Point(984, 877)
    quit_left = Point(2, 2)
    quit_right = Point(60, 50)
    
    # user input from clicking on the window 
    click_point = win.getMouse()
    
    while not inbetween(click_rock_left, click_point, click_rock_right) and not inbetween(click_paper_left, click_point, click_paper_right) and not inbetween(click_scissor_left, click_point, click_scissor_right) and not inbetween(quit_left, click_point, quit_right):
        
        # let the user click again 
        click_point = win.getMouse()
    
    # report which image the user clicked on and return its value 
    if inbetween(click_rock_left, click_point, click_rock_right):
        return 'r'
    
    elif inbetween(click_paper_left, click_point, click_paper_right):
        return 'p'
    
    elif inbetween(click_scissor_left, click_point, click_scissor_right):
        return 's'
    
    elif inbetween(quit_left, click_point, quit_right):
        return 'quit'

# prints whether you tie, win, or lose to the window 
def lose_win_tie(value, win):
    if value == 0:
        tie_txt = Text (Point(250, 300), 'Its a Tie')
        tie_txt.setSize(30)
        tie_txt.draw(win)               
    elif value == 1:
        winning_txt = Text (Point(250, 300), 'You Win')
        winning_txt.setSize(30)
        winning_txt.draw(win) 
    elif value == 2:
        lose_txt = Text (Point(250, 300), 'You Lose')
        lose_txt.setSize(30)
        lose_txt.draw(win)
        
# Clears the lose_win_tie text and the scoreboard
def clear_txt(win):
    a = Rectangle (Point(100, 250), Point(400, 400))
    a.setFill('Blue')
    b = Rectangle (Point(521, 170), Point(721, 363))
    b.setFill('Green')
    c = Rectangle (Point(770, 159), Point(968, 372))
    c.setFill('Orange')
    a.draw(win)
    b.draw(win)
    c.draw(win)
    


from graphics import *
from random import *

def main():
    # Creates the window 
    win = GraphWin('Rock Paper Scissors', 750, 750)
    
    # prints the title to the window
    title = Text (Point(500, 50), 'Welcome to the Game of Rock Paper Scissors!')
    title.setTextColor('Purple')
    title.setSize(30)
    title.draw(win)
    
    # Create the score board and print to the window 
    scoreboard = Rectangle(Point(995, 400), Point(500, 100))
    scoreboard_line = Line(Point(747.5, 100), Point(747.5, 400))
    scoreboard_lineA = Line(Point(500, 140), Point(995, 140))
    scoreboard.setWidth(5)
    scoreboard_line.setWidth(5)
    scoreboard_lineA.setWidth(5)
    scoreboard.draw(win)
    scoreboard_line.draw(win)
    scoreboard_lineA.draw(win)
    
    scoreboard_player_txt = Text(Point(623.75, 120), 'You')
    scoreboard_comp_txt = Text(Point(871.25, 120), 'Computer')
    scoreboard_player_txt.setSize(25)
    scoreboard_comp_txt.setSize(25)
    scoreboard_player_txt.draw(win)
    scoreboard_comp_txt.draw(win)
    
    # insert the three images of rock, paper, and scissor
    rock_image = Image(Point(150, 750), "Rock.gif")
    rock_image.draw(win)
    paper_image = Image(Point(485, 750), "paper.gif")
    paper_image.draw(win)
    scissor_image = Image(Point(835, 750), "scissor.gif")
    scissor_image.draw(win)
    
    # Create quit button
    quit_box = Rectangle(Point(2, 2), Point(60, 50))
    quit_txt = Text(Point(30, 25), 'Quit')
    quit_box.setFill('red')
    quit_box.setWidth(3)
    quit_txt.setSize(20)
    quit_box.draw(win)
    quit_txt.draw(win)
    
    # create a list of options 
    rps = ['r', 'p', 's']
    
    # set play game flag to true
    play_game = True
    
    # Initialize the score for the player and the computer 
    player_score = 0 
    computer_score = 0   
   
    # while statement for if the user still wants to play the game 
    while play_game == True:
        # generate a random answer for the computer 
        computer = rps[randint(0,2)]
        
        player = clickable_images(win)
        clear_txt(win)
        if player == computer:
            lose_win_tie(0, win)
        elif player == 'r':
            if computer == 'p':
                lose_win_tie(2, win)
                computer_score += 1
            else:
                lose_win_tie(1, win)
                player_score += 1
                
        elif player == 'p':
            if computer == 's':
                lose_win_tie(2, win)
                computer_score += 1
            else:
                lose_win_tie(1, win)
                player_score += 1
                
        elif player == 's':
            if computer == 'r':
                lose_win_tie(2, win)
                computer_score += 1
            else:
                lose_win_tie(1, win)
                player_score += 1
                
        elif player == 'quit':
            play_game = False
        comp_score_txt = Text(Point(875, 250), computer_score)
        player_score_txt = Text(Point(625, 250), player_score)
        comp_score_txt.setSize(30)
        player_score_txt.setSize(30)
        comp_score_txt.draw(win)
        player_score_txt.draw(win)
    win.close() 
main()
