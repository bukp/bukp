from PIL import Image
import os

input_folder = "ressources\\diving photos\\full"
output_folder = "ressources\\diving photos\\low"

new_width = 300

for i in os.listdir(input_folder):

    image = Image.open(input_folder+"\\"+i)
    
    image.resize((new_width, image.height*new_width//image.width), Image.Resampling.LANCZOS).save(output_folder+"\\"+i)
