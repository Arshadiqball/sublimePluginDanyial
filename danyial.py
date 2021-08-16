import sublime
import sublime_plugin


class Laravel2Command(sublime_plugin.TextCommand):

	def gog(self,edit,key):
		print(key + " is pressed");
		# print(fname + " Refsnes")
		# self.view.insert(edit, 0, "Hello, 3!")
		files=self.view.file_name().split("\\");
		module_name=files[6];
		print(files[7] + " is route");
		if files[7]=='modules': 
			files[6]=files[8];
			pass
		txt="";
		if key=='v': 
			txt="Modules\\"+files[6]+"\\Resources\\ blade.php";
			pass
		if key=='m': 
			txt="Modules\\"+files[6]+"\\Entities\\ .php";
			pass
		if key=='w': 
			txt="Modules\\"+files[6]+"\\Routes\\ .php";
			pass
		if key=='c': 
			txt="Modules\\"+files[6]+"\\http\\ controller.php";
			pass
		if key=='j': 
			txt="public\\js\\modules\\"+files[6]+"\\ .js";
			pass



		# if files[7]=='Resources': 
		# 	txt="Modules\\"+files[6]+"\\http\\ controller.php";
		# 	pass
		# if files[7]=='Entities': 
		# 	txt="Modules\\"+files[6]+"\\http\\ controller.php";
		# 	pass
		# if files[7]=='modules': 
		# 	txt="Modules\\"+files[6]+"\\http\\ controller.php";
		# 	pass
		# if files[7]=='Http': 
		# 	txt="Modules\\"+files[6]+"\\http\\ controller.php";
		# 	pass
		# 



		self.view.window().run_command('show_overlay', {"overlay": "goto", "text": txt,"show_files": "true"})

	 
	def run(self, edit,key):
		
		self.gog(edit,key);



