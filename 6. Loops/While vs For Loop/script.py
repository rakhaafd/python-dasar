# count = 0
# while count < 5:
#     print("Ini adalah pengulangan ke-", count + 1)
#     count += 1
#     # Ini adalah pengulangan ke-1
#     # Ini adalah pengulangan ke-2
#     # Ini adalah pengulangan ke-3
#     # Ini adalah pengulangan ke-4
#     # Ini adalah pengulangan ke-5


number = 0
while number != 10:
    number = int(input("Masukkan angka (masukkan 10 untuk berhenti): "))
    if number != 10:
        print("Kamu memasukkan", number)
print("Program selesai.")