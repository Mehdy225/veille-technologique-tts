# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os 
  
mytext = 'Salut o terre d’espérance Pays de l’hospitalité. Tes légions remplies de vaillance Ont relevé ta dignité. Tes fils, chère Côte d’Ivoire, Fiers artisans de ta grandeur Tous rassemblés et pour ta gloire, Te batiront dans le bonheur Fiers ivoiriens le pays nous appelle.Si nous avons, dans la paix, ramené la liberté Notre devoir sera d’être un modèle De l’espérance promise à l’humanité En forgeant, unis dans la foi nouvelle,La patrie de la vraie fraternité.'
  
# Language we want to use 
language = 'fr'
  

myobj = gTTS(text=mytext, lang=language, slow=False) 
  

myobj.save("output.mp3") 
  
# Play the converted file 
os.system("start output.mp3") 

