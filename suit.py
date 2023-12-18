import random

def play_rps():
    choices = ["batu", "kertas", "gunting"]
    
    user_choice = input("Pilih batu, gunting, atau kertas: ").lower()
    if user_choice not in choices:
        print("Pilihan tidak valid. Pilih antara batu, gunting, atau kertas.")
        return
    
    computer_choice = random.choice(choices)
    
    print(f"Komputer memilih: {computer_choice}")

    if user_choice == computer_choice:
        print("Hasil: Seri!")
    elif (
        (user_choice == "batu" and computer_choice == "gunting") or
        (user_choice == "kertas" and computer_choice == "batu") or
        (user_choice == "gunting" and computer_choice == "kertas")
    ):
        print("Hasil: Anda menang!")
    else:
        print("Hasil: Anda kalah!")

if __name__ == "__main__":
    play_rps()
