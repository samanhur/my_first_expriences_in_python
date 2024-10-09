python_url='https://www.python.org'
youtube_url='https://www.youtube.com'
print(python_url)
print(youtube_url)
print(python_url.removeprefix('https://'))
print(youtube_url.removeprefix('https://www.'))
simlple_youtube_url=youtube_url.removeprefix("https://")
print(simlple_youtube_url)

filename = "python_notes.txt"
simple_filename = filename.removesuffix(".txt")
print(filename.removesuffix('.txt'))
print(simple_filename)
