import pandas as pd

stadiums_df = pd.read_csv("data/Stadiums_in_SaudiArabia.csv")
match_df = pd.read_csv("data/wcmatches.csv")

def get_stadium_info(stadium_name):
    stadium = stadiums_df[stadiums_df['Stadium Name'].str.contains(stadium_name, case=False, na=False)]
    if not stadium.empty:
        stadium_info = stadium.iloc[0]
        response = f"{stadium_info['Stadium Name']} - {stadium_info['Location']} (Capacity: {stadium_info['Capacity']}): {stadium_info['Notes']}"
    else:
        response = "Stadium not found."
    return response

def get_match_data(user_input):
    user_input = user_input.lower()
    filtered_df = match_df.copy()

    # Month check
    months = match_df['month'].str.lower().unique()
    for month in months:
        if month in user_input:
            filtered_df = filtered_df[filtered_df['month'].str.lower() == month]

    # Year check
    for word in user_input.split():
        if word.isdigit() and len(word) == 4:
            filtered_df = filtered_df[filtered_df['year'] == int(word)]

    # Country check
    for country in match_df['country'].str.lower().unique():
        if country in user_input:
            filtered_df = filtered_df[filtered_df['country'].str.lower() == country]

    # Team check
    for team in pd.concat([match_df['home_team'], match_df['away_team']]).str.lower().unique():
        if team in user_input:
            filtered_df = filtered_df[
                (filtered_df['home_team'].str.lower() == team) |
                (filtered_df['away_team'].str.lower() == team)
            ]

    # Group/stage check
    if "group" in user_input:
        filtered_df = filtered_df[filtered_df['stage'].str.lower().str.contains("group")]

    # Wins/losses
    if "win" in user_input or "won" in user_input:
        filtered_df = filtered_df[filtered_df['outcome'].str.lower().str.contains("win")]

    if filtered_df.empty:
        return "No matches found for your query."

    # Format response
    response = "\n".join(
        f"{row['date']} - {row['home_team']} vs {row['away_team']} in {row['city']} ({row['stage']})"
        for _, row in filtered_df.head(10).iterrows()
    )
    return response

#def speak(text):
   # tts = gTTS(text)
    #filename = "response.mp3"
   # tts.save(filename)
  #  os.system(f"start {filename}")
