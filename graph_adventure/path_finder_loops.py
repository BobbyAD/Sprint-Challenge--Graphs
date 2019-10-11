# I think if I differentiate between "loops" and "branches" I can solve it as effectively as possible. 
# Go to nearest loop (it actually starts on 000 in this maze)
# Go through that loop counter-clockwise, knocking numbers off of it as you go and put them in visited (obviously)
# If you finish a loop, immediately go to the nearest spot in another loop