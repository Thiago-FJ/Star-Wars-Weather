import temp
import planets
from translate import Translator
import translate
trad = Translator(from_lang="english",to_lang="pt-br")

n = 14

for i in range(1,n+1):
    if temp.clime.lower() == planets.a[i]['Clima']:
        temp.clime = trad.translate(str(temp.clime)).lower()
        print(f"A temperatura na cidade: {temp.city} é de {temp.temp:.1f}°C\nParece que está {temp.clime}")
        print("Parece com:",planets.a[i]['Nome'])
    else:
        continue

