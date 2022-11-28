#este codigo usa o nome de uma cidade que o usuario digitar.
#fala qual a temmperatura atual do local indicado.
#indica também o clima.
#usa as informaçoes de temperaturaeratura e clima para indicar um pokemon que voce acharia no local no momento. `1`

import requests, random, base64, io, string
from PIL import Image
from io import BytesIO
from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "pokemonnn"

@app.route("/")
def index():
	flash("Digite o nome de uma cidade")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():

	if request.form.get("cidade") == "":
		flash("Erro, Insira um nome de cidade valido")
		return render_template("index.html")

	else:		
		
		city = request.form.get("cidade")

		api_address = "http://api.openweathermap.org/data/2.5/weather?appid=3f0894b09e85ac5744a17a170a15b5b8&units=metric&q="
		url = api_address + city
		rain = "a"
		json_data = requests.get(url).json()

		if json_data["cod"] == "404":
			flash("Erro, Insira um nome de cidade valido")
			return render_template("index.html")

		rain = str(json_data['weather'] [0] ['main'])
		temperatura = int((json_data['main'] ['temp']))
		pokeapi = "https://pokeapi.co/api/v2/type/"

		if rain == "Thunderstorm" or rain == "Rain":

			urlpoke = pokeapi + "electric"
			pokejson = requests.get(urlpoke).json()
			poke_rand = random.choice(pokejson["pokemon"])
			pokera = poke_rand["pokemon"] ["name"]
			pokenome = pokera.replace("-", " ")	

			flash("Em " + city + " esta chovendo, atualmente " + str(temperatura) + " Graus Celsius")
			flash(string.capwords(pokenome) + " é um pokemon do tipo elétrico")

		elif temperatura < 5:

			urlpoke = pokeapi + "ice"
			pokejson = requests.get(urlpoke).json()
			poke_rand = random.choice(pokejson["pokemon"])
			pokera = poke_rand["pokemon"] ["name"]
			pokenome = pokera.replace("-", " ")

			flash("Em " + city + " não esta chovendo, atualmente " + str(temperatura) + " Graus Celsius")
			flash(string.capwords(pokenome) + " é um pokemon do tipo gelo")

		elif temperatura >= 5 and temperatura < 10:

			urlpoke = pokeapi + "water"
			pokejson = requests.get(urlpoke).json()
			poke_rand = random.choice(pokejson["pokemon"])
			pokera = poke_rand["pokemon"] ["name"]
			pokenome = pokera.replace("-", " ")

			flash("Em " + city + " não esta chovendo, atualmente " + str(temperatura) + " Graus Celsius")
			flash(string.capwords(pokenome) + " é um pokemon do tipo água")

		elif temperatura >= 12 and temperatura < 15:

			urlpoke = pokeapi + "grass"
			pokejson = requests.get(urlpoke).json()
			poke_rand = random.choice(pokejson["pokemon"])
			pokera = poke_rand["pokemon"] ["name"]
			pokenome = pokera.replace("-", " ")

			flash("Em " + city + " não esta chovendo, atualmente " + str(temperatura) + " Graus Celsius")
			flash(string.capwords(pokenome) + " é um pokemon do tipo grama")

		elif temperatura >= 15 and temperatura < 21:

			urlpoke = pokeapi + "ground"
			pokejson = requests.get(urlpoke).json()
			poke_rand = random.choice(pokejson["pokemon"])
			pokera = poke_rand["pokemon"] ["name"]
			pokenome = pokera.replace("-", " ")

			flash("Em " + city + " não esta chovendo, atualmente " + str(temperatura) + " Graus Celsius")
			flash(string.capwords(pokenome) + " é um pokemon do tipo solo")

		elif temperatura >= 23 and temperatura < 27:

			urlpoke = pokeapi + "bug"
			pokejson = requests.get(urlpoke).json()
			poke_rand = random.choice(pokejson["pokemon"])
			pokera = poke_rand["pokemon"] ["name"]
			pokenome = pokera.replace("-", " ")

			flash("Em " + city + " não esta chovendo, atualmente " + str(temperatura) + " Graus Celsius")
			flash(string.capwords(pokenome) + " é um pokemon do tipo inseto")

		elif temperatura >= 27 and temperatura < 34:

			urlpoke = pokeapi + "rock"
			pokejson = requests.get(urlpoke).json()
			poke_rand = random.choice(pokejson["pokemon"])
			pokera = poke_rand["pokemon"] ["name"]
			pokenome = pokera.replace("-", " ")

			flash("Em " + city + " não esta chovendo, atualmente " + str(temperatura) + " Graus Celsius")
			flash(string.capwords(pokenome) + " é um pokemon do tipo pedra")

		elif temperatura > 33:

			urlpoke = pokeapi + "fire"
			pokejson = requests.get(urlpoke).json()
			poke_rand = random.choice(pokejson["pokemon"])
			pokera = poke_rand["pokemon"] ["name"]
			pokenome = pokera.replace("-", " ")

			flash("Em " + city + " não esta chovendo, atualmente " + str(temperatura) + " Graus Celsius")
			flash(string.capwords(pokenome) + " é um pokemon do tipo fogo")

		else:

			urlpoke = pokeapi + "normal"
			pokejson = requests.get(urlpoke).json()
			poke_rand = random.choice(pokejson["pokemon"])
			pokera = poke_rand["pokemon"] ["name"]
			pokenome = pokera.replace("-", " ")

			flash("Em " + city + " não esta chovendo, atualmente " + str(temperatura) + " Graus Celsius")
			flash(string.capwords(pokenome) + " é um pokemon do tipo normal")




		pokeidurl = poke_rand["pokemon"] ["url"]
		response = requests.get(pokeidurl).json()["sprites"] ["other"] ["official-artwork"] ["front_default"]


		if response is None:
			response = requests.get(pokeidurl).json()["sprites"] ["front_default"]
			uurl = requests.get(response)
			img = Image.open(BytesIO(uurl.content))	
			data = io.BytesIO()
			img.save(data, "PNG")
			encoded_img_data = base64.b64encode(data.getvalue())

		else:
			uurl = requests.get(response)
			img = Image.open(BytesIO(uurl.content))	
			data = io.BytesIO()
			img.save(data, "PNG")
			encoded_img_data = base64.b64encode(data.getvalue())
		return render_template("index.html", img_data=encoded_img_data.decode('utf-8'))