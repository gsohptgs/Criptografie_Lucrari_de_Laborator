import random

# Tabelul de permutare P conform standardului DES
P_TABLE = [
    16,  7, 20, 21,
    29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11,  4, 25
]

def format_biti(sir):
    """Grupează biții câte 4 pentru o afișare clară la ecran."""
    return ' '.join(sir[i:i+4] for i in range(0, len(sir), 4))

def permutare_p(bloc_32):
    """Aplică tabelul de permutare P asupra blocului de 32 de biți."""
    return ''.join(bloc_32[pozitie - 1] for pozitie in P_TABLE)

def xor_biti(sir1, sir2):
    """Aplică operația XOR bit cu bit (adunare modulo 2)."""
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(sir1, sir2))

def des_sarcina_2_10():
    print("=== LUCRARE DE LABORATOR NR. 4: ALGORITMUL DES (Sarcina 2.10) ===")
    print("1 - Generare aleatorie a datelor (Recomandat - rapid)")
    print("2 - Introducere manuala de la tastatura")
    
    optiune = input("Alege modul de introducere a datelor (1 sau 2): ").strip()

    if optiune == "1":
        s_output = ''.join(random.choice('01') for _ in range(32))
        l_anterior = ''.join(random.choice('01') for _ in range(32))
    elif optiune == "2":
        s_output = input("Introdu S1(B1)...S8(B8) (exact 32 de biti de 0 si 1): ").replace(" ", "")
        l_anterior = input("Introdu L_(i-1) (exact 32 de biti de 0 si 1): ").replace(" ", "")
        if len(s_output) != 32 or len(l_anterior) != 32 or not set(s_output + l_anterior).issubset({'0', '1'}):
            print("Eroare: Datele trebuie sa contina exact 32 de caractere binare (0 sau 1)!")
            return
    else:
        print("Optiune invalida!")
        return

    print("\n--- 1. DATE DE INTRARE ---")
    print(f"S1(B1)...S8(B8) : {format_biti(s_output)}")
    print(f"L_(i-1)         : {format_biti(l_anterior)}")

    print("\n--- 2. TABELUL DE PERMUTARE P UTILIZAT ---")
    for i in range(0, 32, 4):
        print(f"  {P_TABLE[i]:2d}  {P_TABLE[i+1]:2d}  {P_TABLE[i+2]:2d}  {P_TABLE[i+3]:2d}")

    f_rezultat = permutare_p(s_output)
    print("\n--- 3. PAS INTERMEDIAR: APLICAREA PERMUTARII P ---")
    print("Formula: f = P(S1(B1)...S8(B8))")
    print(f"Rezultat f      : {format_biti(f_rezultat)}")

    r_curent = xor_biti(l_anterior, f_rezultat)
    print("\n--- 4. PAS FINAL: CALCULUL LUI R_i (OPERATIA XOR) ---")
    print("Formula: R_i = L_(i-1) XOR f")
    print(f"  {format_biti(l_anterior)}  (L_(i-1))")
    print(f"⊕ {format_biti(f_rezultat)}  (f)")
    print("  " + "-" * 39)
    print(f"  {format_biti(r_curent)}  (R_i)")

    print(f"\nREZULTAT FINAL R_i (32 biti): {r_curent}")

des_sarcina_2_10()