import pygame
import random

pygame.init()

display_width = 900
display_height = 400

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake")

done = False

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
background = white

x = 50
y = 50

clock = pygame.time.Clock()

snake_block = 10
#snake_speed = 15

users = {}
scores = []

font_style = pygame.font.SysFont(None, 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [display_width / 9, display_height / 4])


def show_score(number):
    score = font_style.render("Your score: " + str(number), True, black)
    screen.blit(score, [0, 0])


def gameSnake(snake_speed, food_time_limit, username=None):
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    lenght_of_snake = 1

    food_width = random.randint(5, 15)
    food_height = random.randint(5, 15)
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
    #food_time_limit = 5000
    last_food_time = pygame.time.get_ticks()

    while not game_over:

        while game_close:
            screen.fill(white)
            message("Looser, r - repeat, c - close. Your score is: " + str(lenght_of_snake - 1), red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        playagain()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(green)

        if pygame.time.get_ticks() - last_food_time > food_time_limit:
            foodx = round(random.randrange(0, display_width - food_width) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - food_height) / 10.0) * 10.0
            food_width = random.randint(5, 15)
            food_height = random.randint(5, 15)
            last_food_time = pygame.time.get_ticks()

        pygame.draw.rect(screen, red, [foodx, foody, food_width, food_height])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > lenght_of_snake:
            del snake_List[0]

        our_snake(snake_block, snake_List)
        show_score(lenght_of_snake - 1)
        scores.append(show_score(lenght_of_snake - 1))

        if x1 >= foodx and x1 <= foodx + food_width and y1 >= foody and y1 <= foody + food_height:
            foodx = round(random.randrange(0, display_width - food_width) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - food_height) / 10.0) * 10.0
            food_width = random.randint(5, 15)
            food_height = random.randint(5, 15)
            lenght_of_snake += 1
            update_score(username)
            last_food_time = pygame.time.get_ticks()

        pygame.display.update()
        clock.tick(snake_speed)
    users[username] = lenght_of_snake - 1
    #users.append((username, lenght_of_snake - 1)) 

    #pygame.quit()
    #quit()

def create_user(username):
    """global users
    for user in users:
        if user["username"] == username:
            print("User already exists. Updating existing user.")
            return
    
    scoresOfUsers = 0
    for i in scores:
        scoresOfUsers = scores[i]
    
    users.append({"username": username, "score": scoresOfUsers})
    print("User created successfully!")
    print("User list:", users)"""
    if username in users:
        print("User already exists. Current score:", users[username])
    else:
        users[username] = 0  
        print("User created successfully! Username:", username)

def playagain():
    option = input("Do you want to play again? (Y/N): ").lower()
    if option == "y":
        option = input("Are you a new user? (Y/N): ").lower()
        if option == "y":
            start_game()
        elif option == "n":
            start_game()
        else:
            print("Invalid option! Please enter Y or N.")
    elif option == "n":
        option = input("Are you a new user? (Y/N): ").lower()
        if option == "y":
            start_game()
        elif option == "n":
            show_user_table()
        else:
            print("Invalid option! Please enter Y or N.")
    else:
        print("Invalid option! Please enter Y or N.")

def get_level_settings(level):
    if level == '1':  
        return 10, 5000 
    elif level == '2': 
        return 15, 3000  
    elif level == '3': 
        return 20, 2000  
    
def update_score(username, increment=1):
    if username in users:
        users[username] += increment
    else:
        print(f"User {username} does not exist. Use create_user() to add the user first.")


def start_game():
    global users
    print("Welcome to Snake Game!")
    username = input("Please enter your username: ")
    print("Hello, " + username + "!")
    create_user(username)
    
    level = input("Choose a level (1: Easy, 2: Medium, 3: Hard): ")
    while level not in ['1', '2', '3']:
        print("Invalid level! Please choose 1, 2, or 3.")
        level = input("Choose a level (1: Easy, 2: Medium, 3: Hard): ")
    
    snake_speed, food_time_limit = get_level_settings(level)
    
    gameSnake(snake_speed, food_time_limit, username)
    playagain()
        
def show_user_table():
    """global users
    print("User Scores:")
    for user in users:
        print(f"Username: {user['username']}, Score: {user['score']}\n")"""
    print("User Scores:")
    for username, score in users.items():
        print(f"Username: {username}, Score: {score}")


start_game()
show_user_table()