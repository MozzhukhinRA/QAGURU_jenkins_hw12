import random


class UserPage:
   @staticmethod
   def generate_data_users():
        first_name = random.choice(["Max", "Pavel", "Alex", "Skot"])
        last_name = random.choice(["Kuznetsov", "Alekin", "Stepanov", "Pierro"])
        full_name = f'{first_name} {last_name}'
        moth = random.choice(["April","February", "May", "September"])
        year = random.randint(1950, 2025)


        mail = f'{first_name.lower()}.{last_name.lower()}@gmail.com'
        return  {"first_name" : first_name,
        "last_name" : last_name,
        "full_name" : full_name,
        "moth" : moth,
        "year" : year,
        "mail" : mail,
        "gender" : random.choice(["Male", "Female", "Other"]),
        "phone" : f'9{random.randint(000000000, 999999999)}',
        "birth" : f'15 {moth} {year}',
        "sub" : f'{random.choice(["English", "Physics"])}',
        "hobbies" : f'{random.choice(["Sports", "Music"])}',
        "picture" : 'photo.jpeg',
        "address" : f'{random.choice(["Piter", "Ryazan"])}',
        "region" : 'Uttar Pradesh Merrut'
        }












