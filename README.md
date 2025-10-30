# 🔎 Instagram unfollowers finder

A simple web app that compares **Instagram followers** and **followings** to show who doesn't follow you back.

This tool analyzes your Instagram profile (followers and following lists) and finds **non-mutual connections** — users you follow who don’t follow you in return.


## 🛠️ Tech Stack

- **Language:** Python
- **Packages:** instagrapi, flask

## ⚙️ Installation

### 1. Clone repository

```
git clone https://github.com/lifan2029/insta-unfollowers-finder.git
```

### 2. Go to project folder

```
cd insta-unfollowers-finder
```

### 3. Install packages

```
pip install -r requirements.txt
```

### 4. Set your config data
This account will be used to obtain user data.  
Instagram has been hiding public data since 2022. 

```python
LOGIN = "" # instagram login (13 line in app.py)
PASSWORD = "" # instagram password (14 line in app.py)
```

### 5. Open in browser
```
http://127.0.0.1:5000
```

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

## ⚠️ Disclaimer

This is a **test/demo project** created for learning and educational purposes only.  
It is **not intended for production use** and should **not be used to interact with Instagram directly**.

Instagram does **not support or allow** the use of unofficial automation or scraping tools.  
For any real-world integration, please use the **official [Instagram Graph API](https://developers.facebook.com/docs/instagram-api/)** in accordance with Instagram’s [Platform Policy](https://developers.facebook.com/terms).

By using this project, you acknowledge that it is for **testing, local use, and personal experimentation only**.

## ✨ Author

Developed by [lifan2029](https://github.com/your-username) — Fullstack developer.  
If you like this project, feel free to ⭐ star it on GitHub!

📧 lifan2029@gmail.com  
