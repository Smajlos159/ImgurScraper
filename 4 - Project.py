import requests, os, random, string, time

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
if not os.path.isfile("images.html"):
    html_file = open("images.html", 'a+')
    html_file.write(html_file_prefix)
    html_file.close()
html_file = open("images.html", 'a')
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
        html_file.write(f'<img src="Images\\{output_file_name}.png"></img>\n')

finish_time = time.time() # Stopping point for timer
print(f"> Done in {round(finish_time - start_time, 2)} seconds!")
time.sleep(7.5)
exit