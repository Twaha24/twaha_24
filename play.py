import matplotlib. pyplot as plt
import numpy as np

def draw_pitch():
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Pitch Outline & Centre Line
    plt.plot([0, 0], [0, 1], color="green", lw=2)  # Left boundary
    plt.plot([0, 1], [1, 1], color="green", lw=2)  # Top boundary
    plt.plot([1, 1], [1, 0], color="green", lw=2)  # Right boundary
    plt.plot([1, 0], [0, 0], color="green", lw=2)  # Bottom boundary
    plt.plot([0.5, 0.5], [0, 1], color="green", lw=2)  # Centre line

    # Left and Right Penalty Areas
    plt.plot([0.05, 0.05], [0.25, 0.75], color="green", lw=2)  # Left penalty box
    plt.plot([0.95, 0.95], [0.25, 0.75], color="green", lw=2)  # Right penalty box

    # Left and Right 6-yard Areas
    plt.plot([0.15, 0.15], [0.4, 0.6], color="green", lw=2)
    plt.plot([0.85, 0.85], [0.4, 0.6], color="green", lw=2)

    # Centre Circle
    center_circle = plt.Circle((0.5, 0.5), 0.1, color="green", fill=False, lw=2)
    ax.add_patch(center_circle)

    # Left and Right Penalty Spots
    ax.plot(0.05, 0.5, 'ko')  # Left penalty spot
    ax.plot(0.95, 0.5, 'ko')  # Right penalty spot

    # Add a center spot
    ax.plot(0.5, 0.5, 'ko')

    # Mark the goal area (optional for more detail)
    ax.plot([0, 0.05], [0.4, 0.4], color="green", lw=2)
    ax.plot([0, 0.05], [0.6, 0.6], color="green", lw=2)
    ax.plot([1, 0.95], [0.4, 0.4], color="green", lw=2)
    ax.plot([1, 0.95], [0.6, 0.6], color="green", lw=2)

    # Set limits
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])

    # Title
    plt.title('Football Pitch')

def place_players(ax, positions):
    # Draw players as blue circles on the pitch
    for position in positions:
        ax.plot(position[0], position[1], 'bo', markersize=10)

def main():
    # Create a figure for the football pitch
    fig, ax = plt.subplots(figsize=(10, 6))

    # Draw the pitch
    draw_pitch()

    # Define player positions as (x, y) coordinates (normalized 0 to 1)
    player_positions = [
        (0.1, 0.1), (0.2, 0.3), (0.4, 0.2), (0.5, 0.7), (0.7, 0.5), (0.9, 0.8)  # Example positions
    ]

    # Place players on the pitch
    place_players(ax, player_positions)

    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()
