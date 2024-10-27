# Made by RoSwagger Developers at roswagger.com
# Visit our creator program here for unrestricted access for free at
# discord.roswagger.com

from roswagger import swagify

datestring = "2006-02-27T21:06:40.3Z"
format = "f"  # Choose from 't', 'T', 'd', 'D', 'f', 'F', 'R'

# Formats and examples are in README.md 

ex = swagify(datestring, format)
print(ex)
