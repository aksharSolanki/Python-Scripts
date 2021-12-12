
# AUTHOR: AKSHAR
# DATE: DECEMBER 09, 2021

baseballTeam = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketballTeam = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])


# DISPLAY MEMBERS OF BASEBALL TEAM
def show_baseball():
    print("\nMembers of baseball team: " + str(baseballTeam))


# DISPLAY MEMBERS OF BASKETBALL TEAM
def show_basketball():
    print("\nMembers of basketball team: " + str(basketballTeam))


# STUDENTS THAT PLAY BOTH SPORTS
def play_both():
    print("\nStudents who play both sports: " + str(baseballTeam & basketballTeam))


# STUDENTS THAT PLAY EITHER OF SPORTS
def play_either():
    print("\nStudents who play either sports: " + str(baseballTeam | basketballTeam))


# STUDENTS THAT PLAY BASEBALL BUT NOT BASKETBALL
def play_baseball_only():
    print("\nStudents who only play baseball: " + str(baseballTeam - basketballTeam))


# STUDENTS THAT PLAY BASKETBALL BUT NOT BASEBALL
def play_basketball_only():
    print("\nStudents who only play basketball: " + str(basketballTeam - baseballTeam))


# STUDENTS THAT PLAY ONE SPORT
def play_one_sport():
    print("\nStudents who play one sport: " + str(baseballTeam ^ basketballTeam)+ "\n")

print("\n--------------------------------------------------------------------")
show_baseball()
show_basketball()
play_both()
play_either()
play_baseball_only()
play_basketball_only()
play_one_sport()
print("--------------------------------------------------------------------\n")


