<?php

// what does php recieve
var_dump($_FILES);

// move uploaded files to a nice dictionary
foreach ($_FILES["mFiles"]["tmp_name"] as $key => $value) {
    $targetPath = "uploads/" . basename($_FILES["mFiles"]["name"][$key]);
    move_uploaded_file($value, $targetPath);
}
