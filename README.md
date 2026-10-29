# Regular Season Tracker

This is a Tool that will help me continually update power rankings and track
the value that players are adding as we go through the season. Both rankings
and player trackers will take into account the box scores of every game of the
season and will be described below. All files will write to the same output
file with the file including the last analyzed game.

REGULAR SEASON POWER RANKINGS TRACKER
The regular season tracker will work in the following way. There will be a
preseason power rankings done by myself that will start with a weight of 27
games to reflect 1/3 of the 82 game seasons games. These power rankings will
have an associated st dev's above the mean that each team recieved in my
grading scale. Said Std Dev are important because they will be the teams
initial score and will be represented by variable "S". This is the seeding
process to account for low sample size to start.

A new generated text file will be generated after teams first game which will
be iterated on every night of the nba. This page will keep track of a total
cumulative score for the teams season represented by the variable "S" as well
as a number that contribute to said weight (27(for preseason power rankings) +
number of games played).

The formula for calculating result of a game will be as follows: The winning
team will look like this: Sn = (S*n+(S+Sldfb))/n+1, where Sn is the new S for
the team; Sldfb is the difference between the S of the loser and the S of the
worst S in the league. The losing team will be the inverse formula, so Sn =
(S*n+(S-Swdft))/n+1, where Swdft is the winners difference from the top S in
the league.

Once this calculation has been done it will update the S for both teams
(rounded to 3 decimal places.) then iterate the n to n+1.

At the end of all adding box scores program will write a new text file with
updated S and n values and will document the last input game.

MVP OR PLAYER VALUE CALCULATION
This one is much more straight forward. There will be a text file that will be
appended to after every box score. It will contain every team and slowly add
players that fit the criteria.

For every box score, check every +/- stat. If the player in question made the
difference in a win vs a loss then it is recorded. Each player will have a
score S, that is cumulatively counted throughout the seasonThe complete formula
is as follows:
Player on winning team +/- > difference in score in game S+=1;
Player on winning team +/- = difference in score in game S+=.5;
Player on losing team +/- = difference in score in game S-=.5;
Player on losing team +/- < difference in score in game S-=1;
All other players will not have their numbers scored.

Will have a function to generate all players and sort them based on their value.