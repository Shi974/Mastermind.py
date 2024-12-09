import random

print( (3**2)//2 )

COLORS = ["R", "V", "B", "O", "J", "N"]
TRIES = 10
CODE_LENGTH = 4

def gen_code():
  code = []

  for _ in range(CODE_LENGTH):
    color = random.choice(COLORS)
    code.append(color)

  return code


def guess_code():
  while True:
    guess = input("Essai : ").upper().split(" ")
  
    if len(guess) != CODE_LENGTH:
      print(f"Vous devez deviner un code de {CODE_LENGTH} couleurs séparé par des espaces.")
      continue

    for color in guess:
      if color not in COLORS:
        print(f"Désolé, la couleur {color} est invalide. Essayez à nouveau.")
        break
    else:
      break

  return guess


def check_code(guess, real_code):
  color_counts = {}
  correct_pos = 0
  incorrect_pos = 0

  for color in real_code:
    if color not in color_counts:
      color_counts[color] = 0
    color_counts[color] += 1

  for guess_color, real_color in zip(guess, real_code):
    if guess_color == real_color:
      correct_pos += 1
      color_counts[guess_color] -= 1

  for guess_color, real_color in zip(guess, real_code):
    if guess_color in color_counts and color_counts[guess_color] > 0:
      incorrect_pos += 1
      color_counts[guess_color] -= 1

  return correct_pos, incorrect_pos


def emojify_code(code):
  emojis = ""
  for bille in code:
    match bille:
      case "R":
        emojis += "🔴"
      case "V":
        emojis += "🟢"
      case "B":
        emojis += "⚪"
      case "O":
        emojis += "🟠"
      case "J":
        emojis += "🟡"
      case "N":
        emojis += "⚫"

  return emojis


def game():
  print(f"🔴🟢⚪🟠🟡⚫ Bienvenue dans Mastermind ! ⚫🟡🟠⚪🟢🔴 \nVous avez {TRIES} essais pour deviner le code de constitué {CODE_LENGTH} billes.")
  print("Les couleurs valides pour ce challenge sont ", *COLORS)
  code = gen_code()
  #print(f"Débogage, vrai code : {code}")
  for attempts in range (1, TRIES + 1):
    guess = guess_code()
    correct_pos, incorrect_pos = check_code(guess, code)

    if correct_pos == CODE_LENGTH:
      print(f"Bravo ! 🎉 Vous avez deviné le code en {attempts} essais !")
      emojis = emojify_code(code)
      print(emojis)
      break
    
    print(f"Placements corrects : {correct_pos} | Mauvais placements : {incorrect_pos}")

  else: 
    print("Vous avez épuisé vos essais. Le code était : ", *code)
    emojis = emojify_code(code)
    print(emojis)


if __name__ == "__main__":
  game()