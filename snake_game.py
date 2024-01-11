import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Définition des constantes
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
SNAKE_SIZE = 30  # Augmenté la taille du serpent
FPS = 5  # Réduit la vitesse du jeu

# Couleurs
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Direction initiale du serpent
direction = (1, 0)

# Chargez les images sans utiliser le chemin absolu
try:
    snake_image = pygame.image.load("snake.png")
    apple_image = pygame.image.load("apple.png")

    # Redimensionnez les images si nécessaire
    snake_image = pygame.transform.scale(snake_image, (SNAKE_SIZE, SNAKE_SIZE))
    apple_image = pygame.transform.scale(apple_image, (SNAKE_SIZE, SNAKE_SIZE))
except pygame.error as e:
    print(f"Erreur lors du chargement des images : {e}")
    sys.exit(1)

# Fonction principale
def main():
    global direction

    # Initialisation de l'écran
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Horloge Pygame
    clock = pygame.time.Clock()

    while True:
        snake, apple = reset_game()  # Réinitialiser le jeu
        game_over_flag = False

        while not game_over_flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    handle_key_event(event.key)

            # Mise à jour de la position du serpent
            snake = move_snake(snake)

            # Vérification des collisions avec la pomme
            if snake[0] == apple:
                snake.append(snake[-1])  # Ajouter une nouvelle section au serpent
                apple = generate_apple(snake)

            # Vérification des collisions avec le serpent lui-même
            if check_collision(snake):
                game_over_flag = True
                print("Game Over!")  # Ajoutez un message ou une interface graphique pour indiquer la fin du jeu
                pygame.time.delay(2000)  # Attendre 2 secondes (2000 millisecondes) après la collision
                break  # Sortir de la boucle pour réinitialiser le jeu

            # Dessin de l'écran
            screen.fill(WHITE)
            draw_snake(screen, snake)
            draw_apple(screen, apple)
            pygame.display.flip()

            # Contrôle de la vitesse du jeu
            clock.tick(FPS)

# Fonction pour réinitialiser le jeu
def reset_game():
    global direction

    direction = (1, 0)

    # Initialisation du serpent
    snake = [(100, 100), (90, 100), (80, 100)]

    # Position initiale de la pomme
    apple = generate_apple(snake)

    return snake, apple

# Fonction pour générer une nouvelle position pour la pomme
def generate_apple(snake):
    while True:
        apple = (
            random.randrange(0, WIDTH // GRID_SIZE) * GRID_SIZE,
            random.randrange(0, HEIGHT // GRID_SIZE) * GRID_SIZE
        )
        if apple not in snake:
            return apple

# Fonction pour afficher le serpent
def draw_snake(screen, snake):
    for segment in snake:
        screen.blit(snake_image, segment)

# Fonction pour afficher la pomme
def draw_apple(screen, apple):
    screen.blit(apple_image, apple)

# Fonction pour déplacer le serpent
def move_snake(snake):
    global direction
    x, y = snake[0]
    x += direction[0] * SNAKE_SIZE
    y += direction[1] * SNAKE_SIZE

    # Ajout de la nouvelle tête du serpent
    snake.insert(0, (x, y))

    # Retrait de la queue si la longueur du serpent est dépassée
    if len(snake) > 1:
        snake.pop()

    return snake

# Fonction pour vérifier les collisions avec le serpent lui-même
def check_collision(snake):
    return snake[0] in snake[1:]

# Fonction pour gérer les événements de touche
def handle_key_event(key):
    global direction
    if key == pygame.K_LEFT and direction != (1, 0):
        direction = (-1, 0)
    elif key == pygame.K_RIGHT and direction != (-1, 0):
        direction = (1, 0)
    elif key == pygame.K_UP and direction != (0, 1):
        direction = (0, -1)
    elif key == pygame.K_DOWN and direction != (0, -1):
        direction = (0, 1)

# Fonction pour afficher l'écran de fin de jeu
def game_over():
    print("Game Over!")  # Ajoutez un message ou une interface graphique pour indiquer la fin du jeu
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
