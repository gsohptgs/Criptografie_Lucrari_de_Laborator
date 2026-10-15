# Cifrul Cezar - Implementare UTM FCIM (Sarcina 1.1 si 1.2)
# Alfabetul romanesc extins (31 de litere)
ALFABET = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
N = len(ALFABET)

def curata_text(text):
    text_curat = ""
    for char in text.upper():
        if char in ALFABET:
            text_curat += char
    return text_curat

def genereaza_alfabet_permutat(k2_text):
    k2_curat = curata_text(k2_text)
    cheie_unica = ""
    for char in k2_curat:
        if char not in cheie_unica:
            cheie_unica += char
            
    restul = ""
    for char in ALFABET:
        if char not in cheie_unica:
            restul += char
            
    return cheie_unica + restul

def criptare(text, k1, alfabet):
    rez = ""
    for char in text:
        idx = alfabet.index(char)
        nou_idx = (idx + k1) % N
        rez += alfabet[nou_idx]
    return rez

def decriptare(criptograma, k1, alfabet):
    rez = ""
    for char in criptograma:
        idx = alfabet.index(char)
        nou_idx = (idx - k1) % N
        rez += alfabet[nou_idx]
    return rez

def main():
    print("=== CIFRUL CEZAR (1 CHEIE SI 2 CHEI) ===")
    print("1. Single-Key Caesar Cipher")
    print("2. Two-Key Caesar Cipher")
    
    opt = input("Alege optiunea (1 sau 2): ").strip()
    op = input("Alege operatia ('e' pt criptare, 'd' pt decriptare): ").strip().lower()
    
    k1 = int(input(f"Introdu cheia k1 (1-{N-1}): "))
    
    alfabet_lucru = ALFABET
    if opt == '2':
        k2 = input("Introdu cheia k2 (minim 7 litere): ").strip()
        alfabet_lucru = genereaza_alfabet_permutat(k2)
        print("Alfabet permutat:", alfabet_lucru)
        
    msg = input("Introdu mesajul: ").strip()
    msg_curat = curata_text(msg)
    
    if op.startswith('e'):
        rez = criptare(msg_curat, k1, alfabet_lucru)
        print("\n[+] Text procesat:", msg_curat)
        print("[+] Mesaj Criptat:", rez)
    else:
        rez = decriptare(msg_curat, k1, alfabet_lucru)
        print("\n[+] Criptograma procesata:", msg_curat)
        print("[+] Mesaj Decriptat:", rez)

if __name__ == "__main__":
    main()