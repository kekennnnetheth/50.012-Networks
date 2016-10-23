# Done by: Tan Shun Yu (1001171)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['name']
    namelength = len(text)

    # very lame algorithm to mimic those 'find your ____ trivias'
    if (namelength<4):
        return render_template('breedpage.html', name=text, pic="/static/breed1.jpg", breed="American Bobtail Cat", desc="While the breed is still developing, breeders say that Bobtails are playful, energetic, and friendly, and possess an uncanny intelligence for Houdini-type escapes from closed rooms and fastened cages. Very people-oriented, they are not above demanding human attention by meowing or commandeering available laps.")
    elif (namelength<6 and namelength>3):
        return render_template('breedpage.html', name=text, pic="/static/breed2.jpg", breed="Bengal Cat", desc="The Bengal may look like a wild cat, but breeders insist that the Bengal is as lovably friendly and docile as any full-blooded domestic cat. Fanciers describe Bengals as playful, gregarious, and energetic cats that have a generous dose of feline curiosity and that want to be involved with their family. Not intimidated by water, they will sometimes join their family for a swim, as long as it's on their terms.")
    elif (namelength<8 and namelength>5):
        return render_template('breedpage.html', name=text, pic="/static/breed3.jpg", breed="Burmese Cat", desc="Breeders and fanciers report that Burmese are amusing, playful, and super-smart, the perfect interactive cats for home, office, shop, any place where people are in need of love and entertainment. They are as active as the Siamese and love to play. Devoted cats, Burmese are loyal and people-oriented. Breeders report temperament differences between males and females. The females are highly curious, active, and very emotionally involved with their family. The altered males love their humans too, but are more placid. They like to lounge about, usually on top of whatever you're doing. They take life as it comes. The only issue about which they are passionately concerned is the selected cuisine and when it will be served.")
    elif (namelength<10 and namelength>7):
        return render_template('breedpage.html', name=text, pic="/static/breed4.jpg", breed="Himalayan Cat", desc="Himmies, as fanciers call them, are perfect indoor cat companions. They are gentle, calm, and sweet-tempered, but they possess a playful side as well. Like the Siamese, Himalayans love to play fetch, and a scrap of crumpled paper or a kitty toy will entertain them for hours. Himalayans are devoted and dependent upon their humans for companionship and protection. They crave affection and love to be petted and groomed, which is fortunate, since every Himalayan family will spend part of each day doing just that.")
    else:
        return render_template('breedpage.html', name=text, pic="/static/breed5.jpg", breed="Munchkin Cat", desc="For their part, Munchkins, oblivious to the controversy surrounding them, go on being just what they are, cats; self-assured and outgoing. They love to wrestle and play with their long-legged feline friends, happily unaware that there's anything different about them. Nor do their feline companions treat them like members of the vertically challenged. Only humans look at them askance.")

# snake game
@app.route('/cat1/')
def cat1():
    return render_template('cat1page.html')

# weather
@app.route('/cat2/')
def cat2():
    return render_template('cat2page.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
