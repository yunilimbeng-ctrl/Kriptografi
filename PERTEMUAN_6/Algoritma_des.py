from typing import List

# ---------- TABEL STANDAR DES ----------
IP = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,
      57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]

IP_INV = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,
          36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]

E = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,
     20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

P = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

PC_1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,
        63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]

PC_2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,
        41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]

S_BOXES = [
# S1
[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
 [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
 [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
 [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],
# S2
[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
 [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
 [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
 [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],
# S3
[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
 [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
 [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
 [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],
# S4
[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
 [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
 [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
 [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],
# S5
[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
 [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
 [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
 [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],
# S6
[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
 [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
 [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
 [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],
# S7
[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
 [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
 [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
 [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],
# S8
[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
 [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
 [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
 [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
]

SHIFTS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

# ---------- UTILITY ----------
def str_to_bits(s: str) -> List[int]:
    bits=[]
    for ch in s:
        val = ord(ch)
        bits.extend([(val >> (7-i)) & 1 for i in range(8)])
    return bits

def bytes_to_bits(bs: bytes) -> List[int]:
    bits=[]
    for b in bs:
        bits.extend([(b >> (7-i)) & 1 for i in range(8)])
    return bits

def bits_to_hex(bits: List[int]) -> str:
    b = bits[:]
    while len(b) % 4 != 0:
        b.append(0)
    hexs=''
    for i in range(0,len(b),4):
        val = b[i]*8 + b[i+1]*4 + b[i+2]*2 + b[i+3]
        hexs += '{:X}'.format(val)
    if len(hexs)%2 != 0:
        hexs = '0' + hexs
    return hexs

def permute(bits: List[int], table: List[int]) -> List[int]:
    return [bits[i-1] for i in table]

def left_shift(bits: List[int], n:int) -> List[int]:
    return bits[n:] + bits[:n]

def xor_bits(a: List[int], b: List[int]) -> List[int]:
    return [x ^ y for x,y in zip(a,b)]

def split_chunks(bits: List[int], size:int) -> List[List[int]]:
    return [bits[i:i+size] for i in range(0,len(bits),size)]

def sbox_sub(bits48: List[int]) -> List[int]:
    out=[]
    blocks = split_chunks(bits48,6)
    for i,blk in enumerate(blocks):
        row = (blk[0] << 1) | blk[5]
        col = (blk[1] << 3) | (blk[2] << 2) | (blk[3] << 1) | blk[4]
        val = S_BOXES[i][row][col]
        out.extend([(val >> (3-j)) & 1 for j in range(4)])
    return out

# ---------- KEY SCHEDULE ----------
def generate_C_D_and_subkeys(key_bits_64: List[int]):
    key56 = permute(key_bits_64, PC_1)
    C = key56[:28]
    D = key56[28:]
    Cs=[C.copy()]
    Ds=[D.copy()]
    subkeys=[]
    for shift in SHIFTS:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        Cs.append(C.copy())
        Ds.append(D.copy())
        combined = C + D
        K = permute(combined, PC_2)  # 48-bit
        subkeys.append(K)
    return Cs, Ds, subkeys

# ---------- FEISTEL ----------
def feistel(R: List[int], subkey48: List[int]):
    expanded = permute(R, E)            # 48
    x = xor_bits(expanded, subkey48)    # 48
    s_out = sbox_sub(x)                 # 32
    p_out = permute(s_out, P)           # 32
    return p_out, expanded, x, s_out

# ---------- BLOCK ENCRYPT ----------
def encrypt_block(block64_bits: List[int], subkeys: List[List[int]]):
    ip = permute(block64_bits, IP)
    L = ip[:32]
    R = ip[32:]
    rounds=[]
    for i in range(16):
        f_out, expanded, xored, sbox_out = feistel(R, subkeys[i])
        newR = xor_bits(L, f_out)
        rounds.append({
            'round': i+1,
            'L_before': L.copy(),
            'R_before': R.copy(),
            'E_R': expanded,
            'XOR': xored,
            'S_out': sbox_out,
            'P_out': f_out,
            'L_after': R.copy(),
            'R_after': newR.copy()
        })
        L, R = R, newR
    preout = R + L
    cipher = permute(preout, IP_INV)
    return cipher, ip, rounds

# ---------- PADDING PKCS#5 ----------
def pkcs5_pad(b: bytes) -> bytes:
    pad_len = 8 - (len(b) % 8)
    if pad_len == 0:
        pad_len = 8
    return b + bytes([pad_len])*pad_len

# ---------- PRINT HELPERS ----------
def print_binary_table_for_text(text: str, label="Text"):
    print(f"\n{label} -> binary (per char, 8-bit):")
    for ch in text:
        print(f" '{ch}' -> {format(ord(ch),'08b')} (0x{format(ord(ch),'02X')})")
    print()

def group_bits_str(bits: List[int], group=8):
    s=''.join(str(b) for b in bits)
    return ' '.join(s[i:i+group] for i in range(0,len(s),group))

# ---------- MAIN ----------
def main():
    print("=== DES Praktikum Lengkap ===")
    plaintext = input("Masukkan plaintext (teks bebas):\n> ")
    key_in = input("Masukkan kunci (maks 8 karakter):\n> ")
    if key_in.strip()=="":
        print("Kunci tidak boleh kosong.")
        return
    # pad/truncate key ke 8 chars
    if len(key_in) > 8:
        key_in = key_in[:8]
    elif len(key_in) < 8:
        key_in = key_in + ' '*(8-len(key_in))

    # tampilkan biner key & plaintext (sebelum padding)
    print_binary_table_for_text(key_in, label="Key (dipakai 8 bytes)")
    print_binary_table_for_text(plaintext, label="Plaintext (sebelum padding)")

    # key bits 64
    key_bits = str_to_bits(key_in)
    print("Kunci awal (64-bit):")
    print(group_bits_str(key_bits,8))

    # PC-1 -> C0 D0
    key56 = permute(key_bits, PC_1)
    print("\nPermutasi PC-1 (56-bit) - matriks 8x7:")
    for i in range(0,56,7):
        print(' '.join(str(b) for b in key56[i:i+7]))
    C0 = key56[:28]
    D0 = key56[28:]
    print("\nC0:")
    for i in range(0,28,7):
        print(' '.join(str(b) for b in C0[i:i+7]))
    print("\nD0:")
    for i in range(0,28,7):
        print(' '.join(str(b) for b in D0[i:i+7]))

    # generate C_i, D_i, subkeys K1..K16
    Cs, Ds, subkeys = generate_C_D_and_subkeys(key_bits)

    print("\n--- Semua C_i dan D_i (i=0..16) ---")
    for i in range(len(Cs)):
        print(f"C{i}: {''.join(str(x) for x in Cs[i])}")
        print(f"D{i}: {''.join(str(x) for x in Ds[i])}")

    print("\n--- 16 Subkeys K1..K16 (48-bit, grouped per-6) ---")
    for idx,k in enumerate(subkeys, start=1):
        s=''.join(str(b) for b in k)
        grp=' '.join(s[j:j+6] for j in range(0,48,6))
        print(f"K{idx:02d}: {grp}")

    # plaintext padding & blocks
    plain_bytes = plaintext.encode('utf-8')
    padded = pkcs5_pad(plain_bytes)
    print(f"\nPlaintext bytes (utf-8): {list(plain_bytes)}")
    print(f"Padded bytes (PKCS#5): {list(padded)} (pad len = {padded[-1]})")
    print("Padded bytes -> binary per byte:")
    print(' '.join(format(b,'08b') for b in padded))

    # encrypt per-block
    blocks = [padded[i:i+8] for i in range(0,len(padded),8)]
    all_cipher_bits=[]
    for bi,blk in enumerate(blocks, start=1):
        blk_bits = bytes_to_bits(blk)
        print(f"\n--- Blok {bi} ---")
        print("Plaintext block bits (64):")
        print(group_bits_str(blk_bits,8))
        cipher_bits, ip, rounds_info = encrypt_block(blk_bits, subkeys)
        print("\nInitial Permutation (IP):")
        print(group_bits_str(ip,8))
        # tampilkan ringkasan tiap round (bisa sangat panjang)
        for r in rounds_info:
            print(f"\n-- Round {r['round']:2d} --")
            print("L before :", ''.join(str(x) for x in r['L_before']))
            print("R before :", ''.join(str(x) for x in r['R_before']))
            print("E(R)     :", ''.join(str(x) for x in r['E_R']))
            print("XOR w/K  :", ''.join(str(x) for x in r['XOR']))
            print("S-out    :", ''.join(str(x) for x in r['S_out']))
            print("P(out)   :", ''.join(str(x) for x in r['P_out']))
            print("L after  :", ''.join(str(x) for x in r['L_after']))
            print("R after  :", ''.join(str(x) for x in r['R_after']))
        print("\nCipher block bits (64) after IP^-1:")
        print(group_bits_str(cipher_bits,8))
        all_cipher_bits.extend(cipher_bits)

    # final outputs
    print("\n=== OUTPUT AKHIR ===")
    print("Ciphertext (biner):")
    print(group_bits_str(all_cipher_bits,8))
    print("\nCiphertext (hexadesimal):")
    print(bits_to_hex(all_cipher_bits))
    print("\nSelesai.")

if __name__ == "__main__":
    main()
