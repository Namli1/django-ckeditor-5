import ClassicEditor from './src/ckeditor';
import './src/override-django.css';

let editors = [];

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener("DOMContentLoaded", () => {
    let allEditors = document.querySelectorAll('.django_ckeditor_5');
    for (let i = 0; i < allEditors.length; ++i) {
        let script_id = `${allEditors[i].id}_script`
        document.querySelector(`[for$="${allEditors[i].id}"]`).style.float = 'none';
        let config = JSON.parse(document.getElementById(script_id).textContent);
        
        config['simpleUpload'] = {
            'uploadUrl': '/ckeditor5/image_upload/', 'headers': {
                'X-CSRFToken': getCookie('csrftoken'),
            }
        }

        config['compressionUpload'] = {
            'uploadUrl': '/ckeditor5/image_upload/', 
            'headers': {
                'X-CSRFToken': getCookie('csrftoken'),
            },
            'imageQuality': 0.5, //The desired quality of the image, value between 0 and 1
            'imageMaxWidth': 1111, // The maximum width of the image, image will be resized if it is too big
            'imageMaxHeight': 1111, //The maximum height of the image, image will be resized if it is too big
            'imageConvertSize': 1500000, //1.5MB //The file size upon which a PNG image will be converted to a JPEG
            'maxFileSize': 3145728, //3MB //The maximum file size the image can have, otherwise will throw an error

        }

        config['imageRemoveEvent'] = {
            callback: (imagesSrc, nodeObjects) => {
                // note: imagesSrc is array of src & nodeObjects is array of nodeObject
                // node object api: https://ckeditor.com/docs/ckeditor5/latest/api/module_engine_model_node-Node.html
    
                const xhr = new XMLHttpRequest();

                console.log(imagesSrc[0]);
                console.log(`/ckeditor5/image_delete${imagesSrc[0]}`);
                xhr.open("POST", `/ckeditor5/image_delete${imagesSrc}` , true);
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                xhr.send();

                console.log('callback called', imagesSrc, nodeObjects);
            }
        }

        //print(config)
        ClassicEditor.create(allEditors[i],
            config).then( editor => {
                editors.push(editor);        
            } ).catch(error => {
                console.error( error );
            });
    }
    window.editors = editors;
    window.ClassicEditor = ClassicEditor;
});
