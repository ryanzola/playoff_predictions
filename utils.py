import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def display_logo_and_score(team_logo_path, team_score, ax_logo, ax_score):
    # Display logo
    logo_img = mpimg.imread("./img/" + team_logo_path + ".png")
    ax_logo.imshow(logo_img)
    ax_logo.axis('off')  # Hide axes for logo

    # Display score
    ax_score.text(0.5, 0.5, str(team_score), fontsize=48, ha='center')
    ax_score.axis('off')  # Hide axes for score

# fig, axs = plt.subplots(2, 2, figsize=(8, 6))

# # Rams
# team_a_logo_path = 'path_to_team_a_logo.png'  # Replace with your image path
# team_a_score = 24  # Replace with actual score
# display_logo_and_score(team_a_logo_path, team_a_score, axs[0, 0], axs[0, 1])

# # Lions
# team_b_logo_path = 'path_to_team_b_logo.png'  # Replace with your image path
# team_b_score = 30  # Replace with actual score
# display_logo_and_score(team_b_logo_path, team_b_score, axs[1, 0], axs[1, 1])

# plt.tight_layout()
# plt.show()

# Calculate the average points for and against for the season and the last 4 games for each team
def calculate_averages(points_for, points_against):
    last4_for = points_for[-4:]
    last4_against = points_against[-4:]

    averages = {
        'average_points_for': round(sum(points_for) / len(points_for)),
        'average_last4_points_for': round(sum(last4_for) / len(last4_for)),
        'average_points_against': round(sum(points_against) / len(points_against)),
        'average_last4_points_against': round(sum(last4_against) / len(last4_against))
    }
    return averages

# Calculate predictions for each team
# The average of the last 4 games is weighted more heavily
# This is because the last 4 games are more indicative of the current form of the team
def calculate_predictions(team1, team2):
    team1_points = ((0.3 * team1['average_points_for'] + (0.7 * team1['average_last4_points_for'])) + ((0.3 * team2['average_points_against'])+(0.7 * team2['average_last4_points_against']))) / 2
    team2_points = ((0.3 * team2['average_points_for'] + (0.7 * team2['average_last4_points_for'])) + ((0.3 * team1['average_points_against'])+(0.7 * team1['average_last4_points_against']))) / 2

    return {
        'team1': round(team1_points),
        'team2': round(team2_points)
    }

# Calculate 3-game moving averages for each team
# This is used to get a better idea of the current form of the team
def calculate_moving_averages(points_for, points_against):
    moving_averages = {
        'moving_average_points_for': [],
        'moving_average_points_against': []
    }

    for i in range(len(points_for)):
        if i < 2:
            moving_averages['moving_average_points_for'].append(0)
            moving_averages['moving_average_points_against'].append(0)
        else:
            moving_averages['moving_average_points_for'].append(round((points_for[i-2] + points_for[i-1] + points_for[i]) / 3))
            moving_averages['moving_average_points_against'].append(round((points_against[i-2] + points_against[i-1] + points_against[i]) / 3))

    return moving_averages