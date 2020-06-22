# ===== Preface =====
# 
# This question is very difficult in C and C++, where there is
# insufficient library support to answer it in an hour. If you
# prefer to program in one of those languages, please ask us to
# provide you with a question designed for those languages instead!
# 
# 
# ===== Intro =====
# 
# The Delphix San Francisco office is located in San Francisco’s
# financial district.  BART (Bay Area Rapid Transit) is a public
# transportation system serving the San Francisco Bay Area. Many
# engineers in the SF office use the Montgomery Street BART station
# to get to/from the office.
# 
# As engineers in the office will tell you, the BART system is
# infamously off schedule. Luckily, the BART public API
# (http://api.bart.gov/docs/overview/index.aspx) has a real-time
# information feed containing information about real-time estimated
# departures for specific stations. Your goal is to write a small
# program that utilizes the BART API that will quickly tell us the
# current time, the next 10 trains leaving Montgomery Street station,
# where they are going, and in how many minutes they leave the
# station.
# 
# Rules/constraints:
# * Print the trains in the order that they are leaving the station
# * Limit the output to the next 10 trains leaving the station
# * Print the number of minutes that the train will leave the station
# * Print the destination of the train
# 
# Example output:
# 
#     --------------------------------------------------
#     Montgomery St.  04:36:04 PM PDT
#     --------------------------------------------------
#     2 min  Dublin/Pleasanton
#     4 min  Daly City
#     5 min  Millbrae
#     5 min  Pittsburg/Bay Point
#     7 min  Fremont
#     9 min  Pleasant Hill
#     10 min  SF Airport
#     12 min  Daly City
#     12 min  Richmond
#     14 min  Millbrae
# 
# Your output does not need to match this, this is just an example.
# If you have better ideas of how to display the data, please do!
# 
# You should implement this in whatever language you're most
# comfortable with -- just make sure your code is production
# quality, well designed, and easy to read.
# 
# Finally, please help us by keeping this question and your
# answer secret so that every candidate has a fair chance in
# future Delphix interviews.
# 
# 
# ===== Steps =====
# 
# 1.  Choose the language you want to code in from the menu
#     labeled "Plain Text" in the top right corner of the
#     screen. You will see a "Run" button appear on the top
#     left -- clicking this will send your code to a Linux
#     server and compile / run it. Output will appear on the
#     right side of the screen.
#     
#     For information about what libraries are available for
#     your chosen language, see:
# 
#         https://coderpad.io/languages
# 
# 2.  Pull up the documentation for the API you'll be using:
# 
#       http://api.bart.gov/docs/etd/etd.aspx
# 
# 3.  You'll need an API key in order to query the data from
#     BART. You can create your own key
#     (http://www.bart.gov/schedules/developers/api) or use the demo
#     key:
# 
#         MW9S-E7SL-26DU-VV8V
# 
#     Make sure to use the API a bit to familiarize yourself 
#     with all of the outputs.
# 
# 4.  Implement the functionality described above, using data
#     fetched dynamically from the BART API described here:
# 
#       http://api.bart.gov/docs/etd/etd.aspx
# 
# 5.  Add any tests for your code to the main() method of
#     your program so that we can easily run them.
# 
# 
# 
# ====== FAQs =====
# 
# Q:  How do I know if my solution is correct?
# A:  Make sure you've read the prompt carefully and you're
#     convinced your program does what you think it should
#     in the common case. If your program does what the prompt 
#     dictates, you will get full credit. We do not use an
#     auto-grader, so we do not have any values for you to
#     check correctness against.
#     
# Q:  What is Delphix looking for in a solution?
# A:  After submitting your code, we'll have a pair of engineers
#     evaluate it and determine next steps in the interview process.
#     We are looking for correct, easy-to-read, robust code.
#     Specifically, ensure your code is idiomatic and laid out
#     logically. Ensure it is correct. Ensure it handles all edge
#     cases and error cases elegantly.
#     
# Q:  If I need a clarification, who should I ask?
# A:  Send all questions to the email address that sent you
#     this document, and an engineer at Delphix will get
#     back to you ASAP (we're pretty quick during normal
#     business hours).
# 
# Q:  How long should this question take me?
# A:  Approximately 1 hour, but it could take more or less
#     depending on your experience with web APIs and the
#     language you choose.
# 
# Q:  When is this due?
# A:  We will begin grading your answer 24 hours after it is
#     sent to you, so that is the deadline.
#     
# Q:  What if something comes up and I cannot complete the
#     problem during the 24 hours?
# A:  Reach out to us and let us know! We will work with you
#     to figure out an extension if necessary.
# 
# Q:  How do I turn in my solution?
# A:  Anything you've typed into this document will be saved.
#     Email us when you are done with your solution. We will
#     respond confirming we've received the solution within
#     24 hours.
# 
# Q:  Can I use any external resources to help me?
# A:  Absolutely! Feel free to use any online resources you
#     like, but please don't collaborate with anyone else.
# 
# Q:  Can I use my favorite library in my program?
# A:  Unfortunately, there is no way to load external
#     libraries into CoderPad, so you must stick to what
#     they provide out of the box for your language:
# 
#         https://coderpad.io/languages
# 
#     If you really want to use something that's not
#     available, email the address that sent you this link
#     and we will work with you to find a solution.
# 
# Q:  Can I code this up in a different IDE?
# A:  Of course! However, we do not have your environment
#     to run your code in. We ask that you submit your final
#     code via CoderPad (and make sure it can run). This gives
#     our graders the ability to run your code rather than guessing.
# 
# Q:  Why does my program terminate unexpectedly in
#     CoderPad, and why can't I read from stdin or pass
#     arguments on the command line?
# A:  CoderPad places a limit on the runtime and amount of
#     output your code can use, but you should be able to
#     make your code fit within those limits. You can hard
#     code any arguments or inputs to the program in your
#     main() method or in your tests.
# 
# Q:  I'm a Vim/Emacs fan -- is there any way to use those
#     keybindings? What about changing the tab width? Font
#     size?
# A:  Yes! Hit the button at the bottom of the screen that
#     looks like a keyboard.


"""
    Module contains class Station to fetch details of arrival of trains from various destination.
    
"""
import requests
from requests.exceptions import HTTPError
import logging
logger = logging.getLogger(__name__)

class BartApi:
    API_URL='http://api.bart.gov/api/etd.aspx'
    DEMO_API_KEY='MW9S-E7SL-26DU-VV8V'
    
    def __init__(self,api_key=None):
        if api_key:
            self.__api_key=api_key
        else:
            self.__api_key=self.DEMO_API_KEY
        
        logging.info (""" 
        Welcome to BART API.
        
        Below are command Options -
        
            etd          Requests estimated departure time for specified station.
            
            help         Provides a summary of the commands available through the BSA API.
            
            bsa          Requests current advisory information.
            
            count        Request the number of trains currently active in the system.
            
            elev         Requests current elevator status information.
            
            routeinfo    Requests detailed information regarding a specific route.
            
            routes       Requests detailed information current routes.
        
        Use function fetch_bart_details(command_name) to get relevant information.
        
        For more details :
        
        http://api.bart.gov/docs/overview/index.aspx
            
        """)

    def fetch_bart_details(self,command_name):
        api_dictionary=dict()
        api_dictionary['API_URL'] = self.API_URL
        
        api_dictionary['API_URL_PARAMS'] = {'cmd': command_name,
                                            'key': self.__api_key,
                                            'json':'y',
                                            'pretty':'true'
                                           }            
        
        return api_dictionary 
        
        

class Station(object):
    """
        Class Station
    """
    API_URL='http://api.bart.gov/api/etd.aspx'
    API_KEY='MW9S-E7SL-26DU-VV8V'
    API_URL_PARAMS = {'cmd':'etd',
                      'key': API_KEY,
                      'json':'y',
                      'pretty':'true'
                     }
        
    def __init__(self,station_name):
        """ 
            Constructor for Station Class
            
            sets station_name parameter
        """
        self.station_name=station_name
        
        b=BartApi()
        self.bart_api_params=b.fetch_bart_details('etd')
        
        
    
    @staticmethod
    def request_data(url, params):
        """ 
            Static method to connect to URL and fetch data based on parameter provided.
        """
        
        try:
            #request data for given url, with specified paramters
            response = requests.get(url,params=params)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
            
            return response.json()
            
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  
        except Exception as err:
            print(f'Other error occurred: {err}') 
        else:
            print('Success!') 
        
    def get_station_json(self):
        """ 
            Method to request data by passing details of API URL and paramaters.
            
            Returns a dictionary of fetched data.
            
        
        """
        
        api_url = self.bart_api_params['API_URL']
        
        api_url_param = self.bart_api_params['API_URL_PARAMS']
        station_abbrevation={'orig': self.station_name.strip() }
        api_url_param.update(station_abbrevation)
        
        #fetch data for a particular station
        fetch_data = self.request_data(api_url,api_url_param)
        
        if not fetch_data:
            print ("Incorrect station parameters. Check if Station Name '{}' is correct".format(self.station_name))
            return None
        
        return fetch_data
    
    def fetch_station_details(self):
        """ 
            Method to fetch station detail 
            
            Returns a dictionary of relevant details for users.
            This information can be stored in a database, or 
            printed on screen for users.
            
        """        
        try:
            station_json = self.get_station_json()['root']['station']
        except:
            logging.error("incorrect input provided. ")
            return None
            
        
        dict_data = dict()

        #get station name
        dict_data['start_station_name'] = station_json[0]['name']
        
        #get date and time
        dict_data['current_date'] = self.get_station_json()['root']['date']
        dict_data['current_time'] = self.get_station_json()['root']['time']
        
        
        #get destination data in a dictionary of "destination_name":"time"
        destination_dict={}
        
        for i,j in enumerate(station_json[0]['etd']):
            try:
                destination_dict[j['destination']] = int(j["estimate"][0]['minutes'])
            except:
                #in case Train is Leaving, its time of leaving will be 'Leaving' 
                #and is default set to 0
                destination_dict[j['destination']] = 0
        
        dict_data['destintation_data'] = destination_dict
        return dict_data

    def print_station_details(self,num_of_rows):
        '''
            Method : print_station_details
            
            Args:
                num_of_rows ( int ) : number of records for destination data to be printed on output screen. If this value is more than number of destination trains at a station, or if invalid value(less than 1 or not integer), then it EXITS.
                
                
        
        '''
        try:
            get_dict=self.fetch_station_details()
        except:
            logging.error("incorrect input provided. ")
             
        if get_dict: 
            destination_key=get_dict['destintation_data']
            station_name = get_dict['start_station_name']
            date_string = get_dict['current_date'] 
            time_string = get_dict['current_time'] 

            if num_of_rows<1 or not isinstance(num_of_rows, int):
                print ("incorrect value for number of rows({}) to be printed. Exiting. ".format(num_of_rows))
            elif num_of_rows>len(destination_key):
                print (f"Number of destination data requested ({num_of_rows}) for Station '{station_name}'(abbrevated as '{self.station_name}') is more than Number of destination available")
                print ("Exiting")
            else:

                print ("--------------------------------------------------")
                print (f"{station_name}    {date_string}   {time_string}")
                print ("--------------------------------------------------")
                for k, v in sorted(destination_key.items(), key=lambda item: item[1]):
                    if num_of_rows>0:
                        print (v, " min ",k)
                        num_of_rows=num_of_rows-1


def main():
    """ 
        Main Driver program for our module.
    """
    print (""" 
    Welcome to Delphix Online Assessment Test Round 1.
    In given module, we have attempted to meet requirements.
    
    The code is divided into 2 Classes - 
        class BartApi - an API class from which we fetch API related information. 
        class Station - class containing Station related attributes and methods.
    
    To run this class, please provide 2 inputs -
        a. station name - abbrevated station name for which we need to fetch details.
        b. number of records to be fetched. Default = 10. 
    
    """)
    
    station_abbrevation = input("Provide abbrevated station name for which we need to fetch details :  ").strip()
    num_records = input("""provide number of records to be fetched. Default is 10. Hit enter if no value to be passed. :  """)
    
    if not num_records:
        num_records=10
    else:
        num_records=int(num_records)
    mystation = Station(station_abbrevation)
    mystation.print_station_details(num_records)
    

if __name__ == '__main__':
    main()
 
    
