from flask import Flask,render_template

FAI=Flask(__name__) #current application instance

@FAI.route('/Bappa') #url mapping or routing to function # /suffix -> is used in case of flask but in django we use -> suffix/
def Bappa(): 
    return 'Happy Ganesh Chaturthi !!'


@FAI.route('/htmlpage')
def htmlpage():
    return render_template('htmlpage.html',name='Soumya',age=23)

@FAI.route('/sfiles')
def sfiles():
    return render_template('sfiles.html')




if __name__=='__main__': # giving condition so that it will work for only current application
    FAI.run(debug=True)

# here everything is done by application instance
# request, response, url mapping, running of server

