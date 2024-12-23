# Program sederhana untuk mengisi dan menampilkan elemen list
user_list = []

print("Masukkan string satu per satu. Ketik 'selesai' untuk berhenti.")

# Input string dari user
while (item := input("Masukkan string: ")) != "selesai":
    user_list.append(item)

# Tampilkan list dan pilih indeks
print("\nList Anda:", user_list)
if user_list:  # Pastikan list tidak kosong
    try:
        index = int(input("Masukkan indeks yang ingin ditampilkan: "))
        print(f"Item di indeks {index}: {user_list[index]}")
    except (ValueError, IndexError):
        print("Indeks tidak valid.")
else:
    print("List kosong, tidak ada yang bisa ditampilkan.")
