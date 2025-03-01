import csv
import random

# Shona names
shona_names = ["Tatenda", "Rumbidzai", "Tendai", "Tariro", "Farai", "Nyasha", "Tinashe", "Tapiwa", "Kudakwashe", "Chipo", "Simba", "Tafadzwa",
               "Tawanda", "Tafara", "Tadiwa", "Kundai", "Tendekai", "Munashe", "Tariro", "Tanaka", "Rudo", "Shamiso", "Tawananyasha", "Tariro"]

# English names
english_names = ["John", "Emma", "Michael", "Sophia", "William", "Olivia", "James", "Ava", "Benjamin", "Isabella", "Daniel", "Mia",
                 "Alexander", "Emily", "Jacob", "Charlotte", "Matthew", "Amelia", "Ethan", "Harper", "Samuel", "Ella", "Grace", "Noah"]

# Surnames
surnames = ["Mazvita", "Mukanya", "Mukuru", "Mupedzapasi", "Nyamande", "Nyandoro", "Chitando", "Chingwende", "Chinotimba", "Chinamasa",
            "Chigumba", "Gumbo", "Mukono", "Mupita", "Nyamayaro", "Nyamhondoro", "Chirinda", "Chivende", "Chiremba", "Chinoda"]

# Generate the dataset
dataset = []
for _ in range(10000):
    if random.random() < 0.5:
        name = random.choice(english_names)
    else:
        name = random.choice(shona_names)
    surname = random.choice(surnames)
    age = random.randint(18, 60)
    gender = random.choice(["Male", "Female"])
    marital_status = random.choice(["Single", "Married", "Divorced", "Widowed"])
    has_children = random.choice(["Yes", "No"])
    work = random.choice(["Employed", "Unemployed"])
    talent = random.choice(["Singing", "Dancing", "Drawing", "Writing"])
    school = random.choice(["Primary School", "Secondary School", "College", "University"])
    disability_type = random.choice(["Physical Disability", "Hearing Impairment", "Visual Impairment", "Intellectual Disability"])
    specific_needs = random.choice(["Mobility Aid", "Hearing Aid", "Braille Material", "Assistive Technology"])
    distribute = random.choice(['Yes'])
    entry = {
        "name": name,
        "surname": surname,
        "age": age,
        "gender": gender,
        "marital_status": marital_status,
        "has_children": has_children,
        "work": work,
        "talent": talent,
        "school": school,
        "disability_type": disability_type,
        "specific_needs": specific_needs,
        'distribute': distribute
    }

    dataset.append(entry)

# Save the dataset to a CSV file
filename = "mixed_names_dataset.csv"
with open(filename, mode="w", newline="") as file:
    fieldnames = dataset[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(dataset)

print(f"The dataset has been saved to {filename} as a CSV file.")