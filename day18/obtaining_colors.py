import colorgram

colors = colorgram.extract('painting.jpg', 20)
c = []
for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    new_color = (r, g, b)
    c.append(new_color)

print(c)
