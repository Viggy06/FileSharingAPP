import shutil
from rest_framework import serializers

from .models import *

#Validation Serializers
# class FileSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Files
#         fields = '__all__'

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length = 100000 , allow_empty_file = False , use_url = False)
    )

    folder = serializers.CharField(required = False)

    #to create a zip file of uploaded files
    def zip_files(self, folder):
        shutil.make_archive(f'public/static/zip/{folder}', 'zip', f'public/static/{folder}')

    def create(self, validated_data):
        print("INSIDE CREATE")
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        file_list = []

        for file in files:
            files_obj = Files.objects.create(folder = folder, file = file)
            file_list.append(files_obj)
            print(file_list)
        
        self.zip_files(folder.uid)
        
        return {'files': {}, 'folder': str(folder.uid)}