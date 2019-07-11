# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 02:30:31 2019

@author: RAHEEL
"""

import sys
import json



def is_US_State(state_name):
    
    us_states = {
         'Alaska':'AK',
         'Alabama':'AL',
         'Arkansas':'AR',
         'American Samoa':'AS',
         'Arizona':'AZ',
         'California':'CA',
         'Colorado':'CO',
         'Connecticut':'CT',
         'District of Columbia':'DC',
         'Delaware':'DE',
         'Florida':'FL',
         'Georgia':'GA',
         'Guam':'GU',
         'Hawaii':'HI',
         'Iowa':'IA',
         'Idaho':'ID',
         'Illinois':'IL',
         'Indiana':'IN',
         'Kansas':'KS',
         'Kentucky':'KY',
         'Louisiana':'LA',
         'Massachusetts':'MA',
         'Maryland':'MD',
         'Maine':'ME',
         'Michigan':'MI',
         'Minnesota':'MN',
         'Missouri':'MO',
         'Northern Mariana Islands':'MP',
         'Mississippi':'MS',
         'Montana':'MT',
         'National':'NA',
         'North Carolina':'NC',
         'North Dakota':'ND',
         'Nebraska':'NE',
         'New Hampshire':'NH',
         'New Jersey':'NJ',
         'New Mexico':'NM',
         'Nevada':'NV',
         'New York':'NY',
         'Ohio':'OH',
         'Oklahoma':'OK',
         'Oregon':'OR',
         'Pennsylvania':'PA',
         'Puerto Rico':'PR',
         'Rhode Island':'RI',
         'South Carolina':'SC',
         'South Dakota':'SD',
         'Tennessee':'TN',
         'Texas':'TX',
         'Utah':'UT',
         'Virginia':'VA',
         'Virgin Islands':'VI',
         'Vermont':'VT',
         'Washington':'WA',
         'Wisconsin':'WI',
         'West Virginia':'WV',
         'Wyoming': 'WY'
        }
    
    
    state_name = str(state_name)#.encode("utf-8")
    state_name = state_name.upper()
    #print (state_name)
        
    target_state = ""
    retval="No"
    for item in us_states:
        target_state = str(item).upper()
        if (state_name == target_state):
            retval = us_states.get(item)
        elif (state_name.find(target_state)>=0):
            retval = us_states.get(item)
            
        
    return retval
    
    

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    #make the dictionary for the sentiments
    scores = {}
    for line in sent_file:
        term,score = line.split("\t")
        scores[term] = int(score)
    
    state_sentiments={}
    totalScore=0

    strStateCode = ""
    for line in tweet_file:                            
        tweet = (json.loads(line.strip()).get("user"))
        tweet_text = (json.loads(line.strip()).get("text"))
        
        if isinstance(tweet,dict):
            for s in tweet_text.split(): #get score
                    totalScore+= int(str(scores.get(s)).replace("None","0"))
            
             
        if isinstance(tweet,dict):
            strloc =  tweet.get("location")
            if isinstance(strloc,str):
                strStateCode = is_US_State(strloc)
                if (strStateCode!="No"):
                    state_sentiments[strStateCode] = int(str(state_sentiments.get(strStateCode)).replace("None","0")) + totalScore                
            
        totalScore = 0
            

    dict2 = sorted(state_sentiments.items(), key=lambda kv:kv[1], reverse=True)
    txtstate= ""
    
    for itemx in dict2:
        tmpstr = str(itemx).replace("('","").replace(")","").replace("',","")
        #txtstate = tmpstr[:2].strip().rstrip('\n')
        txtstate = tmpstr.strip().rstrip('\n')
        #print(txtstate.strip().rstrip('\n').lstrip())                
        sys.stdout.write(txtstate)
        
        break;
        
        
if __name__ == '__main__':
  main()
