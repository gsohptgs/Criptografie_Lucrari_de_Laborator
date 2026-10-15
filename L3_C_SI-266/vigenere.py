alfabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"

def vigenere():
    print("--- CIFRUL VIGENÈRE (Sarcina 3.2) ---")
    operatie = input("Alege operația (criptare/decriptare): ").strip().lower()
    text = input("Introdu mesajul: ").replace(" ", "").upper()
    cheie = input("Introdu cheia (minim 7 litere): ").replace(" ", "").upper()

    if len(cheie) < 7:
        return "Eroare: Lungimea cheii nu trebuie să fie mai mică de 7."
    
    for c in text + cheie:
        if c not in alfabet:
            return f"Eroare: Caracterul '{c}' nu este permis. Folosește doar literele A-Z, cu sau fără diacritice."

    rezultat = ""
    for i, m in enumerate(text):
        idx_m = alfabet.index(m)
        idx_k = alfabet.index(cheie[i % len(cheie)])
        
        # Criptarea și decriptarea pe baza modelului matematic
        if operatie == "criptare":
            idx_c = (idx_m + idx_k) % 31
        elif operatie == "decriptare":
            idx_c = (idx_m - idx_k) % 31
        else:
            return "Operație invalidă."
            
        rezultat += alfabet[idx_c]
    
    return f"Rezultat: {rezultat}"

print(vigenere())