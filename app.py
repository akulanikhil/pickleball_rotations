import streamlit as st
import random

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

    # Randomly assign numbers to players
    assigned_numbers = random.sample(range(1, num_players + 1), num_players)

    # Get the rotation based on the number of players
    rotation = rotations[num_players]

    # Map assigned numbers to player names
    player_assignments = {assigned_numbers[i]: players[i] for i in range(num_players)}

    return player_assignments, rotation


def replace_numbers_with_names(rotation, player_assignments):
    # Replace numbers in the rotation with the player names
    replaced_rotation = []
    for match in rotation:
        for number, name in player_assignments.items():
            match = match.replace(str(number), name)
        replaced_rotation.append(match)
    return replaced_rotation


# Streamlit App
st.title('Pickleball Player Rotation Generator')

# Input for player names
player_input = st.text_input('Enter player names (comma separated):')

if player_input:
    players = [name.strip() for name in player_input.split(',')]

    if 6 <= len(players) <= 12:
        # Assign players and generate rotation
        player_assignments, rotation = assign_players(players)

        if player_assignments and rotation:
            # Replace rotation numbers with player names
            replaced_rotation = replace_numbers_with_names(rotation, player_assignments)

            st.write("### Player Assignments")
            for player, number in player_assignments.items():
                st.write(f"{player}: {number}")

            st.write("### Rotation (with Player Names)")
            for match in replaced_rotation:
                st.write(match)
    else:
        st.error('Please enter between 6 and 12 players.')
