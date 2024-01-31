import random

feet_in_mile = 5200
meters_in_kilometer = 1000
friends = ["Leo", "Magnus", "Johnpaul", "Divinewealth", "Rita"]

def get_file_extendion(filename):
	return filename[filename.index(".") + 1:]

def roll_dice(number):
	return random.randint(1, number)
