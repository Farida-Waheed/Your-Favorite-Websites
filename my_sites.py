import webbrowser

sites = {
    1: ("Google", "https://www.google.com"),
    2: ("YouTube", "https://www.youtube.com"),
    3: ("Wikipedia", "https://www.wikipedia.org"),
    4: ("GitHub", "https://www.github.com")
}

def open_site(url):
    webbrowser.open(url)
