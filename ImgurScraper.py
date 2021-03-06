import requests, os, random, string, time, ctypes

ctypes.windll.kernel32.SetConsoleTitleW("ImgurScraper") # Console Title
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
        if character_mode == 5 or character_mode == 7:
            break
        else:
            print("> Only 5 or 7!")
    except:
        print("> Only 5 or 7!")

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
        if fails%10 == 0: #Updates hitrate every 10 fails
            current_time = time.time() # Gets current time for CPM
            ctypes.windll.kernel32.SetConsoleTitleW(f"ImgurScraper [Progress: {output_file_name}/{number_images}] [Hitrate: {round(output_file_name / fails * 100, 4)}%] [CPM: {int((output_file_name + fails) / (current_time - start_time) * 60)}]") # Updates console title
    else:
        output_file_name += 1
        print(f"> Hit! [{output_file_name}/{number_images}] [URL: i.imgur.com/{image_code}.png]")
        open(f"Images\\{output_file_name}.png", 'wb').write(r.content)
        current_time = time.time()  # Gets current time for CPM
        if fails != 0:
            ctypes.windll.kernel32.SetConsoleTitleW(f"ImgurScraper [Progress: {output_file_name}/{number_images}] [Hitrate: {round(output_file_name / fails * 100, 4)}%] [CPM: {int((output_file_name + fails) / (current_time - start_time) * 60)}]") # Updates console title
finish_time = time.time() # Stopping point for timer
print(f"> Done in {round(finish_time - start_time, 2)} seconds!")
input("> Press enter to exit\n> ")
exit