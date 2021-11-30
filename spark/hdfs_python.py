from hdfs import InsecureClient
client = InsecureClient( "http://master:9870", user="hdfs" )

import os
import time
def load_txt( path ) :
    files = client.list( path )
    data = []
    label = []
    for filename in files :
        # print( filename )
        lang = filename.split( "-" )        # en 11.txt
        label.append( lang[0] )
        file = os.path.join( path, filename )
        try :
            with client.read( file, encoding="utf-8" ) as f :
                print( file )
                langfile = f.read()
                langtext = langfile.lower()
                a = ord( "a" )      # 97  
                z = ord( "z" )      # 123
                counts = [ i for i in range( 26 ) ]
                for char in langtext :
                    code = ord( char )
                    if code >= a and code <= z :
                        counts[ code-a ] += 1
                total = sum( counts )
                count = list( map( lambda x : x/total, counts ) )  
                data.append( count )
            # print( data )    
        except Exception :
            time.sleep( 1 )    
    return data, label

train_data, train_label = load_txt( "/input/lang/train/" )
test_data, test_label = load_txt( "/input/lang/test/" )

from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier()
model = forest.fit( train_data, train_label )
predicts = model.predict( test_data )
from sklearn.metrics import accuracy_score
score = accuracy_score( test_label, predicts )
print( score )

