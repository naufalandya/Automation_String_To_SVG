import svgwrite

def string_to_svg(input_string, output_file="output.svg", font_size=30, fill_color='white', background_color='black'):
    dwg = svgwrite.Drawing(output_file, profile='tiny', size=('100%', '100%'))
    
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill=background_color))
    
    dwg.add(dwg.text(input_string, insert=(40, 80), fill=fill_color, font_size=f'{font_size}px'))

    dwg.save()

input_string = "(๑˃ᴗ˂)ﻭ"
string_to_svg(input_string, fill_color='white', background_color='black')
