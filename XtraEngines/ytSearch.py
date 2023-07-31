from pytube import Search



def SearchEngine(searchTerm):
	vE = Search(searchTerm)
	results = vE.results
	
	
	
	
	return result 
	
def AutoSuggestEngine(searchTerm):
	vE = Search(searchTerm)
	
	auto_sugest = vE.completion_suggestions
	
	
	
	return {"data": {"suggestions": auto_sugest}}
	
