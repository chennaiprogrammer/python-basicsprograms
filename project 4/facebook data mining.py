import json
import facebook

def main():
	token = "user token"
	graph = facebook.GraphAPI(token)
	#fields = ['first_name', 'location{location}','email','link']
	profile = graph.get_object('me',fields='first_name,location,link,email')
	#return desired fields
	print(json.dumps(profile, indent=4))

if __name__ == '__main__':
	main()