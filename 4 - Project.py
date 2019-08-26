import requests, os, random, string, time
if not os.path.isdir("Images"):
        os.mkdir("Images")
output_file_name = 0
while True:
        try:
                number_images = int(input("> How many images do you want to scrape?\n> "))
                break
        except ValueError:
                print("> Only numbers!")
start_time = time.time() # Starting point for timer
while output_file_name != number_images:
    image_code = ""
    for char in range(7):
        char = random.choice(string.ascii_letters + string.digits)
        image_code += char
    r = requests.get(f"https://i.imgur.com/{image_code}.png", stream=True)
    if r.url == "https://i.imgur.com/removed.png":
        print(f"> Fail! [URL: i.imgur.com/{image_code}.png]")
    else:
        output_file_name += 1
        print(f"> Hit! [{output_file_name}/{number_images}] [URL: i.imgur.com/{image_code}.png]")
        open(f"Images\\{output_file_name}.png", 'wb').write(r.content)
finish_time = time.time() # Stopping point for timer
print(f"> Done in {round(finish_time - start_time, 2)} seconds!")
time.sleep(7.5)
exit