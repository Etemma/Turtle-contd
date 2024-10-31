import colorgram
rgb_colors = []
rg = []
colors = colorgram.extract('image.jpg', 30)
col = colorgram.extract('img.png', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
for _ in col:
    r = _.rgb.r
    g = _.rgb.g
    b = _.rgb.b
    new_col = (r, g, b)
    rg.append(new_col)

print(rgb_colors)
print(rg)
