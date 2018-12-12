
**read**

	returns the json provided in the previews POST call 

* **URL** 
	/api/resource 

* **Method**
	GET 

* **URL Params**
	None
* **Data Params**
	None

* **Success Response**
	**Content:** {“somthing”:”blabla”} 

* **Error Response**
	**Content:** “Request Failed”

* **Sample Call**
	curl http://18.194.230.122/api/resource 


**trigger**

	triggers the write function that writes the passed json on a txt file at the other instance 

* **URL** 
	/api/resource 

* **Method**
	POST 

* **URL Params**
	None
* **Data Params**
	any json

* **Success Response**
	**Content:** “Request executed successfully!” 

* **Error Response**
	**Content:** “Request Failed”

* **Sample Call**
	curl -X POST -H "Content-Type: application/json" -d '{"something": "blabla"}' http://3.121.223.3/api/resource

 
