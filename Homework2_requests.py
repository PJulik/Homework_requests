import requests
from settings import TOKEN

class YaUploader:
    host = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = TOKEN

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def get_upload_link(self):
        uri = 'v1/disk/resources/upload/'
        url = self.host + uri
        params = {'path': f'/{"homework.json"}'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json()['href']

    def upload(self, file_path):
        upload_link = self.get_upload_link()
        response = requests.put(upload_link, headers=self.get_headers(), data=open(file_path, 'rb'))

if __name__== '__main__':
    path_to_file = r'C:\Users\user\Desktop\Homework_requests\homework.json'
    uploader = YaUploader(TOKEN)
    result = uploader.upload(path_to_file)
