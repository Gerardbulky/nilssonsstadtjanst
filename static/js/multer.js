
const express = require('express');
const { request } = require('http');
const multer = require('multer');


const app = express();


app.listen(5000);









// define storage for the images
const storage = multer.diskStorage({

    // destination for files
    destination:function (request, file, callback){
        callback(null, '/static/uploads/image');
    },

    // add back the extension
    filename:function (request, file, callback) {
        callback(null, Date.now() + file.originalname);
    },
});

    // upload parameter for multer
    const upload = multer({
        storage:storage,
        limits:{
            fieldSize: 1024 * 1024 * 3,
        },
    });


router.get('/new', (request, response) => {
    response.render('new');
});

router.post('/', upload.single('image'), async (request, response) => {
    console.log(request.file);
    let blog = new blog({
        img: request.file.filename,
    });
});