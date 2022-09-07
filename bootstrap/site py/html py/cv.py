#coding:utf-8
import  cgi



# ces 2 modules permettront de gerer  les accents, defauts d'affichages
import sys
import codecs
    # remodifier l'encodage pour la sortie stadard
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())





    # definir l'entete format ---> ( nom de l'entete: type; valeur)
print("Content-type: text/html; charset=utf-8\n")
#print("Content-type: text/css; charset=utf-8\n")

html = """ <!DOCTYPE html>


<html>

  <head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>www.MonCV.com </title>
	
	<!-- css-->
	
	
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" 
		rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x"
		crossorigin="anonymous">
		
	<link rel="stylsheet" href="css/bootstrap.min.css"/>
	<link rel="stylesheet" href="css/styl.css"/>
	
	 
	
  </head>
  
  <body>
	<!--header-->
		<header class="container-fluid header1">
			
				<div class="cv"> 
				<marquee>
					Mon CV
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
		
	<!--cv-->
		<section class="container-fluid vitae">
			
			<div class="container-fluid">
				<div class="row profil">
					<div class="col-md-3 col-lg-3 col-xs-12 col-sm-12 photo">
							<a href="image/photo.html"> 
							
								<img src="icone/photo.jpg"  alt="Ma photo" class="radius" width="400px" height="397px"  align="left"   title="un clic pour agrandir!!!!"/>   	
								
									<!-- attribu border pour l'epaisseur de la bordure de l'image-->
							
							</a>
					</div>
					
						
					<div class="col-md-8 col-lg-8 col-xs-12 col-sm-12 marge">	
							
									<h1>	
										 Judicael Mahoukpè ADIKPETO
									</h1>
					
					
								
								
									<a href="mailto:adikpetoiudhael@gmail.com">
								
										<h2>
											 adikpetoiudhael@gmail.com
										</h2>
									</a>
								
						
								
								
									<h2>
										 +229 973-932-67
									</h2>
						
							
								
								
									<h2> 
										 Cotonou-BENIN									
									</h2>
								
									<h2>	
										<u>	Sexe	</u> : masculin
									</h2>
							
									<h2>	
										<u>	Date de naissance	</u> : 10/novembre/2002						<!--la balise paire <u> </u> permet de souligner -->
									</h2>
							
									<h2>	
										<u>	Nationalié	</u> : béninoise
									</h2>
							
							
								<citation auteur="Socrate">	<h2>	<em>	“Connais-toi toi-même.”	</em>	</h2>	</citation></br>
					</div>
				</div>
			</div>
			
			
			
			<div class="container f">
				
				<div class="row">
					<div class="col-md-6 col-lg-6 col-xs-12 col-sm-12">
						<h3 align="center">
							<u>
								DIPLOMES
							</u>
						</h3>
					
						<p>
							<ul>
							
								<li>
									<u>
									
										2020
										
									</u> : 
										<strong>
										
											Diplôme du Baccalauréat (BAC) scientifique série C	<br/>	
									
											<u>
												Cotonou-BENIN	
											</u> : College d'Enseignement Générale Sainte Marie Stella	<br/><br/>
											
										</strong>
									
								</li>
								
								<li>
									<u>
									
										20217
										
									</u> : 
										<strong>
										
											Diplôme du Brevet d'Etudes du Premier Cycle (BEPC) série : Mod.court	<br/>
									
											<u>
												Cotonou-BENIN
											</u> : College d'Enseignement Générale Sainte Marie Stella	<br/><br/>
											
										</strong>
								</li>
								
								<li>
									<u>
									
										2013
										
									</u> : 
										<strong>
										
											Certificat d'Etudes Primaires (CEP)	<br/>
									
											<u>
												Cotonou-BENIN
											</u> : Ecole Primaire Privée cité-houéyiho	<br/> 
											
										</strong>
								</li>
								
							</ul>
						</p>

					</div>
					
					<div class="col-md-6 col-lg-6 col-xs-12 col-sm-12">
						<h3 align="center">
							<u>
								COMPETENCE
							</u>
						</h3>
					
						<p>
							<ul>
								
								<li>
									<u>
									
										WORD
										
									</u> : 
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" /> 
											
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" /> 
											
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" />
									
								</li>	
									<br/>
								
								
								<li>
									<u>
									
										EXEL
										
									</u> : 
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" /> 

											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" /> 

											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" />
									
								</li>	
									<br/>
								
								
								<li>
									<u>
									
										POWER POINT
										
									</u>: 
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" /> 
											
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" />
								
								</li>	
									<br/>
								
								
								<li>
								
									<u>
									
										ADOBE ILLUSTRATOR CC
										
									</u> :
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" /> 
											
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" /> 

											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" />
									
								</li>	
									<br/>
								
								
								<li>
									<u>
									
										HTML
										
									</u> :
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" /> 

											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" /> 

											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" /> 

											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" /> 

											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" />
									
								
								</li>	
									<br/>
								
								
								<li>
									<u>
									
										CSS
										
									</u> : 
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" /> 

											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" /> 

											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" />
									
								</li>	
									<br/>
								
								
								<li>				
									<u>
									
										LANGAGE C
										
									</u> : 
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" />
									
								</li>	
									<br/>
								
								
								<li>				
									<u>
									
										PYTHON
										
									</u> : 
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  	
											
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" /> 

											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" /> 

											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" /> 

											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" />
									
								</li>	
									<br/>
									
							</ul>
							
						
						</p>
					</div>
					
					<div class="col-md-6 col-lg-6 col-xs-12 col-sm-12">
						<h3 align="center">
							<u>
								EDUCATION
							</u>
						</h3>
						
						<p align="center">
								 J’ai tout appris au cours mais également à travers des recherches.
						</p>
						
					</div>
			

				
					
					<div class="col-md-6 col-lg-6 col-xs-12 col-sm-12">
						<h3 align="center">
							<u>
								HOBBIES		
							</u>
						</h3>
						<p>
							<ul>
							
								<li>
								
									<u>
									
										Séries Animées
										
									</u>	
									
								</li>
									<br/>
								
								<li>
								
									<u>
									
										Jeux Videos	
										
									</u>	
									
								</li>
									<br/>
								
								<li>
								
									<u>
									
										Musique
										
									</u>	
									
								</li>
								
							</ul>
							
						
						</p>
					
					</div>
					
					<div class="col-md-12 col-lg-12 col-xs-12 col-sm-12">
						<h3 align="center">		
							<u>
							
								LANGUES	
								
							</u>	
						</h3>
						<p>
							<ul>
								<li>
								
									<u>	
									
										Fon	
										
									</u> :
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
												
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
												
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
												
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
												
											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" />
									
								</li>	
									<br/>
								
								<li>
									
									<u>	
									
										Français
										
									</u> :  
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
								
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
											
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" /> 
											
											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" />
														
								</li>	
									<br/>
								
								<li>
								
									<u>
									
										Anglais
										
									</u> : 
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" /> 
												
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
												
											<img src="icone/cercle.png" alt="cercle" width="15px" height="15px" align="bottom" />  
													
											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" /> 
											
											<img src="icone/noir.png" alt="cercle" width="15px" height="15px" align="bottom" />
											
								</li>
								
							</ul>
						</p>
					</div>
				</div>
			
			</div>
			
			
			
		
		</section>
	<!-- end Cv-->
	
	
	
	





	
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
					<a href="formulaire.html">
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
