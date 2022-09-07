# coding:utf-8
import cgi

# definir l'entete format ---> ( nom de l'entete: type; valeur)
print("Content-type: text/html; charset=utf-8\n")
#print("Content-type: text/css; charset=utf-8\n")

html = """ <!DOCTYPE html>

<html>

  <head>
	<meta charset="utf-8">
	<title>www.MonCV.com </title>
	
	<!-- css-->
	
	<link rel="stylsheet" href="css/bootstrap.min.css"/>
	<link rel="stylesheet" href="css/styl.css"/>
	 
	
  </head>
  
  <body>
	<!--header-->
		<header class="container-fluid header1">
			
				<div class="formulaire"> 
				<marquee>
					Mon Formulaire
				</marquee>
				</div>
				<nav class="menu1"> 
					<a href="index.py">
						Accueil
					</a>
					<a href="formulaire.py">
						Formulaire
					</a>
					<a href="cv.py">
						CV
					</a>
				</nav>
		
				
		</header>
	<!-- end header-->
		<form method="post" action="result.py">
			<p>
				<fieldset>
					<legend>Vos informations</legend> <!-- Titre du fieldset -->
						<label for="nom">
							Votre nom :
						</label>	<input type="text" name="nom" id="nom" placeholder="Ex: ADIKPETO" size="35" required />
							<br/><br/>
						
						
						<label for="prenom">
							Votre prénoms:
						</label>	<input type="text" name="prenom" id="prenom" placeholder="Ex: Mahoukpè Judicael" size="35" required />

						<label for="pseudo">
						
							<br/><br/>
							
							Votre pseudo :
						</label> 	<input type="text" name="pseudo" id="pseudo" placeholder="Ex: iudhael002" size="35" maxlength="20" />
						<br/><br/>
						
						
						<label for="sexe">
							Sexe:
						</label>	<label	for="sexe">	M	</label>	<input type="radio" name="sexe" id="sexe" required /> 
						
									<label	for="sexe">	F	</label>	<input type="radio" name="sexe" id="sexe" required /> 


						<br/><br/>
						<label for="dat">
							Votre date de naissance:
						</label> 	<input type="date" name="date" id="dat" min="10" max="100" required />
						
						<br/><br/>
						
						<label for="age">
							Votre age :
						</label> 	<input type="number" name="age" id="age" placeholder="Ex: 18 " size="10" min="10" max="100" required />
						
						<br/><br/>
						
						<label for="mail">
							Votre mail :
						</label> 	<input type="email" name="mail" id="mail" placeholder="Ex: adikpetoiudhael@gmail.com" size="35" required />
						
						<br/><br/>
						
						<label for="tell">
							Votre téléphone :
						</label> 	<input type="tel" name="tel" id="tell" placeholder="Ex: +xxx xxx-xxx-xxx" size="35" required />
						
						<br/><br/>
						
						
						<label for="pays">Sur  quel continent etes-vous ?</label>
							<select name="pays" id="pays">
								<optgroup label="Europe">
								
									<option value="france">	France	</option>
									
									<option value="espagne">	Espagne	</option>
									
									<option value="italie">	Italie	</option>
									
									<option value="royaume-uni">	Royaume-Uni	</option>
									
								</optgroup>
																					<!--selected permet de choisir l'Afrique par défaut-->
								<optgroup label="Amérique">
								
									<option value="canada">	Canada	</option>
									
									<option value="etats-unis">	Etats-Unis	</option>
									
								</optgroup>
								
								<optgroup label="Asie">
								
									<option value="chine">	Chine	</option>
									
									<option value="japon">	Japon	</option>
									
								</optgroup>
								
								<optgroup label="Afrique"  >
								
									<option value="chine">	Bénin	</option>
									
									<option value="japon">	Togo	</option>
									
									<option value="japon">	Ghana	</option>
									
									<option value="japon">	Niger	</option>
									
									<option value="japon">	Nigéria	</option>
									
									<option value="japon">	Cote-d'Ivoire	</option>
									
									<option value="japon">	Cameroun	</option>
									
									<option value="japon">	Afrique du Sud	</option>
									
									
								</optgroup>
								
								<optgroup label="Océanie">
								
									<option value="Australie">	Australie	</option>
									
									<option value="Nouvelle-Zélande">	Nouvelle-Zélande	</option>
									
									<option value="Fidji">	Fidji	</option>
									
									<option value="Îles Cook">	Îles Cook.	</option>
									
									<option value="Îles Marshall">	Îles Marshall	</option>
									
									
								</optgroup>	
								
							</select>
							
						<br/><br/>
						
						<label for="ameliorer">
							Comment pensez-vous que je pourrais améliorer mon site et mon CV ?
						</label><br />	
						
							<textarea name="ameliorer" id="ameliorer" rows="10" cols="55" required > </textarea>
							
							<br/><br/>
							
							<input type="submit"  value="Envoyer" id="marge" />
				</fieldset>
				
				
				
			</p>
		</form>
		
		

	
	
	
	




	
<!--footer-->
		<footer  class="container-fluid footer">
			
			<nav class="menu_footer">
				<a href="index.py">
					Accueil
								
				</a>
				<a href="formulaire.py">
					Formulaire
				</a>
				<a href="cv.py">
					CV
				</a>
														
			</nav>
			
			
			
			<div id="contact">
				<div class="element2">
					<a href="formulaire.html">
						<center>
							<img src="icone/facebook.png" alt="facebook" width="70%"  title="Facebook !!"/>
						</center>
					</a>
				</div>
						
				<div class="element2">
					<a href="formulaire.html">
						<center>
							<img src="icone/whatsapp.png" alt="whatsapp" width="70%"  title="Whatsapp !!"/>
						</center>
					</a>
				</div>
					
				<div class="element2">
					<a href="formulaire.html">
						<center>
							<img src="icone/instagram.png" alt="instagram" width="70%"  title="Instagram !!"/>
						</center>
					</a>
				</div>
					
				<div class="element2">
					<a href="formulaire.html">
						<center>
							<img src="icone/mail.png" alt="mail" width="70%"  title="Mail !!"/>
						</center>
					</a>
				</div>
					
				<div class="element2">
					<a href="formulaire.html">
						<center>
							<img src="icone/telegram.png" alt="telegram" width="70%"  title="Telegram !!"/>
						</center>
					</a>
				</div>
				
				<div class="element2">
					<a href="formulaire.py">
						<center>
							<img src="icone/linkedin.png" alt="linkedin" width="70%"  title="Linkedin !!"/>
						</center>
					</a>
				</div>
			</div>
			
		</footer>
	<!--end footer-->
	

	


  </body>
  
</html>

"""

print(html)
