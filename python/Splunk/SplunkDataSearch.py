import requests
from xml.etree import cElementTree as ET
import json
from os import path
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SplunkDataSearch():
    def __init__(self):
        self.user = "ontheroof123"
        self.password = "12345678"
        
        #retrive root path that will be where to start searching from
        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, "../Data", "ProjectConfigData.txt"))
        with open(filepath, 'r') as file:
            data = file.readlines()
        data[0] = data[0].strip('\n')
        searchpath = 'source='+data[0]+'*'
        print(searchpath)

        searchQuery = searchpath

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
        print(response.text)
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
            stringconversion = "Log Entry Number: " + str(index)
            filepath_logentry = entry['source'].split('/')
            team = ''
            #finding team responsible for the file
            for item in filepath_logentry:
                if (item == 'Red') or (item == 'Blue') or (item == 'White'):
                    team = item
            #log entry number, time of upload, data in entry, team, file path
            self.item_return.append([stringconversion, entry['_time'], entry['_raw'], team, entry['source']])
            index +=1