from pathlib import Path
import urllib.parse
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
from PIL import Image
from django.conf import settings

suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
def humansize(nbytes):
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

class NoImageException(Exception):
    pass

class ImageTooLargeException(Exception):
    def __init__(self, fileSize):
        self.fileSize = fileSize

def image_verify(f):
    try:
        Image.open(f).verify()
    except IOError:
        raise NoImageException

# Check the image file size and raise exception if too big
def check_image_size(f):
    if f.size > settings.CKEDITOR5_MAX_FILE_SIZE:
        image_size = humansize(f.size)
        raise ImageTooLargeException(image_size)

def handle_uploaded_file(f):
    folder = getattr(settings, 'CKEDITOR_5_UPLOADS_FOLDER', 'django_ckeditor_5')
    uploads_path = Path(settings.MEDIA_ROOT, folder)
    #TODO: Need to do resizing + compressing here!!!
    fs = FileSystemStorage(location=uploads_path)
    filename = fs.save(f.name, f)
    return '/'.join([urllib.parse.urljoin(fs.base_url, folder), filename])


def upload_file(request):
    has_perm = settings.CKEDITOR_5_UPLOAD_PERMISSION if hasattr(settings, 'CKEDITOR_5_UPLOAD_PERMISSION') else request.user.is_staff
    print(has_perm)
    if request.method == 'POST' and has_perm: #request.user.is_staff:
        form = UploadFileForm(request.POST, request.FILES)
        try:
            image_verify(request.FILES['upload'])
        except NoImageException as ex:
            return JsonResponse({
                "error": {
                    "message": "{}".format(str(ex))
                }
            })
        try:
            check_image_size(request.FILES['upload'])
        except ImageTooLargeException as ex:
            return JsonResponse({
                "error": {
                    "message": "Image must be under 3MB, it is currently {}".format(ex.fileSize)
                }
            })
        if form.is_valid():
            url = handle_uploaded_file(request.FILES['upload'])
            print(url)
            return JsonResponse({'url': url,})
    else:
        return JsonResponse({
                "error": {
                    "message": "You do not have the permission to upload files."
                }
            })
    raise Http404(_('Page not found.'))
