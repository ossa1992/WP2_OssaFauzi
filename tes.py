import random

def sorting(numbers):
    sorted_numbers = numbers.copy()
    sorted_numbers.sort()
    return sorted_numbers

def searching(numbers, target):
    if target in numbers:
        return "Angka ditemukan"
    else:
        return "Angka tidak ditemukan"

def main():
    numbers = []
    while True:
        print("Menu Pilihan:")
        print("1. Input Angka")
        print("2. Sorting")
        print("3. Searching")
        print("4. Keluar")
        choice = input("Masukkan pilihan [1/2/3/4]: ")

        if choice == '1':
            print("\nINPUT ANGKA")
            n = int(input("Masukkan jumlah nilai tugas: "))
            print("Input Angka Secara Acak")
            print("-----------------------------")
            for i in range(n):
                angka = int(input(f"Angka {i+1}: "))
                numbers.append(angka)
            print()
        
        elif choice == '2':
            sorted_numbers = sorting(numbers)
            print("\nTAMPIL HASIL SORTING")
            print("Hasil sorting:", sorted_numbers)
            print()
        
        elif choice == '3':
            print("\nTAMPIL HASIL SEARCHING")
            target = int(input("Masukkan angka yang ingin dicari: "))
            result = searching(numbers, target)
            print(result)
            print()
        
        elif choice == '4':
            break
        
        else:
            print("Pilihan tidak valid")
            print()

if __name__ == "__main__":
    main()
