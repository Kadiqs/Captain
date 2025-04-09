import pandas as pd
import qrcode
import json
import os
from gtts import gTTS

QR_FOLDER = "qrpng"
os.makedirs(QR_FOLDER, exist_ok=True)

def get_ticket_info(user_input):
    try:
        tickets_df = pd.read_csv("tickets.csv")
    except FileNotFoundError:
        return "No ticket data found."

    user_input = user_input.lower()
    filtered_df = tickets_df.copy()

    found = False  # Track if anything matched

    # Check seat number
    for seat in tickets_df['seat'].str.lower().unique():
        if seat in user_input:
            filtered_df = filtered_df[tickets_df['seat'].str.lower() == seat]
            found = True
            break

    # Check name
    for name in tickets_df['name'].str.lower().unique():
        if name in user_input:
            filtered_df = filtered_df[tickets_df['name'].str.lower() == name]
            found = True
            break

    # Check match/team
    for match in tickets_df['match'].str.lower().unique():
        if any(team in user_input for team in match.split()):
            filtered_df = filtered_df[tickets_df['match'].str.lower().str.contains(match)]
            found = True
            break

    # Gate number
    for gate in tickets_df['gate'].str.lower().unique():
        if gate in user_input:
            filtered_df = filtered_df[tickets_df['gate'].str.lower() == gate]
            found = True
            break

    if not found and ("ticket" in user_input or "seat" in user_input or "book" in user_input):
        # Fallback to full list
        filtered_df = tickets_df.head(10)

    if filtered_df.empty:
        return "No ticket info found for your query."

    response = "\n".join(
        f"{row['name']} - Seat {row['seat']} for {row['match']} (Gate: {row['gate']})"
        for _, row in filtered_df.iterrows()
    )
    return response



def append_ticket_to_csv(ticket_data):
    try:
        df = pd.read_csv("tickets.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["name", "match", "seat", "gate", "QR Image Path"])
    
    df_new = pd.DataFrame([ticket_data])
    df = pd.concat([df, df_new], ignore_index=True)
    df.to_csv("tickets.csv", index=False)
    print("Ticket added to tickets.csv")

def generate_ticket_qr(ticket_data):
    qr = qrcode.make(ticket_data)
    filename = f"{ticket_data['name']}_ticket.png"
    filepath = os.path.join(QR_FOLDER, filename)
    qr.save(filepath)
    print(f"QR code saved as {filepath}")
    return filepath 

def save_ticket_json(ticket_data):
    filename = f"{ticket_data['name']}_ticket.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(ticket_data, f, ensure_ascii=False, indent=2)
    print(f"Ticket data saved to {filename}")
