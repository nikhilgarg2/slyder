
'''create a file with name as local_settings.py in the same folder as settings.py and fill the details
in the following format'''


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'slyder',
    	'USER': 'root',
	'PASSWORD': 'dellxps123',
 	'OPTIONS':{
		'autocommit':True,
          }
	}
}




'''also configure the settings in first.connect.py to complete the settings'''
