import os
import shutil

def Download_Competition_Dataset(name, path):
	if not os.path.exists(path):
		os.makedirs(path)
	kaggle.api.authenticate()
	print(kaggle.api.competition_list_files(name), end='\n\n')
	kaggle.api.competition_download_files(name, path=os.path.join(path))
	print('\n\nDownload completed\n')

def Download_Dataset(name, path):
	if not os.path.exists(path):
		os.makedirs(path)
	kaggle.api.authenticate()
	kaggle.api.dataset_download_files(name, path=os.path.join(path),unzip=True)
	print('\n\nDownload completed\n')#Executed only if there wasnt an error in downloading
	
if __name__ == '__main__':
	#C:\Users\<username>\.kaggle
	path = 'Dataset' #Folder to save downloaded Dataset
	name = 'imagenet-object-localization-challenge'
	Download_Competition_Dataset(name, path)
