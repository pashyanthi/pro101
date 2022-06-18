import os
import shutil
import dropbox
from dropbox.files import WriteMode

class foldertrans:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_files(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from): 
         for filename in files:
            local_path = os.path.join(root,filename)
            relative_path =os.path.relpath(local_path,file_from) 
            dropbox_path = os.path.join(file_to,relative_path) 
            with open(local_path, 'rb') as f: 
                dbx.files_upload(f.read(), dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token="sl.BGchf9mM_YvEE5n7ZTX-N_254fFQnaO1kT3CJ-auaGglY_OZYxsEhm4t522SIzQV55MRT6e71e5jJwzSo8JJnSNDHT_rDmGE_CqUL0ARE3NVUI1GtmUE0BdkagvPD5tQKO56kE0"
    foldertrans_obj=foldertrans(access_token)
    folder_from=input("Enter the file to be uploaded")
    folder_to=input("enter the cloud path")
    foldertrans_obj.upload_files(folder_from,folder_to)
    print("the folder has been moved successfully")

main()       
               