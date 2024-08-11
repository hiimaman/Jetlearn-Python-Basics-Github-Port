# She thought I stole it... (I did, from chatGPT)

def get_menu(sweet, savory, quick, healthy):
  if sweet == 'yes':
    return "Pancakes with Syrup"
  elif savory == 'yes':
    return "Scrambled Eggs and Bacon"
  elif quick == 'yes':
    return "Cereal with Milk"
  elif healthy == 'yes':
    return "Smoothie or Oatmeal"
  else:
    return "Toast with Butter and Jam"  # Default option if no preferences are selected


def main():
  print("Welcome to the Breakfast Menu Generator!")
  print("Please answer the following questions with 'yes' or 'no':")

  sweet = input("Do you prefer sweet dishes? ")
  savory = input("Do you prefer savory dishes? ")
  quick = input("Do you need a quick meal? ")
  healthy = input("Do you prefer healthy options? ")

  menu_item = get_menu(sweet, savory, quick, healthy)
  print("\nYour Breakfast Menu:")
  print(f"- {menu_item}")


if __name__ == "__main__":
  main()
