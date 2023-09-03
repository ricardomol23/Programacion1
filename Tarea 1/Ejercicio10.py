def main():
    try:
        num_shows = int(input("Ingresa el número de shows asistidos en el último año: "))
        
        if num_shows > 3:
            print("True")
        else:
            print("False")
    except ValueError:
        print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()