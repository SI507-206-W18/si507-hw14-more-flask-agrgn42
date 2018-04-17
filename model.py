
import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0


def init():
    global entries, next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        next_id = len(entries)
        f.close()
    except:
        entries = []
        next_id = 0

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()    # this gives you the time now
    time_string = now.strftime("%b %d, %Y %-I:%M %p")   # this is s string formatting function, -I is the time now without the starting 0
    entry = {"author": name, "text": text, "timestamp": time_string, "id": str(next_id)}
    entries.insert(0, entry) ## add to front of list
    next_id +=1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")


def delete_entry(post_id):
    global entries
    for item in entries:
        if post_id in item.values() or int(post_id) in item.values():
            entries.remove(item)
    entries_dict = json.dumps(entries)
    fwrite = open(GUESTBOOK_ENTRIES_FILE, 'w')
    fwrite.write(entries_dict)
    fwrite.close()




