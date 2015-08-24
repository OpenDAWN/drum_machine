from boto.s3.connection import S3Connection
from boto.s3.key import Key
import os
import glob
import json

conn=S3Connection('AKIAIAWWSIRQDBHQK3XQ','/q/U4T9pConWG0nhSPLBhs69E4HTIH+OBQFuZMj9')
                  
conn.get_all_buckets()
bucket = conn.get_bucket('choqueuse')

directories=[{'type':"main",'directory':"wav/*"},]

list_files=[]
for indice in range(len(directories)):
    
    type=directories[indice]['type']
    files=glob.glob(directories[indice]['directory'])
    filename_list=files
    path = 'samples/'
    
    
    for index,filename in  enumerate(filename_list):
        
        full_filename = os.path.join(path, filename)
        key = Key(bucket, full_filename)
        
        if (key.exists() is False):
            print('%s' % filename)
            key.set_contents_from_filename(filename)
            key.set_acl('public-read')
            
        
