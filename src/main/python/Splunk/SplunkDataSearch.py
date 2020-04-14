import requests
from xml.etree import cElementTree as ET
import json

class SplunkDataSearch():
    def __init__(self):
        self.user = "cjuare01"
        self.password = "Ijk342fvn$"
        
        searchQuery = "source=/root/Desktop/splunkuploadtest*"

        sessionID = self.search(searchQuery)

        isDone = 0
        while (isDone == 0):
            isDone = self.isSearchDone(sessionID)
            if isDone == 1:
                self.getSearchResults(sessionID)
                break
            elif isDone == 2:
                break

    def search(self, searchQuery):
        #search splunk with given search query
        data = {'search': 'search '+searchQuery}
        response = requests.post('https://localhost:8089/services/search/jobs', data=data, verify=False, auth=(self.user, self.password))
        #parse returned xml file string
        root = ET.fromstring(response.text)
        #print(response.text)
        #extract session ID
        sessionID = root.find('sid').text
        print("Session ID obtained: " + sessionID)

        return sessionID

    def isSearchDone(self, sessionID):
        #request progress/status on splunk search
        params = (('output_mode', 'json'),)
        response = requests.get('https://localhost:8089/services/search/jobs/' + sessionID, params=params, verify=False,
                            auth=(self.user, self.password))

        jsonObject = json.loads(response.text)
        isDone = jsonObject['entry'][0]['content']['isDone']
        isFailed = jsonObject['entry'][0]['content']['isFailed']

        if isDone:
            print("Search is Done")
            return 1
        elif isFailed:
            print("Search has Failed")
            return 2
        else:
            return 0

    def getSearchResults(self, sessionID):
        #request search results
        params = (('output_mode', 'json'),)
        response = requests.get('https://localhost:8089/services/search/jobs/'+sessionID+'/results', params=params, verify=False, auth=(self.user, self.password))
        jsonObject = json.loads(response.text)

        # Explores json format keys and values
        # for key in jsonObject:
        #   value = jsonObject[key] #.get(key,"default")
        #   print(type(key))
        #   print(type(value))
        #   print("Key and val are ({}) = ({})".format(key, value))

        #explore returned results dic
        # for dic in jsonObject['results']:
        #   for key in dic:
        #     value = dic[key]
        #     print(type(value))
        #     print(type(key))
        #     print("Key and val are ({}) = ({})".format(key, value))

        index = 1
        self.item_return = []
        for entry in jsonObject['results']:
            #print()
            #print("Log Entry: {}".format(entry['_raw']))
            #print("Timestamp: {}".format(entry['_time']))
            stringconversion = "Log Entry Number: " + str(index)
            self.item_return.append([stringconversion, entry['_time'], entry['_raw']])
            index +=1