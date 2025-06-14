import streamlit as st
import random
import re
import pandas as pd

# Hard-coded rotations based on the provided PDF
rotations = {
    6: [
        "1 & 2 vs 3 & 4",
        "5 & 6 vs 1 & 3",
        "---------------",
        "2 & 4 vs 3 & 5",
        "1 & 6 vs 2 & 3",
        "---------------",
        "4 & 5 vs 2 & 6",
        "1 & 4 vs 3 & 6",
        "---------------",
        "1 & 5 vs 4 & 6"
    ],
    7: [
        "1 & 2 vs 3 & 4",
        "1 & 5 vs 6 & 7",
        "---------------",
        "2 & 3 vs 4 & 5",
        "2 & 6 vs 1 & 7",
        "---------------",
        "3 & 5 vs 1 & 4",
        "2 & 7 vs 3 & 6",
        "---------------",
        "4 & 7 vs 5 & 6"
    ],
    8: [
        "1 & 2 vs 3 & 4",
        "5 & 6 vs 7 & 8",
        "---------------",
        "1 & 8 vs 2 & 7",
        "3 & 5 vs 4 & 6",
        "---------------",
        "1 & 3 vs 6 & 8",
        "2 & 4 vs 5 & 7",
        "---------------",
        "1 & 5 vs 4 & 8",
        "2 & 3 vs 6 & 7",
        "---------------",
        "1 & 6 vs 4 & 7",
        "2 & 3 vs 5 & 8",
    ],
    9: [
        "1 & 2 vs 3 & 4",
        "5 & 6 vs 7 & 8",
        "---------------",
        "1 & 9 vs 2 & 3",
        "4 & 5 vs 6 & 7",
        "---------------",
        "8 & 9 vs 1 & 3",
        "2 & 6 vs 4 & 7",
        "---------------",
        "3 & 8 vs 1 & 5",
        "2 & 7 vs 4 & 9",
        "---------------",
        "1 & 7 vs 2 & 5",
        "3 & 6 vs 4 & 8",
        "---------------",
        "5 & 8 vs 6 & 9",
        "9 & 2 vs 1 & 7",
    ],
    10: [
        "1 & 2 vs 3 & 4",
        "5 & 6 vs 7 & 8",
        "---------------",
        "9 & 10 vs 1 & 4",
        "2 & 8 vs 3 & 5",
        "---------------",
        "2 & 6 vs 1 & 7",
        "3 & 9 vs 4 & 10",
        "---------------",
        "5 & 8 vs 1 & 9",
        "2 & 10 vs 3 & 6",
        "---------------",
        "4 & 5 vs 7 & 9",
        "1 & 6 vs 8 & 10",
        "---------------",
        "4 & 8 vs 5 & 9",
        "6 & 7 vs 2 & 3",
        "---------------",
        "7 & 10 vs 1 & 8"
    ],
    11: [
        "1 & 2 vs 3 & 4",
        "5 & 6 vs 7 & 8",
        "---------------",
        "9 & 10 vs 1 & 11",
        "2 & 8 vs 3 & 6",
        "---------------",
        "4 & 7 vs 5 & 9",
        "10 & 11 vs 2 & 6",
        "---------------",
        "1 & 8 vs 3 & 11",
        "4 & 5 vs 7 & 10",
        "---------------",
        "6 & 11 vs 1 & 9",
        "3 & 5 vs 2 & 7",
        "---------------",
        "4 & 8 vs 1 & 10",
        "6 & 9 vs 2 & 3",
        "---------------",
        "4 & 11 vs 5 & 7",
        "8 & 10 vs 9 & 2"
    ],
    12: [
        "1 & 2 vs 3 & 4",
        "5 & 6 vs 7 & 8",
        "---------------",
        "9 & 10 vs 11 & 12",
        "1 & 8 vs 2 & 7",
        "---------------",
        "3 & 6 vs 4 & 5",
        "7 & 11 vs 9 & 12",
        "---------------",
        "6 & 10 vs 1 & 3",
        "2 & 4 vs 3 & 5",
        "---------------",
        "8 & 9 vs 10 & 11",
        "1 & 12 vs 2 & 3",
        "---------------",
        "4 & 6 vs 8 & 11",
        "5 & 9 vs 10 & 12",
        "---------------",
        "1 & 7 vs 9 & 11",
        "2 & 12 vs 5 & 8",
        "---------------",
        "4 & 10 vs 6 & 7"
    ],
}

def assign_players(players):
    num_players = len(players)
    if num_players not in rotations:
        return None, None
    assigned_numbers = random.sample(range(1, num_players + 1), num_players)
    rotation = rotations[num_players]
    player_assignments = {assigned_numbers[i]: players[i] for i in range(num_players)}
    return player_assignments, rotation

def replace_numbers_with_names(rotation, player_assignments):
    replaced_rotation = []
    for match in rotation:
        line = match
        for number in sorted(player_assignments.keys(), key=lambda x: -len(str(x))):
            name = player_assignments[number]
            pattern = rf'(?<!\d){number}(?!\d)'
            line = re.sub(pattern, name, line)
        replaced_rotation.append(line)
    return replaced_rotation

# Streamlit App
st.set_page_config(page_title='Rotation Generator')

tab1, tab2 = st.tabs(['Pickleball', 'Jeff'])

with tab1:
    st.title('Pickleball Player Rotation Generator')
    player_input = st.text_input('Enter player names (comma separated):', key='pickleball_input')
    if player_input:
        players = [name.strip() for name in player_input.split(',')]
        if 6 <= len(players) <= 12:
            player_assignments, rotation = assign_players(players)
            if player_assignments and rotation:
                replaced_rotation = replace_numbers_with_names(rotation, player_assignments)
                st.write("### Player Assignments")
                for num in sorted(player_assignments):
                    st.write(f"{num}: {player_assignments[num]}")
                st.write("### Rotation (with Player Names)")
                for match in replaced_rotation:
                    st.write(match)
        else:
            st.error('Please enter between 6 and 12 players.')

with tab2:
    st.title("Jeff's Random Groups of Four")
    # File uploader for Excel
    uploaded_file = st.file_uploader('Upload Excel file (column of names)', type=['xlsx', 'xls'], key='jeff_upload')
    names = []
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        col = st.selectbox('Select column containing names', df.columns, key='jeff_column')
        names += df[col].dropna().astype(str).tolist()

    # Manual input as fallback or addition
    jeff_input = st.text_input('Or enter player names (comma separated):', key='jeff_input')
    if jeff_input:
        manual = [n.strip() for n in jeff_input.split(',') if n.strip()]
        names += manual

    # Generate groups if we have at least one name
    if names:
        # Shuffle for randomness
        random.shuffle(names)
        # Split into groups of 4
        groups = [names[i:i+4] for i in range(0, len(names), 4)]
        st.write('### Random Groups')
        for idx, group in enumerate(groups, start=1):
            st.write(f"Group {idx}: {', '.join(group)}")
