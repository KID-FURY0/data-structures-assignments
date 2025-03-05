def main():
    # Input for domestic animals
    domestic_animals = []
    n = int(input("Enter the number of domestic animals: "))
    for i in range(n):
        animal = input(f"Enter domestic animal {i + 1}: ")
        domestic_animals.append(animal)

    # Input for wild animals
    wild_animals = []
    x = int(input("Enter the number of wild animals: "))
    for i in range(x):
        animal = input(f"Enter wild animal {i + 1}: ")
        wild_animals.append(animal)

    # Combine the two lists
    all_animals = domestic_animals + wild_animals

    # Print all animals
    print("\nAll animals:")
    for animal in all_animals:
        print(animal)

if __name__ == "__main__":
    main()