from rest_framework import serializers
from .models import Files, Folder
import shutil
import os

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length = 100000, allow_empty_file = False, use_url = False)
    )
    folder =  serializers.CharField(required = False)

    def zip_files(self,folder):
        shutil.make_archive(f'public/static/zip/{folder}', 'zip', f'public/static/{folder}')

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        files_obj_arr = []
        for file in files:
            files_obj = Files.objects.create(folder=folder, file=file)
            files_obj_arr.append(files_obj)

        self.zip_files(folder.uid)
        return {'files': {},  'folder': folder.uid}  
        # return files_obj_arr


