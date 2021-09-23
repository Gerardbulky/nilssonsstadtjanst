$(document).ready(function(){
// ADDING Eventlistener to Contact-form.   
    $("#contact-form").submit(function(event){
        event.preventDefault();
            emailjs.send("gmail","nilssonsstadtjanst", {
    "from_name": document.getElementById("fullname").value,
    "from_email": document.getElementById("emailaddress").value,
    "from_subject": document.getElementById("subject").value,
    "from_message": document.getElementById("messagesummary").value,
    })
})

 // ADDING Alerts using sweetAlert.js
     $("#button").click(function(){
         var name = $("#fullname").val();
         var email = $("#emailaddress").val();
         var subject = $("#subject").val();
         
         if(name == '' || email == '' || subject == '') {
                   swal({
                          title: "Field Empty!!",
                        text: "Kontrollera det fält som saknas!!",
                          icon: "warning",
                          button: "Ok!",
                       });
         } else {
                    swal({
                        title: "Skickat in. Vi hör av oss!!",
                          icon: "success",
                          button: "Ok!",
                       });
                    };

                });
      
            });