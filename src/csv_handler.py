import pandas as pd

def append_ticket_to_csv(ticket_data):
    # Try to read the existing CSV file
    try:
        df = pd.read_csv("tickets.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["name", "match", "seat", "gate", "QR Image Path"])  
    
    # Append the new ticket data
    df_new = pd.DataFrame([ticket_data])  # Convert ticket data to DataFrame
    df = pd.concat([df, df_new], ignore_index=True)  # Concatenate the old and new DataFrames
    
    # Save the updated DataFrame back to CSV
    df.to_csv("tickets.csv", index=False)
    print("Ticket added to tickets.csv")
