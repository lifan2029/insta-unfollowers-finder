from instagrapi import Client
from flask import Flask, render_template, request, jsonify
import os
import time
from instagrapi.exceptions import (
    ClientError,
    ClientLoginRequired,
    ClientUnauthorizedError
)

app = Flask(__name__)

LOGIN = ""
PASSWORD = ""

@app.route("/")
def index():
    return render_template("index.html")

try:
    from instagrapi.exceptions import ClientThrottled, FloodWaitError
except ImportError:
    ClientThrottled = ClientError
    FloodWaitError = ClientError

def safe_action(action_func, *args, max_retries=6, base_delay=5, **kwargs):
    attempt = 0
    while True:
        try:
            return action_func(*args, **kwargs)
        except (ClientThrottled, FloodWaitError) as e:
            attempt += 1
            if attempt > max_retries:
                return {}  # TODO: New add handler
            delay = base_delay * (2 ** (attempt - 1))
            print(f"⚠️ Rate limit / Flood detected. Жду {delay} сек. (попытка {attempt}/{max_retries})")
            time.sleep(delay)
        except ClientUnauthorizedError as e:
            print(f"⚠️ Игнорируем ClientUnauthorizedError: {e}")
            return {} # TODO: New add handler
        except ClientLoginRequired:
            raise
        except ClientError as e:
            attempt += 1
            if attempt > max_retries:
                return {}
            delay = base_delay * (2 ** (attempt - 1))
            print(f"⚠️ ClientError: {e}. Жду {delay} сек. и пробую снова")
            time.sleep(delay)
        except Exception as e:
            attempt += 1
            if attempt > max_retries:
                return {}
            delay = base_delay * (2 ** (attempt - 1))
            print(f"⚠️ Неожиданная ошибка: {e}. Жду {delay} сек.")
            time.sleep(delay)

@app.route("/check", methods=["POST"])
def check():
    username = request.json.get("username")
    try:
        cl = Client()

        if (os.path.exists("session.json")):
            cl.load_settings("session.json")
        else:
            cl.login(LOGIN, PASSWORD)

        cl.dump_settings("session.json")

        target_user_id = safe_action(cl.user_id_from_username, username)
        followers_dict = safe_action(cl.user_followers, target_user_id)
        following_dict = safe_action(cl.user_following, target_user_id)
        followers = [u.username for u in followers_dict.values()]
        following = [u.username for u in following_dict.values()]
        not_following_back = sorted(set(following) - set(followers))
        return jsonify({"status": "ok", "users": not_following_back})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)