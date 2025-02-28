Django CKEditor 5 
==================

   CKEditor 5 for Django >= 2.0

Quick start
-----------

 .. code-block:: bash
 
        pip install django-ckeditor-5

1. Add "django_ckeditor_5" to your INSTALLED_APPS setting like this:

 .. code-block:: python

        INSTALLED_APPS = [
            ...
            'django_ckeditor_5',
        ]


2. Include the app URLconf in your project urls.py like this:
 
  .. code-block:: python

       urlpatterns += [ 
           path("ckeditor5/", include('django_ckeditor_5.urls')),
       ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
3. Add to your settings.py:

  .. code-block:: python

      STATIC_URL = '/static/'
      MEDIA_URL = '/media/'
      MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
      CKCKEDITOR_5_UPLOADS_FOLDER = "media/uploads/" # Add location of folder to store the image uploads
      CKEDITOR5_MAX_FILE_SIZE = 3145728 # Add maximum file size for upload in bytes (example is 3MB)
      CKEDITOR_5_UPLOAD_PERMISSION = "blog.add_post" #Specify the permission required to upload files in the editor, default is staff permission

      customColorPalette = [
            {
                'color': 'hsl(4, 90%, 58%)',
                'label': 'Red'
            },
            {
                'color': 'hsl(340, 82%, 52%)',
                'label': 'Pink'
            },
            {
                'color': 'hsl(291, 64%, 42%)',
                'label': 'Purple'
            },
            {
                'color': 'hsl(262, 52%, 47%)',
                'label': 'Deep Purple'
            },
            {
                'color': 'hsl(231, 48%, 48%)',
                'label': 'Indigo'
            },
            {
                'color': 'hsl(207, 90%, 54%)',
                'label': 'Blue'
            },
        ]

      CKEDITOR_5_CUSTOM_CSS = 'path_to.css' # optional
      CKEDITOR_5_CONFIGS = { 
        'default': {
            'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                        'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],
    
        },
        'extends': {
            'blockToolbar': [
                'paragraph', 'heading1', 'heading2', 'heading3',
                '|',
                'bulletedList', 'numberedList',
                '|',
                'blockQuote', 'imageUpload'
            ],
            'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
            'code','subscript', 'superscript', 'highlight', '|',
                        'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                        'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                        'insertTable',],
            'image': {
                'toolbar': ['imageTextAlternative', 'imageTitle', '|', 'imageStyle:alignLeft', 'imageStyle:full',
                            'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
                'styles': [
                    'full',
                    'side',
                    'alignLeft',
                    'alignRight',
                    'alignCenter',
                ]
    
            },
            'table': {
                'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
                'tableProperties', 'tableCellProperties' ],
                'tableProperties': {
                    'borderColors': customColorPalette,
                    'backgroundColors': customColorPalette
                },
                'tableCellProperties': {
                    'borderColors': customColorPalette,
                    'backgroundColors': customColorPalette
                }
            },
            'heading' : {
                'options': [
                    { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                    { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                    { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                    { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
                ]
            }
        }
    }



4. Add to your `models.py`:

  .. code-block:: python


        from django.db import models
        from django_ckeditor_5.fields import CKEditor5Field
        
        
        class Article(models.Model):
            title=models.CharField('Title', max_length=200)
            text=CKEditor5Field('Text', config_name='extends')
            

Includes the following ckeditor5 plugins:

            Essentials,
            UploadAdapter,
            Autoformat,
            Bold,
            Italic,
            Underline,
            Strikethrough, Code, Subscript, Superscript,
            BlockQuote,
            Heading,
            //Image,
            ImageWithTitle,
            ImageCaption,
            ImageStyle,
            ImageToolbar,
            ImageUpload,
            ImageResize,
            Link,
            List,
            Paragraph,
            Alignment,
            Font,
            PasteFromOffice,
            SimpleUploadAdapter,
            MediaEmbed,
            RemoveFormat,
            Table, TableToolbar,
            TableProperties, TableCellProperties,
            Indent, IndentBlock,
            Highlight,
            TodoList,
            ImageTitle

