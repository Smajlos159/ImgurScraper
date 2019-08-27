import requests, os, random, string, time, ctypes

ctypes.windll.kernel32.SetConsoleTitleW("ImgurScraper") # Console Title
html_file_prefix = """<!DOCTYPE html> 
<head>
    <meta charset="UTF-8">
    <title>Scraped Images</title>
</head>
<style>
img {
    margin-top: 50px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    border: 3px solid black;
    width:700px
}
h1 {
    background-color: cyan;
    border: 3px solid black;
    font-family: Impact;
    font-weight: bold
}
</style>
<body bgcolor="lightblue">
<h1 align="center">Scrapped Images</h1>
"""
if not os.path.isfile("images.html"):           # Creates HTML file if not already created
    with open("images.html", 'a+') as html_file:
        html_file.write(html_file_prefix)
html_file = open("images.html", 'a')
if not os.path.isdir("Images"):                 # Creates Images dir if not already created
    os.mkdir("Images")
output_file_name = 0
fails = 0  # Used for the calculation of hitrate
while True:
        try:
                number_images = int(input("> How many images do you want to scrape?\n> "))
                break
        except ValueError:
                print("> Only numbers!")
while True:
        try:
                character_mode = int(input("> Do you want to use 5-character or 7-character scraping mode [5=HIGH HITRATE|7=NEWER IMAGES] ?  (5/7)\n> "))
                break
        except ValueError:
                print("> Answer only 5 or 7!")
start_time = time.time() # Starting point for timer
while output_file_name != number_images:
    image_code = ""
    for char in range(character_mode):                        # Generates image characters
        char = random.choice(string.ascii_letters + string.digits)
        image_code += char
    r = requests.get(f"https://i.imgur.com/{image_code}.png", stream=True)
    if r.url == "https://i.imgur.com/removed.png":
        print(f"> Fail! [URL: i.imgur.com/{image_code}.png]")
        fails += 1
        if fails%25 == 0: #Updates hitrate every 10 fails
            current_time = time.time() # Gets current time for CPM
            ctypes.windll.kernel32.SetConsoleTitleW(f"ImgurScraper [Progress: {output_file_name}/{number_images}] [Hitrate: {round(output_file_name / fails * 100, 4)}%] [CPM: {int((output_file_name + fails) / (current_time - start_time) * 60)}]") # Updates console title
    else:
        output_file_name += 1
        print(f"> Hit! [{output_file_name}/{number_images}] [URL: i.imgur.com/{image_code}.png]")
        open(f"Images\\{output_file_name}.png", 'wb').write(r.content)
        with open("images.html", 'a+') as html_file: # Writes image into the HTML file
            html_file.write(f'<img src="Images\\{output_file_name}.png"></img>\n')
        current_time = time.time()  # Gets current time for CPM
        if fails != 0:
            ctypes.windll.kernel32.SetConsoleTitleW(f"ImgurScraper [Progress: {output_file_name}/{number_images}] [Hitrate: {round(output_file_name / fails * 100, 4)}%] [CPM: {int((output_file_name + fails) / (current_time - start_time) * 60)}]") # Updates console title
finish_time = time.time() # Stopping point for timer
print(f"> Done in {round(finish_time - start_time, 2)} seconds!")
input("> Press enter to exit\n> ")
exit