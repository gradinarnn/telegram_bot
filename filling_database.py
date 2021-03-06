from array import array

from loader import skills_categories_db

category = (
    "๐ Tech", "โ๏ธ Wellness", "๐ฅ Trends", "๐ฆ Knowledge", "๐ฌ Languages", "๐ญ Art", "๐ Sports",
    "๐คน๐ผโโ๏ธ Entertaiment")

category_tech = (
    "๐งญ Marketing", "โ๏ธ SaaS", "๐ค Engineering", "๐ธ Investing", "๐ Crypto", "๐ฆ Startups", "๐ง  AI", "๐ Product",
    "๐ AR/VR", "๐ DTC")
category_wellness = (
    "๐ง๐ปโโ๏ธ Meditation", "๐ Outdoors", "๐ Health", "๐ฅ Veganism", "๐ฝ Nutrition", "๐ Medicine", "๐๐ปโโ๏ธ Fitness",
    "๐๐ปโโ๏ธ Weights", "๐ฑ Mindfulness")

category_trends = ("๐ฆ Stocks", "๐ฆ Entrepreneurship", "๐  Real Estate", "๐ฏ Pitch Practice", "โก๏ธ Small Business")

category_knowlenge = (
    "๐ชด Education", "๐งฌ Biology", "๐ณ Philosophy", "๐ช Psychology", "๐ฎ The Future", "๐ช History", "โ๏ธ Science",
    "๐งฎ Math", "๐งฒ Physics", "๐ธ Space")

category_languages = (
    "๐ฌ๐ง British English", "๐บ๐ธ American English", "๐ท๐บ Russian", "๐ซ๐ท French", "๐ฉ๐ช German", "๐บ๐ฆ Ukranian",
    "๐จ๐ณ Mandarin", "๐ฎ๐ฉ Indonesian", "๐ช๐ฌ Arabic", "๐ง๐ท Portuguese", "๐ช๐ธ Spanish", "๐ฏ๐ต Japanese")

category_art = (
    "๐ผ Design", "๐  Writing", "๐ Architecture", "๐ Books", "๐ง Food&Drink", "๐ธ Photography", "๐ Beauty",
    "๐ Fashion", "๐ฝ Sci-Fi", "๐ญ Theater", "๐๐ฝ Dance", "๐ Art")

category_sports = (
    "๐ด๐ผโโ๏ธ Cycling", "๐ Cricket", "๐๐ฝโโ๏ธ Golf", "โฝ๏ธ Soccer", "๐คผ MMA", "โพ๏ธ Baseball", "๐ Formula 1",
    "โน๐ฝโโ๏ธ Basketball", "๐ Football", "๐พ Tennis", "โธ Ice skating", "๐น Skateboard", "๐ฃ๐พโโ๏ธ Rowing",
    "๐๐ปโโ๏ธ Swimming",
    "๐ Hockey")

category_intertaiment = (
    "๐ฎ Gaming", "๐ Performances", "๐ Storytelling", "๐ Comedy", "๐ง Music", "๐ฆธ๐ปโโ๏ธ Celebrities",
    "๐ป Anime & Manga",
    "๐ Variety", "๐น Movies", "๐คฉ Fun", "๐ฉ๐ฝโ๐ Trivia", "๐ป Podcasts", "๐ค Karaoke", "โ๏ธ Advice", "๐บ Television")

all = (category_tech, category_wellness, category_trends, category_knowlenge, category_languages, category_art,
       category_sports, category_intertaiment)


def filling_db():
    a = 0
    for i in category:
        skills_categories_db.add_categories(a+1, i)
        b=0
        for j in all[a]:
            b+=1
            skills_categories_db.add_skills(a+1,b,j)

        a+=1



skills_categories_db.create_table_categories()
skills_categories_db.create_table_skills()
filling_db()
