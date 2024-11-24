import pandas as pd

def read_excel_sheet(file_path, sheet_name):
    """
    Reads a specific sheet from an Excel file.

    Parameters:
    file_path (str): The path to the Excel file.
    sheet_name (str): The name of the sheet to be read.

    Returns:
    pd.DataFrame: The data from the specified sheet as a pandas DataFrame.
    """
    try:
        # Read the specified sheet
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def adjust_team_cells(df, target_rank):
    # Locate combined row with '2TM' or '3TM' in "Team"
    combined_row = df.loc[(df.index == target_rank) & (df['Team'].isin(['2TM', '3TM']))]
    
    # If a combined row exists
    if not combined_row.empty:
        # Identify individual team rows for the player
        player_id = df.loc[target_rank, 'Player']  # Assuming there's a "Player" column
        individual_rows = df[(df['Player'] == player_id) & (~df['Team'].isin(['2TM', '3TM']))]
        
        # Concatenate unique team names
        teams_played = '+'.join(individual_rows['Team'].unique())
        df.at[target_rank, 'Team'] = teams_played
        
        print(individual_rows)

        # Drop individual team rows and reset the index
        df = df.drop(index=individual_rows.index)
    
    return df

        