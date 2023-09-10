from src.__main__ import main

##### COMMON NAME INFORMATION #####
#  most common english letters:  e, t, a, i, o, n, s, h, r
#  most common starting letters: t, a, o, d, w
#  most common ending letters:   e, s, d, t

##### TO-DO #####
#  Add an ending/beginning bias to some letters
#       For example, if at beginning don't double letter
#  Maybe don't let multiple double letters generate in one name lol
#  Let users change settings
#  Potential: add name meanings (prefixes & suffixes)
#  Save generated names to a file
#  Allow user to change and create their own settings.ini?
#  Branch off of gui-test to change settings to QDialog
#  Save the old generators and let people choose

#### BUGS ####
#  Settings window crashes the program after opening it twice
#  Settings window crashes when user enters letters

if __name__ == '__main__':
    main()
