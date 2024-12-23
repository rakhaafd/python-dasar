def process_string(input_string):
    result = ''
    for char in input_string:
        if char.isalpha():  # Memeriksa apakah karakter adalah huruf
            if char.lower() in ['a', 'i', 'u', 'e', 'o']:  # Huruf vokal
                
                result += '*'
            else:  # Huruf konsonan
                order = ord(char.lower()) - 96
                result += str(order)
        else:  # Karakter bukan huruf
            result += char
    return result

# Meminta input dari pengguna
userInput = input('Masukkan kalimat: ')
# Memproses string
output = process_string(userInput)
# Menampilkan hasil
print('Output:', output)
