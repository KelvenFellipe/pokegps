#este codigo usa o nome de uma cidade que o usuario digitar.
#fala qual a temmperatura atual do local indicado.
#indica também o clima.
#usa as informaçoes de temperatura e clima para indicar um pokemon que voce acharia no local no momento. `1`

import requests
import random
import json
from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "pokemonnn"

@app.route("/")
def index():
	flash("Digite o nome de uma cidade")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():

	city = request.form.get("cidade")

	api_address = "http://api.openweathermap.org/data/2.5/weather?appid=3f0894b09e85ac5744a17a170a15b5b8&units=metric&q="
	url = api_address + city
	rain = "a"
	json_data = requests.get(url).json()
	rain = str(json_data['weather'] [0] ['main'])
	temperatura = (json_data['main'] ['temp'])
	tipo = "a"	
	temp = int(temperatura)
	pokeapi = "https://pokeapi.co/api/v2/type/"

	if rain == "Thunderstorm" or rain == "Rain":

		tipo = "electric"
		urlpoke = pokeapi + tipo
		pokejson = requests.get(urlpoke).json()
		poke_rand = random.choice(pokejson["pokemon"])
		pokera = poke_rand["pokemon"] ["name"]	

		flash("Em " + city + " esta chovendo, atualmente " + str(temp) + " Graus Celsius")
		flash(pokera + " é um pokemon do tipo elétrico")

	elif temp < 5:
		tipo = "ice"
		urlpoke = pokeapi + tipo
		pokejson = requests.get(urlpoke).json()
		poke_rand = random.choice(pokejson["pokemon"])
		pokera = poke_rand["pokemon"] ["name"]

		flash("Em " + city + " não esta chovendo, atualmente " + str(temp) + " Graus Celsius")
		flash(pokera + " é um pokemon do tipo gelo")

	elif temp >= 5 and temp < 10:
		tipo = "water"
		urlpoke = pokeapi + tipo
		pokejson = requests.get(urlpoke).json()
		poke_rand = random.choice(pokejson["pokemon"])
		pokera = poke_rand["pokemon"] ["name"]

		flash("Em " + city + " não esta chovendo, atualmente " + str(temp) + " Graus Celsius")
		flash(pokera + " é um pokemon do tipo água")

	elif temp >= 12 and temp < 15:
		tipo = "grass"
		urlpoke = pokeapi + tipo
		pokejson = requests.get(urlpoke).json()
		poke_rand = random.choice(pokejson["pokemon"])
		pokera = poke_rand["pokemon"] ["name"]

		flash("Em " + city + " não esta chovendo, atualmente " + str(temp) + " Graus Celsius")
		flash(pokera + " é um pokemon do tipo grama")

	elif temp >= 15 and temp < 21:
		tipo = "ground"
		urlpoke = pokeapi + tipo
		pokejson = requests.get(urlpoke).json()
		poke_rand = random.choice(pokejson["pokemon"])
		pokera = poke_rand["pokemon"] ["name"]

		flash("Em " + city + " não esta chovendo, atualmente " + str(temp) + " Graus Celsius")
		flash(pokera + " é um pokemon do tipo solo")

	elif temp >= 23 and temp < 27:
		tipo = "bug"
		urlpoke = pokeapi + tipo
		pokejson = requests.get(urlpoke).json()
		poke_rand = random.choice(pokejson["pokemon"])
		pokera = poke_rand["pokemon"] ["name"]

		flash("Em " + city + " não esta chovendo, atualmente " + str(temp) + " Graus Celsius")
		flash(pokera + " é um pokemon do tipo inseto")

	elif temp >= 27 and temp < 34:
		tipo = "rock"
		urlpoke = pokeapi + tipo
		pokejson = requests.get(urlpoke).json()
		poke_rand = random.choice(pokejson["pokemon"])
		pokera = poke_rand["pokemon"] ["name"]

		flash("Em " + city + " não esta chovendo, atualmente " + str(temp) + " Graus Celsius")
		flash(pokera + " é um pokemon do tipo pedra")

	elif temp > 33:
		tipo = "fire"
		urlpoke = pokeapi + tipo
		pokejson = requests.get(urlpoke).json()
		poke_rand = random.choice(pokejson["pokemon"])
		pokera = poke_rand["pokemon"] ["name"]

		flash("Em " + city + " não esta chovendo, atualmente " + str(temp) + " Graus Celsius")
		flash(pokera + " é um pokemon do tipo fogo")

	else:
		tipo = "normal"
		urlpoke = pokeapi + tipo
		pokejson = requests.get(urlpoke).json()
		poke_rand = random.choice(pokejson["pokemon"])
		pokera = poke_rand["pokemon"] ["name"]

		flash("Em " + city + " não esta chovendo, atualmente " + str(temp) + " Graus Celsius")
		flash(pokera + " é um pokemon do tipo normal")



	return render_template("index.html")