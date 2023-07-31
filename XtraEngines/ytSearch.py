from pytube import Search



def SearchEngine(searchTerm):
	vE = Search(searchTerm)
	results = vE.results
	auto_sugest = vE.completion_suggestions
	
	
	
	return results
	
def AutoSuggestEngine(searchTerm):
	vE = Search(searchTerm)
	
	auto_sugest = vE.completion_suggestions
	
	
	
	return {"data": {"suggestions": auto_sugest}}
	
