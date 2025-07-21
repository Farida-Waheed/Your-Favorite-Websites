This is a beginner-friendly Python project that lets you open your favorite websites using a simple text-based menu. It's a great way to learn about:

- Python modules
- Functions and dictionaries
- User input
- The `webbrowser` module

## 📁 Project Structure

```

favorite-websites/
├── main.py         # Main script with the website menu
└── my\_sites.py     # Custom module with website data and open function

````

## 🧠 How It Works

- `my_sites.py` contains:
  - A dictionary mapping numbers to website names and URLs.
  - A function `open_site(url)` that opens a URL in your default browser using `webbrowser.open()`.

- `main.py`:
  - Imports the dictionary and function from `my_sites.py`.
  - Displays a menu of websites.
  - Asks the user to pick one.
  - Opens the selected site.

## ▶️ How to Run

1. Make sure both `main.py` and `my_sites.py` are in the same folder.
2. Run the `main.py` script using Python:

```bash
python main.py
````

3. Enter the number of the website you want to open.

## 🧪 Example Output

```
Favorite Websites Menu:
1 - Google
2 - YouTube
3 - Wikipedia
4 - GitHub
Enter a number: 2
```

✅ **YouTube** will open in your default browser!

## ✅ Requirements

* Python 3.x
* No external libraries needed (uses the built-in `webbrowser` module)

🧑‍💻 Author
Made with ❤️ as part of the NTI x ITIDA Summer Internship 2025
by Farida Waheed
