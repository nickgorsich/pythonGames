
''' BRAWL STARS INFORMATION DISPLAY '''

import json
import http
import requests


#iowa city
API_KEY = ("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImIxZDZlMGQ4LTk3NmItNGMzOC1hNjJlLTc5YTQ4ZGU3OTYxNiIsImlhdCI6MTc2NTQ3NzI0Miwic3ViIjoiZGV2ZWxvcGVyLzI4OTIyYWQyLWYzMjItMzM2MS1lYzY4LTU0NWU0OGQwZGQ2OCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiNjMuMTUyLjE1LjIxMCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.bK8DJ9Usy7GsqTudf40K11m4fRcCgBtFp8xmDirDeJR3MlaCWSDC3D6dknv5_O_HD5mwqdhgfOjzbS0LbrilGQ")


# Base URL for API
BASE_URL = "https://api.brawlstars.com/v1"

# Define headers with the API key
HEADERS = {"Authorization": f"Bearer {API_KEY}"}  # The API requires the key in the Authorization header

BRAWLER_ID =  "https://api.brawlstars.com/v1/brawlers/{BRAWLER_ID}"
BRAWLER_STATS = "https://api.brawlstars.com/v1/brawlers/16000000"


# Retrieves player leaderboards
def get_player_leaderboard(country_code="global"):
    url = f"{BASE_URL}/rankings/{country_code}/players"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()  # Return JSON data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


# formatter for raw player data
def format_player_data(player_data):
    formatted_data = []

    # List of emojis to cycle through
    emojis = ["🏷️ ", "👤", "🎨", "🖼️ ", "🏆", "🚀", "🎖️ ", "📈", "🏅", "👥", "🥇", "🤝", "🤖", "🎭", "🏠"]
    
    # 🎮 Player Profile
    formatted_data.append("  🎮 Player Profile")
    formatted_data.append("━━━━━━━━━━━━━━━━━━━━━━")
    
    for index, (key, value) in enumerate(player_data.items()):
        emoji = emojis[index % len(emojis)]  # Cycle through emojis if more keys than emojis

        if isinstance(value, dict):
            formatted_data.append(f"{emoji} {key.capitalize()}:")
            for sub_key, sub_value in value.items():
                formatted_data.append(f"   🔸 {sub_key.capitalize()}: {sub_value}")
        else:
            formatted_data.append(f"{emoji} {key.capitalize()}: {value}")

        # Stops after 'club' (optional)
        if key == "club":
            break

    return "\n".join(formatted_data)


# function to return brawler data, calls formatter
def initialize_brawlers_data(player_data):

    formatted_data = []

        # 🔥 Brawler Section (Always Included)
    formatted_data.append("\n🔥 Brawlers")
    formatted_data.append("━━━━━━━━━━━━━━━━━━━━━━")

    # total_brawlers = 0
    # for brawler in player_data["brawlers"]:
    #     total_brawlers += 1

    brawler_count = 0
    if "brawlers" in player_data and player_data["brawlers"]:
        for brawler in player_data["brawlers"]:
            brawler_count += 1
        formatted_data.append(f"\n{brawler_count}/88 Brawlers\n") # {total brawlers} instead of 88

    if "brawlers" in player_data and player_data["brawlers"]:
        for brawler in player_data["brawlers"]:
            #print(brawler)
            formatted_data.append(format_brawler_data(brawler))  # Calls helper function
    else:
        formatted_data.append("❌ No Brawlers Found")

    
    return "\n".join(formatted_data)


# retrieves players raw brawler data 
def get_brawlers_data(player_tag):
    """ Replace "#" in player tag with "%23" for URL encoding """
    encoded_tag = player_tag.replace("#", "%23")
    url = f"{BASE_URL}/players/{encoded_tag}"


    # Make a GET request to the API
    response = requests.get(url, headers=HEADERS)


    if response.status_code == 200:
        try:
            return initialize_brawlers_data(response.json())  # ✅ Ensure it's parsed as JSON
        except ValueError:
            print("❌ Error: Response is not valid JSON.")
            return None
    else:
        return None  # Return None if request fails


# for formatter that initialize_brawlers_data calls
def format_brawler_data(brawler):
    """Formats an individual brawler's information."""
    
    formatted_brawler = []

    if brawler not in player_data.get("brawlers", []):
        return f"\nINVALID OR UNOWNED BRAWLER: '{brawler_name}'"

    formatted_brawler.append(f"🏆 {brawler['name']} (ID: {brawler['id']})")
    formatted_brawler.append(f"   🔹 Power: {brawler['power']}")
    formatted_brawler.append(f"   🔹 Rank: {brawler['rank']}")
    formatted_brawler.append(f"   🔹 Trophies: {brawler['trophies']} (Highest: {brawler['highestTrophies']})")

    # Hypercharge
    # hypercharge = brawler.get("hypercharge", [])
    # formatted_brawler.append("   ⚡🟣  Hypercharge: " + (", ".join(hc["name"] for hc in hypercharge) if hypercharge else "-"))

    # Star Powers
    star_powers = brawler.get("starPowers", [])
    formatted_brawler.append("   ⭐  Star Powers: " + (", ".join(sp["name"] for sp in star_powers) if star_powers else "-"))

    # Gadgets
    gadgets = brawler.get("gadgets", [])
    formatted_brawler.append("   🟢  Gadgets: " + (", ".join(g["name"] for g in gadgets) if gadgets else "-"))

    # Gears
    gears = brawler.get("gears", [])
    formatted_brawler.append("   ⚙️   Gears: " + (", ".join(f"{gear['name']}" for gear in gears) if gears else "-"))


    return "\n".join(formatted_brawler)


# retrieves raw player data
def get_player_data(player_tag):

    """ Replace "#" in player tag with "%23" for URL encoding """
    encoded_tag = player_tag.replace("#", "%23")
    url = f"{BASE_URL}/players/{encoded_tag}"


    # Make a GET request to the API
    response = requests.get(url, headers=HEADERS)


    if response.status_code == 200:
        try:
            return response.json()  # ✅ Ensure it's parsed as JSON
        except ValueError:
            print("❌ Error: Response is not valid JSON.")
            return None
    else:
        return None  # Return None if request fails


# formatter for battle data
def format_battle(battle):
    formatted_battle = []

    # 📅 Battle Time
    battle_time = battle.get("battleTime", "Unknown Time")
    battle_yr = battle_time[0:4]
    battle_mo = battle_time[4:6]
    battle_day = battle_time[6:8]
    formatted_date = (f"{battle_mo}/{battle_day}/{battle_yr}")
    formatted_time = (f"{battle_time[9:11]}:{battle_time[11:13]}")
    final_time = military_to_standard(formatted_time)

    formatted_battle.append(f"📅 Battle Date: {formatted_date}")
    formatted_battle.append(f"🕒 Battle Time: {final_time}")


    # 🎮 Event Info
    event = battle.get("event", {})
    event_mode = event.get("mode", "Unknown Mode").capitalize()
    event_map = event.get("map", "Unknown Map")

    # 🏆 Battle Details
    battle_info = battle.get("battle", {})
    battle_result = battle_info.get("result", "Unknown").capitalize() # unknown?
    battle_type = battle_info.get("type", "Unknown").capitalize()
    duration = battle_info.get("duration", "Unknown") # unknown?
    trophy_change = battle_info.get("trophyChange", 0)

    trophy_display = f"{'+ ' if int(trophy_change) >= 0 else '- '}{trophy_change}🏆"

    # Adding to Output
    formatted_battle.append(f"⚔️  Mode: {event_mode} - {battle_type}")
    formatted_battle.append(f"🗺️  Map: {event_map}")
    formatted_battle.append(f"Result: {battle_result.upper()} | {trophy_display}")
    formatted_battle.append(f"⏳ Duration: {duration} sec")
    #formatted_battle.append(f"⏳ Duration: {duration//60}m {duration%60} sec")

    # 🌟 Star Player 
    star_player = battle_info.get("starPlayer", {})
    if star_player:
        sp_name = star_player.get("name", "Unknown Player")
        sp_brawler = star_player.get("brawler", {}).get("name", "Unknown Brawler")
        formatted_battle.append(f"🌟 Star Player: {sp_name} ({sp_brawler})")

    # 🏅 Teams
    teams = battle_info.get("teams", [])
    formatted_battle.append("\n🏅 Teams")
    formatted_battle.append("━━━━━━━━━━━━━━━━━━━━━━")

    for i, team in enumerate(teams, start=1):
        formatted_battle.append(f"  🔹 Team {i}")
        for player in team:
            player_name = player.get("name", "Unknown")
            brawler = player.get("brawler", {})
            brawler_name = brawler.get("name", "Unknown Brawler")
            brawler_power = brawler.get("power", "?")
            brawler_trophies = brawler.get("trophies", "?")
            formatted_battle.append(f"    👤 {player_name} - {brawler_name} (Power {brawler_power}, {brawler_trophies}🏆)")

    return "\n".join(formatted_battle)


# time function to change bogus time data to readable time, and for cleaner code
def military_to_standard(time_str):
    # Split hours and minutes
    hours, minutes = map(int, time_str.split(":"))

    # Determine AM or PM
    period = "AM" if hours < 12 else "PM"

    # Convert hours to 12-hour format
    standard_hours = hours % 12
    standard_hours = 12 if standard_hours == 0 else standard_hours  # Convert 0 to 12 for AM/PM

    return f"{standard_hours}:{minutes:02d} {period}"


# retrieves raw club data
def get_club_info(club_tag):
    """Fetches club stats and member information from the Brawl Stars API."""
    """ Replace "#" in player tag with "%23" for URL encoding """
    encoded_tag = club_tag.replace("#", "%23")
    url = f"{BASE_URL}/clubs/{encoded_tag}"


    # Make a GET request to the API
    response = requests.get(url, headers=HEADERS)


    if response.status_code == 200:
        try:
            return response.json()  # ✅ Ensure it's parsed as JSON
        except ValueError:
            print("❌ Error: Response is not valid JSON.")
            return None
    else:
        return None  # Return None if request fails


# formatter for raw club data
def format_club_data(club_data):
    """Formats the club data into a structured and visually appealing format."""
    formatted_data = []
    emojis = ["🏷️", "🏆", "📜", "🏅", "🎭", "🔰", "📌", "👥"]
    
    formatted_data.append("  🏠 Club Profile")
    formatted_data.append("━━━━━━━━━━━━━━━━━━━━━━")
    
    keys = ["tag", "name", "description", "type", "trophies", "required_trophies", "badge_id"]
    for index, key in enumerate(keys):
        if key in club_data:
            emoji = emojis[index % len(emojis)]
            formatted_data.append(f"{emoji} {key.replace('_', ' ').capitalize()}: {club_data[key]}")
    
    formatted_data.append("\n👥 Club Members")
    formatted_data.append("━━━━━━━━━━━━━━━━━━━━━━")
    count = 1
    for member in club_data.get("members", []):
        formatted_data.append(f"{count}. {member['name']} ({member['role']}) - {member['trophies']} Trophies")
        count += 1

    return "\n".join(formatted_data)


# retrieves raw individual brawler info
def get_brawler_info(player_tag, brawler_name):
    """Fetches specific brawler info from a player's account."""
    player_data = get_player_data(player_tag)
    if not isinstance(player_data, dict):  # Ensure we have valid data
        return "Error fetching player data"
    
    # Loop through all brawlers and check for a name match (case-insensitive)
    for brawler in player_data.get("brawlers", []):
        if brawler.get("name", "").strip().upper() == brawler_name.strip().upper():
            return brawler  # Return matching brawler's stats
    
    return f"Does not own Brawler: '{brawler_name}'"


# UNFINISHED, retrieves raw data for a brawlers GENERAL (not personal) stats
def get_general_brawler_stats(brawler_id):
    """Fetches general information about a brawler."""
    url = f"{BASE_URL}/brawlers/{brawler_id}"

    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()  # Return brawler stats




################# -----------------  MAIN  METHOD  ----------------  ######################
global_code = "global"
local_code = "us"
global_Leaderboard_data = get_player_leaderboard(global_code)
local_Leaderboard_data = get_player_leaderboard(local_code)


if __name__ == "__main__":


    #player_tag = "#8V8V88V8P" # Fatsnealy
    #player_tag = "#2QPUQYJYU" # Pinksheep
    #player_tag = "#8LQYGCVJP" # BloodFire
    #player_tag = "#8UCJVVGYU" # You Wish You
    #player_tag = "#GJ2COURUY" # Giggs
    #player_tag = "#R9GJYQ9C"  # JuiceStain
    #player_tag = "#8GVVU9GQC" # mythoes
    #player_tag = "#8PG8Q22U" # Sean Kingston
    player_tag = ""

    #club_tag = "#2JG28UQ28" # Knights Templar
    club_tag = "#808PJOYJP" # BadBoys


    '''Inputs'''
    #player_tag = ("#") + input("Player Tag: ")
    #club_tag = ("#") + input("Club Tag: ")

    player_data = get_player_data(player_tag)
    brawler_data = get_brawlers_data(player_tag)

    print("What information would you like to see? Enter [y] or [n]\n")
    
    a = input("Player Profile? ")
    if player_data and a.upper() == "Y":
        print("\n\n")
        print(format_player_data(player_data))
        print("\n-----------------------------------\n")


    b = input("Your Brawler Info? ")
    if brawler_data and b.upper() == "Y":

        print("\nWould you like to see the data for ALL your brawlers, or just one?")
        b1 = input("Enter [all] or [one]: ")
        print()
        
        if b1.upper() == "ALL":
            print(brawler_data)

        elif b1.upper() == "ONE":
            b2 = input("Which brawler?: ")
            brawler_name = b2.upper()
            print(format_brawler_data(get_brawler_info(player_tag, brawler_name)))

        else:
            print("Invalid Input. Rerun code")
        print("\n-----------------------------------\n")


    c = input("Local Leaderboards? ") 
    if c.upper() == "Y" and local_Leaderboard_data:
        print("\nLocal Leaderboard:\n")
        for index, player in enumerate(local_Leaderboard_data["items"], start=1):

            trophies = player['trophies']
            if trophies == 1:  
                trophies = "100000+"

            print(f"{index}. {player['name']} - {trophies} Trophies")
        print()


    d = input("Global Leaderboards? ")
    if d.upper() == "Y" and global_Leaderboard_data:
        print("\nGlobal Leaderboard:\n")
        for index, player in enumerate(global_Leaderboard_data["items"], start=1):

            trophies = player['trophies']
            if trophies == 1:  
                trophies = "100000+"

            print(f"{index}. {player['name']} - {trophies} Trophies")
        print() 



    e = input("Battle Log? ")
    if e.upper() == "Y":

        print("How many of your most recent battles would you like to see?")
        e1 = input("Enter integer between 1-25: \n")

        r = requests.Session()
        r.headers.update({"Authorization": "Bearer {}".format(API_KEY)})
        battleLog = r.get(f'https://api.brawlstars.com/v1/players/%23{player_tag[1:]}/battlelog')
        blist = battleLog.json()["items"]
        print("\n\nRECENT BATTLE LOG:\n━━━━━━━━━━━━━━━━━━━━━━")

        for i in range(int(e1)):
            battle = blist[i]
            print(f"{format_battle(battle)}\n\n")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


    f = input("Club Info? ")
    if f.upper() == "Y":
        print()
        print(format_club_data(get_club_info(club_tag)))

    
    #print(get_player_data(player_tag))

print("\n\nEnd\n") 

