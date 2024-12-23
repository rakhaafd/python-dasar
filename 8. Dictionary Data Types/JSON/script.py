import json

# data = '''
# {
#     "name": "Rakha",
#     "age": 17,
#     "hobby": ["exploring technology", "designing UI/UX", "coding"],
#     "education": {
#         "school": "SMKN7 Semarang",
#         "major": "SIJA",
#         "grade": "XI SIJA 1"
#     },
#     "skills": {
#         "programming": ["Python", "JavaScript", "HTML", "CSS"],
#         "tools": ["Docker", "Linux CLI", "Figma"]
#     },
#     "dream": "Full-stack developer"
# }
# '''

# data_json = json.loads(data) # gunakan json.loads untuk conversi json ke dict
# print(type(data)) # masih str (atau json mentah)
# print(type(data_json)) # dict


dicti = {
    "name": "Rakha",
    "age": 17,
    "is_student": True,  # Boolean True
    "is_employed": False,  # Boolean False
    "address": None,  # None (akan menjadi null di JSON)
    "hobbies": ["coding", "designing", "traveling"],
    "grades": {
        "math": 95,
        "english": 88
    }
}

# Menulis dictionary ke file JSON
with open("data.json", "w") as json_file:
    json.dump(dicti, json_file, indent=4)  # indent=4 untuk format yang lebih rapi

print("Data telah diekspor ke file 'data.json'")

# json_dicti = json.dumps(dicti) # gunakan json.dumps untuk conversi dict ke json
# print(json_dicti)
# print(type(json_dicti)) # berubah jadi str yg menandakan sudah jadi json
# print(type(dicti))

# convert file JSON menjadi dict
import json

# Membuka dan memuat file JSON
with open("data.json", "r") as json_file:
    data = json.load(json_file)  # Memuat data JSON ke dalam dictionary

# Menampilkan data yang dimuat
print(data)