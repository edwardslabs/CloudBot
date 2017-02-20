from cleverwrap import CleverWrap
from cloudbot import hook

@hook.on_start()
def get_key(bot):
    global api_key, cb
    api_key = bot.config.get("api_keys", {}).get("cleverbot", None)
    cb = Cleverbot(api_key)

@hook.command("ask", "gonzo", "gonzobot", "cleverbot", "cb")
def chitchat(text):
    """chat with cleverbot.com"""
    return cb.say(text)
